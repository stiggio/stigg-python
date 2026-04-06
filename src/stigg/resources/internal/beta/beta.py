# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .event_queues import (
    EventQueuesResource,
    AsyncEventQueuesResource,
    EventQueuesResourceWithRawResponse,
    AsyncEventQueuesResourceWithRawResponse,
    EventQueuesResourceWithStreamingResponse,
    AsyncEventQueuesResourceWithStreamingResponse,
)

__all__ = ["BetaResource", "AsyncBetaResource"]


class BetaResource(SyncAPIResource):
    @cached_property
    def event_queues(self) -> EventQueuesResource:
        return EventQueuesResource(self._client)

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
    def event_queues(self) -> AsyncEventQueuesResource:
        return AsyncEventQueuesResource(self._client)

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
    def event_queues(self) -> EventQueuesResourceWithRawResponse:
        return EventQueuesResourceWithRawResponse(self._beta.event_queues)


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def event_queues(self) -> AsyncEventQueuesResourceWithRawResponse:
        return AsyncEventQueuesResourceWithRawResponse(self._beta.event_queues)


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def event_queues(self) -> EventQueuesResourceWithStreamingResponse:
        return EventQueuesResourceWithStreamingResponse(self._beta.event_queues)


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def event_queues(self) -> AsyncEventQueuesResourceWithStreamingResponse:
        return AsyncEventQueuesResourceWithStreamingResponse(self._beta.event_queues)
