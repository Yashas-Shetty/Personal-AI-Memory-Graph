'use client';

import { useState, useEffect } from 'react';
import { api, MemoryStats } from '@/lib/api';

type View = 'notes' | 'tasks' | 'chat';

export default function Home() {
  const [currentView, setCurrentView] = useState<View>('notes');
  const [stats, setStats] = useState<MemoryStats | null>(null);

  // Data states
  const [notes, setNotes] = useState<any[]>([]);
  const [tasks, setTasks] = useState<any[]>([]);
  const [selectedNote, setSelectedNote] = useState<any | null>(null);

  // Input states
  const [noteInput, setNoteInput] = useState('');
  const [taskInput, setTaskInput] = useState('');
  const [chatInput, setChatInput] = useState('');
  const [chatAnswer, setChatAnswer] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchStats();
    loadContent();
  }, [currentView]);

  const fetchStats = async () => {
    try {
      const data = await api.getStats();
      setStats(data);
    } catch (err) { console.error(err); }
  };

  const loadContent = async () => {
    try {
      if (currentView === 'notes') {
        const data = await api.listMemories('note');
        setNotes(data);
        if (data.length > 0 && !selectedNote) setSelectedNote(data[0]);
      } else if (currentView === 'tasks') {
        const data = await api.listMemories('task');
        setTasks(data);
      }
    } catch (err) { console.error(err); }
  };

  const handleSaveNote = async () => {
    if (!noteInput.trim()) return;
    setLoading(true);
    try {
      await api.ingest(noteInput, 'note');
      setNoteInput('');
      await loadContent();
      fetchStats();
    } catch (err) { console.error(err); }
    finally { setLoading(false); }
  };

  const handleSaveTask = async () => {
    if (!taskInput.trim()) return;
    setLoading(true);
    try {
      await api.ingest(taskInput, 'task');
      setTaskInput('');
      await loadContent();
      fetchStats();
    } catch (err) { console.error(err); }
    finally { setLoading(false); }
  };

  const handleChat = async () => {
    if (!chatInput.trim()) return;
    setLoading(true);
    setChatAnswer(null);
    try {
      const answer = await api.query(chatInput);
      setChatAnswer(answer);
    } catch (err) { console.error(err); }
    finally { setLoading(false); }
  };

  return (
    <div className="flex h-screen bg-[#020203] text-[#f8fafc] font-sans overflow-hidden">

      {/* 
        --- SIDEBAR --- 
        Using a very deep navy/black for the sidebar to separate it from the main content.
      */}
      <aside className="w-20 md:w-72 border-r border-white-[0.05] bg-[#08090b] flex flex-col py-10 px-6 gap-10 z-20">
        <div className="flex items-center gap-4 px-2">
          <div className="w-12 h-12 bg-gradient-to-tr from-[#6366f1] to-[#a855f7] rounded-[14px] flex items-center justify-center text-white font-black text-2xl shadow-[0_0_20px_rgba(99,102,241,0.3)] shrink-0">
            Ω
          </div>
          <div className="hidden md:block">
            <h1 className="text-sm font-black tracking-[0.2em] text-white">SS PERSONAL</h1>
            <p className="text-[10px] text-[#475569] font-bold tracking-widest uppercase">Memory OS v1</p>
          </div>
        </div>

        <nav className="flex flex-col gap-3 flex-1 w-full">
          <NavItem
            active={currentView === 'notes'}
            onClick={() => setCurrentView('notes')}
            icon="󱞒"
            label="Knowledge"
            activeColor="bg-indigo-500"
          />
          <NavItem
            active={currentView === 'tasks'}
            onClick={() => setCurrentView('tasks')}
            icon="󰄬"
            label="Objectives"
            activeColor="bg-sky-500"
          />
          <NavItem
            active={currentView === 'chat'}
            onClick={() => setCurrentView('chat')}
            icon="󰚩"
            label="Neural Hub"
            activeColor="bg-violet-500"
          />
        </nav>

        {/* Brain Stats Section */}
        <div className="hidden md:flex flex-col gap-5 p-6 rounded-[24px] bg-white/[0.03] border border-white/[0.05]">
          <div className="flex items-center gap-2">
            <span className="w-1.5 h-1.5 bg-indigo-500 rounded-full animate-pulse shadow-[0_0_8px_rgba(99,102,241,0.8)]"></span>
            <span className="text-[10px] uppercase font-black tracking-[0.2em] text-[#64748b]">System Core</span>
          </div>
          <div className="space-y-4">
            <div className="flex flex-col">
              <span className="text-[10px] text-[#475569] uppercase font-bold tracking-wider">Indexed Documents</span>
              <span className="text-xl font-bold tabular-nums text-white">{stats?.vector_count ?? 0}</span>
            </div>
            <div className="flex flex-col">
              <span className="text-[10px] text-[#475569] uppercase font-bold tracking-wider">Active Relations</span>
              <span className="text-xl font-bold tabular-nums text-emerald-400">{stats?.graph_count ?? 0}</span>
            </div>
          </div>
        </div>
      </aside>

      {/* --- MAIN CONTENT CANVAS --- */}
      <main className="flex-1 relative overflow-hidden flex flex-col bg-[#020203]">
        {/* Cinematic Glow Backgrounds */}
        <div className="absolute top-0 right-0 w-[800px] h-[800px] bg-indigo-500/[0.04] blur-[150px] rounded-full -mr-80 -mt-80 pointer-events-none"></div>
        <div className="absolute bottom-0 left-0 w-[800px] h-[800px] bg-sky-500/[0.03] blur-[150px] rounded-full -ml-80 -mb-80 pointer-events-none"></div>

        {/* --- KNOWLEDGE/NOTES VIEW --- */}
        {currentView === 'notes' && (
          <div className="flex-1 flex overflow-hidden animate-in fade-in zoom-in-95 duration-700">
            {/* Folder / Sidebar */}
            <div className="w-80 border-r border-white-[0.05] flex flex-col bg-[#050608]">
              <div className="p-8 border-b border-white-[0.05] flex justify-between items-center bg-[#08090b]">
                <h2 className="text-sm font-black tracking-[0.2em] uppercase text-white">Archive</h2>
                <button
                  onClick={() => { setSelectedNote(null); setNoteInput(''); }}
                  className="w-10 h-10 rounded-xl bg-indigo-500/10 text-indigo-400 flex items-center justify-center hover:bg-indigo-500/20 transition-all border border-indigo-500/10 shadow-lg shadow-indigo-500/5 group"
                >
                  <span className="text-2xl group-hover:scale-125 transition-transform">+</span>
                </button>
              </div>
              <div className="flex-1 overflow-y-auto p-4 space-y-3 scrollbar-hide">
                {notes.map(note => (
                  <div
                    key={note.id}
                    onClick={() => setSelectedNote(note)}
                    className={`p-5 rounded-2xl cursor-pointer transition-all duration-300 border ${selectedNote?.id === note.id ? 'bg-[#1e1b4b]/50 border-indigo-500/30' : 'hover:bg-white/[0.03] border-transparent'}`}
                  >
                    <div className="font-bold truncate text-sm text-[#f1f5f9]">{note.content.split('\n')[0]}</div>
                    <div className="flex justify-between items-center mt-3">
                      <span className={`text-[10px] font-bold uppercase tracking-widest ${selectedNote?.id === note.id ? 'text-indigo-400' : 'text-[#475569]'}`}>
                        {note.metadata?.timestamp ? new Date(note.metadata.timestamp).toLocaleDateString() : 'Dec 20'}
                      </span>
                      <div className="w-1 h-1 bg-white/20 rounded-full"></div>
                    </div>
                  </div>
                ))}
                {notes.length === 0 && <p className="text-center text-[#475569] mt-20 italic text-sm font-bold uppercase tracking-[0.2em]">Memories Blank</p>}
              </div>
            </div>

            {/* Workspace Area */}
            <div className="flex-1 flex flex-col p-12 md:p-24 overflow-y-auto scrollbar-hide">
              {selectedNote ? (
                <div className="flex-1 flex flex-col gap-10 max-w-4xl mx-auto w-full">
                  <div className="flex items-center gap-4">
                    <div className="h-[1px] w-8 bg-indigo-500"></div>
                    <div className="text-indigo-500 font-black text-[10px] uppercase tracking-[0.4em] select-none">
                      Retrieved Node
                    </div>
                  </div>
                  <div className="text-4xl font-black text-white leading-snug whitespace-pre-wrap tracking-tighter">
                    {selectedNote.content}
                  </div>
                  {selectedNote.metadata?.summary && (
                    <div className="mt-16 bg-white/[0.02] p-10 rounded-[32px] border border-white/[0.06] relative shadow-2xl">
                      <div className="absolute -top-4 left-10 bg-[#020203] px-4 py-1 border border-white/[0.06] rounded-full text-[10px] font-black tracking-widest text-[#64748b] uppercase">AI Summary</div>
                      <p className="italic text-[#94a3b8] text-2xl leading-relaxed font-medium">
                        "{selectedNote.metadata.summary}"
                      </p>
                    </div>
                  )}
                </div>
              ) : (
                <div className="flex-1 flex flex-col gap-8 max-w-4xl mx-auto w-full">
                  <div className="flex items-center gap-4">
                    <div className="h-[1px] w-8 bg-indigo-500 animate-pulse"></div>
                    <div className="text-indigo-500 font-black text-[10px] uppercase tracking-[0.4em] select-none">
                      Input Capture
                    </div>
                  </div>
                  <textarea
                    value={noteInput}
                    onChange={(e) => setNoteInput(e.target.value)}
                    className="flex-1 bg-transparent text-5xl font-black outline-none placeholder:text-[#1e1e24] leading-tight resize-none mt-8 tracking-tighter text-white"
                    placeholder="What's the thought?"
                  />
                  <div className="flex justify-end p-8">
                    <button
                      onClick={handleSaveNote}
                      disabled={loading || !noteInput.trim()}
                      className="bg-indigo-600 hover:bg-indigo-500 disabled:opacity-20 px-12 py-5 rounded-[22px] font-black uppercase text-[11px] tracking-[0.3em] transition-all shadow-[0_20px_40px_-10px_rgba(79,70,229,0.3)] text-white hover:scale-105 active:scale-95"
                    >
                      {loading ? 'Synthesizing...' : 'Commit to Brain'}
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>
        )}

        {/* --- OBJECTIVES/TASKS VIEW --- */}
        {currentView === 'tasks' && (
          <div className="flex-1 max-w-5xl mx-auto w-full p-12 md:p-32 flex flex-col gap-20 animate-in fade-in slide-in-from-right-12 duration-1000">
            <header className="space-y-4">
              <div className="flex items-center gap-4 mb-2">
                <div className="w-12 h-1 bg-sky-500 rounded-full shadow-[0_0_12px_rgba(14,165,233,0.8)]"></div>
                <span className="text-xs font-black tracking-[0.4em] text-sky-500 uppercase">Strategic Objectives</span>
              </div>
              <h2 className="text-8xl font-black tracking-tighter text-white">Action <br />Items</h2>
            </header>

            <div className="relative group max-w-3xl">
              <div className="absolute -inset-1 bg-gradient-to-r from-sky-500 to-indigo-500 rounded-[40px] blur-2xl opacity-10 group-focus-within:opacity-30 transition duration-1000"></div>
              <div className="relative bg-[#0d0d10] p-3 rounded-[34px] border border-white/[0.08] flex items-center shadow-2xl">
                <input
                  value={taskInput}
                  onChange={(e) => setTaskInput(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && handleSaveTask()}
                  className="flex-1 bg-transparent p-6 text-2xl outline-none placeholder:text-[#2d2d35] font-black tracking-tight"
                  placeholder="Insert new mission..."
                />
                <button
                  onClick={handleSaveTask}
                  className="bg-sky-500 hover:bg-sky-400 px-12 py-5 rounded-[24px] text-white font-black uppercase tracking-[0.2em] text-[10px] transition-all shadow-xl shadow-sky-900/40 active:scale-95"
                >
                  Create
                </button>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-10">
              {tasks.map(task => (
                <div key={task.id} className="group flex flex-col gap-6 p-10 bg-white/[0.02] border border-white/[0.03] rounded-[40px] hover:bg-white/[0.04] transition-all duration-500 hover:border-white/[0.08]">
                  <div className="w-12 h-12 rounded-2xl border-2 border-white/[0.05] group-hover:border-sky-500/50 flex items-center justify-center transition-all bg-[#080808]">
                    <div className="w-4 h-4 bg-sky-500 rounded-lg opacity-0 group-hover:opacity-100 transition-all scale-50 group-hover:scale-100 shadow-[0_0_15px_rgba(14,165,233,1)]"></div>
                  </div>
                  <div className="space-y-4">
                    <p className="text-3xl font-black text-[#94a3b8] group-hover:text-white transition-colors tracking-tight leading-tight">{task.content}</p>
                    <p className="text-[10px] text-[#475569] uppercase tracking-[0.3em] font-black">
                      {task.metadata?.timestamp ? new Date(task.metadata.timestamp).toLocaleTimeString() : 'Mission Logged'}
                    </p>
                  </div>
                </div>
              ))}
              {tasks.length === 0 && (
                <div className="col-span-full py-32 text-center flex flex-col items-center gap-10 opacity-10 animate-pulse">
                  <span className="text-[120px] filter grayscale">🛰️</span>
                  <p className="uppercase tracking-[1.5em] font-black text-xs">Orbit Clear</p>
                </div>
              )}
            </div>
          </div>
        )}

        {/* --- NEURAL HUB / CHAT VIEW --- */}
        {currentView === 'chat' && (
          <div className="flex-1 flex flex-col max-w-6xl mx-auto w-full p-12 md:p-24 animate-in fade-in zoom-in-105 duration-1000">
            <div className="flex-1 flex flex-col gap-20 justify-center pb-48">
              {chatAnswer ? (
                <div className="space-y-12 animate-in fade-in slide-in-from-bottom-12 duration-1000">
                  <div className="flex items-center gap-6">
                    <div className="w-16 h-16 rounded-[24px] bg-indigo-500/10 text-indigo-500 flex items-center justify-center text-3xl shadow-inner border border-indigo-500/10">Ψ</div>
                    <div>
                      <span className="text-[11px] uppercase font-black tracking-[0.5em] text-indigo-500/80">Neural Output</span>
                      <p className="text-[10px] text-[#475569] font-bold uppercase tracking-widest mt-1">Sourced from Multimodal Memory</p>
                    </div>
                  </div>
                  <div className="text-5xl font-black text-white leading-[1.15] tracking-tighter first-letter:text-8xl first-letter:mr-2 first-letter:float-left first-letter:text-indigo-500">
                    {chatAnswer}
                  </div>
                </div>
              ) : !loading && (
                <div className="text-center space-y-16 opacity-30 select-none">
                  <div className="text-[160px] leading-none font-black text-white mix-blend-overlay opacity-10 drop-shadow-2xl">Ω</div>
                  <div className="space-y-4">
                    <h2 className="text-4xl font-black uppercase tracking-[0.8em] text-white">Synapse Hub</h2>
                    <p className="text-2xl max-w-xl mx-auto leading-relaxed font-bold text-[#64748b]">Bridge the gap between your ideas and actions.</p>
                  </div>
                  <div className="flex justify-center flex-wrap gap-4">
                    <SuggestionChip text="Status report" onClick={() => setChatInput("Give me a brief status report of my tasks.")} color="border-sky-500/20" />
                    <SuggestionChip text="Recall deep notes" onClick={() => setChatInput("Find my most important notes on technology.")} color="border-indigo-500/20" />
                  </div>
                </div>
              )}

              {loading && (
                <div className="flex flex-col items-center gap-16 py-20">
                  <div className="relative">
                    <div className="w-32 h-32 border-[12px] border-indigo-500/5 border-t-indigo-500 rounded-full animate-spin"></div>
                    <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-16 h-16 bg-indigo-500/20 rounded-full blur-2xl animate-pulse"></div>
                  </div>
                  <div className="text-center space-y-4">
                    <span className="text-lg font-black tracking-[1em] text-indigo-500 uppercase animate-pulse ml-[1em]">Scanning Core</span>
                    <p className="text-[10px] text-[#475569] tracking-[0.4em] uppercase font-black">Interrogating ChromaDB + Neo4j</p>
                  </div>
                </div>
              )}
            </div>

            {/* Neural Input Dock */}
            <div className="absolute bottom-16 left-1/2 -translate-x-1/2 w-full max-w-4xl px-12 z-40">
              <div className="bg-[#0f1115]/90 backdrop-blur-3xl p-4 rounded-[48px] border border-white/[0.08] shadow-[0_50px_100px_-20px_rgba(0,0,0,0.8)] flex items-center gap-6 group hover:border-white/[0.15] transition-all">
                <input
                  value={chatInput}
                  onChange={(e) => setChatInput(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && handleChat()}
                  className="flex-1 bg-transparent p-6 text-3xl outline-none placeholder:text-[#1e2026] pr-0 font-black tracking-tight text-white"
                  placeholder="Enter Neural Query..."
                />
                <button
                  onClick={handleChat}
                  disabled={loading || !chatInput.trim()}
                  className="w-20 h-20 bg-white text-black rounded-[40px] flex items-center justify-center hover:scale-[1.05] active:scale-95 transition-all shadow-2xl disabled:opacity-5 disabled:scale-100 shrink-0"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14" /><path d="m12 5 7 7-7 7" /></svg>
                </button>
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

function NavItem({ active, onClick, icon, label, activeColor }: { active: boolean; onClick: () => void; icon: string; label: string; activeColor: string }) {
  return (
    <button
      onClick={onClick}
      className={`group flex items-center gap-6 p-6 rounded-[30px] transition-all duration-500 w-full relative overflow-hidden ${active ? `bg-white/[0.04]` : 'text-[#475569] hover:bg-white/[0.02] hover:text-[#94a3b8]'}`}
    >
      <span className={`text-4xl leading-none font-serif transition-all duration-700 ${active ? 'text-white' : 'grayscale opacity-40 group-hover:grayscale-0 group-hover:opacity-100'}`}>
        {icon}
      </span>
      <span className={`hidden md:block font-black uppercase text-[11px] tracking-[0.2em] transition-all duration-500 ${active ? 'text-white translate-x-2' : 'group-hover:translate-x-1'}`}>
        {label}
      </span>
      {active && (
        <div className={`absolute left-0 top-1/2 -translate-y-1/2 w-1.5 h-12 ${activeColor} rounded-r-full shadow-[0_0_20px_rgba(99,102,241,1)]`}></div>
      )}
    </button>
  );
}

function SuggestionChip({ text, onClick, color }: { text: string; onClick: () => void; color: string }) {
  return (
    <button
      onClick={onClick}
      className={`px-8 py-3 rounded-full border ${color} text-[10px] uppercase font-black tracking-[0.2em] text-[#475569] hover:border-white/20 hover:text-white transition-all bg-white/[0.02] active:scale-95`}
    >
      {text}
    </button>
  );
}
