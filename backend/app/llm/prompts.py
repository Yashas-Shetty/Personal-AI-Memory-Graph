"""
Prompt templates for Gemini LLM.
"""

# Template for reasoning over retrieved context
REASONING_PROMPT = """
You are a Personal AI Memory Assistant. Use the following retrieved context from the user's long-term memory to answer their question. 

If the context isn't sufficient, answer honestly based on what you have, and avoid making up facts.

Retrieved Context:
{context}

User Question: "{query}"

Answer the question concisely and highlight how this information relates to their past activities or goals.
"""

# Template for extracting entities and relationships from text
ENTITY_EXTRACTION_PROMPT = """
Analyze the following text and extract entities (concepts, tools, goals, tasks) and their relationships.

Text: "{text}"

Return the result as a Valid JSON object matching this structure:
{{
    "entities": ["list", "of", "unique", "entity", "names"],
    "relationships": [
        {{
            "source": "EntityName",
            "target": "TargetEntityName",
            "type": "RELATIONSHIP_TYPE"
        }}
    ]
}}

Rules:
- Entities should be simple strings.
- Relationship types MUST be one of: {valid_types}.
- Do not create self-referencing relationships (source == target).
- Ensure JSON output.
"""
