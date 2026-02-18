# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .plans import (
    PlansResource,
    AsyncPlansResource,
    PlansResourceWithRawResponse,
    AsyncPlansResourceWithRawResponse,
    PlansResourceWithStreamingResponse,
    AsyncPlansResourceWithStreamingResponse,
)
from .features import (
    FeaturesResource,
    AsyncFeaturesResource,
    FeaturesResourceWithRawResponse,
    AsyncFeaturesResourceWithRawResponse,
    FeaturesResourceWithStreamingResponse,
    AsyncFeaturesResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import event_report_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .addons.addons import (
    AddonsResource,
    AsyncAddonsResource,
    AddonsResourceWithRawResponse,
    AsyncAddonsResourceWithRawResponse,
    AddonsResourceWithStreamingResponse,
    AsyncAddonsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.v1.event_report_response import EventReportResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def features(self) -> FeaturesResource:
        return FeaturesResource(self._client)

    @cached_property
    def addons(self) -> AddonsResource:
        return AddonsResource(self._client)

    @cached_property
    def plans(self) -> PlansResource:
        return PlansResource(self._client)

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def report(
        self,
        *,
        events: Iterable[event_report_params.Event],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventReportResponse:
        """Reports raw usage events for event-based metering.

        Events are ingested
        asynchronously and aggregated into usage totals.

        Args:
          events: A list of usage events to report

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/events",
            body=maybe_transform({"events": events}, event_report_params.EventReportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventReportResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def features(self) -> AsyncFeaturesResource:
        return AsyncFeaturesResource(self._client)

    @cached_property
    def addons(self) -> AsyncAddonsResource:
        return AsyncAddonsResource(self._client)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        return AsyncPlansResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def report(
        self,
        *,
        events: Iterable[event_report_params.Event],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventReportResponse:
        """Reports raw usage events for event-based metering.

        Events are ingested
        asynchronously and aggregated into usage totals.

        Args:
          events: A list of usage events to report

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/events",
            body=await async_maybe_transform({"events": events}, event_report_params.EventReportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventReportResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.report = to_raw_response_wrapper(
            events.report,
        )

    @cached_property
    def features(self) -> FeaturesResourceWithRawResponse:
        return FeaturesResourceWithRawResponse(self._events.features)

    @cached_property
    def addons(self) -> AddonsResourceWithRawResponse:
        return AddonsResourceWithRawResponse(self._events.addons)

    @cached_property
    def plans(self) -> PlansResourceWithRawResponse:
        return PlansResourceWithRawResponse(self._events.plans)


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.report = async_to_raw_response_wrapper(
            events.report,
        )

    @cached_property
    def features(self) -> AsyncFeaturesResourceWithRawResponse:
        return AsyncFeaturesResourceWithRawResponse(self._events.features)

    @cached_property
    def addons(self) -> AsyncAddonsResourceWithRawResponse:
        return AsyncAddonsResourceWithRawResponse(self._events.addons)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithRawResponse:
        return AsyncPlansResourceWithRawResponse(self._events.plans)


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.report = to_streamed_response_wrapper(
            events.report,
        )

    @cached_property
    def features(self) -> FeaturesResourceWithStreamingResponse:
        return FeaturesResourceWithStreamingResponse(self._events.features)

    @cached_property
    def addons(self) -> AddonsResourceWithStreamingResponse:
        return AddonsResourceWithStreamingResponse(self._events.addons)

    @cached_property
    def plans(self) -> PlansResourceWithStreamingResponse:
        return PlansResourceWithStreamingResponse(self._events.plans)


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.report = async_to_streamed_response_wrapper(
            events.report,
        )

    @cached_property
    def features(self) -> AsyncFeaturesResourceWithStreamingResponse:
        return AsyncFeaturesResourceWithStreamingResponse(self._events.features)

    @cached_property
    def addons(self) -> AsyncAddonsResourceWithStreamingResponse:
        return AsyncAddonsResourceWithStreamingResponse(self._events.addons)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithStreamingResponse:
        return AsyncPlansResourceWithStreamingResponse(self._events.plans)
