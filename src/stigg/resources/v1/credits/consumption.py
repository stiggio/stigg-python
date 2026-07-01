# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.credits import consumption_consume_params, consumption_consume_async_params
from ....types.v1.credits.consumption_consume_response import ConsumptionConsumeResponse
from ....types.v1.credits.consumption_consume_async_response import ConsumptionConsumeAsyncResponse

__all__ = ["ConsumptionResource", "AsyncConsumptionResource"]


class ConsumptionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConsumptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return ConsumptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsumptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return ConsumptionResourceWithStreamingResponse(self)

    def consume(
        self,
        *,
        amount: float,
        currency_id: str,
        customer_id: str,
        idempotency_key: str,
        created_at: Union[str, datetime] | Omit = omit,
        dimensions: Dict[str, Union[str, float, bool]] | Omit = omit,
        resource_id: str | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConsumptionConsumeResponse:
        """
        Consumes a specified amount of credits directly from a customer wallet, with no
        feature mapping. Returns the optimistic balance.

        Args:
          amount: The amount of credits to consume

          currency_id: The credit currency to consume from (required)

          customer_id: The customer to consume credits from (required)

          idempotency_key: A unique key used to deduplicate the consumption (required)

          created_at: Optional timestamp the consumption is attributed to

          dimensions: Optional dimensions describing the consumption

          resource_id: Optional resource the consumption is attributed to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            "/api/v1/credits/consumption",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency_id": currency_id,
                    "customer_id": customer_id,
                    "idempotency_key": idempotency_key,
                    "created_at": created_at,
                    "dimensions": dimensions,
                    "resource_id": resource_id,
                },
                consumption_consume_params.ConsumptionConsumeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsumptionConsumeResponse,
        )

    def consume_async(
        self,
        *,
        consumptions: Iterable[consumption_consume_async_params.Consumption],
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConsumptionConsumeAsyncResponse:
        """Consumes credits directly from customer wallets asynchronously.

        Consumptions are
        reconciled asynchronously into the credit balances.

        Args:
          consumptions: The credit consumptions to report (up to 1000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            "/api/v1/credits/consumption/async",
            body=maybe_transform(
                {"consumptions": consumptions}, consumption_consume_async_params.ConsumptionConsumeAsyncParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsumptionConsumeAsyncResponse,
        )


class AsyncConsumptionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConsumptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConsumptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsumptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncConsumptionResourceWithStreamingResponse(self)

    async def consume(
        self,
        *,
        amount: float,
        currency_id: str,
        customer_id: str,
        idempotency_key: str,
        created_at: Union[str, datetime] | Omit = omit,
        dimensions: Dict[str, Union[str, float, bool]] | Omit = omit,
        resource_id: str | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConsumptionConsumeResponse:
        """
        Consumes a specified amount of credits directly from a customer wallet, with no
        feature mapping. Returns the optimistic balance.

        Args:
          amount: The amount of credits to consume

          currency_id: The credit currency to consume from (required)

          customer_id: The customer to consume credits from (required)

          idempotency_key: A unique key used to deduplicate the consumption (required)

          created_at: Optional timestamp the consumption is attributed to

          dimensions: Optional dimensions describing the consumption

          resource_id: Optional resource the consumption is attributed to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            "/api/v1/credits/consumption",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency_id": currency_id,
                    "customer_id": customer_id,
                    "idempotency_key": idempotency_key,
                    "created_at": created_at,
                    "dimensions": dimensions,
                    "resource_id": resource_id,
                },
                consumption_consume_params.ConsumptionConsumeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsumptionConsumeResponse,
        )

    async def consume_async(
        self,
        *,
        consumptions: Iterable[consumption_consume_async_params.Consumption],
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConsumptionConsumeAsyncResponse:
        """Consumes credits directly from customer wallets asynchronously.

        Consumptions are
        reconciled asynchronously into the credit balances.

        Args:
          consumptions: The credit consumptions to report (up to 1000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            "/api/v1/credits/consumption/async",
            body=await async_maybe_transform(
                {"consumptions": consumptions}, consumption_consume_async_params.ConsumptionConsumeAsyncParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsumptionConsumeAsyncResponse,
        )


class ConsumptionResourceWithRawResponse:
    def __init__(self, consumption: ConsumptionResource) -> None:
        self._consumption = consumption

        self.consume = to_raw_response_wrapper(
            consumption.consume,
        )
        self.consume_async = to_raw_response_wrapper(
            consumption.consume_async,
        )


class AsyncConsumptionResourceWithRawResponse:
    def __init__(self, consumption: AsyncConsumptionResource) -> None:
        self._consumption = consumption

        self.consume = async_to_raw_response_wrapper(
            consumption.consume,
        )
        self.consume_async = async_to_raw_response_wrapper(
            consumption.consume_async,
        )


class ConsumptionResourceWithStreamingResponse:
    def __init__(self, consumption: ConsumptionResource) -> None:
        self._consumption = consumption

        self.consume = to_streamed_response_wrapper(
            consumption.consume,
        )
        self.consume_async = to_streamed_response_wrapper(
            consumption.consume_async,
        )


class AsyncConsumptionResourceWithStreamingResponse:
    def __init__(self, consumption: AsyncConsumptionResource) -> None:
        self._consumption = consumption

        self.consume = async_to_streamed_response_wrapper(
            consumption.consume,
        )
        self.consume_async = async_to_streamed_response_wrapper(
            consumption.consume_async,
        )
