# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ConsumptionConsumeResponse", "Data", "DataCredit", "DataEntity"]


class DataCredit(BaseModel):
    """
    The optimistic credit balance after consumption (when sync credit consumption is enabled)
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
    """Result of a synchronous direct credit consumption"""

    amount: float
    """The amount of credits consumed"""

    currency_id: str = FieldInfo(alias="currencyId")
    """The credit currency the credits were consumed from"""

    customer_id: str = FieldInfo(alias="customerId")
    """The customer the credits were consumed from"""

    timestamp: datetime
    """The timestamp the consumption was attributed to"""

    credit: Optional[DataCredit] = None
    """
    The optimistic credit balance after consumption (when sync credit consumption is
    enabled)
    """

    entities: Optional[List[DataEntity]] = None
    """The current usage of each governance entitlement this request counted towards.

    Absent when governance is not enabled or the usage is unknown. Entitlements
    whose usage could not be read, and those of repeated idempotent requests, are
    left out
    """

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """The resource the consumption was attributed to"""


class ConsumptionConsumeResponse(BaseModel):
    """Response object"""

    data: Data
    """Result of a synchronous direct credit consumption"""
