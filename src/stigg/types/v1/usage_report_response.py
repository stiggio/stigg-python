# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UsageReportResponse", "Data", "DataCredit"]


class DataCredit(BaseModel):
    """Optimistic credit balance for a credit-backed feature"""

    consumed: float
    """
    The credits this single reportUsage call deducted, in credit units — scoped to
    this one measurement (0 for idempotency duplicates). Contrast `currentUsage`,
    which is the wallet-wide running total shared across all features on this
    currency. Use it to reconcile expected per-call deductions.
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


class Data(BaseModel):
    """Recorded usage with period info"""

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

    value: int
    """The usage measurement record"""

    credit: Optional[DataCredit] = None
    """Optimistic credit balance for a credit-backed feature"""

    current_usage: Optional[float] = FieldInfo(alias="currentUsage", default=None)
    """The current measured usage value"""

    next_reset_date: Optional[datetime] = FieldInfo(alias="nextResetDate", default=None)
    """The date when the next usage reset will occur"""

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """Resource id"""

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


class UsageReportResponse(BaseModel):
    """
    Response containing reported usage measurements with current usage values, period information, and reset dates for each measurement.
    """

    data: List[Data]
    """Array of usage measurements with current values and period info"""
