# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContractListParams"]


class ContractListParams(TypedDict, total=False):
    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    customer_external_id: Annotated[str, PropertyInfo(alias="customerExternalId")]
    """Filter by the exact external ID of the customer the contract belongs to"""

    limit: int
    """Maximum number of items to return"""

    name: str
    """Filter by exact contract name"""

    state: str
    """Filter by contract state. Supports comma-separated values for multiple states"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
