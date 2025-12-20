'use client';

import { useState, useEffect } from 'react';
import { api, MemoryStats } from '@/lib/api';

export default function Home() {
  const [stats, setStats] = useState<MemoryStats | null>(null);
  const [ingestText, setIngestText] = useState('');
  const [queryText, setQueryText] = useState('');
  const [lastAnswer, setLastAnswer] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Load stats on mount
  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      const data = await api.getStats();
      setStats(data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleIngest = async () => {
    if (!ingestText.trim()) return;
    setLoading(true);
    try {
      await api.ingest(ingestText);
      setIngestText('');
      await fetchStats();
      alert('Memory stored successfully!');
    } catch (err) {
      setError('Ingestion failed');
    } finally {
      setLoading(false);
    }
  };

  const handleQuery = async () => {
    if (!queryText.trim()) return;
    setLoading(true);
    setLastAnswer(null);
    try {
      const answer = await api.query(queryText);
      setLastAnswer(answer);
    } catch (err) {
      setError('Query failed');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = async () => {
    if (!confirm('Are you sure you want to clear ALL memories?')) return;
    try {
      await api.reset();
      await fetchStats();
      setLastAnswer(null);
    } catch (err) {
      alert('Reset failed');
    }
  };

  return (
    <main className="min-h-screen bg-slate-950 text-slate-100 p-8">
      <div className="max-w-4xl mx-auto space-y-12">
        {/* Header */}
        <header className="flex justify-between items-center border-b border-slate-800 pb-6">
          <div>
            <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 to-emerald-400 bg-clip-text text-transparent">
              Personal AI Memory Graph
            </h1>
            <p className="text-slate-400 mt-2">Your hybrid semantic & relationship surrogate brain.</p>
          </div>
          <button
            onClick={handleReset}
            className="text-xs bg-red-500/10 hover:bg-red-500/20 text-red-400 px-3 py-1 rounded border border-red-500/20 transition"
          >
            Reset Memory
          </button>
        </header>

        {/* Stats Row */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <StatCard label="Vector Memories" value={stats?.vector_count ?? '--'} />
          <StatCard label="Graph Concepts" value={stats?.graph_count ?? '--'} />
          <StatCard label="System Status" value={stats?.status ?? 'Connecting...'} />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-12 mt-12">
          {/* Ingest Section */}
          <section className="space-y-4">
            <h2 className="text-xl font-semibold flex items-center gap-2">
              <span className="w-2 h-2 bg-emerald-500 rounded-full"></span>
              Ingest New Memory
            </h2>
            <textarea
              className="w-full h-40 bg-slate-900 border border-slate-800 rounded-lg p-4 focus:ring-2 focus:ring-emerald-500 outline-none transition"
              placeholder="What should I remember? (e.g., 'I started learning Next.js today...')"
              value={ingestText}
              onChange={(e) => setIngestText(e.target.value)}
            />
            <button
              onClick={handleIngest}
              disabled={loading}
              className="w-full bg-emerald-600 hover:bg-emerald-500 disabled:opacity-50 py-3 rounded-lg font-medium transition"
            >
              {loading ? 'Processing...' : 'Store Memory'}
            </button>
          </section>

          {/* Query Section */}
          <section className="space-y-4">
            <h2 className="text-xl font-semibold flex items-center gap-2">
              <span className="w-2 h-2 bg-blue-500 rounded-full"></span>
              Retrieve & Reason
            </h2>
            <div className="flex gap-2">
              <input
                className="flex-1 bg-slate-900 border border-slate-800 rounded-lg px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500 transition"
                placeholder="Ask your memory anything..."
                value={queryText}
                onChange={(e) => setQueryText(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && handleQuery()}
              />
              <button
                onClick={handleQuery}
                disabled={loading}
                className="bg-blue-600 hover:bg-blue-500 disabled:opacity-50 px-6 rounded-lg transition"
              >
                Ask
              </button>
            </div>

            <div className="mt-6 min-h-[160px] bg-slate-900/50 border border-slate-800 rounded-xl p-6 relative overflow-hidden">
              {loading && !lastAnswer && (
                <div className="absolute inset-0 flex items-center justify-center bg-slate-950/20 backdrop-blur-sm">
                  <div className="animate-pulse text-blue-400">AI is thinking...</div>
                </div>
              )}

              {lastAnswer ? (
                <div className="text-slate-100 max-w-none">
                  <p className="text-lg leading-relaxed whitespace-pre-wrap">{lastAnswer}</p>
                </div>
              ) : (
                <p className="text-slate-500 italic text-center mt-12">Reasoned answer will appear here...</p>
              )}
            </div>
          </section>
        </div>
      </div>
    </main>
  );
}

function StatCard({ label, value }: { label: string; value: string | number }) {
  return (
    <div className="bg-slate-900 border border-slate-800 p-6 rounded-xl text-center">
      <div className="text-slate-400 text-sm font-medium mb-1">{label}</div>
      <div className="text-2xl font-bold">{value}</div>
    </div>
  );
}
