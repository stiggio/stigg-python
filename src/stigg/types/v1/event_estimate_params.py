# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EventEstimateParams"]


class EventEstimateParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Customer id"""

    event_name: Required[Annotated[str, PropertyInfo(alias="eventName")]]
    """The name of the usage event"""

    dimensions: Dict[str, Union[str, float, bool]]
    """Dimensions associated with the usage event"""

    resource_id: Annotated[Optional[str], PropertyInfo(alias="resourceId")]
    """Resource id"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
