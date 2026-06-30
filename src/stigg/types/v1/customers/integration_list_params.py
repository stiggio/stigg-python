# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IntegrationListParams"]


class IntegrationListParams(TypedDict, total=False):
    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    limit: int
    """Maximum number of items to return"""

    vendor_identifier: Annotated[
        List[
            Literal[
                "AUTH0",
                "ZUORA",
                "STRIPE",
                "HUBSPOT",
                "AWS_MARKETPLACE",
                "SNOWFLAKE",
                "SALESFORCE",
                "BIG_QUERY",
                "OPEN_FGA",
                "APP_STORE",
                "RECEIVED",
                "PREQUEL",
                "AIRWALLEX",
            ]
        ],
        PropertyInfo(alias="vendorIdentifier"),
    ]
    """Filter by vendor identifier.

    Supports comma-separated values for multiple vendors (e.g., STRIPE,HUBSPOT)
    """

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
