# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AddonUpdateParams"]


class AddonUpdateParams(TypedDict, total=False):
    billing_id: Annotated[Optional[str], PropertyInfo(alias="billingId")]
    """The unique identifier for the entity in the billing provider"""

    dependencies: Optional[SequenceNotStr[str]]
    """List of addons the addon is dependant on"""

    description: Optional[str]
    """The description of the package"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """The display name of the package"""

    max_quantity: Annotated[Optional[int], PropertyInfo(alias="maxQuantity")]
    """The maximum quantity of this addon that can be added to a subscription"""

    metadata: Dict[str, str]
    """Metadata associated with the entity"""
