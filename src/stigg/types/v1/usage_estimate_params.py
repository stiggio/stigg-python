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
    """The value to report for usage.

    Must be a whole number — the REST API does not accept fractional (float) usage
    values; scale up (e.g. report cents instead of dollars, or milliseconds instead
    of seconds) if you need sub-unit precision.
    """

    dimensions: Dict[str, Union[str, float, bool]]
    """Additional dimensions for the usage report"""

    resource_id: Annotated[Optional[str], PropertyInfo(alias="resourceId")]
    """The customer resource this usage applies to.

    Optional — only required if the customer has multiple resources (for example,
    one subscription per workspace or site) and usage needs to be tracked separately
    per resource; omit it to report usage at the customer level.
    """

    update_behavior: Annotated[Literal["DELTA", "SET"], PropertyInfo(alias="updateBehavior")]
    """
    How the reported value is applied: DELTA (default) adds it to the feature's
    current usage; SET treats it as the new absolute usage total, and Stigg computes
    the delta internally.
    """

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
