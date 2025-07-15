# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v2.customers.sub_customer_retrieve_response import SubCustomerRetrieveResponse

__all__ = ["SubCustomerResource", "AsyncSubCustomerResource"]


class SubCustomerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubCustomerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#accessing-raw-response-data-eg-headers
        """
        return SubCustomerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubCustomerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#with_streaming_response
        """
        return SubCustomerResourceWithStreamingResponse(self)

    def retrieve(
        self,
        ref_id: str,
        *,
        x_api_key: str,
        x_environment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubCustomerRetrieveResponse:
        """
        Get a single customer by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ref_id:
            raise ValueError(f"Expected a non-empty value for `ref_id` but received {ref_id!r}")
        extra_headers = {"X-API-KEY": x_api_key, "X-ENVIRONMENT-ID": x_environment_id, **(extra_headers or {})}
        return self._get(
            f"/api/v1/customers/{ref_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubCustomerRetrieveResponse,
        )


class AsyncSubCustomerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubCustomerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubCustomerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubCustomerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#with_streaming_response
        """
        return AsyncSubCustomerResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        ref_id: str,
        *,
        x_api_key: str,
        x_environment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubCustomerRetrieveResponse:
        """
        Get a single customer by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ref_id:
            raise ValueError(f"Expected a non-empty value for `ref_id` but received {ref_id!r}")
        extra_headers = {"X-API-KEY": x_api_key, "X-ENVIRONMENT-ID": x_environment_id, **(extra_headers or {})}
        return await self._get(
            f"/api/v1/customers/{ref_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubCustomerRetrieveResponse,
        )


class SubCustomerResourceWithRawResponse:
    def __init__(self, sub_customer: SubCustomerResource) -> None:
        self._sub_customer = sub_customer

        self.retrieve = to_raw_response_wrapper(
            sub_customer.retrieve,
        )


class AsyncSubCustomerResourceWithRawResponse:
    def __init__(self, sub_customer: AsyncSubCustomerResource) -> None:
        self._sub_customer = sub_customer

        self.retrieve = async_to_raw_response_wrapper(
            sub_customer.retrieve,
        )


class SubCustomerResourceWithStreamingResponse:
    def __init__(self, sub_customer: SubCustomerResource) -> None:
        self._sub_customer = sub_customer

        self.retrieve = to_streamed_response_wrapper(
            sub_customer.retrieve,
        )


class AsyncSubCustomerResourceWithStreamingResponse:
    def __init__(self, sub_customer: AsyncSubCustomerResource) -> None:
        self._sub_customer = sub_customer

        self.retrieve = async_to_streamed_response_wrapper(
            sub_customer.retrieve,
        )
