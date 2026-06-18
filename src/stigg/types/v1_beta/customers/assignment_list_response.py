# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AssignmentListResponse"]


class AssignmentListResponse(BaseModel):
    """A capability assignment for an entity belonging to a customer.

    Defines how much of the capability the entity may consume (`usageLimit`) and how often the counter resets (`cadence`).
    """

    id: str
    """Synthetic UUID identifier — also the cursor anchor for paginated lists"""

    cadence: Literal["MONTH"]
    """Usage-reset cadence. Currently only `MONTH` is supported"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    entity_id: str = FieldInfo(alias="entityId")
    """The entity refId this assignment is attached to"""

    parent_id: Optional[str] = FieldInfo(alias="parentId", default=None)
    """Parent entity refId in the hierarchy, or `null` for a root."""

    scope_entity_ids: List[str] = FieldInfo(alias="scopeEntityIds")
    """Dimension-scoped sub-budget key: the set of entity refIds this budget applies
    to.

    Empty is the node-wide budget that always matches; a non-empty set only applies
    when every listed entity is present in the resolved set (order-insensitive).
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""

    usage_limit: Optional[float] = FieldInfo(alias="usageLimit", default=None)
    """Maximum usage allowed within one cadence window"""

    currency_id: Optional[str] = FieldInfo(alias="currencyId", default=None)
    """Currency refId this assignment grants (present for credit capabilities)."""

    feature_id: Optional[str] = FieldInfo(alias="featureId", default=None)
    """Feature refId this assignment grants (present for feature capabilities)."""
