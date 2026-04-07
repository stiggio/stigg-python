# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CustomerIntegrationResponse",
    "Data",
    "DataSyncData",
    "DataSyncDataSyncRevisionPriceBillingData",
    "DataSyncDataSyncRevisionBillingData",
    "DataSyncDataSyncRevisionMarketplaceData",
]


class DataSyncDataSyncRevisionPriceBillingData(BaseModel):
    """
    Price billing sync revision data containing billing ID, link URL, and price group package billing ID
    """

    billing_id: str = FieldInfo(alias="billingId")
    """Billing integration id"""

    billing_link_url: str = FieldInfo(alias="billingLinkUrl")
    """Billing integration url"""

    price_group_package_billing_id: str = FieldInfo(alias="priceGroupPackageBillingId")
    """Price group package billing id"""


class DataSyncDataSyncRevisionBillingData(BaseModel):
    """Billing sync revision data containing billing ID and link URL"""

    billing_id: str = FieldInfo(alias="billingId")
    """Billing integration id"""

    billing_link_url: str = FieldInfo(alias="billingLinkUrl")
    """Billing integration url"""


class DataSyncDataSyncRevisionMarketplaceData(BaseModel):
    """Marketplace sync revision data containing dimensions"""

    dimensions: str
    """Dimensions of the marketplace sync revision"""


DataSyncData: TypeAlias = Union[
    DataSyncDataSyncRevisionPriceBillingData,
    DataSyncDataSyncRevisionBillingData,
    DataSyncDataSyncRevisionMarketplaceData,
    None,
]


class Data(BaseModel):
    """External billing or CRM integration link"""

    id: str
    """Integration details"""

    synced_entity_id: Optional[str] = FieldInfo(alias="syncedEntityId", default=None)
    """Synced entity id"""

    vendor_identifier: Literal[
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
    ] = FieldInfo(alias="vendorIdentifier")
    """The vendor identifier of integration"""

    sync_data: Optional[DataSyncData] = FieldInfo(alias="syncData", default=None)
    """
    Price billing sync revision data containing billing ID, link URL, and price
    group package billing ID
    """


class CustomerIntegrationResponse(BaseModel):
    """Response object"""

    data: Data
    """External billing or CRM integration link"""
