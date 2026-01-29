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


class Customer(TypedDict, total=False):
    id: Required[str]
    """Customer slug"""

    email: Required[Optional[str]]
    """The email of the customer"""

    name: Required[Optional[str]]
    """The name of the customer"""

    metadata: Dict[str, str]
    """Additional metadata"""

    payment_method_id: Annotated[str, PropertyInfo(alias="paymentMethodId")]
    """Billing provider payment method id"""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]
    """Timestamp of when the record was last updated"""
