# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PermissionCheckParams", "ResourcesAndAction"]


class PermissionCheckParams(TypedDict, total=False):
    user_id: Required[Annotated[str, PropertyInfo(alias="userId")]]
    """ID of the user to check permissions for"""

    resources_and_actions: Required[Annotated[Iterable[ResourcesAndAction], PropertyInfo(alias="resourcesAndActions")]]
    """List of resources and actions to check permissions for"""


class ResourcesAndAction(TypedDict, total=False):
    action: Required[object]
    """Action to check permissions for"""

    resource: Required[str]
    """Resource to check permissions for"""
