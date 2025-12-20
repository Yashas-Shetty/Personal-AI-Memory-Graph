const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface MemoryStats {
  vector_count: number;
  graph_count: number;
  status: string;
}

export interface IngestResponse {
  message?: string;
  error?: string;
}

export interface QueryResponse {
  answer: string;
}

export const api = {
  async getStats(): Promise<MemoryStats> {
    const res = await fetch(`${API_URL}/memory/stats`);
    if (!res.ok) throw new Error('Failed to fetch stats');
    return res.json();
  },

  async ingest(text: str, source: string = 'web_ui'): Promise<IngestResponse> {
    const res = await fetch(`${API_URL}/ingest`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, source }),
    });
    return res.json();
  },

  async query(query: string): Promise<string> {
    const res = await fetch(`${API_URL}/query/reason?query=${encodeURIComponent(query)}`, {
      method: 'POST',
    });
    const data = await res.json();
    return data; // ReasoningService returns simple string currently
  },

  async reset(): Promise<any> {
    const res = await fetch(`${API_URL}/memory/clear`, { method: 'POST' });
    return res.json();
  }
};
