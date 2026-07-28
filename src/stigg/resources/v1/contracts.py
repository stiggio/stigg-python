# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import contract_list_params, contract_create_params, contract_update_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.v1.contract_list_response import ContractListResponse
from ...types.v1.contract_create_response import ContractCreateResponse
from ...types.v1.contract_delete_response import ContractDeleteResponse
from ...types.v1.contract_update_response import ContractUpdateResponse
from ...types.v1.contract_retrieve_response import ContractRetrieveResponse

__all__ = ["ContractsResource", "AsyncContractsResource"]


class ContractsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return ContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return ContractsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_id: str,
        subscriptions: Iterable[contract_create_params.Subscription],
        activation_end_date: Union[str, datetime] | Omit = omit,
        activation_start_date: Union[str, datetime] | Omit = omit,
        name: Optional[str] | Omit = omit,
        po_number: Optional[str] | Omit = omit,
        setup_billing: bool | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractCreateResponse:
        """
        Creates a contract for a customer together with all of its (custom)
        subscriptions in a single atomic operation. Every new subscription is created
        inside one transaction — any validation or creation failure rolls the whole
        contract back. Each subscription entry is either a new subscription to create or
        a reference to an existing custom subscription. Returns the created contract.

        Args:
          customer_id: The customer ref ID the contract belongs to

          subscriptions: The subscriptions to attach to the contract (must be non-empty). Each entry is
              either a new subscription to create or a reference to an existing custom
              subscription.

          activation_end_date: Optional contract activation end date

          activation_start_date: Optional contract activation start date

          name: Optional contract name

          po_number: Optional purchase-order number

          setup_billing: Whether to set up billing for the contract by creating a billing contract in the
              connected billing provider. When false, the contract only provisions access
              (grants entitlements) and no billing contract is created. Defaults to true.

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
            "/api/v1/contracts",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "subscriptions": subscriptions,
                    "activation_end_date": activation_end_date,
                    "activation_start_date": activation_start_date,
                    "name": name,
                    "po_number": po_number,
                    "setup_billing": setup_billing,
                },
                contract_create_params.ContractCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveResponse:
        """
        Retrieves a single contract by its ID, enriched with a preview of its upcoming
        (next) invoice when one is available. Returns 404 when no contract with that ID
        exists in the environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-ACCOUNT-ID": x_account_id,
                    "X-ENVIRONMENT-ID": x_environment_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/api/v1/contracts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        activation_end_date: Union[str, datetime] | Omit = omit,
        activation_start_date: Union[str, datetime] | Omit = omit,
        name: Optional[str] | Omit = omit,
        po_number: Optional[str] | Omit = omit,
        setup_billing: bool | Omit = omit,
        subscription_ids: SequenceNotStr[str] | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractUpdateResponse:
        """
        Updates a contract's metadata (name, PO number, activation dates) and optionally
        re-links its subscriptions. Best-effort re-syncs the change to the connected
        billing provider.

        Args:
          activation_end_date: New activation end date

          activation_start_date: New activation start date

          name: New contract name

          po_number: New purchase-order number

          setup_billing: Enable billing on a provision-access-only contract by creating a billing
              contract in the connected billing provider. Only takes effect when true and the
              contract has no billing yet; omitting it leaves billing unchanged. Billing is
              never removed by an update.

          subscription_ids: When provided, replaces the set of subscriptions linked to the contract
              (subscription ref IDs)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-ACCOUNT-ID": x_account_id,
                    "X-ENVIRONMENT-ID": x_environment_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/api/v1/contracts/{id}", id=id),
            body=maybe_transform(
                {
                    "activation_end_date": activation_end_date,
                    "activation_start_date": activation_start_date,
                    "name": name,
                    "po_number": po_number,
                    "setup_billing": setup_billing,
                    "subscription_ids": subscription_ids,
                },
                contract_update_params.ContractUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        customer_external_id: str | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        state: str | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[ContractListResponse]:
        """
        Retrieves a cursor-paginated list of contracts in the environment, fetched live
        from the connected billing provider. Each contract is enriched with a preview of
        its upcoming (next) invoice when one is available. Returns an empty list when no
        billing provider is connected. Supports filtering by customer external ID,
        state, and name.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          customer_external_id: Filter by the exact external ID of the customer the contract belongs to

          limit: Maximum number of items to return

          name: Filter by exact contract name

          state: Filter by contract state. Supports comma-separated values for multiple states

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
        return self._get_api_list(
            "/api/v1/contracts",
            page=SyncMyCursorIDPage[ContractListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "customer_external_id": customer_external_id,
                        "limit": limit,
                        "name": name,
                        "state": state,
                    },
                    contract_list_params.ContractListParams,
                ),
            ),
            model=ContractListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractDeleteResponse:
        """
        Deletes a contract: cancels the contract in the connected billing provider and
        cancels every subscription linked to it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
            path_template("/api/v1/contracts/{id}/archive", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractDeleteResponse,
        )


class AsyncContractsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncContractsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_id: str,
        subscriptions: Iterable[contract_create_params.Subscription],
        activation_end_date: Union[str, datetime] | Omit = omit,
        activation_start_date: Union[str, datetime] | Omit = omit,
        name: Optional[str] | Omit = omit,
        po_number: Optional[str] | Omit = omit,
        setup_billing: bool | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractCreateResponse:
        """
        Creates a contract for a customer together with all of its (custom)
        subscriptions in a single atomic operation. Every new subscription is created
        inside one transaction — any validation or creation failure rolls the whole
        contract back. Each subscription entry is either a new subscription to create or
        a reference to an existing custom subscription. Returns the created contract.

        Args:
          customer_id: The customer ref ID the contract belongs to

          subscriptions: The subscriptions to attach to the contract (must be non-empty). Each entry is
              either a new subscription to create or a reference to an existing custom
              subscription.

          activation_end_date: Optional contract activation end date

          activation_start_date: Optional contract activation start date

          name: Optional contract name

          po_number: Optional purchase-order number

          setup_billing: Whether to set up billing for the contract by creating a billing contract in the
              connected billing provider. When false, the contract only provisions access
              (grants entitlements) and no billing contract is created. Defaults to true.

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
            "/api/v1/contracts",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "subscriptions": subscriptions,
                    "activation_end_date": activation_end_date,
                    "activation_start_date": activation_start_date,
                    "name": name,
                    "po_number": po_number,
                    "setup_billing": setup_billing,
                },
                contract_create_params.ContractCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveResponse:
        """
        Retrieves a single contract by its ID, enriched with a preview of its upcoming
        (next) invoice when one is available. Returns 404 when no contract with that ID
        exists in the environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-ACCOUNT-ID": x_account_id,
                    "X-ENVIRONMENT-ID": x_environment_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/api/v1/contracts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        activation_end_date: Union[str, datetime] | Omit = omit,
        activation_start_date: Union[str, datetime] | Omit = omit,
        name: Optional[str] | Omit = omit,
        po_number: Optional[str] | Omit = omit,
        setup_billing: bool | Omit = omit,
        subscription_ids: SequenceNotStr[str] | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractUpdateResponse:
        """
        Updates a contract's metadata (name, PO number, activation dates) and optionally
        re-links its subscriptions. Best-effort re-syncs the change to the connected
        billing provider.

        Args:
          activation_end_date: New activation end date

          activation_start_date: New activation start date

          name: New contract name

          po_number: New purchase-order number

          setup_billing: Enable billing on a provision-access-only contract by creating a billing
              contract in the connected billing provider. Only takes effect when true and the
              contract has no billing yet; omitting it leaves billing unchanged. Billing is
              never removed by an update.

          subscription_ids: When provided, replaces the set of subscriptions linked to the contract
              (subscription ref IDs)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-ACCOUNT-ID": x_account_id,
                    "X-ENVIRONMENT-ID": x_environment_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/api/v1/contracts/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "activation_end_date": activation_end_date,
                    "activation_start_date": activation_start_date,
                    "name": name,
                    "po_number": po_number,
                    "setup_billing": setup_billing,
                    "subscription_ids": subscription_ids,
                },
                contract_update_params.ContractUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        customer_external_id: str | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        state: str | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ContractListResponse, AsyncMyCursorIDPage[ContractListResponse]]:
        """
        Retrieves a cursor-paginated list of contracts in the environment, fetched live
        from the connected billing provider. Each contract is enriched with a preview of
        its upcoming (next) invoice when one is available. Returns an empty list when no
        billing provider is connected. Supports filtering by customer external ID,
        state, and name.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          customer_external_id: Filter by the exact external ID of the customer the contract belongs to

          limit: Maximum number of items to return

          name: Filter by exact contract name

          state: Filter by contract state. Supports comma-separated values for multiple states

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
        return self._get_api_list(
            "/api/v1/contracts",
            page=AsyncMyCursorIDPage[ContractListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "customer_external_id": customer_external_id,
                        "limit": limit,
                        "name": name,
                        "state": state,
                    },
                    contract_list_params.ContractListParams,
                ),
            ),
            model=ContractListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractDeleteResponse:
        """
        Deletes a contract: cancels the contract in the connected billing provider and
        cancels every subscription linked to it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
            path_template("/api/v1/contracts/{id}/archive", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractDeleteResponse,
        )


class ContractsResourceWithRawResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.create = to_raw_response_wrapper(
            contracts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contracts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            contracts.update,
        )
        self.list = to_raw_response_wrapper(
            contracts.list,
        )
        self.delete = to_raw_response_wrapper(
            contracts.delete,
        )


class AsyncContractsResourceWithRawResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.create = async_to_raw_response_wrapper(
            contracts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contracts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            contracts.update,
        )
        self.list = async_to_raw_response_wrapper(
            contracts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            contracts.delete,
        )


class ContractsResourceWithStreamingResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.create = to_streamed_response_wrapper(
            contracts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contracts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            contracts.update,
        )
        self.list = to_streamed_response_wrapper(
            contracts.list,
        )
        self.delete = to_streamed_response_wrapper(
            contracts.delete,
        )


class AsyncContractsResourceWithStreamingResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.create = async_to_streamed_response_wrapper(
            contracts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contracts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            contracts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            contracts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            contracts.delete,
        )
