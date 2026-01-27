# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CouponListParams"]


class CouponListParams(TypedDict, total=False):
    after: str
    """Starting after this UUID for pagination"""

    before: str
    """Ending before this UUID for pagination"""

    limit: int
    """Items per page"""
