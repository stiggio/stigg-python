# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from .entity_types import (
    EntityTypesResource,
    AsyncEntityTypesResource,
    EntityTypesResourceWithRawResponse,
    AsyncEntityTypesResourceWithRawResponse,
    EntityTypesResourceWithStreamingResponse,
    AsyncEntityTypesResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from .customers.customers import (
    CustomersResource,
    AsyncCustomersResource,
    CustomersResourceWithRawResponse,
    AsyncCustomersResourceWithRawResponse,
    CustomersResourceWithStreamingResponse,
    AsyncCustomersResourceWithStreamingResponse,
)

__all__ = ["BetaResource", "AsyncBetaResource"]


class BetaResource(SyncAPIResource):
    @cached_property
    def customers(self) -> CustomersResource:
        return CustomersResource(self._client)

    @cached_property
    def entity_types(self) -> EntityTypesResource:
        return EntityTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return BetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return BetaResourceWithStreamingResponse(self)


class AsyncBetaResource(AsyncAPIResource):
    @cached_property
    def customers(self) -> AsyncCustomersResource:
        return AsyncCustomersResource(self._client)

    @cached_property
    def entity_types(self) -> AsyncEntityTypesResource:
        return AsyncEntityTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncBetaResourceWithStreamingResponse(self)


class BetaResourceWithRawResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def customers(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self._beta.customers)

    @cached_property
    def entity_types(self) -> EntityTypesResourceWithRawResponse:
        return EntityTypesResourceWithRawResponse(self._beta.entity_types)


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self._beta.customers)

    @cached_property
    def entity_types(self) -> AsyncEntityTypesResourceWithRawResponse:
        return AsyncEntityTypesResourceWithRawResponse(self._beta.entity_types)


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def customers(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self._beta.customers)

    @cached_property
    def entity_types(self) -> EntityTypesResourceWithStreamingResponse:
        return EntityTypesResourceWithStreamingResponse(self._beta.entity_types)


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self._beta.customers)

    @cached_property
    def entity_types(self) -> AsyncEntityTypesResourceWithStreamingResponse:
        return AsyncEntityTypesResourceWithStreamingResponse(self._beta.entity_types)
