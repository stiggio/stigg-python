# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DataExportTriggerSyncResponse", "Data", "DataResult"]


class DataResult(BaseModel):
    """Per-destination trigger results."""

    destination_id: str = FieldInfo(alias="destinationId")
    """Provider destination ID"""

    triggered: bool
    """True if a transfer was kicked"""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """Error message if triggered=false on a hard failure"""

    transfer_id: Optional[str] = FieldInfo(alias="transferId", default=None)
    """Provider-side transfer ID"""


class Data(BaseModel):
    """Per-destination trigger results across the batch."""

    results: List[DataResult]
    """Per-destination trigger results"""


class DataExportTriggerSyncResponse(BaseModel):
    """Response object"""

    data: Data
    """Per-destination trigger results across the batch."""
