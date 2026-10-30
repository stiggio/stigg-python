# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
from .....types.v1.customers.entities import entitlement_list_params, entitlement_upsert_params
from .....types.v1.customers.entities.entitlement_list_response import EntitlementListResponse
from .....types.v1.customers.entities.entitlement_upsert_response import EntitlementUpsertResponse

__all__ = ["EntitlementsResource", "AsyncEntitlementsResource"]


class EntitlementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return EntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return EntitlementsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        currency_id: str | Omit = omit,
        entity_id: str | Omit = omit,
        feature_id: str | Omit = omit,
        limit: int | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[EntitlementListResponse]:
        """
        Returns a cursor-paginated list of entity entitlements for the given customer.
        An entity entitlement ties an entity to a feature or currency with a usage limit
        and reset cadence.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          currency_id: Filter entity entitlements to a specific currency, by its ID. Mutually exclusive
              with `featureId`.

          entity_id: Filter entity entitlements to a specific entity ID

          feature_id: Filter entity entitlements to a specific feature, by its ID. Mutually exclusive
              with `currencyId`.

          limit: Maximum number of items to return

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
        return self._get_api_list(
            path_template("/api/v1/customers/{id}/entities/entitlements", id=id),
            page=SyncMyCursorIDPage[EntitlementListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "currency_id": currency_id,
                        "entity_id": entity_id,
                        "feature_id": feature_id,
                        "limit": limit,
                    },
                    entitlement_list_params.EntitlementListParams,
                ),
            ),
            model=EntitlementListResponse,
        )

    def upsert(
        self,
        id: str,
        *,
        entity_entitlements: Iterable[entitlement_upsert_params.EntityEntitlement],
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementUpsertResponse:
        """Batched create-or-update of entity entitlements.

        Existing entity entitlements
        matched by (entityId, featureId or currencyId, scopeEntityIds) are updated; new
        ones are created. On update, omitted fields (usageLimit, cadence) are preserved;
        on create both are required.

        Args:
          entity_entitlements: Entity entitlements to upsert (1–100 per request)

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
        return self._put(
            path_template("/api/v1/customers/{id}/entities/entitlements", id=id),
            body=maybe_transform(
                {"entity_entitlements": entity_entitlements}, entitlement_upsert_params.EntitlementUpsertParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementUpsertResponse,
        )


class AsyncEntitlementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncEntitlementsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        currency_id: str | Omit = omit,
        entity_id: str | Omit = omit,
        feature_id: str | Omit = omit,
        limit: int | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EntitlementListResponse, AsyncMyCursorIDPage[EntitlementListResponse]]:
        """
        Returns a cursor-paginated list of entity entitlements for the given customer.
        An entity entitlement ties an entity to a feature or currency with a usage limit
        and reset cadence.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          currency_id: Filter entity entitlements to a specific currency, by its ID. Mutually exclusive
              with `featureId`.

          entity_id: Filter entity entitlements to a specific entity ID

          feature_id: Filter entity entitlements to a specific feature, by its ID. Mutually exclusive
              with `currencyId`.

          limit: Maximum number of items to return

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
        return self._get_api_list(
            path_template("/api/v1/customers/{id}/entities/entitlements", id=id),
            page=AsyncMyCursorIDPage[EntitlementListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "currency_id": currency_id,
                        "entity_id": entity_id,
                        "feature_id": feature_id,
                        "limit": limit,
                    },
                    entitlement_list_params.EntitlementListParams,
                ),
            ),
            model=EntitlementListResponse,
        )

    async def upsert(
        self,
        id: str,
        *,
        entity_entitlements: Iterable[entitlement_upsert_params.EntityEntitlement],
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementUpsertResponse:
        """Batched create-or-update of entity entitlements.

        Existing entity entitlements
        matched by (entityId, featureId or currencyId, scopeEntityIds) are updated; new
        ones are created. On update, omitted fields (usageLimit, cadence) are preserved;
        on create both are required.

        Args:
          entity_entitlements: Entity entitlements to upsert (1–100 per request)

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
        return await self._put(
            path_template("/api/v1/customers/{id}/entities/entitlements", id=id),
            body=await async_maybe_transform(
                {"entity_entitlements": entity_entitlements}, entitlement_upsert_params.EntitlementUpsertParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementUpsertResponse,
        )


class EntitlementsResourceWithRawResponse:
    def __init__(self, entitlements: EntitlementsResource) -> None:
        self._entitlements = entitlements

        self.list = to_raw_response_wrapper(
            entitlements.list,
        )
        self.upsert = to_raw_response_wrapper(
            entitlements.upsert,
        )


class AsyncEntitlementsResourceWithRawResponse:
    def __init__(self, entitlements: AsyncEntitlementsResource) -> None:
        self._entitlements = entitlements

        self.list = async_to_raw_response_wrapper(
            entitlements.list,
        )
        self.upsert = async_to_raw_response_wrapper(
            entitlements.upsert,
        )


class EntitlementsResourceWithStreamingResponse:
    def __init__(self, entitlements: EntitlementsResource) -> None:
        self._entitlements = entitlements

        self.list = to_streamed_response_wrapper(
            entitlements.list,
        )
        self.upsert = to_streamed_response_wrapper(
            entitlements.upsert,
        )


class AsyncEntitlementsResourceWithStreamingResponse:
    def __init__(self, entitlements: AsyncEntitlementsResource) -> None:
        self._entitlements = entitlements

        self.list = async_to_streamed_response_wrapper(
            entitlements.list,
        )
        self.upsert = async_to_streamed_response_wrapper(
            entitlements.upsert,
        )
