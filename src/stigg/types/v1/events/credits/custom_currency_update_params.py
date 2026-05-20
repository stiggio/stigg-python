# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CustomCurrencyUpdateParams", "Units"]


class CustomCurrencyUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """A human-readable description of the custom currency.

    Send an empty string to clear.
    """

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """The display name of the custom currency"""

    metadata: Optional[Dict[str, str]]
    """Additional metadata to attach to the custom currency"""

    symbol: Optional[str]
    """The symbol used to represent the custom currency.

    Send an empty string to clear.
    """

    units: Units
    """Singular and plural unit labels for a custom currency.

    Both fields are required when supplied.
    """


class Units(TypedDict, total=False):
    """Singular and plural unit labels for a custom currency.

    Both fields are required when supplied.
    """

    plural: Required[str]
    """Plural form of the unit label"""

    singular: Required[str]
    """Singular form of the unit label"""
