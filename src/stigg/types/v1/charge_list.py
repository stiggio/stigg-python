# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ChargeList",
    "Data",
    "DataCreditRate",
    "DataPrice",
    "DataTier",
    "DataTierFlatPrice",
    "DataTierUnitPrice",
    "Pagination",
]


class DataCreditRate(BaseModel):
    """Credit rate configuration for credit-based pricing"""

    amount: float
    """Credit rate amount"""

    currency_id: str = FieldInfo(alias="currencyId")
    """Custom currency identifier"""

    cost_formula: Optional[str] = FieldInfo(alias="costFormula", default=None)
    """Optional cost formula expression"""


class DataPrice(BaseModel):
    """The flat price amount and currency, when applicable"""

    amount: float
    """The price amount"""

    currency: Literal[
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
    """ISO 4217 currency code"""


class DataTierFlatPrice(BaseModel):
    """Flat price for this tier"""

    amount: float
    """The price amount"""

    currency: Literal[
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
    """ISO 4217 currency code"""


class DataTierUnitPrice(BaseModel):
    """Per-unit price in this tier"""

    amount: float
    """The price amount"""

    currency: Literal[
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
    """ISO 4217 currency code"""


class DataTier(BaseModel):
    """A single tier within a tiered charge"""

    flat_price: Optional[DataTierFlatPrice] = FieldInfo(alias="flatPrice", default=None)
    """Flat price for this tier"""

    unit_price: Optional[DataTierUnitPrice] = FieldInfo(alias="unitPrice", default=None)
    """Per-unit price in this tier"""

    up_to: Optional[float] = FieldInfo(alias="upTo", default=None)
    """Upper bound of this tier (null for unlimited)"""


class Data(BaseModel):
    """A single pricing row on a plan or addon.

    Each charge encodes one (billingPeriod, billingModel, billingCadence, billingCountryCode) combination. Plans and addons own many of these — one per currency / billing period / feature.
    """

    id: str
    """Unique identifier of the charge"""

    billing_cadence: Literal["RECURRING", "ONE_OFF"] = FieldInfo(alias="billingCadence")
    """The billing cadence (RECURRING or ONE_OFF)"""

    billing_model: Literal["FLAT_FEE", "MINIMUM_SPEND", "PER_UNIT", "USAGE_BASED", "CREDIT_BASED"] = FieldInfo(
        alias="billingModel"
    )
    """
    The billing model (FLAT_FEE, PER_UNIT, USAGE_BASED, CREDIT_BASED, MINIMUM_SPEND)
    """

    billing_period: Literal["MONTHLY", "ANNUALLY"] = FieldInfo(alias="billingPeriod")
    """The billing period (MONTHLY or ANNUALLY)"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the charge was created"""

    billing_country_code: Optional[str] = FieldInfo(alias="billingCountryCode", default=None)
    """ISO country code for localized pricing, if any"""

    billing_id: Optional[str] = FieldInfo(alias="billingId", default=None)
    """Identifier in the external billing integration (e.g. Stripe price id), if any"""

    block_size: Optional[float] = FieldInfo(alias="blockSize", default=None)
    """Block size for usage-based pricing"""

    credit_grant_cadence: Optional[Literal["BEGINNING_OF_BILLING_PERIOD", "MONTHLY"]] = FieldInfo(
        alias="creditGrantCadence", default=None
    )
    """When credits are granted (for credit-based pricing)"""

    credit_rate: Optional[DataCreditRate] = FieldInfo(alias="creditRate", default=None)
    """Credit rate configuration for credit-based pricing"""

    crm_id: Optional[str] = FieldInfo(alias="crmId", default=None)
    """Identifier in the linked CRM, if any"""

    crm_link_url: Optional[str] = FieldInfo(alias="crmLinkUrl", default=None)
    """Deep link to the charge in the linked CRM, if any"""

    feature_id: Optional[str] = FieldInfo(alias="featureId", default=None)
    """The feature this charge meters, if metered"""

    max_unit_quantity: Optional[float] = FieldInfo(alias="maxUnitQuantity", default=None)
    """Maximum unit quantity that can be purchased"""

    min_unit_quantity: Optional[float] = FieldInfo(alias="minUnitQuantity", default=None)
    """Minimum unit quantity that can be purchased"""

    price: Optional[DataPrice] = None
    """The flat price amount and currency, when applicable"""

    tiers: Optional[List[DataTier]] = None
    """Tiered pricing rows when the charge is tiered"""

    tiers_mode: Optional[Literal["VOLUME", "GRADUATED"]] = FieldInfo(alias="tiersMode", default=None)
    """Tiered pricing mode (VOLUME or GRADUATED) when the charge is tiered"""

    top_up_custom_currency_id: Optional[str] = FieldInfo(alias="topUpCustomCurrencyId", default=None)
    """Custom currency identifier for top-up pricing, if any"""

    used_in_subscriptions: Optional[bool] = FieldInfo(alias="usedInSubscriptions", default=None)
    """True if this charge is referenced by at least one subscription"""


class Pagination(BaseModel):
    """Pagination metadata including cursors for navigating through results"""

    next: Optional[str] = None
    """
    Cursor for fetching the next page of results, or null if no additional pages
    exist
    """

    prev: Optional[str] = None
    """Cursor for fetching the previous page of results, or null if at the beginning"""


class ChargeList(BaseModel):
    """Response list object"""

    data: List[Data]

    pagination: Pagination
    """Pagination metadata including cursors for navigating through results"""
