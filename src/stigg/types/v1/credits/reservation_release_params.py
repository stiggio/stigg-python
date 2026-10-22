# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ReservationReleaseParams"]


class ReservationReleaseParams(TypedDict, total=False):
    consumed_amount: Required[Annotated[float, PropertyInfo(alias="consumedAmount")]]
    """The amount of credits to consume at release.

    Up to the reserved amount is charged to the credits that backed the reservation;
    the rest returns to the balance, and any amount above the reservation is
    consumed normally.
    """

    currency_id: Required[Annotated[str, PropertyInfo(alias="currencyId")]]
    """The credit currency of the reservation"""

    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """The customer the reservation was made for"""

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]
    """The resource the reservation was made for, if any"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
