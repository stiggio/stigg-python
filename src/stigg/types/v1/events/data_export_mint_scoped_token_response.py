# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DataExportMintScopedTokenResponse", "Data"]


class Data(BaseModel):
    """Scoped token + expiry + provider-specific metadata for the FE SDK."""

    token: str
    """Provider scoped JWT"""

    expires_at: str = FieldInfo(alias="expiresAt")
    """ISO8601 token expiry"""

    provider_metadata: Dict[str, object] = FieldInfo(alias="providerMetadata")
    """Provider-specific extras the FE embedded SDK needs"""


class DataExportMintScopedTokenResponse(BaseModel):
    """Response object"""

    data: Data
    """Scoped token + expiry + provider-specific metadata for the FE SDK."""
