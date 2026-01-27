# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionListParams"]


class SubscriptionListParams(TypedDict, total=False):
    after: str
    """Starting after this UUID for pagination"""

    before: str
    """Ending before this UUID for pagination"""

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """Filter by customer ID"""

    limit: int
    """Items per page"""

    status: str
    """
    Filter by subscription status (comma-separated for multiple statuses, e.g.,
    ACTIVE,IN_TRIAL)
    """
