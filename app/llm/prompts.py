"""
Prompt templates for Gemini LLM.
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
