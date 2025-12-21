const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';
console.log('Frontend API URL:', API_URL);

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

  async ingest(text: string, source: string = 'note'): Promise<IngestResponse> {
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

    // If FastAPI returns a validation error or 404, it's an object with a 'detail' key
    if (data && typeof data === 'object' && data.detail) {
      throw new Error(typeof data.detail === 'string' ? data.detail : JSON.stringify(data.detail));
    }

    return data; // Should be a string now
  },

  async reset(): Promise<any> {
    const res = await fetch(`${API_URL}/memory/clear`, { method: 'POST' });
    return res.json();
  },

  async listMemories(source?: string): Promise<any[]> {
    const url = source ? `${API_URL}/memory/list?source=${source}` : `${API_URL}/memory/list`;
    const res = await fetch(url);
    const data = await res.json();
    return data.memories || [];
  }
};
