# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CreditGetUsageParams"]


class CreditGetUsageParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Filter by customer ID (required)"""

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """Filter by currency ID"""

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]
    """Filter by resource ID"""

    time_range: Annotated[Literal["LAST_DAY", "LAST_WEEK", "LAST_MONTH", "LAST_YEAR"], PropertyInfo(alias="timeRange")]
    """Time range for usage data (LAST_DAY, LAST_WEEK, LAST_MONTH, LAST_YEAR).

    Defaults to LAST_MONTH
    """
