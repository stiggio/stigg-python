# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["AssignmentUpsertParams", "Assignment"]


class AssignmentUpsertParams(TypedDict, total=False):
    assignments: Required[Iterable[Assignment]]
    """Assignments to upsert (1–100 per request)"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]


class Assignment(TypedDict, total=False):
    """A single assignment to create or update.

    Identify the capability with exactly one of `featureId` or `currencyId`. The natural key is the `(entityId, capability, scopeEntityIds)` triple. On create both `usageLimit` and `cadence` are required; on update they may be omitted individually to preserve the existing value.
    """

    entity_id: Required[Annotated[str, PropertyInfo(alias="entityId")]]
    """The entity refId this assignment is attached to"""

    cadence: Literal["MONTH"]
    """Usage-reset cadence (required on create). Currently only `MONTH` is supported"""

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """Currency refId this assignment grants (credit budgets).

    Mutually exclusive with `featureId`.
    """

    feature_id: Annotated[str, PropertyInfo(alias="featureId")]
    """Feature refId this assignment grants. Mutually exclusive with `currencyId`."""

    parent_id: Annotated[Optional[str], PropertyInfo(alias="parentId")]
    """Parent entity refId in the hierarchy.

    Omit to leave the current parent untouched (a new node defaults to a root);
    `null` detaches to a root; a refId sets or changes the parent. Reparenting an
    existing node is leaf-only.
    """

    scope_entity_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="scopeEntityIds")]

    usage_limit: Annotated[float, PropertyInfo(alias="usageLimit")]
    """Maximum usage allowed within one cadence window (required on create)"""
