# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

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
from .....types.v1.events.credits import grant_list_params, grant_create_params
from .....types.v1.events.credits.grant_list_response import GrantListResponse
from .....types.v1.events.credits.credit_grant_response import CreditGrantResponse

__all__ = ["GrantsResource", "AsyncGrantsResource"]


class GrantsResource(SyncAPIResource):
    """Operations related to credit grants"""

    @cached_property
    def with_raw_response(self) -> GrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return GrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return GrantsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: float,
        currency_id: str,
        customer_id: str,
        display_name: str,
        grant_type: Literal["PAID", "PROMOTIONAL", "RECURRING"],
        await_payment_confirmation: bool | Omit = omit,
        billing_information: grant_create_params.BillingInformation | Omit = omit,
        comment: str | Omit = omit,
        cost: grant_create_params.Cost | Omit = omit,
        effective_at: Union[str, datetime] | Omit = omit,
        expire_at: Union[str, datetime] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        payment_collection_method: Literal["CHARGE", "INVOICE", "NONE"] | Omit = omit,
        priority: int | Omit = omit,
        resource_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditGrantResponse:
        """
        Creates a new credit grant for a customer with specified amount, type, and
        optional billing configuration.

        Args:
          amount: The credit amount to grant

          currency_id: The credit currency ID (required)

          customer_id: The customer ID to grant credits to (required)

          display_name: The display name for the credit grant

          grant_type: The type of credit grant (PAID, PROMOTIONAL, RECURRING)

          await_payment_confirmation: Whether to wait for payment confirmation before returning (default: true)

          billing_information: Billing information for the credit grant

          comment: An optional comment on the credit grant

          cost: The monetary cost of the credit grant

          effective_at: The date when the credit grant becomes effective

          expire_at: The date when the credit grant expires

          metadata: Additional metadata for the credit grant

          payment_collection_method: The payment collection method (CHARGE, INVOICE, NONE)

          priority: The priority of the credit grant (lower number = higher priority)

          resource_id: The resource ID to scope the grant to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/credits/grants",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency_id": currency_id,
                    "customer_id": customer_id,
                    "display_name": display_name,
                    "grant_type": grant_type,
                    "await_payment_confirmation": await_payment_confirmation,
                    "billing_information": billing_information,
                    "comment": comment,
                    "cost": cost,
                    "effective_at": effective_at,
                    "expire_at": expire_at,
                    "metadata": metadata,
                    "payment_collection_method": payment_collection_method,
                    "priority": priority,
                    "resource_id": resource_id,
                },
                grant_create_params.GrantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditGrantResponse,
        )

    def list(
        self,
        *,
        customer_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: grant_list_params.CreatedAt | Omit = omit,
        currency_id: str | Omit = omit,
        limit: int | Omit = omit,
        resource_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[GrantListResponse]:
        """
        Retrieves a paginated list of credit grants for a customer.

        Args:
          customer_id: Filter by customer ID (required)

          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          currency_id: Filter by currency ID

          limit: Maximum number of items to return

          resource_id: Filter by resource ID. When omitted, only grants without a resource are returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/credits/grants",
            page=SyncMyCursorIDPage[GrantListResponse],
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
                        "created_at": created_at,
                        "currency_id": currency_id,
                        "limit": limit,
                        "resource_id": resource_id,
                    },
                    grant_list_params.GrantListParams,
                ),
            ),
            model=GrantListResponse,
        )

    def void(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditGrantResponse:
        """
        Voids an existing credit grant, preventing further consumption of the remaining
        credits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/credits/grants/{id}/void",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditGrantResponse,
        )


class AsyncGrantsResource(AsyncAPIResource):
    """Operations related to credit grants"""

    @cached_property
    def with_raw_response(self) -> AsyncGrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncGrantsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: float,
        currency_id: str,
        customer_id: str,
        display_name: str,
        grant_type: Literal["PAID", "PROMOTIONAL", "RECURRING"],
        await_payment_confirmation: bool | Omit = omit,
        billing_information: grant_create_params.BillingInformation | Omit = omit,
        comment: str | Omit = omit,
        cost: grant_create_params.Cost | Omit = omit,
        effective_at: Union[str, datetime] | Omit = omit,
        expire_at: Union[str, datetime] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        payment_collection_method: Literal["CHARGE", "INVOICE", "NONE"] | Omit = omit,
        priority: int | Omit = omit,
        resource_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditGrantResponse:
        """
        Creates a new credit grant for a customer with specified amount, type, and
        optional billing configuration.

        Args:
          amount: The credit amount to grant

          currency_id: The credit currency ID (required)

          customer_id: The customer ID to grant credits to (required)

          display_name: The display name for the credit grant

          grant_type: The type of credit grant (PAID, PROMOTIONAL, RECURRING)

          await_payment_confirmation: Whether to wait for payment confirmation before returning (default: true)

          billing_information: Billing information for the credit grant

          comment: An optional comment on the credit grant

          cost: The monetary cost of the credit grant

          effective_at: The date when the credit grant becomes effective

          expire_at: The date when the credit grant expires

          metadata: Additional metadata for the credit grant

          payment_collection_method: The payment collection method (CHARGE, INVOICE, NONE)

          priority: The priority of the credit grant (lower number = higher priority)

          resource_id: The resource ID to scope the grant to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/credits/grants",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency_id": currency_id,
                    "customer_id": customer_id,
                    "display_name": display_name,
                    "grant_type": grant_type,
                    "await_payment_confirmation": await_payment_confirmation,
                    "billing_information": billing_information,
                    "comment": comment,
                    "cost": cost,
                    "effective_at": effective_at,
                    "expire_at": expire_at,
                    "metadata": metadata,
                    "payment_collection_method": payment_collection_method,
                    "priority": priority,
                    "resource_id": resource_id,
                },
                grant_create_params.GrantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditGrantResponse,
        )

    def list(
        self,
        *,
        customer_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: grant_list_params.CreatedAt | Omit = omit,
        currency_id: str | Omit = omit,
        limit: int | Omit = omit,
        resource_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[GrantListResponse, AsyncMyCursorIDPage[GrantListResponse]]:
        """
        Retrieves a paginated list of credit grants for a customer.

        Args:
          customer_id: Filter by customer ID (required)

          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          currency_id: Filter by currency ID

          limit: Maximum number of items to return

          resource_id: Filter by resource ID. When omitted, only grants without a resource are returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/credits/grants",
            page=AsyncMyCursorIDPage[GrantListResponse],
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
                        "created_at": created_at,
                        "currency_id": currency_id,
                        "limit": limit,
                        "resource_id": resource_id,
                    },
                    grant_list_params.GrantListParams,
                ),
            ),
            model=GrantListResponse,
        )

    async def void(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditGrantResponse:
        """
        Voids an existing credit grant, preventing further consumption of the remaining
        credits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/credits/grants/{id}/void",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditGrantResponse,
        )


class GrantsResourceWithRawResponse:
    def __init__(self, grants: GrantsResource) -> None:
        self._grants = grants

        self.create = to_raw_response_wrapper(
            grants.create,
        )
        self.list = to_raw_response_wrapper(
            grants.list,
        )
        self.void = to_raw_response_wrapper(
            grants.void,
        )


class AsyncGrantsResourceWithRawResponse:
    def __init__(self, grants: AsyncGrantsResource) -> None:
        self._grants = grants

        self.create = async_to_raw_response_wrapper(
            grants.create,
        )
        self.list = async_to_raw_response_wrapper(
            grants.list,
        )
        self.void = async_to_raw_response_wrapper(
            grants.void,
        )


class GrantsResourceWithStreamingResponse:
    def __init__(self, grants: GrantsResource) -> None:
        self._grants = grants

        self.create = to_streamed_response_wrapper(
            grants.create,
        )
        self.list = to_streamed_response_wrapper(
            grants.list,
        )
        self.void = to_streamed_response_wrapper(
            grants.void,
        )


class AsyncGrantsResourceWithStreamingResponse:
    def __init__(self, grants: AsyncGrantsResource) -> None:
        self._grants = grants

        self.create = async_to_streamed_response_wrapper(
            grants.create,
        )
        self.list = async_to_streamed_response_wrapper(
            grants.list,
        )
        self.void = async_to_streamed_response_wrapper(
            grants.void,
        )
