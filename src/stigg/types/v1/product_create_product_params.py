# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProductCreateProductParams"]


class ProductCreateProductParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the entity"""

    description: Optional[str]
    """Description of the product"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of the product"""

    metadata: Optional[Dict[str, str]]
    """Additional metadata for the product"""

    multiple_subscriptions: Annotated[bool, PropertyInfo(alias="multipleSubscriptions")]
    """Indicates if multiple subscriptions to this product are allowed"""
