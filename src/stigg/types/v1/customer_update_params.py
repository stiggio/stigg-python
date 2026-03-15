# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomerUpdateParams", "Integration"]


class CustomerUpdateParams(TypedDict, total=False):
    billing_currency: Annotated[
        Optional[
            Literal[
                "usd",
                "aed",
                "all",
                "amd",
                "ang",
                "aud",
                "awg",
                "azn",
                "bam",
                "bbd",
                "bdt",
                "bgn",
                "bif",
                "bmd",
                "bnd",
                "bsd",
                "bwp",
                "byn",
                "bzd",
                "brl",
                "cad",
                "cdf",
                "chf",
                "cny",
                "czk",
                "dkk",
                "dop",
                "dzd",
                "egp",
                "etb",
                "eur",
                "fjd",
                "gbp",
                "gel",
                "gip",
                "gmd",
                "gyd",
                "hkd",
                "hrk",
                "htg",
                "idr",
                "ils",
                "inr",
                "isk",
                "jmd",
                "jpy",
                "kes",
                "kgs",
                "khr",
                "kmf",
                "krw",
                "kyd",
                "kzt",
                "lbp",
                "lkr",
                "lrd",
                "lsl",
                "mad",
                "mdl",
                "mga",
                "mkd",
                "mmk",
                "mnt",
                "mop",
                "mro",
                "mvr",
                "mwk",
                "mxn",
                "myr",
                "mzn",
                "nad",
                "ngn",
                "nok",
                "npr",
                "nzd",
                "pgk",
                "php",
                "pkr",
                "pln",
                "qar",
                "ron",
                "rsd",
                "rub",
                "rwf",
                "sar",
                "sbd",
                "scr",
                "sek",
                "sgd",
                "sle",
                "sll",
                "sos",
                "szl",
                "thb",
                "tjs",
                "top",
                "try",
                "ttd",
                "tzs",
                "uah",
                "uzs",
                "vnd",
                "vuv",
                "wst",
                "xaf",
                "xcd",
                "yer",
                "zar",
                "zmw",
                "clp",
                "djf",
                "gnf",
                "ugx",
                "pyg",
                "xof",
                "xpf",
            ]
        ],
        PropertyInfo(alias="billingCurrency"),
    ]
    """The billing currency of the customer"""

    billing_id: Annotated[Optional[str], PropertyInfo(alias="billingId")]
    """The unique identifier for the entity in the billing provider"""

    coupon_id: Annotated[Optional[str], PropertyInfo(alias="couponId")]
    """Customer level coupon"""

    email: Optional[str]
    """The email of the customer"""

    integrations: Iterable[Integration]
    """List of integrations"""

    metadata: Dict[str, str]
    """Additional metadata"""

    name: Optional[str]
    """The name of the customer"""


class Integration(TypedDict, total=False):
    """External billing or CRM integration link"""

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
