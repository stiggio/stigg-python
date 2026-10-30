# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EntityTypeCheckActiveEntitiesResponse", "Data"]


class Data(BaseModel):
    """Whether an entity type has active entities"""

    has_active_entities: bool = FieldInfo(alias="hasActiveEntities")
    """
    Whether at least one active (non-archived) entity of the entity type exists,
    across every customer
    """


class EntityTypeCheckActiveEntitiesResponse(BaseModel):
    """Wrapped response with whether an entity type has active entities"""

    data: Data
    """Whether an entity type has active entities"""
