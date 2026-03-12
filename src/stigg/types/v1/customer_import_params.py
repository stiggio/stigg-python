# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomerImportParams", "Customer"]


class CustomerImportParams(TypedDict, total=False):
    customers: Required[Iterable[Customer]]
    """List of customer objects to import"""

    integration_id: Annotated[str, PropertyInfo(alias="integrationId")]
    """Integration details"""


class Customer(TypedDict, total=False):
    id: Required[str]
    """Customer slug"""

    email: Required[Optional[str]]
    """The email of the customer"""

    name: Required[Optional[str]]
    """The name of the customer"""

    billing_id: Annotated[str, PropertyInfo(alias="billingId")]
    """Id in the billing provider"""

    metadata: Dict[str, str]
    """Additional metadata"""

    payment_method_id: Annotated[str, PropertyInfo(alias="paymentMethodId")]
    """Billing provider payment method id"""

    salesforce_id: Annotated[str, PropertyInfo(alias="salesforceId")]
    """The unique identifier for the customer in Salesforce integration"""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]
    """Timestamp of when the record was last updated"""
