# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.v1_beta import entity_type_list_params, entity_type_upsert_params
from ...types.v1_beta.entity_type_list_response import EntityTypeListResponse
from ...types.v1_beta.entity_type_upsert_response import EntityTypeUpsertResponse

__all__ = ["EntityTypesResource", "AsyncEntityTypesResource"]


class EntityTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntityTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return EntityTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntityTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return EntityTypesResourceWithStreamingResponse(self)

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
    ) -> SyncMyCursorIDPage[EntityTypeListResponse]:
        """
        Returns a cursor-paginated list of entity types defined in the environment.
        Entity types are vendor-defined categories of resource that can be governed
        (e.g. Org, Team, User).

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
            "/api/v1-beta/entity-types",
            page=SyncMyCursorIDPage[EntityTypeListResponse],
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
                    entity_type_list_params.EntityTypeListParams,
                ),
            ),
            model=EntityTypeListResponse,
        )

    def upsert(
        self,
        *,
        types: Iterable[entity_type_upsert_params.Type],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityTypeUpsertResponse:
        """Batched create-or-update of entity types.

        Existing types matched by id are
        updated; new ids are created. Idempotent — re-submitting the same payload
        converges to the same state.

        Args:
          types: Entity types to upsert (1–100 per request)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/v1-beta/entity-types",
            body=maybe_transform({"types": types}, entity_type_upsert_params.EntityTypeUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityTypeUpsertResponse,
        )


class AsyncEntityTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntityTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntityTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntityTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncEntityTypesResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[EntityTypeListResponse, AsyncMyCursorIDPage[EntityTypeListResponse]]:
        """
        Returns a cursor-paginated list of entity types defined in the environment.
        Entity types are vendor-defined categories of resource that can be governed
        (e.g. Org, Team, User).

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
            "/api/v1-beta/entity-types",
            page=AsyncMyCursorIDPage[EntityTypeListResponse],
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
                    entity_type_list_params.EntityTypeListParams,
                ),
            ),
            model=EntityTypeListResponse,
        )

    async def upsert(
        self,
        *,
        types: Iterable[entity_type_upsert_params.Type],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityTypeUpsertResponse:
        """Batched create-or-update of entity types.

        Existing types matched by id are
        updated; new ids are created. Idempotent — re-submitting the same payload
        converges to the same state.

        Args:
          types: Entity types to upsert (1–100 per request)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/v1-beta/entity-types",
            body=await async_maybe_transform({"types": types}, entity_type_upsert_params.EntityTypeUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityTypeUpsertResponse,
        )


class EntityTypesResourceWithRawResponse:
    def __init__(self, entity_types: EntityTypesResource) -> None:
        self._entity_types = entity_types

        self.list = to_raw_response_wrapper(
            entity_types.list,
        )
        self.upsert = to_raw_response_wrapper(
            entity_types.upsert,
        )


class AsyncEntityTypesResourceWithRawResponse:
    def __init__(self, entity_types: AsyncEntityTypesResource) -> None:
        self._entity_types = entity_types

        self.list = async_to_raw_response_wrapper(
            entity_types.list,
        )
        self.upsert = async_to_raw_response_wrapper(
            entity_types.upsert,
        )


class EntityTypesResourceWithStreamingResponse:
    def __init__(self, entity_types: EntityTypesResource) -> None:
        self._entity_types = entity_types

        self.list = to_streamed_response_wrapper(
            entity_types.list,
        )
        self.upsert = to_streamed_response_wrapper(
            entity_types.upsert,
        )


class AsyncEntityTypesResourceWithStreamingResponse:
    def __init__(self, entity_types: AsyncEntityTypesResource) -> None:
        self._entity_types = entity_types

        self.list = async_to_streamed_response_wrapper(
            entity_types.list,
        )
        self.upsert = async_to_streamed_response_wrapper(
            entity_types.upsert,
        )
