# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AddonCreateParams"]


class AddonCreateParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the entity"""

    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]
    """The display name of the package"""

    product_id: Required[Annotated[str, PropertyInfo(alias="productId")]]
    """The product id of the package"""

    billing_id: Annotated[Optional[str], PropertyInfo(alias="billingId")]
    """The unique identifier for the entity in the billing provider"""

    description: Optional[str]
    """The description of the package"""

    max_quantity: Annotated[Optional[int], PropertyInfo(alias="maxQuantity")]
    """The maximum quantity of this addon that can be added to a subscription"""

    metadata: Dict[str, str]
    """Metadata associated with the entity"""

    pricing_type: Annotated[Optional[Literal["FREE", "PAID", "CUSTOM"]], PropertyInfo(alias="pricingType")]
    """The pricing type of the package"""

    status: Literal["DRAFT", "PUBLISHED", "ARCHIVED"]
    """The status of the package"""
