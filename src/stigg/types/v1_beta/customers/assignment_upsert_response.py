# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AssignmentUpsertResponse", "Data"]


class Data(BaseModel):
    """A capability assignment for an entity belonging to a customer.

    Defines how much of the capability the entity may consume (`usageLimit`) and how often the counter resets (`cadence`).
    """

    id: str
    """Synthetic UUID identifier — also the cursor anchor for paginated lists"""

    cadence: Literal["MONTH"]
    """Usage-reset cadence. Currently only `MONTH` is supported"""

    capability_id: str = FieldInfo(alias="capabilityId")
    """The capability refId this assignment grants"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    entity_id: str = FieldInfo(alias="entityId")
    """The entity refId this assignment is attached to"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""

    usage_limit: float = FieldInfo(alias="usageLimit")
    """Maximum usage allowed within one cadence window"""


class AssignmentUpsertResponse(BaseModel):
    """Assignments after upsert."""

    data: List[Data]
