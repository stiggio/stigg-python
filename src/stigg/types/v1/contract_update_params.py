# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ContractUpdateParams"]


class ContractUpdateParams(TypedDict, total=False):
    activation_end_date: Annotated[Union[str, datetime], PropertyInfo(alias="activationEndDate", format="iso8601")]
    """New activation end date"""

    activation_start_date: Annotated[Union[str, datetime], PropertyInfo(alias="activationStartDate", format="iso8601")]
    """New activation start date"""

    name: Optional[str]
    """New contract name"""

    po_number: Annotated[Optional[str], PropertyInfo(alias="poNumber")]
    """New purchase-order number"""

    setup_billing: Annotated[bool, PropertyInfo(alias="setupBilling")]
    """
    Enable billing on a provision-access-only contract by creating a billing
    contract in the connected billing provider. Only takes effect when true and the
    contract has no billing yet; omitting it leaves billing unchanged. Billing is
    never removed by an update.
    """

    subscription_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="subscriptionIds")]
    """
    When provided, replaces the set of subscriptions linked to the contract
    (subscription ref IDs)
    """

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
