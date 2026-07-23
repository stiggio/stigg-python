# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["CustomerRetrieveGovernanceParams"]


class CustomerRetrieveGovernanceParams(TypedDict, total=False):
    after: str
    """Return items that come after this cursor"""

    currency_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="currencyIds")]
    """Currency ids to include, repeated per value (e.g.

    `?currencyIds=credits`). Omit both featureIds and currencyIds for tree mode.
    """

    entity_id_search: Annotated[str, PropertyInfo(alias="entityIdSearch")]
    """Case-insensitive substring match on the entity id (`%`/`_` matched literally)."""

    entity_type_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="entityTypeIds")]
    """Filter to one or more entity types, repeated per value (e.g.

    `?entityTypeIds=team&entityTypeIds=user`).
    """

    feature_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="featureIds")]
    """Feature ids to include, repeated per value (e.g.

    `?featureIds=ai-tokens&featureIds=seats`). Omit both featureIds and currencyIds
    for tree mode — every node in the hierarchy with no usage configuration
    attached.
    """

    limit: int
    """Maximum number of items to return"""

    min_utilization: Annotated[float, PropertyInfo(alias="minUtilization")]
    """Only nodes with utilization ≥ this value (e.g.

    0.8 for ≥80%, 1 for at/over limit).
    """

    order: Literal["asc", "desc"]
    """Sort direction: `asc` or `desc` (default `desc`)."""

    scope: Literal["all", "nodeWide", "scoped"]
    """
    Filter by configuration scope: `all` (default), `nodeWide` (`[]` only), or
    `scoped` (non-empty only).
    """

    sort_by: Annotated[
        Literal["utilization", "currentUsage", "usageLimit", "scopeSize", "id", "createdAt"],
        PropertyInfo(alias="sortBy"),
    ]
    """
    Sort key: `utilization` (default, cross-capability-safe), `currentUsage`,
    `usageLimit`, `scopeSize`, `id`, or `createdAt`.
    """

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
