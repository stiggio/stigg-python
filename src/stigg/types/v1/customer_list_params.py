# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CustomerListParams"]


class CustomerListParams(TypedDict, total=False):
    ending_before: str
    """Ending before this UUID for pagination"""

    limit: int
    """Items per page"""

    starting_after: str
    """Starting after this UUID for pagination"""
