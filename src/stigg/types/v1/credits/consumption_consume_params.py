# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ConsumptionConsumeParams"]


class ConsumptionConsumeParams(TypedDict, total=False):
    amount: Required[float]
    """The amount of credits to consume"""

    currency_id: Required[Annotated[str, PropertyInfo(alias="currencyId")]]
    """The credit currency to consume from (required)"""

    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """The customer to consume credits from (required)"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="idempotencyKey")]]
    """A unique key used to deduplicate the consumption (required)"""

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Optional timestamp the consumption is attributed to"""

    dimensions: Dict[str, Union[str, float, bool]]
    """Optional dimensions describing the consumption"""

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]
    """Optional resource the consumption is attributed to"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
