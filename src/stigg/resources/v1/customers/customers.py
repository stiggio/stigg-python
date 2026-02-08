# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import (
    customer_list_params,
    customer_import_params,
    customer_update_params,
    customer_provision_params,
    customer_list_resources_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from .payment_method import (
    PaymentMethodResource,
    AsyncPaymentMethodResource,
    PaymentMethodResourceWithRawResponse,
    AsyncPaymentMethodResourceWithRawResponse,
    PaymentMethodResourceWithStreamingResponse,
    AsyncPaymentMethodResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from .promotional_entitlements import (
    PromotionalEntitlementsResource,
    AsyncPromotionalEntitlementsResource,
    PromotionalEntitlementsResourceWithRawResponse,
    AsyncPromotionalEntitlementsResourceWithRawResponse,
    PromotionalEntitlementsResourceWithStreamingResponse,
    AsyncPromotionalEntitlementsResourceWithStreamingResponse,
)
from ....types.v1.customer_response import CustomerResponse
from ....types.v1.customer_list_response import CustomerListResponse
from ....types.v1.customer_import_response import CustomerImportResponse
from ....types.v1.customer_list_resources_response import CustomerListResourcesResponse

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def payment_method(self) -> PaymentMethodResource:
        return PaymentMethodResource(self._client)

    @cached_property
    def promotional_entitlements(self) -> PromotionalEntitlementsResource:
        return PromotionalEntitlementsResource(self._client)

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
        Retrieves a customer by their unique identifier, including billing information
        and subscription status.

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
        Updates an existing customer's properties such as name, email, and billing
        information.

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
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[CustomerListResponse]:
        """
        Retrieves a paginated list of customers in the environment.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/customers",
            page=SyncMyCursorIDPage[CustomerListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=CustomerListResponse,
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
        """Archives a customer, preventing new subscriptions.

        Optionally cancels existing
        subscriptions.

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

    def import_(
        self,
        *,
        customers: Iterable[customer_import_params.Customer],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerImportResponse:
        """Imports multiple customers in bulk.

        Used for migrating customer data from
        external systems.

        Args:
          customers: List of customer objects to import

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/customers/import",
            body=maybe_transform({"customers": customers}, customer_import_params.CustomerImportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerImportResponse,
        )

    def list_resources(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[CustomerListResourcesResponse]:
        """
        Get a list of customerresources

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/api/v1/customers/{id}/resources",
            page=SyncMyCursorIDPage[CustomerListResourcesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    customer_list_resources_params.CustomerListResourcesParams,
                ),
            ),
            model=CustomerListResourcesResponse,
        )

    def provision(
        self,
        *,
        id: str,
        coupon_id: Optional[str] | Omit = omit,
        default_payment_method: Optional[customer_provision_params.DefaultPaymentMethod] | Omit = omit,
        email: Optional[str] | Omit = omit,
        integrations: Iterable[customer_provision_params.Integration] | Omit = omit,
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
        Creates a new customer and optionally provisions an initial subscription in a
        single operation.

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
                customer_provision_params.CustomerProvisionParams,
            ),
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
        Restores an archived customer, allowing them to create new subscriptions again.

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
    def promotional_entitlements(self) -> AsyncPromotionalEntitlementsResource:
        return AsyncPromotionalEntitlementsResource(self._client)

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
        Retrieves a customer by their unique identifier, including billing information
        and subscription status.

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
        Updates an existing customer's properties such as name, email, and billing
        information.

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

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomerListResponse, AsyncMyCursorIDPage[CustomerListResponse]]:
        """
        Retrieves a paginated list of customers in the environment.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/customers",
            page=AsyncMyCursorIDPage[CustomerListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=CustomerListResponse,
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
        """Archives a customer, preventing new subscriptions.

        Optionally cancels existing
        subscriptions.

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

    async def import_(
        self,
        *,
        customers: Iterable[customer_import_params.Customer],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerImportResponse:
        """Imports multiple customers in bulk.

        Used for migrating customer data from
        external systems.

        Args:
          customers: List of customer objects to import

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/customers/import",
            body=await async_maybe_transform({"customers": customers}, customer_import_params.CustomerImportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerImportResponse,
        )

    def list_resources(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomerListResourcesResponse, AsyncMyCursorIDPage[CustomerListResourcesResponse]]:
        """
        Get a list of customerresources

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/api/v1/customers/{id}/resources",
            page=AsyncMyCursorIDPage[CustomerListResourcesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    customer_list_resources_params.CustomerListResourcesParams,
                ),
            ),
            model=CustomerListResourcesResponse,
        )

    async def provision(
        self,
        *,
        id: str,
        coupon_id: Optional[str] | Omit = omit,
        default_payment_method: Optional[customer_provision_params.DefaultPaymentMethod] | Omit = omit,
        email: Optional[str] | Omit = omit,
        integrations: Iterable[customer_provision_params.Integration] | Omit = omit,
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
        Creates a new customer and optionally provisions an initial subscription in a
        single operation.

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
                customer_provision_params.CustomerProvisionParams,
            ),
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
        Restores an archived customer, allowing them to create new subscriptions again.

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
        self.import_ = to_raw_response_wrapper(
            customers.import_,
        )
        self.list_resources = to_raw_response_wrapper(
            customers.list_resources,
        )
        self.provision = to_raw_response_wrapper(
            customers.provision,
        )
        self.unarchive = to_raw_response_wrapper(
            customers.unarchive,
        )

    @cached_property
    def payment_method(self) -> PaymentMethodResourceWithRawResponse:
        return PaymentMethodResourceWithRawResponse(self._customers.payment_method)

    @cached_property
    def promotional_entitlements(self) -> PromotionalEntitlementsResourceWithRawResponse:
        return PromotionalEntitlementsResourceWithRawResponse(self._customers.promotional_entitlements)


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

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
        self.import_ = async_to_raw_response_wrapper(
            customers.import_,
        )
        self.list_resources = async_to_raw_response_wrapper(
            customers.list_resources,
        )
        self.provision = async_to_raw_response_wrapper(
            customers.provision,
        )
        self.unarchive = async_to_raw_response_wrapper(
            customers.unarchive,
        )

    @cached_property
    def payment_method(self) -> AsyncPaymentMethodResourceWithRawResponse:
        return AsyncPaymentMethodResourceWithRawResponse(self._customers.payment_method)

    @cached_property
    def promotional_entitlements(self) -> AsyncPromotionalEntitlementsResourceWithRawResponse:
        return AsyncPromotionalEntitlementsResourceWithRawResponse(self._customers.promotional_entitlements)


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

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
        self.import_ = to_streamed_response_wrapper(
            customers.import_,
        )
        self.list_resources = to_streamed_response_wrapper(
            customers.list_resources,
        )
        self.provision = to_streamed_response_wrapper(
            customers.provision,
        )
        self.unarchive = to_streamed_response_wrapper(
            customers.unarchive,
        )

    @cached_property
    def payment_method(self) -> PaymentMethodResourceWithStreamingResponse:
        return PaymentMethodResourceWithStreamingResponse(self._customers.payment_method)

    @cached_property
    def promotional_entitlements(self) -> PromotionalEntitlementsResourceWithStreamingResponse:
        return PromotionalEntitlementsResourceWithStreamingResponse(self._customers.promotional_entitlements)


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

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
        self.import_ = async_to_streamed_response_wrapper(
            customers.import_,
        )
        self.list_resources = async_to_streamed_response_wrapper(
            customers.list_resources,
        )
        self.provision = async_to_streamed_response_wrapper(
            customers.provision,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            customers.unarchive,
        )

    @cached_property
    def payment_method(self) -> AsyncPaymentMethodResourceWithStreamingResponse:
        return AsyncPaymentMethodResourceWithStreamingResponse(self._customers.payment_method)

    @cached_property
    def promotional_entitlements(self) -> AsyncPromotionalEntitlementsResourceWithStreamingResponse:
        return AsyncPromotionalEntitlementsResourceWithStreamingResponse(self._customers.promotional_entitlements)
