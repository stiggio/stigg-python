# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import usage_report_params, usage_history_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.usage_report_response import UsageReportResponse
from ...types.v1.usage_history_response import UsageHistoryResponse

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return UsageResourceWithStreamingResponse(self)

    def history(
        self,
        feature_id: str,
        *,
        customer_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        group_by: str | Omit = omit,
        resource_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageHistoryResponse:
        """
        Retrieves historical usage data for a customer's metered feature over time.

        Args:
          start_date: The start date of the range

          end_date: The end date of the range

          resource_id: Resource id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not feature_id:
            raise ValueError(f"Expected a non-empty value for `feature_id` but received {feature_id!r}")
        return self._get(
            f"/api/v1/usage/{customer_id}/history/{feature_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_date": start_date,
                        "end_date": end_date,
                        "group_by": group_by,
                        "resource_id": resource_id,
                    },
                    usage_history_params.UsageHistoryParams,
                ),
            ),
            cast_to=UsageHistoryResponse,
        )

    def report(
        self,
        *,
        usages: Iterable[usage_report_params.Usage],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageReportResponse:
        """Reports usage measurements for metered features.

        The reported usage is used to
        track, limit, and bill customer consumption.

        Args:
          usages: A list of usage reports to be submitted in bulk

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/usage",
            body=maybe_transform({"usages": usages}, usage_report_params.UsageReportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageReportResponse,
        )


class AsyncUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncUsageResourceWithStreamingResponse(self)

    async def history(
        self,
        feature_id: str,
        *,
        customer_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        group_by: str | Omit = omit,
        resource_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageHistoryResponse:
        """
        Retrieves historical usage data for a customer's metered feature over time.

        Args:
          start_date: The start date of the range

          end_date: The end date of the range

          resource_id: Resource id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not feature_id:
            raise ValueError(f"Expected a non-empty value for `feature_id` but received {feature_id!r}")
        return await self._get(
            f"/api/v1/usage/{customer_id}/history/{feature_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_date": start_date,
                        "end_date": end_date,
                        "group_by": group_by,
                        "resource_id": resource_id,
                    },
                    usage_history_params.UsageHistoryParams,
                ),
            ),
            cast_to=UsageHistoryResponse,
        )

    async def report(
        self,
        *,
        usages: Iterable[usage_report_params.Usage],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageReportResponse:
        """Reports usage measurements for metered features.

        The reported usage is used to
        track, limit, and bill customer consumption.

        Args:
          usages: A list of usage reports to be submitted in bulk

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/usage",
            body=await async_maybe_transform({"usages": usages}, usage_report_params.UsageReportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageReportResponse,
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.history = to_raw_response_wrapper(
            usage.history,
        )
        self.report = to_raw_response_wrapper(
            usage.report,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.history = async_to_raw_response_wrapper(
            usage.history,
        )
        self.report = async_to_raw_response_wrapper(
            usage.report,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.history = to_streamed_response_wrapper(
            usage.history,
        )
        self.report = to_streamed_response_wrapper(
            usage.report,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.history = async_to_streamed_response_wrapper(
            usage.history,
        )
        self.report = async_to_streamed_response_wrapper(
            usage.report,
        )
