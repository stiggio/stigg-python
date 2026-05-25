# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .entities import (
    EntitiesResource,
    AsyncEntitiesResource,
    EntitiesResourceWithRawResponse,
    AsyncEntitiesResourceWithRawResponse,
    EntitiesResourceWithStreamingResponse,
    AsyncEntitiesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .entity_types import (
    EntityTypesResource,
    AsyncEntityTypesResource,
    EntityTypesResourceWithRawResponse,
    AsyncEntityTypesResourceWithRawResponse,
    EntityTypesResourceWithStreamingResponse,
    AsyncEntityTypesResourceWithStreamingResponse,
)
from .customers.customers import (
    CustomersResource,
    AsyncCustomersResource,
    CustomersResourceWithRawResponse,
    AsyncCustomersResourceWithRawResponse,
    CustomersResourceWithStreamingResponse,
    AsyncCustomersResourceWithStreamingResponse,
)

__all__ = ["V1BetaResource", "AsyncV1BetaResource"]


class V1BetaResource(SyncAPIResource):
    @cached_property
    def customers(self) -> CustomersResource:
        return CustomersResource(self._client)

    @cached_property
    def entity_types(self) -> EntityTypesResource:
        return EntityTypesResource(self._client)

    @cached_property
    def entities(self) -> EntitiesResource:
        return EntitiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1BetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return V1BetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1BetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return V1BetaResourceWithStreamingResponse(self)


class AsyncV1BetaResource(AsyncAPIResource):
    @cached_property
    def customers(self) -> AsyncCustomersResource:
        return AsyncCustomersResource(self._client)

    @cached_property
    def entity_types(self) -> AsyncEntityTypesResource:
        return AsyncEntityTypesResource(self._client)

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        return AsyncEntitiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1BetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1BetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1BetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncV1BetaResourceWithStreamingResponse(self)


class V1BetaResourceWithRawResponse:
    def __init__(self, v1_beta: V1BetaResource) -> None:
        self._v1_beta = v1_beta

    @cached_property
    def customers(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self._v1_beta.customers)

    @cached_property
    def entity_types(self) -> EntityTypesResourceWithRawResponse:
        return EntityTypesResourceWithRawResponse(self._v1_beta.entity_types)

    @cached_property
    def entities(self) -> EntitiesResourceWithRawResponse:
        return EntitiesResourceWithRawResponse(self._v1_beta.entities)


class AsyncV1BetaResourceWithRawResponse:
    def __init__(self, v1_beta: AsyncV1BetaResource) -> None:
        self._v1_beta = v1_beta

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self._v1_beta.customers)

    @cached_property
    def entity_types(self) -> AsyncEntityTypesResourceWithRawResponse:
        return AsyncEntityTypesResourceWithRawResponse(self._v1_beta.entity_types)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithRawResponse:
        return AsyncEntitiesResourceWithRawResponse(self._v1_beta.entities)


class V1BetaResourceWithStreamingResponse:
    def __init__(self, v1_beta: V1BetaResource) -> None:
        self._v1_beta = v1_beta

    @cached_property
    def customers(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self._v1_beta.customers)

    @cached_property
    def entity_types(self) -> EntityTypesResourceWithStreamingResponse:
        return EntityTypesResourceWithStreamingResponse(self._v1_beta.entity_types)

    @cached_property
    def entities(self) -> EntitiesResourceWithStreamingResponse:
        return EntitiesResourceWithStreamingResponse(self._v1_beta.entities)


class AsyncV1BetaResourceWithStreamingResponse:
    def __init__(self, v1_beta: AsyncV1BetaResource) -> None:
        self._v1_beta = v1_beta

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self._v1_beta.customers)

    @cached_property
    def entity_types(self) -> AsyncEntityTypesResourceWithStreamingResponse:
        return AsyncEntityTypesResourceWithStreamingResponse(self._v1_beta.entity_types)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithStreamingResponse:
        return AsyncEntitiesResourceWithStreamingResponse(self._v1_beta.entities)
