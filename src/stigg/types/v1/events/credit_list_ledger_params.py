# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CreditListLedgerParams"]


class CreditListLedgerParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Filter by customer ID (required)"""

    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """Filter by currency ID"""

    limit: int
    """Maximum number of items to return"""

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]
    """Filter by resource ID"""
