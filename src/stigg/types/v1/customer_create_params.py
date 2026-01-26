# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomerCreateParams", "DefaultPaymentMethod", "Integration"]


class CustomerCreateParams(TypedDict, total=False):
    id: Required[str]
    """Customer slug"""

    coupon_id: Annotated[Optional[str], PropertyInfo(alias="couponId")]
    """Customer level coupon"""

    default_payment_method: Annotated[Optional[DefaultPaymentMethod], PropertyInfo(alias="defaultPaymentMethod")]
    """The default payment method details"""

    email: Optional[str]
    """The email of the customer"""

    integrations: Iterable[Integration]
    """List of integrations"""

    metadata: Dict[str, str]
    """Additional metadata"""

    name: Optional[str]
    """The name of the customer"""


class DefaultPaymentMethod(TypedDict, total=False):
    """The default payment method details"""

    billing_id: Required[Annotated[Optional[str], PropertyInfo(alias="billingId")]]
    """The default payment method id"""

    card_expiry_month: Required[Annotated[Optional[float], PropertyInfo(alias="cardExpiryMonth")]]
    """The expiration month of the default payment method"""

    card_expiry_year: Required[Annotated[Optional[float], PropertyInfo(alias="cardExpiryYear")]]
    """The expiration year of the default payment method"""

    card_last4_digits: Required[Annotated[Optional[str], PropertyInfo(alias="cardLast4Digits")]]
    """The last 4 digits of the default payment method"""

    type: Required[Literal["CARD", "BANK", "CASH_APP"]]
    """The default payment method type"""


class Integration(TypedDict, total=False):
    id: Required[str]
    """Integration details"""

    synced_entity_id: Required[Annotated[Optional[str], PropertyInfo(alias="syncedEntityId")]]
    """Synced entity id"""

    vendor_identifier: Required[
        Annotated[
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
            ],
            PropertyInfo(alias="vendorIdentifier"),
        ]
    ]
    """The vendor identifier of integration"""
