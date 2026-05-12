# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CustomCurrencyCreateParams", "Units"]


class CustomCurrencyCreateParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the new custom currency"""

    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]
    """The display name of the custom currency"""

    description: str
    """Description of the currency"""

    metadata: Dict[str, str]
    """Additional metadata to attach to the custom currency"""

    symbol: str
    """The symbol used to represent the custom currency"""

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
