# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DataExportTriggerSyncParams"]


class DataExportTriggerSyncParams(TypedDict, total=False):
    destination_id: Annotated[str, PropertyInfo(alias="destinationId")]
    """Provider destination ID to sync. Omit to sync all destinations."""
