# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["DestinationCreateResponse", "Data", "DataDestination", "DataDestinationLastSyncStatus"]


class DataDestinationLastSyncStatus(BaseModel):
    """Latest sync snapshot for the destination, refreshed by the provider webhook"""

    finished_at: str = FieldInfo(alias="finishedAt")
    """ISO8601 timestamp of when the latest sync finished"""

    status: str
    """Sync status (PENDING, RUNNING, INCOMPLETE, FAILED, SUCCEEDED, CANCELLED)"""

    transfer_id: str = FieldInfo(alias="transferId")
    """Provider transfer ID of the latest sync"""

    blamed_party: Optional[str] = FieldInfo(alias="blamedParty", default=None)
    """Party responsible for a failed sync, as reported by the data-export provider"""

    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """Customer-friendly failure message, when the latest sync failed"""

    rows_transferred: Optional[float] = FieldInfo(alias="rowsTransferred", default=None)
    """Number of rows transferred in the latest sync"""


class DataDestination(BaseModel):
    """A single destination entry under the DATA_EXPORT integration."""

    connected_at: str = FieldInfo(alias="connectedAt")
    """ISO8601 timestamp of when the destination was connected"""

    destination_id: str = FieldInfo(alias="destinationId")
    """Provider destination ID"""

    type: str
    """Destination type (snowflake, bigquery, ...)"""

    connection_status: Optional[str] = FieldInfo(alias="connectionStatus", default=None)
    """Connection status of the destination (connected, failed)"""

    enabled_models: Optional[List[str]] = FieldInfo(alias="enabledModels", default=None)

    last_sync_status: Optional[DataDestinationLastSyncStatus] = FieldInfo(alias="lastSyncStatus", default=None)
    """Latest sync snapshot for the destination, refreshed by the provider webhook"""


class Data(BaseModel):
    """Current destinations under the DATA_EXPORT integration."""

    destinations: List[DataDestination]
    """Current destinations under the DATA_EXPORT integration"""


class DestinationCreateResponse(BaseModel):
    """Response object"""

    data: Data
    """Current destinations under the DATA_EXPORT integration."""
