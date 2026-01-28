# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubscriptionDelegateResponse", "Data", "DataPrice"]


class DataPrice(BaseModel):
    id: str
    """Price ID"""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp"""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


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

    prices: Optional[List[DataPrice]] = None

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """Resource ID"""

    trial_end_date: Optional[datetime] = FieldInfo(alias="trialEndDate", default=None)
    """Subscription trial end date"""

    unit_quantity: Optional[float] = FieldInfo(alias="unitQuantity", default=None)


class SubscriptionDelegateResponse(BaseModel):
    data: Data
