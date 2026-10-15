# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UsageReportParams", "Usage"]


class UsageReportParams(TypedDict, total=False):
    usages: Required[Iterable[Usage]]
    """A list of usage reports to be submitted in bulk"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]


class Usage(TypedDict, total=False):
    """Single usage measurement"""

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

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Timestamp of when the record was created"""

    dimensions: Dict[str, Union[str, float, bool]]
    """Additional dimensions for the usage report"""

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotencyKey")]
    """
    A key you provide to safely retry the same usage report without double-counting
    it. Reports with a previously-seen idempotency key are deduplicated for 7 days;
    after that window a retry is treated as new usage.
    """

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
