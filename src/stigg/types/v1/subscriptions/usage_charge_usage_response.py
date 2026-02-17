# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["UsageChargeUsageResponse", "Data", "DataUsageCharged"]


class DataUsageCharged(BaseModel):
    """A single usage item that was charged."""

    feature_id: Optional[str] = FieldInfo(alias="featureId", default=None)
    """The feature ID for which usage was charged"""

    usage_amount: float = FieldInfo(alias="usageAmount")
    """The number of units charged"""


class Data(BaseModel):
    """
    Result of charging subscription usage including the billing period and charged items.
    """

    invoice_billing_id: Optional[str] = FieldInfo(alias="invoiceBillingId", default=None)
    """The invoice ID in the billing integration"""

    period_end: datetime = FieldInfo(alias="periodEnd")
    """End of the usage billing period"""

    period_start: datetime = FieldInfo(alias="periodStart")
    """Start of the usage billing period"""

    subscription_id: str = FieldInfo(alias="subscriptionId")
    """The subscription ID for which usage was charged"""

    usage_charged: List[DataUsageCharged] = FieldInfo(alias="usageCharged")
    """Usage items that were charged"""


class UsageChargeUsageResponse(BaseModel):
    """Response object"""

    data: Data
    """
    Result of charging subscription usage including the billing period and charged
    items.
    """
