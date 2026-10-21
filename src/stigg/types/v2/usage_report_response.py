# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UsageReportResponse", "Data", "DataUsage", "DataUsageCredit", "DataCredit", "DataEntity"]


class DataUsageCredit(BaseModel):
    """The credits this measurement deducted.

    `null` when the measurement drew from no wallet listed in `credits`. The balance of the wallet it drew from is in the response `credits` list, matched by customer, resource and currency.
    """

    consumed: float
    """
    The credits this single reportUsage call deducted, in credit units — scoped to
    this one measurement (0 for idempotency duplicates). Contrast `currentUsage`,
    which is the wallet-wide running total shared across all features on this
    currency. Use it to reconcile expected per-call deductions.
    """

    currency_id: str = FieldInfo(alias="currencyId")
    """The credit currency identifier"""


class DataUsage(BaseModel):
    """Recorded usage with period info and the credits it deducted"""

    id: str
    """Unique identifier for the entity"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    customer_id: str = FieldInfo(alias="customerId")
    """Customer id"""

    feature_id: str = FieldInfo(alias="featureId")
    """Feature id"""

    timestamp: datetime
    """Timestamp"""

    value: float
    """The usage measurement record"""

    credit: Optional[DataUsageCredit] = None
    """The credits this measurement deducted.

    `null` when the measurement drew from no wallet listed in `credits`. The balance
    of the wallet it drew from is in the response `credits` list, matched by
    customer, resource and currency.
    """

    current_usage: Optional[float] = FieldInfo(alias="currentUsage", default=None)
    """The current measured usage value"""

    next_reset_date: Optional[datetime] = FieldInfo(alias="nextResetDate", default=None)
    """The date when the next usage reset will occur"""

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """The customer resource this usage applies to.

    Optional — only required if the customer has multiple resources (for example,
    one subscription per workspace or site) and usage needs to be tracked separately
    per resource; omit it to report usage at the customer level.
    """

    usage_period_end: Optional[datetime] = FieldInfo(alias="usagePeriodEnd", default=None)
    """
    The end date of the usage period in which this measurement resides (for
    entitlements with a reset period)
    """

    usage_period_start: Optional[datetime] = FieldInfo(alias="usagePeriodStart", default=None)
    """
    The start date of the usage period in which this measurement resides (for
    entitlements with a reset period)
    """


class DataCredit(BaseModel):
    """
    Optimistic credit balance of one wallet (customer, resource and currency) after the request, listed once however many measurements drew from it
    """

    currency_id: str = FieldInfo(alias="currencyId")
    """The credit currency identifier"""

    current_usage: float = FieldInfo(alias="currentUsage")
    """
    The wallet's total consumed credits for this currency (optimistic — includes
    not-yet-reconciled usage), shared across every feature that draws on the
    currency. This is the running balance, not this call's deduction — see
    `consumed` for that.
    """

    customer_id: str = FieldInfo(alias="customerId")
    """Customer id"""

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """The wallet's resource; `null` for the customer-level wallet"""

    timestamp: datetime
    """
    The grant-version timestamp of this balance, used by the SDK for last-write-wins
    reconciliation
    """

    usage_limit: float = FieldInfo(alias="usageLimit")
    """The total credits granted"""

    usage_period_end: Optional[datetime] = FieldInfo(alias="usagePeriodEnd", default=None)
    """
    End of the current credit grant period (when recurring credits reset), if
    applicable
    """


class DataEntity(BaseModel):
    """The usage counted against one governance entitlement"""

    current_usage: float = FieldInfo(alias="currentUsage")
    """The absolute usage counted against the entitlement"""

    customer_id: str = FieldInfo(alias="customerId")
    """The customer whose usage counted towards the entitlement"""

    entitlement_id: str = FieldInfo(alias="entitlementId")
    """The governance entitlement the usage counts towards"""

    entity_id: str = FieldInfo(alias="entityId")
    """The governance entity the entitlement belongs to"""

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """The customer resource the usage counted from; `null` for customer-level usage"""

    scope_entity_ids: List[str] = FieldInfo(alias="scopeEntityIds")
    """The entities the entitlement is scoped to (empty when it is not scoped)"""

    usage_updated_at: datetime = FieldInfo(alias="usageUpdatedAt")
    """When the entitlement usage was last updated"""

    currency_id: Optional[str] = FieldInfo(alias="currencyId", default=None)
    """
    The credit currency the entitlement governs (exactly one of featureId and
    currencyId is set)
    """

    feature_id: Optional[str] = FieldInfo(alias="featureId", default=None)
    """
    The feature the entitlement governs (exactly one of featureId and currencyId is
    set)
    """


class Data(BaseModel):
    """Reported usage measurements and the credit balances they drew from"""

    usages: List[DataUsage]
    """Usage measurements, in request order, with current values and period info"""

    credits: Optional[List[DataCredit]] = None
    """The balance of each credit wallet the request drew from.

    Omitted when no reported feature consumes credits, or when credit balances
    aren't computed synchronously for the environment; each usage's `credit` is then
    `null`.
    """

    entities: Optional[List[DataEntity]] = None
    """The current usage of each governance entitlement this request counted towards.

    Absent when governance is not enabled or the usage is unknown. Entitlements
    whose usage could not be read, and those of repeated idempotent requests, are
    left out
    """


class UsageReportResponse(BaseModel):
    """
    Response containing reported usage measurements with current usage values, period information and reset dates, plus the balance of each credit wallet they drew from.
    """

    data: Data
    """Reported usage measurements and the credit balances they drew from"""
