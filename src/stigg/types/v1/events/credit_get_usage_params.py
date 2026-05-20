# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CreditGetUsageParams"]


class CreditGetUsageParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Filter by customer ID (required)"""

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """Filter by currency ID"""

    end_date: Annotated[Union[str, datetime], PropertyInfo(alias="endDate", format="iso8601")]
    """End date for the credit usage time range (ISO 8601).

    Defaults to now when startDate is provided
    """

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]
    """Filter by resource ID"""

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Start date for the credit usage time range (ISO 8601).

    Takes precedence over timeRange when provided
    """

    time_range: Annotated[Literal["LAST_DAY", "LAST_WEEK", "LAST_MONTH", "LAST_YEAR"], PropertyInfo(alias="timeRange")]
    """Time range for usage data (LAST_DAY, LAST_WEEK, LAST_MONTH, LAST_YEAR).

    Defaults to LAST_MONTH
    """
