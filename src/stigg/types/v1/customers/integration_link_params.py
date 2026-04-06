# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IntegrationLinkParams"]


class IntegrationLinkParams(TypedDict, total=False):
    body_id: Required[Annotated[str, PropertyInfo(alias="id")]]
    """Integration details"""

    synced_entity_id: Required[Annotated[str, PropertyInfo(alias="syncedEntityId")]]
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
