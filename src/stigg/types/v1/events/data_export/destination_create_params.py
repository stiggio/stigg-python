# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["DestinationCreateParams"]


class DestinationCreateParams(TypedDict, total=False):
    destination_id: Required[Annotated[str, PropertyInfo(alias="destinationId")]]
    """The provider destination ID returned by the embedded SDK on connect"""

    destination_type: Required[Annotated[str, PropertyInfo(alias="destinationType")]]
    """The destination type (e.g. snowflake, bigquery)"""

    enabled_models: Annotated[SequenceNotStr[str], PropertyInfo(alias="enabledModels")]

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
