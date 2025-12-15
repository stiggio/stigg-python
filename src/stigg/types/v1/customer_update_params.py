# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomerUpdateParams", "Integration"]


class CustomerUpdateParams(TypedDict, total=False):
    email: Optional[str]
    """The email of the customer"""

    integrations: Iterable[Integration]
    """List of integrations"""

    metadata: Dict[str, str]
    """Additional metadata"""

    name: Optional[str]
    """The name of the customer"""


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
