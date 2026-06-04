# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["AssignmentListParams"]


class AssignmentListParams(TypedDict, total=False):
    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    capability_id: Annotated[str, PropertyInfo(alias="capabilityId")]
    """Filter assignments to a specific capability refId"""

    entity_id: Annotated[str, PropertyInfo(alias="entityId")]
    """Filter assignments to a specific entity refId"""

    limit: int
    """Maximum number of items to return"""
