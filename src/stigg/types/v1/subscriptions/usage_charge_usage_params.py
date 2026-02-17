# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UsageChargeUsageParams"]


class UsageChargeUsageParams(TypedDict, total=False):
    until_date: Annotated[Union[str, datetime], PropertyInfo(alias="untilDate", format="iso8601")]
    """Cutoff date for usage calculation. If not provided, the current time is used."""
