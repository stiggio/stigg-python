# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProductDuplicateProductParams"]


class ProductDuplicateProductParams(TypedDict, total=False):
    body_id: Required[Annotated[str, PropertyInfo(alias="id")]]
    """The unique identifier for the entity"""

    description: Optional[str]
    """Description of the product"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of the product"""
