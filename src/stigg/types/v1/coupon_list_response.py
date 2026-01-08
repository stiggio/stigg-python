# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CouponListResponse", "Data", "DataAmountsOff"]


class DataAmountsOff(BaseModel):
    amount: float
    """The price amount"""

    currency: Optional[
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
    ] = None
    """The price currency"""


class Data(BaseModel):
    id: str
    """The unique identifier for the entity"""

    amounts_off: Optional[List[DataAmountsOff]] = FieldInfo(alias="amountsOff", default=None)
    """Fixed amount discounts in different currencies"""

    billing_id: Optional[str] = FieldInfo(alias="billingId", default=None)
    """The unique identifier for the entity in the billing provider"""

    billing_link_url: Optional[str] = FieldInfo(alias="billingLinkUrl", default=None)
    """The URL to the entity in the billing provider"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    cursor_id: str = FieldInfo(alias="cursorId")
    """Cursor ID for query pagination"""

    description: Optional[str] = None
    """Description of the coupon"""

    duration_in_months: Optional[float] = FieldInfo(alias="durationInMonths", default=None)
    """Duration of the coupon validity in months"""

    name: str
    """Name of the coupon"""

    percent_off: Optional[float] = FieldInfo(alias="percentOff", default=None)
    """Percentage discount off the original price"""

    source: Optional[Literal["STIGG", "STIGG_ADHOC", "STRIPE"]] = None
    """The source of the coupon"""

    status: Literal["ACTIVE", "ARCHIVED"]
    """Current status of the coupon"""

    type: Literal["FIXED", "PERCENTAGE"]
    """Type of the coupon (percentage or fixed amount)"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""


class CouponListResponse(BaseModel):
    data: List[Data]
