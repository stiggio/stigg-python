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
from ...._compat import cached_property
from .assignments import (
    AssignmentsResource,
    AsyncAssignmentsResource,
    AssignmentsResourceWithRawResponse,
    AsyncAssignmentsResourceWithRawResponse,
    AssignmentsResourceWithStreamingResponse,
    AsyncAssignmentsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .entitlements import (
    EntitlementsResource,
    AsyncEntitlementsResource,
    EntitlementsResourceWithRawResponse,
    AsyncEntitlementsResourceWithRawResponse,
    EntitlementsResourceWithStreamingResponse,
    AsyncEntitlementsResourceWithStreamingResponse,
)

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def entitlements(self) -> EntitlementsResource:
        return EntitlementsResource(self._client)

    @cached_property
    def entities(self) -> EntitiesResource:
        return EntitiesResource(self._client)

    @cached_property
    def assignments(self) -> AssignmentsResource:
        return AssignmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return CustomersResourceWithStreamingResponse(self)


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def entitlements(self) -> AsyncEntitlementsResource:
        return AsyncEntitlementsResource(self._client)

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        return AsyncEntitiesResource(self._client)

    @cached_property
    def assignments(self) -> AsyncAssignmentsResource:
        return AsyncAssignmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncCustomersResourceWithStreamingResponse(self)


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithRawResponse:
        return EntitlementsResourceWithRawResponse(self._customers.entitlements)

    @cached_property
    def entities(self) -> EntitiesResourceWithRawResponse:
        return EntitiesResourceWithRawResponse(self._customers.entities)

    @cached_property
    def assignments(self) -> AssignmentsResourceWithRawResponse:
        return AssignmentsResourceWithRawResponse(self._customers.assignments)


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithRawResponse:
        return AsyncEntitlementsResourceWithRawResponse(self._customers.entitlements)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithRawResponse:
        return AsyncEntitiesResourceWithRawResponse(self._customers.entities)

    @cached_property
    def assignments(self) -> AsyncAssignmentsResourceWithRawResponse:
        return AsyncAssignmentsResourceWithRawResponse(self._customers.assignments)


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithStreamingResponse:
        return EntitlementsResourceWithStreamingResponse(self._customers.entitlements)

    @cached_property
    def entities(self) -> EntitiesResourceWithStreamingResponse:
        return EntitiesResourceWithStreamingResponse(self._customers.entities)

    @cached_property
    def assignments(self) -> AssignmentsResourceWithStreamingResponse:
        return AssignmentsResourceWithStreamingResponse(self._customers.assignments)


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithStreamingResponse:
        return AsyncEntitlementsResourceWithStreamingResponse(self._customers.entitlements)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithStreamingResponse:
        return AsyncEntitiesResourceWithStreamingResponse(self._customers.entities)

    @cached_property
    def assignments(self) -> AsyncAssignmentsResourceWithStreamingResponse:
        return AsyncAssignmentsResourceWithStreamingResponse(self._customers.assignments)
