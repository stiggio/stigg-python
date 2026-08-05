# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["CustomerRetrieveGovernanceResponse", "Data", "Pagination"]


class Data(BaseModel):
    """
    A node of the governance hierarchy tree with its usage configuration (limit, cadence, scope) and current usage. Usage is read from a periodically-refreshed read model and may lag the live counter by a short interval; it never gates access.
    """

    cadence: Optional[str] = None
    """Usage-reset cadence as an ISO-8601 single-unit duration, e.g.

    `P1M`, `P30D`, `PT1M`; `null` when the node has no usage configuration.
    """

    current_usage: Optional[float] = FieldInfo(alias="currentUsage", default=None)
    """
    Usage consumed in the current cadence period (may lag the live counter by a
    short interval).
    """

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """
    Human-readable name of the entity, or null when none is set (display the entity
    id instead).
    """

    entity_id: str = FieldInfo(alias="entityId")
    """External id of the entity at this node."""

    entity_type_id: str = FieldInfo(alias="entityTypeId")
    """External id of the entity type (e.g. `team`, `user`)."""

    parent_id: Optional[str] = FieldInfo(alias="parentId", default=None)
    """External id of the parent entity in the tree.

    `null` means the entity is either a root or not yet placed in the hierarchy —
    placement rides on an assignment, so an entity with no limits set has no parent
    yet. Both render at the top level; use it to rebuild the tree.
    """

    scope_entity_ids: List[str] = FieldInfo(alias="scopeEntityIds")
    """The configuration scope (entity ids).

    Empty is the node-wide configuration; a non-empty set is a dimension-scoped
    sub-configuration.
    """

    usage_limit: Optional[float] = FieldInfo(alias="usageLimit", default=None)
    """Hard usage limit for this node per cadence period."""

    usage_period_end: Optional[datetime] = FieldInfo(alias="usagePeriodEnd", default=None)
    """Exclusive end of the cadence period in progress now — when usage resets.

    `null` when the node has no usage configuration, or when a stored cadence cannot
    be parsed.
    """

    usage_period_start: Optional[datetime] = FieldInfo(alias="usagePeriodStart", default=None)
    """
    Start of the cadence period in progress now, derived from the cadence and the
    assignment anchor — it stays correct across a rollover. `null` when the node has
    no usage configuration, or when a stored cadence cannot be parsed.
    """

    utilization: Optional[float] = None
    """`currentUsage / usageLimit` (1 when usageLimit is 0 — always at limit).

    The cross-capability-safe sort key.
    """

    currency_id: Optional[str] = FieldInfo(alias="currencyId", default=None)
    """
    The metered currency ID (present when the configured capability is a credit
    currency).
    """

    feature_id: Optional[str] = FieldInfo(alias="featureId", default=None)
    """The metered feature ID (present when the configured capability is a feature)."""


class Pagination(BaseModel):
    next: Optional[str] = None
    """
    Cursor for fetching the next page of results, or null if no additional pages
    exist
    """


class CustomerRetrieveGovernanceResponse(BaseModel):
    """
    Paginated list of governance tree nodes, each with its usage configuration and current usage.
    """

    data: List[Data]

    pagination: Pagination
