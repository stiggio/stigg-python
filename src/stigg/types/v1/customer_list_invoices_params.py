# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomerListInvoicesParams"]


class CustomerListInvoicesParams(TypedDict, total=False):
    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    contract_external_id: Annotated[str, PropertyInfo(alias="contractExternalId")]
    """
    Filter to invoices for this contract only (contract external ID or Received
    contract ID). Omit for all contracts.
    """

    issued_after: Annotated[Union[str, datetime], PropertyInfo(alias="issuedAfter", format="iso8601")]
    """Filter to invoices issued on or after this date, inclusive (ISO 8601)"""

    issued_before: Annotated[Union[str, datetime], PropertyInfo(alias="issuedBefore", format="iso8601")]
    """Filter to invoices issued on or before this date, inclusive (ISO 8601)"""

    limit: int
    """Maximum number of items to return"""

    order_by: Annotated[Literal["issueDate", "dueDate", "total"], PropertyInfo(alias="orderBy")]
    """Field to sort by: issueDate (default), dueDate, or total"""

    order_dir: Annotated[Literal["ASC", "DESC"], PropertyInfo(alias="orderDir")]
    """Sort direction: ASC (default) or DESC"""

    state_in: Annotated[str, PropertyInfo(alias="stateIn")]
    """Filter by invoice state. Supports comma-separated values for multiple states"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
