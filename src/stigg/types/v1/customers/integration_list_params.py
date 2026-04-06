# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IntegrationListParams"]


class IntegrationListParams(TypedDict, total=False):
    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    limit: int
    """Maximum number of items to return"""

    vendor_identifier: Annotated[str, PropertyInfo(alias="vendorIdentifier")]
    """Filter by vendor identifier.

    Supports comma-separated values for multiple vendors (e.g., STRIPE,HUBSPOT)
    """
