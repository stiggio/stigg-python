# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["FutureUpdateCancelScheduleResponse", "Data"]


class Data(BaseModel):
    id: str
    """external id of the canceled future update subscription"""


class FutureUpdateCancelScheduleResponse(BaseModel):
    data: Data
