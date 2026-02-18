# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProductArchiveProductResponse", "Data", "DataProductSettings"]


class DataProductSettings(BaseModel):
    """Product behavior settings for subscription lifecycle management."""

    subscription_cancellation_time: Literal["END_OF_BILLING_PERIOD", "IMMEDIATE", "SPECIFIC_DATE"] = FieldInfo(
        alias="subscriptionCancellationTime"
    )
    """Time when the subscription will be cancelled"""

    subscription_end_setup: Literal["DOWNGRADE_TO_FREE", "CANCEL_SUBSCRIPTION"] = FieldInfo(
        alias="subscriptionEndSetup"
    )
    """Setup for the end of the subscription"""

    subscription_start_setup: Literal["PLAN_SELECTION", "TRIAL_PERIOD", "FREE_PLAN"] = FieldInfo(
        alias="subscriptionStartSetup"
    )
    """Setup for the start of the subscription"""

    downgrade_plan_id: Optional[str] = FieldInfo(alias="downgradePlanId", default=None)
    """ID of the plan to downgrade to at the end of the billing period"""

    prorate_at_end_of_billing_period: Optional[bool] = FieldInfo(alias="prorateAtEndOfBillingPeriod", default=None)
    """
    Indicates if the subscription should be prorated at the end of the billing
    period
    """

    subscription_start_plan_id: Optional[str] = FieldInfo(alias="subscriptionStartPlanId", default=None)
    """ID of the plan to start the subscription with"""


class Data(BaseModel):
    """Product configuration object"""

    id: str
    """The unique identifier for the entity"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    description: Optional[str] = None
    """Description of the product"""

    display_name: str = FieldInfo(alias="displayName")
    """Display name of the product"""

    metadata: Dict[str, str]
    """Metadata associated with the entity"""

    multiple_subscriptions: bool = FieldInfo(alias="multipleSubscriptions")
    """Indicates if multiple subscriptions to this product are allowed"""

    status: Literal["PUBLISHED", "ARCHIVED"]
    """The status of the product"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""

    product_settings: Optional[DataProductSettings] = FieldInfo(alias="productSettings", default=None)
    """Product behavior settings for subscription lifecycle management."""


class ProductArchiveProductResponse(BaseModel):
    """Response object"""

    data: Data
    """Product configuration object"""
