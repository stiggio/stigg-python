# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from .usage import (
    UsageResource,
    AsyncUsageResource,
    UsageResourceWithRawResponse,
    AsyncUsageResourceWithRawResponse,
    UsageResourceWithStreamingResponse,
    AsyncUsageResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import customer_list_params, customer_create_params, customer_update_params
from .promotional import (
    PromotionalResource,
    AsyncPromotionalResource,
    PromotionalResourceWithRawResponse,
    AsyncPromotionalResourceWithRawResponse,
    PromotionalResourceWithStreamingResponse,
    AsyncPromotionalResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .payment_method import (
    PaymentMethodResource,
    AsyncPaymentMethodResource,
    PaymentMethodResourceWithRawResponse,
    AsyncPaymentMethodResourceWithRawResponse,
    PaymentMethodResourceWithStreamingResponse,
    AsyncPaymentMethodResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.v1.customer_response import CustomerResponse
from ....types.v1.customer_list_response import CustomerListResponse

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def payment_method(self) -> PaymentMethodResource:
        return PaymentMethodResource(self._client)

    @cached_property
    def usage(self) -> UsageResource:
        return UsageResource(self._client)

    @cached_property
    def promotional(self) -> PromotionalResource:
        return PromotionalResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return CustomersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        coupon_id: Optional[str] | Omit = omit,
        default_payment_method: Optional[customer_create_params.DefaultPaymentMethod] | Omit = omit,
        email: Optional[str] | Omit = omit,
        integrations: Iterable[customer_create_params.Integration] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Create a new Customer

        Args:
          id: Customer slug

          coupon_id: Customer level coupon

          default_payment_method: The default payment method details

          email: The email of the customer

          integrations: List of integrations

          metadata: Additional metadata

          name: The name of the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/customers",
            body=maybe_transform(
                {
                    "id": id,
                    "coupon_id": coupon_id,
                    "default_payment_method": default_payment_method,
                    "email": email,
                    "integrations": integrations,
                    "metadata": metadata,
                    "name": name,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Get a single Customer by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/customers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    def update(
        self,
        id: str,
        *,
        coupon_id: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        integrations: Iterable[customer_update_params.Integration] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Update an existing Customer

        Args:
          coupon_id: Customer level coupon

          email: The email of the customer

          integrations: List of integrations

          metadata: Additional metadata

          name: The name of the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/v1/customers/{id}",
            body=maybe_transform(
                {
                    "coupon_id": coupon_id,
                    "email": email,
                    "integrations": integrations,
                    "metadata": metadata,
                    "name": name,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    def list(
        self,
        *,
        ending_before: str | Omit = omit,
        limit: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerListResponse:
        """
        Get a list of Customers

        Args:
          ending_before: Ending before this UUID for pagination

          limit: Items per page

          starting_after: Starting after this UUID for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/customers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            cast_to=CustomerListResponse,
        )

    def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Perform archive on a Customer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/customers/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    def unarchive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Perform unarchive on a Customer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/customers/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def payment_method(self) -> AsyncPaymentMethodResource:
        return AsyncPaymentMethodResource(self._client)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        return AsyncUsageResource(self._client)

    @cached_property
    def promotional(self) -> AsyncPromotionalResource:
        return AsyncPromotionalResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncCustomersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        coupon_id: Optional[str] | Omit = omit,
        default_payment_method: Optional[customer_create_params.DefaultPaymentMethod] | Omit = omit,
        email: Optional[str] | Omit = omit,
        integrations: Iterable[customer_create_params.Integration] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Create a new Customer

        Args:
          id: Customer slug

          coupon_id: Customer level coupon

          default_payment_method: The default payment method details

          email: The email of the customer

          integrations: List of integrations

          metadata: Additional metadata

          name: The name of the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/customers",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "coupon_id": coupon_id,
                    "default_payment_method": default_payment_method,
                    "email": email,
                    "integrations": integrations,
                    "metadata": metadata,
                    "name": name,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Get a single Customer by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/customers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    async def update(
        self,
        id: str,
        *,
        coupon_id: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        integrations: Iterable[customer_update_params.Integration] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Update an existing Customer

        Args:
          coupon_id: Customer level coupon

          email: The email of the customer

          integrations: List of integrations

          metadata: Additional metadata

          name: The name of the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/v1/customers/{id}",
            body=await async_maybe_transform(
                {
                    "coupon_id": coupon_id,
                    "email": email,
                    "integrations": integrations,
                    "metadata": metadata,
                    "name": name,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    async def list(
        self,
        *,
        ending_before: str | Omit = omit,
        limit: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerListResponse:
        """
        Get a list of Customers

        Args:
          ending_before: Ending before this UUID for pagination

          limit: Items per page

          starting_after: Starting after this UUID for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/customers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ending_before": ending_before,
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            cast_to=CustomerListResponse,
        )

    async def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Perform archive on a Customer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/customers/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    async def unarchive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Perform unarchive on a Customer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/customers/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            customers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            customers.update,
        )
        self.list = to_raw_response_wrapper(
            customers.list,
        )
        self.archive = to_raw_response_wrapper(
            customers.archive,
        )
        self.unarchive = to_raw_response_wrapper(
            customers.unarchive,
        )

    @cached_property
    def payment_method(self) -> PaymentMethodResourceWithRawResponse:
        return PaymentMethodResourceWithRawResponse(self._customers.payment_method)

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
        return UsageResourceWithRawResponse(self._customers.usage)

    @cached_property
    def promotional(self) -> PromotionalResourceWithRawResponse:
        return PromotionalResourceWithRawResponse(self._customers.promotional)


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            customers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            customers.update,
        )
        self.list = async_to_raw_response_wrapper(
            customers.list,
        )
        self.archive = async_to_raw_response_wrapper(
            customers.archive,
        )
        self.unarchive = async_to_raw_response_wrapper(
            customers.unarchive,
        )

    @cached_property
    def payment_method(self) -> AsyncPaymentMethodResourceWithRawResponse:
        return AsyncPaymentMethodResourceWithRawResponse(self._customers.payment_method)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        return AsyncUsageResourceWithRawResponse(self._customers.usage)

    @cached_property
    def promotional(self) -> AsyncPromotionalResourceWithRawResponse:
        return AsyncPromotionalResourceWithRawResponse(self._customers.promotional)


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            customers.update,
        )
        self.list = to_streamed_response_wrapper(
            customers.list,
        )
        self.archive = to_streamed_response_wrapper(
            customers.archive,
        )
        self.unarchive = to_streamed_response_wrapper(
            customers.unarchive,
        )

    @cached_property
    def payment_method(self) -> PaymentMethodResourceWithStreamingResponse:
        return PaymentMethodResourceWithStreamingResponse(self._customers.payment_method)

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        return UsageResourceWithStreamingResponse(self._customers.usage)

    @cached_property
    def promotional(self) -> PromotionalResourceWithStreamingResponse:
        return PromotionalResourceWithStreamingResponse(self._customers.promotional)


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            customers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            customers.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            customers.archive,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            customers.unarchive,
        )

    @cached_property
    def payment_method(self) -> AsyncPaymentMethodResourceWithStreamingResponse:
        return AsyncPaymentMethodResourceWithStreamingResponse(self._customers.payment_method)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        return AsyncUsageResourceWithStreamingResponse(self._customers.usage)

    @cached_property
    def promotional(self) -> AsyncPromotionalResourceWithStreamingResponse:
        return AsyncPromotionalResourceWithStreamingResponse(self._customers.promotional)
