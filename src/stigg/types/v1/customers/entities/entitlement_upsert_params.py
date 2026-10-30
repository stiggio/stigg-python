# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["EntitlementUpsertParams", "EntityEntitlement"]


class EntitlementUpsertParams(TypedDict, total=False):
    entity_entitlements: Required[Annotated[Iterable[EntityEntitlement], PropertyInfo(alias="entityEntitlements")]]
    """Entity entitlements to upsert (1–100 per request)"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]


class EntityEntitlement(TypedDict, total=False):
    """A single entity entitlement to create or update.

    Identify the feature or currency with exactly one of `featureId` or `currencyId`. The natural key is the `(entityId, featureId or currencyId, scopeEntityIds)` triple. On create both `usageLimit` and `cadence` are required; on update they may be omitted individually to preserve the existing value.
    """

    entity_id: Required[Annotated[str, PropertyInfo(alias="entityId")]]
    """The entity ID this entity entitlement is attached to"""

    cadence: str
    """
    Usage-reset cadence (required on create) as an ISO-8601 single-unit duration,
    e.g. `P1M`, `P30D`, `PT1M`.
    """

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """Currency ID this entity entitlement grants (credit limits).

    Mutually exclusive with `featureId`.
    """

    feature_id: Annotated[str, PropertyInfo(alias="featureId")]
    """Feature ID this entity entitlement grants.

    Mutually exclusive with `currencyId`.
    """

    parent_id: Annotated[Optional[str], PropertyInfo(alias="parentId")]
    """Parent entity ID in the hierarchy.

    Omit to leave the current parent untouched (a new node defaults to a root);
    `null` detaches to a root; an ID sets or changes the parent. Reparenting or
    detaching an existing node is leaf-only; place a parent before its children, or
    in the same batch.
    """

    scope_entity_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="scopeEntityIds")]
    """
    Dimension-scoped sub-limit: the set of entity IDs this limit applies to
    (order-insensitive, unique, at most 5). Omit or leave empty for the node-wide
    limit.
    """

    usage_limit: Annotated[Optional[float], PropertyInfo(alias="usageLimit")]
    """Maximum usage allowed within one cadence window (required on create)"""
