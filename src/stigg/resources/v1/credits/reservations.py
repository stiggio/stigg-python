# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.credits import reservation_release_params
from ....types.v1.credits.reservation_release_response import ReservationReleaseResponse

__all__ = ["ReservationsResource", "AsyncReservationsResource"]


class ReservationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return ReservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return ReservationsResourceWithStreamingResponse(self)

    def release(
        self,
        reservation_id: str,
        *,
        consumed_amount: float,
        currency_id: str,
        customer_id: str,
        resource_id: str | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReservationReleaseResponse:
        """
        Releases a credit reservation, consuming the given amount and returning the rest
        of the held credits to the balance. Retry a failed release with the same
        reservation ID; it is applied once.

        Args:
          consumed_amount: The amount of credits to consume at release. Up to the reserved amount is
              charged to the credits that backed the reservation; the rest returns to the
              balance, and any amount above the reservation is consumed normally.

          currency_id: The credit currency of the reservation

          customer_id: The customer the reservation was made for

          resource_id: The resource the reservation was made for, if any

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reservation_id:
            raise ValueError(f"Expected a non-empty value for `reservation_id` but received {reservation_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-ACCOUNT-ID": x_account_id,
                    "X-ENVIRONMENT-ID": x_environment_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/api/v1/credits/reservations/{reservation_id}/release", reservation_id=reservation_id),
            body=maybe_transform(
                {
                    "consumed_amount": consumed_amount,
                    "currency_id": currency_id,
                    "customer_id": customer_id,
                    "resource_id": resource_id,
                },
                reservation_release_params.ReservationReleaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationReleaseResponse,
        )


class AsyncReservationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncReservationsResourceWithStreamingResponse(self)

    async def release(
        self,
        reservation_id: str,
        *,
        consumed_amount: float,
        currency_id: str,
        customer_id: str,
        resource_id: str | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReservationReleaseResponse:
        """
        Releases a credit reservation, consuming the given amount and returning the rest
        of the held credits to the balance. Retry a failed release with the same
        reservation ID; it is applied once.

        Args:
          consumed_amount: The amount of credits to consume at release. Up to the reserved amount is
              charged to the credits that backed the reservation; the rest returns to the
              balance, and any amount above the reservation is consumed normally.

          currency_id: The credit currency of the reservation

          customer_id: The customer the reservation was made for

          resource_id: The resource the reservation was made for, if any

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reservation_id:
            raise ValueError(f"Expected a non-empty value for `reservation_id` but received {reservation_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-ACCOUNT-ID": x_account_id,
                    "X-ENVIRONMENT-ID": x_environment_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/api/v1/credits/reservations/{reservation_id}/release", reservation_id=reservation_id),
            body=await async_maybe_transform(
                {
                    "consumed_amount": consumed_amount,
                    "currency_id": currency_id,
                    "customer_id": customer_id,
                    "resource_id": resource_id,
                },
                reservation_release_params.ReservationReleaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationReleaseResponse,
        )


class ReservationsResourceWithRawResponse:
    def __init__(self, reservations: ReservationsResource) -> None:
        self._reservations = reservations

        self.release = to_raw_response_wrapper(
            reservations.release,
        )


class AsyncReservationsResourceWithRawResponse:
    def __init__(self, reservations: AsyncReservationsResource) -> None:
        self._reservations = reservations

        self.release = async_to_raw_response_wrapper(
            reservations.release,
        )


class ReservationsResourceWithStreamingResponse:
    def __init__(self, reservations: ReservationsResource) -> None:
        self._reservations = reservations

        self.release = to_streamed_response_wrapper(
            reservations.release,
        )


class AsyncReservationsResourceWithStreamingResponse:
    def __init__(self, reservations: AsyncReservationsResource) -> None:
        self._reservations = reservations

        self.release = async_to_streamed_response_wrapper(
            reservations.release,
        )
