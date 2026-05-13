# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["GrantListParams", "CreatedAt"]


class GrantListParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Filter by customer ID (required)"""

    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    created_at: Annotated[CreatedAt, PropertyInfo(alias="createdAt")]
    """Filter by creation date using range operators: gt, gte, lt, lte"""

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """Filter by currency ID"""

    limit: int
    """Maximum number of items to return"""

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]
    """Filter by resource ID.

    When omitted, only grants without a resource are returned
    """


class CreatedAt(TypedDict, total=False):
    """Filter by creation date using range operators: gt, gte, lt, lte"""

    gt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Greater than the specified createdAt value"""

    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Greater than or equal to the specified createdAt value"""

    lt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Less than the specified createdAt value"""

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Less than or equal to the specified createdAt value"""
