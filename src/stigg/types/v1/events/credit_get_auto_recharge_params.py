# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CreditGetAutoRechargeParams"]


class CreditGetAutoRechargeParams(TypedDict, total=False):
    currency_id: Required[Annotated[str, PropertyInfo(alias="currencyId")]]
    """Filter by currency ID (required)"""

    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Filter by customer ID (required)"""
