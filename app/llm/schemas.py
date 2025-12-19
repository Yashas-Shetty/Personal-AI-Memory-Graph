"""
Pydantic models for Gemini LLM extraction with strict validation.
"""

from typing import List, Literal, Optional
from pydantic import BaseModel, Field, field_validator, model_validator

# Allowed relationship types
RelationshipType = Literal[
    "LEARNING",
    "USED_FOR",
    "DEPENDS_ON",
    "RELATED_TO",
    "GOAL_IS",
    "REQUIRES"
]


class Entity(BaseModel):
    """
    Represents an extracted entity.
    """
    name: str = Field(..., description="The name of the entity")
    type: str = Field(..., description="The type of the entity (e.g., SKILL, TOOL, GOAL, PROJECT)")

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Entity name must not be empty")
        return v.strip()


class Relationship(BaseModel):
    """
    Represents a relationship between two entities.
    """
    source: str = Field(..., description="The name of the source entity")
    target: str = Field(..., description="The name of the target entity")
    type: str = Field(..., description="The type of relationship")

    @field_validator("type")
    @classmethod
    def type_must_be_uppercase(cls, v: str) -> str:
        return v.upper()

    @model_validator(mode='after')
    def check_self_reference(self) -> 'Relationship':
        if self.source.lower() == self.target.lower():
            raise ValueError("Self-referencing relationships are not allowed")
        return self


class ExtractionResult(BaseModel):
    """
    Container for extracted entities and relationships.
    """
    entities: List[str] = Field(..., description="List of unique entity names")
    relationships: List[Relationship] = Field(default_factory=list, description="List of extracted relationships")

    @field_validator("entities")
    @classmethod
    def unique_entities(cls, v: List[str]) -> List[str]:
        return list(set(e.strip() for e in v if e and e.strip()))
