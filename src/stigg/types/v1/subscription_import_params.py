# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionImportParams", "Subscription"]


class SubscriptionImportParams(TypedDict, total=False):
    subscriptions: Required[Iterable[Subscription]]
    """List of subscription objects to import"""

    integration_id: Annotated[Optional[str], PropertyInfo(alias="integrationId")]
    """Integration ID to use for importing subscriptions"""


class Subscription(TypedDict, total=False):
    id: Required[str]
    """Subscription ID"""

    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Customer ID"""

    plan_id: Required[Annotated[str, PropertyInfo(alias="planId")]]
    """Plan ID"""

    billing_id: Annotated[Optional[str], PropertyInfo(alias="billingId")]
    """Billing ID"""

    end_date: Annotated[Union[str, datetime, None], PropertyInfo(alias="endDate", format="iso8601")]
    """Subscription end date"""

    metadata: Dict[str, str]
    """Additional metadata for the subscription"""

    resource_id: Annotated[Optional[str], PropertyInfo(alias="resourceId")]
    """Resource ID"""

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Subscription start date"""
