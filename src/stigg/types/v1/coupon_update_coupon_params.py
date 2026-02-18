# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["CouponUpdateCouponParams"]


class CouponUpdateCouponParams(TypedDict, total=False):
    description: Optional[str]
    """Description of the coupon"""

    metadata: Optional[Dict[str, str]]
    """Metadata associated with the entity"""

    name: str
    """Name of the coupon"""
