# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubscriptionImportResponse", "Data"]


class Data(BaseModel):
    task_id: str = FieldInfo(alias="taskId")
    """Unique identifier for the import task"""


class SubscriptionImportResponse(BaseModel):
    """Response object"""

    data: Data
