# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomerListParams"]


class CustomerListParams(TypedDict, total=False):
    ending_before: Annotated[str, PropertyInfo(alias="endingBefore")]
    """Ending before this UUID for pagination"""

    limit: int
    """Items per page"""

    starting_after: Annotated[str, PropertyInfo(alias="startingAfter")]
    """Starting after this UUID for pagination"""
