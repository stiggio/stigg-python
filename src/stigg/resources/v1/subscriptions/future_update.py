# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.subscriptions.future_update_cancel_schedule_response import FutureUpdateCancelScheduleResponse
from ....types.v1.subscriptions.future_update_cancel_pending_payment_response import (
    FutureUpdateCancelPendingPaymentResponse,
)

__all__ = ["FutureUpdateResource", "AsyncFutureUpdateResource"]


class FutureUpdateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FutureUpdateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return FutureUpdateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FutureUpdateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return FutureUpdateResourceWithStreamingResponse(self)

    def cancel_pending_payment(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureUpdateCancelPendingPaymentResponse:
        """
        Perform cancel future update on a Subscription

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v1/subscriptions/{id}/future-update/pending-payment",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FutureUpdateCancelPendingPaymentResponse,
        )

    def cancel_schedule(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureUpdateCancelScheduleResponse:
        """
        Perform cancel future update on a Subscription

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v1/subscriptions/{id}/future-update/schedule",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FutureUpdateCancelScheduleResponse,
        )


class AsyncFutureUpdateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFutureUpdateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFutureUpdateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFutureUpdateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncFutureUpdateResourceWithStreamingResponse(self)

    async def cancel_pending_payment(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureUpdateCancelPendingPaymentResponse:
        """
        Perform cancel future update on a Subscription

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v1/subscriptions/{id}/future-update/pending-payment",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FutureUpdateCancelPendingPaymentResponse,
        )

    async def cancel_schedule(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureUpdateCancelScheduleResponse:
        """
        Perform cancel future update on a Subscription

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v1/subscriptions/{id}/future-update/schedule",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FutureUpdateCancelScheduleResponse,
        )


class FutureUpdateResourceWithRawResponse:
    def __init__(self, future_update: FutureUpdateResource) -> None:
        self._future_update = future_update

        self.cancel_pending_payment = to_raw_response_wrapper(
            future_update.cancel_pending_payment,
        )
        self.cancel_schedule = to_raw_response_wrapper(
            future_update.cancel_schedule,
        )


class AsyncFutureUpdateResourceWithRawResponse:
    def __init__(self, future_update: AsyncFutureUpdateResource) -> None:
        self._future_update = future_update

        self.cancel_pending_payment = async_to_raw_response_wrapper(
            future_update.cancel_pending_payment,
        )
        self.cancel_schedule = async_to_raw_response_wrapper(
            future_update.cancel_schedule,
        )


class FutureUpdateResourceWithStreamingResponse:
    def __init__(self, future_update: FutureUpdateResource) -> None:
        self._future_update = future_update

        self.cancel_pending_payment = to_streamed_response_wrapper(
            future_update.cancel_pending_payment,
        )
        self.cancel_schedule = to_streamed_response_wrapper(
            future_update.cancel_schedule,
        )


class AsyncFutureUpdateResourceWithStreamingResponse:
    def __init__(self, future_update: AsyncFutureUpdateResource) -> None:
        self._future_update = future_update

        self.cancel_pending_payment = async_to_streamed_response_wrapper(
            future_update.cancel_pending_payment,
        )
        self.cancel_schedule = async_to_streamed_response_wrapper(
            future_update.cancel_schedule,
        )
