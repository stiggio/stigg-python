# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProductListProductsResponse"]


class ProductListProductsResponse(BaseModel):
    """Product configuration object"""

    id: str
    """The unique identifier for the entity"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    description: Optional[str] = None
    """Description of the product"""

    display_name: str = FieldInfo(alias="displayName")
    """Display name of the product"""

    metadata: Dict[str, str]
    """Metadata associated with the entity"""

    multiple_subscriptions: bool = FieldInfo(alias="multipleSubscriptions")
    """Indicates if multiple subscriptions to this product are allowed"""

    status: Literal["PUBLISHED", "ARCHIVED"]
    """The status of the product"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""
