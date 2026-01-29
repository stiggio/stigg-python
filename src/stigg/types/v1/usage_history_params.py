# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UsageHistoryParams"]


class UsageHistoryParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]]
    """The start date of the range"""

    end_date: Annotated[Union[str, datetime], PropertyInfo(alias="endDate", format="iso8601")]
    """The end date of the range"""

    group_by: Annotated[str, PropertyInfo(alias="groupBy")]

    resource_id: Annotated[Optional[str], PropertyInfo(alias="resourceId")]
    """Resource id"""
