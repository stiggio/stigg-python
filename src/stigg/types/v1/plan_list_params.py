# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PlanListParams", "CreatedAt"]


class PlanListParams(TypedDict, total=False):
    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    created_at: Annotated[CreatedAt, PropertyInfo(alias="createdAt")]
    """Filter by creation date using range operators: gt, gte, lt, lte"""

    limit: int
    """Maximum number of items to return"""

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """Filter by product ID"""

    status: str
    """Filter by status. Supports comma-separated values for multiple statuses"""


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
