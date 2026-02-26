# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SetPackagePricingResponse", "Data"]


class Data(BaseModel):
    """Result of setting package pricing."""

    id: str
    """The package identifier (refId)"""

    pricing_type: Literal["FREE", "PAID", "CUSTOM"] = FieldInfo(alias="pricingType")
    """The pricing type that was set"""


class SetPackagePricingResponse(BaseModel):
    """Response object"""

    data: Data
    """Result of setting package pricing."""
