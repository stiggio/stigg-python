# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["DataExportMintScopedTokenParams"]


class DataExportMintScopedTokenParams(TypedDict, total=False):
    application_origin: Required[Annotated[str, PropertyInfo(alias="applicationOrigin")]]
    """FE origin the resulting JWT is bound to (provider-side anti-fraud)"""

    destination_type: Annotated[str, PropertyInfo(alias="destinationType")]
    """Pin the token to a specific warehouse connect flow"""

    enabled_models: Annotated[SequenceNotStr[str], PropertyInfo(alias="enabledModels")]

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
