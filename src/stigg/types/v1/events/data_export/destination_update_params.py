# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["DestinationUpdateParams"]


class DestinationUpdateParams(TypedDict, total=False):
    enabled_models: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="enabledModels")]]

    integration_id: Required[Annotated[str, PropertyInfo(alias="integrationId")]]
    """Target integration row hosting the destination"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
