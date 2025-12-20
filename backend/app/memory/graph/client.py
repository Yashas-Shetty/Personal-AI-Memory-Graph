"""
Graph memory client (Neo4j placeholder).
"""

from neo4j import GraphDatabase
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)

class GraphClient:
    """
    Client for interacting with Neo4j Graph Database.
    """
    def __init__(self):
        self.uri = settings.NEO4J_URI
        self.user = settings.NEO4J_USER
        self.password = settings.NEO4J_PASSWORD
        self.driver = None

    def connect(self):
        """Establish connection to Neo4j."""
        try:
            self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
            self.driver.verify_connectivity()
            logger.info("Successfully connected to Neo4j.")
        except Exception as e:
            logger.error(f"Failed to connect to Neo4j: {e}")
            raise

    def close(self):
        """Close Neo4j connection."""
        if self.driver:
            self.driver.close()
            logger.info("Neo4j connection closed.")

    def get_session(self):
        """Returns a new Neo4j session."""
        if not self.driver:
            self.connect()
        return self.driver.session()

    def count_nodes(self) -> int:
        """Return the total number of nodes in the graph."""
        with self.get_session() as session:
            result = session.run("MATCH (n) RETURN count(n) as count")
            return result.single()["count"]

    def clear_database(self):
        """Delete everything from the graph."""
        with self.get_session() as session:
            session.run("MATCH (n) DETACH DELETE n")
            logger.info("Graph database cleared.")
