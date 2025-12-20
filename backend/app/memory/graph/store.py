import logging

logger = logging.getLogger(__name__)


import logging
from app.memory.graph.client import GraphClient

logger = logging.getLogger(__name__)


class GraphMemoryStore:
    """
    Graph memory storage using Neo4j.
    """

    def __init__(self):
        self.client = GraphClient()

    def store_memory(self, payload: dict) -> None:
        """
        Store entities and relationships into graph database.
        """
        extraction = payload.get("extraction")
        if not extraction:
            logger.warning("No extraction data found in payload for Graph Store.")
            return

        entities = extraction.get("entities", [])
        relationships = extraction.get("relationships", [])

        if not entities:
            logger.info("No entities to store in Graph.")
            return

        logger.info(f"Storing {len(entities)} entities and {len(relationships)} relationships in Neo4j")

        with self.client.get_session() as session:
            # 1. Create/Merge Entities
            for entity_name in entities:
                session.execute_write(self._merge_entity, entity_name)

            # 2. Create/Merge Relationships
            for rel in relationships:
                # rel is a dict if extraction was dict()
                source = rel.get("source")
                target = rel.get("target")
                rel_type = rel.get("type")
                if source and target and rel_type:
                    session.execute_write(
                        self._merge_relationship, source, target, rel_type
                    )

    @staticmethod
    def _merge_entity(tx, name: str):
        query = "MERGE (e:Entity {name: $name})"
        tx.run(query, name=name)

    @staticmethod
    def _merge_relationship(tx, source: str, target: str, rel_type: str):
        # Note: Cypher doesn't support dynamic relationship types via parameters easily 
        # but for this specific set of types we can secure it or use simple string concat 
        # if the types are validated (which they are in our schema).
        query = (
            f"MATCH (s:Entity {{name: $source}}), (t:Entity {{name: $target}}) "
            f"MERGE (s)-[:{rel_type}]->(t)"
        )
        tx.run(query, source=source, target=target)
