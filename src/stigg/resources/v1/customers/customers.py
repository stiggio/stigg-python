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
from .sub_customer import (
    SubCustomerResource,
    AsyncSubCustomerResource,
    SubCustomerResourceWithRawResponse,
    AsyncSubCustomerResourceWithRawResponse,
    SubCustomerResourceWithStreamingResponse,
    AsyncSubCustomerResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.v1.customer_retrieve_response import CustomerRetrieveResponse

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def sub_customer(self) -> SubCustomerResource:
        return SubCustomerResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#accessing-raw-response-data-eg-headers
        """
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#with_streaming_response
        """
        return CustomersResourceWithStreamingResponse(self)

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
    ) -> CustomerRetrieveResponse:
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
            cast_to=CustomerRetrieveResponse,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def sub_customer(self) -> AsyncSubCustomerResource:
        return AsyncSubCustomerResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#with_streaming_response
        """
        return AsyncCustomersResourceWithStreamingResponse(self)

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
    ) -> CustomerRetrieveResponse:
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
            cast_to=CustomerRetrieveResponse,
        )


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.retrieve = to_raw_response_wrapper(
            customers.retrieve,
        )

    @cached_property
    def sub_customer(self) -> SubCustomerResourceWithRawResponse:
        return SubCustomerResourceWithRawResponse(self._customers.sub_customer)


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.retrieve = async_to_raw_response_wrapper(
            customers.retrieve,
        )

    @cached_property
    def sub_customer(self) -> AsyncSubCustomerResourceWithRawResponse:
        return AsyncSubCustomerResourceWithRawResponse(self._customers.sub_customer)


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.retrieve = to_streamed_response_wrapper(
            customers.retrieve,
        )

    @cached_property
    def sub_customer(self) -> SubCustomerResourceWithStreamingResponse:
        return SubCustomerResourceWithStreamingResponse(self._customers.sub_customer)


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.retrieve = async_to_streamed_response_wrapper(
            customers.retrieve,
        )

    @cached_property
    def sub_customer(self) -> AsyncSubCustomerResourceWithStreamingResponse:
        return AsyncSubCustomerResourceWithStreamingResponse(self._customers.sub_customer)
