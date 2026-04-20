# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .grants import (
    GrantsResource,
    AsyncGrantsResource,
    GrantsResourceWithRawResponse,
    AsyncGrantsResourceWithRawResponse,
    GrantsResourceWithStreamingResponse,
    AsyncGrantsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.v1.events import credit_get_usage_params, credit_list_ledger_params, credit_get_auto_recharge_params
from .....types.v1.events.credit_get_usage_response import CreditGetUsageResponse
from .....types.v1.events.credit_list_ledger_response import CreditListLedgerResponse
from .....types.v1.events.credit_get_auto_recharge_response import CreditGetAutoRechargeResponse

__all__ = ["CreditsResource", "AsyncCreditsResource"]


class CreditsResource(SyncAPIResource):
    @cached_property
    def grants(self) -> GrantsResource:
        """Operations related to credit grants"""
        return GrantsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return CreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return CreditsResourceWithStreamingResponse(self)

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
    ) -> CreditGetAutoRechargeResponse:
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
                    credit_get_auto_recharge_params.CreditGetAutoRechargeParams,
                ),
            ),
            cast_to=CreditGetAutoRechargeResponse,
        )

    def get_usage(
        self,
        *,
        customer_id: str,
        currency_id: str | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        resource_id: str | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        time_range: Literal["LAST_DAY", "LAST_WEEK", "LAST_MONTH", "LAST_YEAR"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditGetUsageResponse:
        """
        Retrieves credit usage time-series data for a customer, grouped by feature, over
        a specified time range.

        Args:
          customer_id: Filter by customer ID (required)

          currency_id: Filter by currency ID

          end_date: End date for the credit usage time range (ISO 8601). Defaults to now when
              startDate is provided

          resource_id: Filter by resource ID

          start_date: Start date for the credit usage time range (ISO 8601). Takes precedence over
              timeRange when provided

          time_range: Time range for usage data (LAST_DAY, LAST_WEEK, LAST_MONTH, LAST_YEAR). Defaults
              to LAST_MONTH

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/credits/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_id": customer_id,
                        "currency_id": currency_id,
                        "end_date": end_date,
                        "resource_id": resource_id,
                        "start_date": start_date,
                        "time_range": time_range,
                    },
                    credit_get_usage_params.CreditGetUsageParams,
                ),
            ),
            cast_to=CreditGetUsageResponse,
        )

    def list_ledger(
        self,
        *,
        customer_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        currency_id: str | Omit = omit,
        limit: int | Omit = omit,
        resource_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[CreditListLedgerResponse]:
        """
        Retrieves a paginated list of credit ledger events for a customer.

        Args:
          customer_id: Filter by customer ID (required)

          after: Return items that come after this cursor

          before: Return items that come before this cursor

          currency_id: Filter by currency ID

          limit: Maximum number of items to return

          resource_id: Filter by resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/credits/ledger",
            page=SyncMyCursorIDPage[CreditListLedgerResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_id": customer_id,
                        "after": after,
                        "before": before,
                        "currency_id": currency_id,
                        "limit": limit,
                        "resource_id": resource_id,
                    },
                    credit_list_ledger_params.CreditListLedgerParams,
                ),
            ),
            model=CreditListLedgerResponse,
        )


class AsyncCreditsResource(AsyncAPIResource):
    @cached_property
    def grants(self) -> AsyncGrantsResource:
        """Operations related to credit grants"""
        return AsyncGrantsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncCreditsResourceWithStreamingResponse(self)

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
    ) -> CreditGetAutoRechargeResponse:
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
                    credit_get_auto_recharge_params.CreditGetAutoRechargeParams,
                ),
            ),
            cast_to=CreditGetAutoRechargeResponse,
        )

    async def get_usage(
        self,
        *,
        customer_id: str,
        currency_id: str | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        resource_id: str | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        time_range: Literal["LAST_DAY", "LAST_WEEK", "LAST_MONTH", "LAST_YEAR"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditGetUsageResponse:
        """
        Retrieves credit usage time-series data for a customer, grouped by feature, over
        a specified time range.

        Args:
          customer_id: Filter by customer ID (required)

          currency_id: Filter by currency ID

          end_date: End date for the credit usage time range (ISO 8601). Defaults to now when
              startDate is provided

          resource_id: Filter by resource ID

          start_date: Start date for the credit usage time range (ISO 8601). Takes precedence over
              timeRange when provided

          time_range: Time range for usage data (LAST_DAY, LAST_WEEK, LAST_MONTH, LAST_YEAR). Defaults
              to LAST_MONTH

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/credits/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "customer_id": customer_id,
                        "currency_id": currency_id,
                        "end_date": end_date,
                        "resource_id": resource_id,
                        "start_date": start_date,
                        "time_range": time_range,
                    },
                    credit_get_usage_params.CreditGetUsageParams,
                ),
            ),
            cast_to=CreditGetUsageResponse,
        )

    def list_ledger(
        self,
        *,
        customer_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        currency_id: str | Omit = omit,
        limit: int | Omit = omit,
        resource_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CreditListLedgerResponse, AsyncMyCursorIDPage[CreditListLedgerResponse]]:
        """
        Retrieves a paginated list of credit ledger events for a customer.

        Args:
          customer_id: Filter by customer ID (required)

          after: Return items that come after this cursor

          before: Return items that come before this cursor

          currency_id: Filter by currency ID

          limit: Maximum number of items to return

          resource_id: Filter by resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/credits/ledger",
            page=AsyncMyCursorIDPage[CreditListLedgerResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_id": customer_id,
                        "after": after,
                        "before": before,
                        "currency_id": currency_id,
                        "limit": limit,
                        "resource_id": resource_id,
                    },
                    credit_list_ledger_params.CreditListLedgerParams,
                ),
            ),
            model=CreditListLedgerResponse,
        )


class CreditsResourceWithRawResponse:
    def __init__(self, credits: CreditsResource) -> None:
        self._credits = credits

        self.get_auto_recharge = to_raw_response_wrapper(
            credits.get_auto_recharge,
        )
        self.get_usage = to_raw_response_wrapper(
            credits.get_usage,
        )
        self.list_ledger = to_raw_response_wrapper(
            credits.list_ledger,
        )

    @cached_property
    def grants(self) -> GrantsResourceWithRawResponse:
        """Operations related to credit grants"""
        return GrantsResourceWithRawResponse(self._credits.grants)


class AsyncCreditsResourceWithRawResponse:
    def __init__(self, credits: AsyncCreditsResource) -> None:
        self._credits = credits

        self.get_auto_recharge = async_to_raw_response_wrapper(
            credits.get_auto_recharge,
        )
        self.get_usage = async_to_raw_response_wrapper(
            credits.get_usage,
        )
        self.list_ledger = async_to_raw_response_wrapper(
            credits.list_ledger,
        )

    @cached_property
    def grants(self) -> AsyncGrantsResourceWithRawResponse:
        """Operations related to credit grants"""
        return AsyncGrantsResourceWithRawResponse(self._credits.grants)


class CreditsResourceWithStreamingResponse:
    def __init__(self, credits: CreditsResource) -> None:
        self._credits = credits

        self.get_auto_recharge = to_streamed_response_wrapper(
            credits.get_auto_recharge,
        )
        self.get_usage = to_streamed_response_wrapper(
            credits.get_usage,
        )
        self.list_ledger = to_streamed_response_wrapper(
            credits.list_ledger,
        )

    @cached_property
    def grants(self) -> GrantsResourceWithStreamingResponse:
        """Operations related to credit grants"""
        return GrantsResourceWithStreamingResponse(self._credits.grants)


class AsyncCreditsResourceWithStreamingResponse:
    def __init__(self, credits: AsyncCreditsResource) -> None:
        self._credits = credits

        self.get_auto_recharge = async_to_streamed_response_wrapper(
            credits.get_auto_recharge,
        )
        self.get_usage = async_to_streamed_response_wrapper(
            credits.get_usage,
        )
        self.list_ledger = async_to_streamed_response_wrapper(
            credits.list_ledger,
        )

    @cached_property
    def grants(self) -> AsyncGrantsResourceWithStreamingResponse:
        """Operations related to credit grants"""
        return AsyncGrantsResourceWithStreamingResponse(self._credits.grants)
