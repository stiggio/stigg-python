# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.credits import auto_recharge_get_auto_recharge_params
from ....types.v1.credits.auto_recharge_get_auto_recharge_response import AutoRechargeGetAutoRechargeResponse

__all__ = ["AutoRechargeResource", "AsyncAutoRechargeResource"]


class AutoRechargeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutoRechargeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AutoRechargeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutoRechargeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AutoRechargeResourceWithStreamingResponse(self)

    def get_auto_recharge(
        self,
        *,
        currency_id: str,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoRechargeGetAutoRechargeResponse:
        """
        Retrieves the automatic recharge configuration for a customer and currency.
        Returns default settings if no configuration exists.

        Args:
          currency_id: Filter by currency ID (required)

          customer_id: Filter by customer ID (required)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/credits/auto-recharge",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency_id": currency_id,
                        "customer_id": customer_id,
                    },
                    auto_recharge_get_auto_recharge_params.AutoRechargeGetAutoRechargeParams,
                ),
            ),
            cast_to=AutoRechargeGetAutoRechargeResponse,
        )


class AsyncAutoRechargeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutoRechargeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutoRechargeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutoRechargeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncAutoRechargeResourceWithStreamingResponse(self)

    async def get_auto_recharge(
        self,
        *,
        currency_id: str,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoRechargeGetAutoRechargeResponse:
        """
        Retrieves the automatic recharge configuration for a customer and currency.
        Returns default settings if no configuration exists.

        Args:
          currency_id: Filter by currency ID (required)

          customer_id: Filter by customer ID (required)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/credits/auto-recharge",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "currency_id": currency_id,
                        "customer_id": customer_id,
                    },
                    auto_recharge_get_auto_recharge_params.AutoRechargeGetAutoRechargeParams,
                ),
            ),
            cast_to=AutoRechargeGetAutoRechargeResponse,
        )


class AutoRechargeResourceWithRawResponse:
    def __init__(self, auto_recharge: AutoRechargeResource) -> None:
        self._auto_recharge = auto_recharge

        self.get_auto_recharge = to_raw_response_wrapper(
            auto_recharge.get_auto_recharge,
        )


class AsyncAutoRechargeResourceWithRawResponse:
    def __init__(self, auto_recharge: AsyncAutoRechargeResource) -> None:
        self._auto_recharge = auto_recharge

        self.get_auto_recharge = async_to_raw_response_wrapper(
            auto_recharge.get_auto_recharge,
        )


class AutoRechargeResourceWithStreamingResponse:
    def __init__(self, auto_recharge: AutoRechargeResource) -> None:
        self._auto_recharge = auto_recharge

        self.get_auto_recharge = to_streamed_response_wrapper(
            auto_recharge.get_auto_recharge,
        )


class AsyncAutoRechargeResourceWithStreamingResponse:
    def __init__(self, auto_recharge: AsyncAutoRechargeResource) -> None:
        self._auto_recharge = auto_recharge

        self.get_auto_recharge = async_to_streamed_response_wrapper(
            auto_recharge.get_auto_recharge,
        )
