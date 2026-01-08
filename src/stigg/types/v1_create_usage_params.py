# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["V1CreateUsageParams", "Usage"]


class V1CreateUsageParams(TypedDict, total=False):
    usages: Required[Iterable[Usage]]
    """A list of usage reports to be submitted in bulk"""


class Usage(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Customer id"""

    feature_id: Required[Annotated[str, PropertyInfo(alias="featureId")]]
    """Feature id"""

    value: Required[int]
    """The value to report for usage"""

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Timestamp of when the record was created"""

    dimensions: Dict[str, str]
    """Additional dimensions for the usage report"""

    resource_id: Annotated[Optional[str], PropertyInfo(alias="resourceId")]
    """Resource id"""

    update_behavior: Annotated[Literal["DELTA", "SET"], PropertyInfo(alias="updateBehavior")]
    """The method by which the usage value should be updated"""
