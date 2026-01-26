# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["FutureUpdateCancelPendingPaymentResponse", "Data"]


class Data(BaseModel):
    id: str
    """Subscription ID"""


class FutureUpdateCancelPendingPaymentResponse(BaseModel):
    data: Data
