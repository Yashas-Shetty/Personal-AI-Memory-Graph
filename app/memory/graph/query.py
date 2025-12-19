"""
Cypher query builders for Neo4j.
"""

def build_entity_query(entity_name: str):
    return f"MATCH (n:Entity {{name: '{entity_name}'}}) RETURN n"
