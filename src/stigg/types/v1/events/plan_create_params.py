# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PlanCreateParams"]


class PlanCreateParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the entity"""

    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]
    """The display name of the package"""

    product_id: Required[Annotated[str, PropertyInfo(alias="productId")]]
    """The product ID to associate the plan with"""

    billing_id: Annotated[Optional[str], PropertyInfo(alias="billingId")]
    """The unique identifier for the entity in the billing provider"""

    description: Optional[str]
    """The description of the package"""

    metadata: Dict[str, str]
    """Metadata associated with the entity"""

    parent_plan_id: Annotated[Optional[str], PropertyInfo(alias="parentPlanId")]
    """The ID of the parent plan, if applicable"""

    pricing_type: Annotated[Optional[Literal["FREE", "PAID", "CUSTOM"]], PropertyInfo(alias="pricingType")]
    """The pricing type of the package"""

    status: Literal["DRAFT", "PUBLISHED", "ARCHIVED"]
    """The status of the package"""
