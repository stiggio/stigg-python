# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionListParams"]


class SubscriptionListParams(TypedDict, total=False):
    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """Filter by customer ID"""

    limit: int
    """Maximum number of items to return"""

    status: str
    """Filter by status (comma-separated)"""
