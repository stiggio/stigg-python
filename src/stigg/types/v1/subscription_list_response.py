# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubscriptionListResponse", "Data", "Pagination"]


class Data(BaseModel):
    id: str
    """Subscription ID"""

    billing_id: Optional[str] = FieldInfo(alias="billingId", default=None)
    """Billing ID"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Created at"""

    customer_id: str = FieldInfo(alias="customerId")
    """Customer ID"""

    payment_collection: Literal["NOT_REQUIRED", "PROCESSING", "FAILED", "ACTION_REQUIRED"] = FieldInfo(
        alias="paymentCollection"
    )
    """Payment collection"""

    plan_id: str = FieldInfo(alias="planId")
    """Plan ID"""

    pricing_type: Literal["FREE", "PAID", "CUSTOM"] = FieldInfo(alias="pricingType")
    """Pricing type"""

    start_date: datetime = FieldInfo(alias="startDate")
    """Subscription start date"""

    status: Literal["PAYMENT_PENDING", "ACTIVE", "EXPIRED", "IN_TRIAL", "CANCELED", "NOT_STARTED"]
    """Subscription status"""

    cancellation_date: Optional[datetime] = FieldInfo(alias="cancellationDate", default=None)
    """Subscription cancellation date"""

    cancel_reason: Optional[
        Literal[
            "UPGRADE_OR_DOWNGRADE",
            "CANCELLED_BY_BILLING",
            "EXPIRED",
            "DETACH_BILLING",
            "TRIAL_ENDED",
            "Immediate",
            "TRIAL_CONVERTED",
            "PENDING_PAYMENT_EXPIRED",
            "ScheduledCancellation",
            "CustomerArchived",
            "AutoCancellationRule",
        ]
    ] = FieldInfo(alias="cancelReason", default=None)
    """Subscription cancel reason"""

    current_billing_period_end: Optional[datetime] = FieldInfo(alias="currentBillingPeriodEnd", default=None)
    """End of the current billing period"""

    current_billing_period_start: Optional[datetime] = FieldInfo(alias="currentBillingPeriodStart", default=None)
    """Start of the current billing period"""

    effective_end_date: Optional[datetime] = FieldInfo(alias="effectiveEndDate", default=None)
    """Subscription effective end date"""

    end_date: Optional[datetime] = FieldInfo(alias="endDate", default=None)
    """Subscription end date"""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata for the subscription"""

    paying_customer_id: Optional[str] = FieldInfo(alias="payingCustomerId", default=None)
    """Paying customer ID for delegated billing"""

    payment_collection_method: Optional[Literal["CHARGE", "INVOICE", "NONE"]] = FieldInfo(
        alias="paymentCollectionMethod", default=None
    )
    """The method used to collect payments for a subscription"""

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """Resource ID"""

    trial_end_date: Optional[datetime] = FieldInfo(alias="trialEndDate", default=None)
    """Subscription trial end date"""


class Pagination(BaseModel):
    """Pagination information including cursors for navigation"""

    next: Optional[str] = None
    """Cursor to fetch the next page (use with after parameter), null if no more pages"""

    prev: Optional[str] = None
    """
    Cursor to fetch the previous page (use with before parameter), null if no
    previous pages
    """


class SubscriptionListResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
    """Pagination information including cursors for navigation"""
