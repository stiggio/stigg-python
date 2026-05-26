# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["EntityUpsertResponse", "Data"]


class Data(BaseModel):
    """A stored entity instance tracked by the governance service for a given customer"""

    id: str
    """The unique identifier for the entity"""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """Timestamp of when the record was deleted"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    metadata: Dict[str, str]
    """Free-form key/value metadata attached to the entity"""

    type_id: str = FieldInfo(alias="typeId")
    """The entity type identifier this entity instantiates"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""


class EntityUpsertResponse(BaseModel):
    """List of entities created or updated by an upsert request"""

    data: List[Data]
