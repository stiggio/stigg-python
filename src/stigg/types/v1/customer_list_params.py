# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CustomerListParams"]


class CustomerListParams(TypedDict, total=False):
    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    limit: int
    """Maximum number of items to return"""
