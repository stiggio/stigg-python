# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["AssignmentUpsertParams", "Assignment"]


class AssignmentUpsertParams(TypedDict, total=False):
    assignments: Required[Iterable[Assignment]]
    """Assignments to upsert (1–100 per request)"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]


class Assignment(TypedDict, total=False):
    """A single assignment to create or update.

    The natural key is the `(entityId, capabilityId)` pair. On create both `usageLimit` and `cadence` are required; on update they may be omitted individually to preserve the existing value.
    """

    capability_id: Required[Annotated[str, PropertyInfo(alias="capabilityId")]]
    """The capability refId this assignment grants"""

    entity_id: Required[Annotated[str, PropertyInfo(alias="entityId")]]
    """The entity refId this assignment is attached to"""

    cadence: Literal["MONTH"]
    """Usage-reset cadence (required on create). Currently only `MONTH` is supported"""

    usage_limit: Annotated[float, PropertyInfo(alias="usageLimit")]
    """Maximum usage allowed within one cadence window (required on create)"""
