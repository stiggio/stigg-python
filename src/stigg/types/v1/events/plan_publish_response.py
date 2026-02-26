# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PlanPublishResponse", "Data"]


class Data(BaseModel):
    task_id: Optional[str] = FieldInfo(alias="taskId", default=None)
    """Task ID for tracking the async publish operation"""


class PlanPublishResponse(BaseModel):
    """Response containing task ID for publish operation"""

    data: Data
