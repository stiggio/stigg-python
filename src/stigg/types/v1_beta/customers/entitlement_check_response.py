# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "EntitlementCheckResponse",
    "Data",
    "DataFeature",
    "DataFeatureChain",
    "DataFeatureFeature",
    "DataCredit",
    "DataCreditCurrency",
    "DataCreditChain",
]


class DataFeatureChain(BaseModel):
    """
    Per-entity governance node — limit and current usage for a single resolved entity.
    """

    current_usage: float = FieldInfo(alias="currentUsage")
    """Amount consumed by this entity in the current cadence period."""

    entity_id: str = FieldInfo(alias="entityId")
    """External id of the entity within the customer."""

    is_granted: bool = FieldInfo(alias="isGranted")
    """Whether this node alone permits the requested usage."""

    scope_entity_ids: List[str] = FieldInfo(alias="scopeEntityIds")
    """External ids of the entities this budget is scoped to.

    Empty (`[]`) is the node-wide budget; a non-empty set is the dimension-scoped
    budget that matched this request — use it to tell apart multiple budgets on the
    same entity.
    """

    usage_limit: Optional[float] = FieldInfo(alias="usageLimit", default=None)
    """Hard usage limit for this node; null when no assignment is configured."""


class DataFeatureFeature(BaseModel):
    id: str
    """The unique reference ID of the entitlement."""

    display_name: str = FieldInfo(alias="displayName")
    """The human-readable name of the entitlement, shown in UI elements."""

    feature_status: Literal["NEW", "SUSPENDED", "ACTIVE"] = FieldInfo(alias="featureStatus")
    """The current status of the feature."""

    feature_type: Literal["BOOLEAN", "NUMBER", "ENUM"] = FieldInfo(alias="featureType")
    """The type of feature associated with the entitlement."""


class DataFeature(BaseModel):
    """Feature entitlement with optional governance chains attached."""

    access_denied_reason: Optional[
        Literal[
            "FeatureNotFound",
            "CustomerNotFound",
            "CustomerIsArchived",
            "CustomerResourceNotFound",
            "NoActiveSubscription",
            "NoFeatureEntitlementInSubscription",
            "RequestedUsageExceedingLimit",
            "RequestedValuesMismatch",
            "BudgetExceeded",
            "Unknown",
            "FeatureTypeMismatch",
            "Revoked",
            "InsufficientCredits",
            "EntitlementNotFound",
        ]
    ] = FieldInfo(alias="accessDeniedReason", default=None)

    is_granted: bool = FieldInfo(alias="isGranted")

    type: Literal["FEATURE"]

    chains: Optional[List[List[DataFeatureChain]]] = None
    """Per-entity rollups, one chain per resolved dimension.

    Omitted when dimensions was not provided.
    """

    current_usage: Optional[float] = FieldInfo(alias="currentUsage", default=None)

    entitlement_updated_at: Optional[datetime] = FieldInfo(alias="entitlementUpdatedAt", default=None)
    """Timestamp of the last update to the entitlement grant or configuration."""

    feature: Optional[DataFeatureFeature] = None

    has_unlimited_usage: Optional[bool] = FieldInfo(alias="hasUnlimitedUsage", default=None)

    reset_period: Optional[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"]] = FieldInfo(
        alias="resetPeriod", default=None
    )

    usage_limit: Optional[float] = FieldInfo(alias="usageLimit", default=None)

    usage_period_anchor: Optional[datetime] = FieldInfo(alias="usagePeriodAnchor", default=None)
    """
    The anchor for calculating the usage period for metered entitlements with a
    reset period configured
    """

    usage_period_end: Optional[datetime] = FieldInfo(alias="usagePeriodEnd", default=None)
    """
    The end date of the usage period for metered entitlements with a reset period
    configured
    """

    usage_period_start: Optional[datetime] = FieldInfo(alias="usagePeriodStart", default=None)
    """
    The start date of the usage period for metered entitlements with a reset period
    configured
    """

    valid_until: Optional[datetime] = FieldInfo(alias="validUntil", default=None)
    """The next time the entitlement should be recalculated"""


class DataCreditCurrency(BaseModel):
    """The currency associated with a credit entitlement."""

    currency_id: str = FieldInfo(alias="currencyId")
    """The unique identifier of the custom currency."""

    display_name: str = FieldInfo(alias="displayName")
    """The display name of the currency."""

    description: Optional[str] = None
    """A description of the currency."""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata associated with the currency."""

    unit_plural: Optional[str] = FieldInfo(alias="unitPlural", default=None)
    """The plural form of the currency unit."""

    unit_singular: Optional[str] = FieldInfo(alias="unitSingular", default=None)
    """The singular form of the currency unit."""


class DataCreditChain(BaseModel):
    """
    Per-entity governance node — limit and current usage for a single resolved entity.
    """

    current_usage: float = FieldInfo(alias="currentUsage")
    """Amount consumed by this entity in the current cadence period."""

    entity_id: str = FieldInfo(alias="entityId")
    """External id of the entity within the customer."""

    is_granted: bool = FieldInfo(alias="isGranted")
    """Whether this node alone permits the requested usage."""

    scope_entity_ids: List[str] = FieldInfo(alias="scopeEntityIds")
    """External ids of the entities this budget is scoped to.

    Empty (`[]`) is the node-wide budget; a non-empty set is the dimension-scoped
    budget that matched this request — use it to tell apart multiple budgets on the
    same entity.
    """

    usage_limit: Optional[float] = FieldInfo(alias="usageLimit", default=None)
    """Hard usage limit for this node; null when no assignment is configured."""


class DataCredit(BaseModel):
    """Credit entitlement with optional governance chains attached."""

    access_denied_reason: Optional[
        Literal[
            "FeatureNotFound",
            "CustomerNotFound",
            "CustomerIsArchived",
            "CustomerResourceNotFound",
            "NoActiveSubscription",
            "NoFeatureEntitlementInSubscription",
            "RequestedUsageExceedingLimit",
            "RequestedValuesMismatch",
            "BudgetExceeded",
            "Unknown",
            "FeatureTypeMismatch",
            "Revoked",
            "InsufficientCredits",
            "EntitlementNotFound",
        ]
    ] = FieldInfo(alias="accessDeniedReason", default=None)

    currency: DataCreditCurrency
    """The currency associated with a credit entitlement."""

    current_usage: float = FieldInfo(alias="currentUsage")

    is_granted: bool = FieldInfo(alias="isGranted")

    type: Literal["CREDIT"]

    usage_limit: float = FieldInfo(alias="usageLimit")

    usage_updated_at: datetime = FieldInfo(alias="usageUpdatedAt")
    """Timestamp of the last update to the credit usage."""

    chains: Optional[List[List[DataCreditChain]]] = None
    """Per-entity rollups, one chain per resolved dimension.

    Omitted when dimensions was not provided.
    """

    entitlement_updated_at: Optional[datetime] = FieldInfo(alias="entitlementUpdatedAt", default=None)
    """Timestamp of the last update to the entitlement grant or configuration."""

    usage_period_end: Optional[datetime] = FieldInfo(alias="usagePeriodEnd", default=None)
    """The end date of the current billing period for recurring credit grants."""

    valid_until: Optional[datetime] = FieldInfo(alias="validUntil", default=None)
    """The next time the entitlement should be recalculated"""


Data: TypeAlias = Annotated[Union[DataFeature, DataCredit], PropertyInfo(discriminator="type")]


class EntitlementCheckResponse(BaseModel):
    """Response object"""

    data: Data
    """Feature entitlement with optional governance chains attached."""
