# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UsageEstimateParams"]


class UsageEstimateParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Customer id"""

    feature_id: Required[Annotated[str, PropertyInfo(alias="featureId")]]
    """Feature id"""

    value: Required[int]
    """The value to report for usage"""

    dimensions: Dict[str, Union[str, float, bool]]
    """Additional dimensions for the usage report"""

    resource_id: Annotated[Optional[str], PropertyInfo(alias="resourceId")]
    """Resource id"""

    update_behavior: Annotated[Literal["DELTA", "SET"], PropertyInfo(alias="updateBehavior")]
    """The method by which the usage value should be updated"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
