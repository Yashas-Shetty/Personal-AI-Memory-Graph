from app.memory.graph.client import GraphClient
import logging

logger = logging.getLogger(__name__)

def get_graph_context(entity_name: str):
    """
    Fetch the entity and its immediate relationships from Neo4j.
    """
    client = GraphClient()
    query = (
        "MATCH (e:Entity {name: $name})-[r]-(neighbor:Entity) "
        "RETURN e.name as source, type(r) as relationship, neighbor.name as target"
    )
    
    context_strings = []
    try:
        with client.get_session() as session:
            result = session.run(query, name=entity_name)
            for record in result:
                context_strings.append(
                    f"{record['source']} -[{record['relationship']}]-> {record['target']}"
                )
    except Exception as e:
        logger.error(f"Error fetching graph context for {entity_name}: {e}")
        
    return context_strings
