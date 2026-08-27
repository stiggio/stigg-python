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
    """The internal ID of the integration this record is linked to"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]


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
    """Custom key-value metadata to attach to the customer.

    When creating a customer, this sets the initial metadata. When updating a
    customer, this replaces the customer's existing metadata object entirely — it is
    not merged key by key. Omit this field on update to leave the customer's
    existing metadata untouched; pass an empty object to clear it.
    """

    payment_method_id: Annotated[str, PropertyInfo(alias="paymentMethodId")]
    """Billing provider payment method id.

    Attaching it makes it the customer's new default payment method for future
    charges; any previously attached payment method is no longer used as the
    default, though it is not removed from the billing provider.
    """

    salesforce_id: Annotated[str, PropertyInfo(alias="salesforceId")]
    """The unique identifier for the customer in Salesforce integration"""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]
    """Timestamp of when the record was last updated"""
