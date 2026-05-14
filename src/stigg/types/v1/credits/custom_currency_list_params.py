# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["CustomCurrencyListParams"]


class CustomCurrencyListParams(TypedDict, total=False):
    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    limit: int
    """Maximum number of items to return"""

    status: List[Literal["ACTIVE", "ARCHIVED"]]
    """Filter by custom currency status.

    Supports comma-separated values (e.g., `ACTIVE,ARCHIVED`). Defaults to `ACTIVE`.
    """
