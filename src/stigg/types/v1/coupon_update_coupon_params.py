# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CouponUpdateCouponParams"]


class CouponUpdateCouponParams(TypedDict, total=False):
    description: Optional[str]
    """Description of the coupon"""

    metadata: Optional[Dict[str, str]]
    """Metadata associated with the entity"""

    name: str
    """Name of the coupon"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
