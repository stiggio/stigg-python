# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["EntityTypeListResponse"]


class EntityTypeListResponse(BaseModel):
    """A vendor-defined category of resource that can be governed (e.g.

    Org, Team, User). Vendors define entity types once per environment; their customers create instances (entities) of these types and the governance engine tracks usage and enforces limits per instance.
    """

    id: str
    """The unique identifier for the entity"""

    attribution_keys: List[str] = FieldInfo(alias="attributionKeys")
    """Dimension keys used to attribute usage events to instances of this type (e.g.

    ["orgId"]). Empty array means no attribution.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    display_name: str = FieldInfo(alias="displayName")
    """The display name for the entity type"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""
