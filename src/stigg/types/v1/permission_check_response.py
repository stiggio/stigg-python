# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PermissionCheckResponse"]


class PermissionCheckResponse(BaseModel):
    permitted_list: List[bool] = FieldInfo(alias="permittedList")
    """
    List of booleans indicating whether the user has access to each resource and
    action correspondingly
    """
