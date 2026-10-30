# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import entity_type_list_params, entity_type_upsert_params, entity_type_archive_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.v1.entity_type_list_response import EntityTypeListResponse
from ...types.v1.entity_type_upsert_response import EntityTypeUpsertResponse
from ...types.v1.entity_type_archive_response import EntityTypeArchiveResponse
from ...types.v1.entity_type_check_active_entities_response import EntityTypeCheckActiveEntitiesResponse

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
        include_archived: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
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
        (e.g. Org, Team, User). Archived entity types are excluded unless
        includeArchived=true.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          include_archived: Whether to include archived entity types. One of: true, false

          limit: Maximum number of items to return

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
            "/api/v1/entity-types",
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
                        "include_archived": include_archived,
                        "limit": limit,
                    },
                    entity_type_list_params.EntityTypeListParams,
                ),
            ),
            model=EntityTypeListResponse,
        )

    def archive(
        self,
        *,
        ids: SequenceNotStr[str],
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityTypeArchiveResponse:
        """Archives entity types in bulk by id.

        An entity type with active entities cannot
        be archived: archive its entities first, or the whole request fails with 400.

        Args:
          ids: Entity type identifiers to act on

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
            "/api/v1/entity-types/archive",
            body=maybe_transform({"ids": ids}, entity_type_archive_params.EntityTypeArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityTypeArchiveResponse,
        )

    def check_active_entities(
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
    ) -> EntityTypeCheckActiveEntitiesResponse:
        """
        Returns whether any active entity of this entity type exists, across every
        customer. An entity type can be archived only when this is false. An unknown
        entity type returns false.

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
            path_template("/api/v1/entity-types/{id}/has-active-entities", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityTypeCheckActiveEntitiesResponse,
        )

    def upsert(
        self,
        *,
        types: Iterable[entity_type_upsert_params.Type],
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
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
        converges to the same state. An upsert of an archived entity type restores it.

        Args:
          types: Entity types to upsert (1–100 per request)

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
        return self._put(
            "/api/v1/entity-types",
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
        include_archived: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
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
        (e.g. Org, Team, User). Archived entity types are excluded unless
        includeArchived=true.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          include_archived: Whether to include archived entity types. One of: true, false

          limit: Maximum number of items to return

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
            "/api/v1/entity-types",
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
                        "include_archived": include_archived,
                        "limit": limit,
                    },
                    entity_type_list_params.EntityTypeListParams,
                ),
            ),
            model=EntityTypeListResponse,
        )

    async def archive(
        self,
        *,
        ids: SequenceNotStr[str],
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityTypeArchiveResponse:
        """Archives entity types in bulk by id.

        An entity type with active entities cannot
        be archived: archive its entities first, or the whole request fails with 400.

        Args:
          ids: Entity type identifiers to act on

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
            "/api/v1/entity-types/archive",
            body=await async_maybe_transform({"ids": ids}, entity_type_archive_params.EntityTypeArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityTypeArchiveResponse,
        )

    async def check_active_entities(
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
    ) -> EntityTypeCheckActiveEntitiesResponse:
        """
        Returns whether any active entity of this entity type exists, across every
        customer. An entity type can be archived only when this is false. An unknown
        entity type returns false.

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
            path_template("/api/v1/entity-types/{id}/has-active-entities", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityTypeCheckActiveEntitiesResponse,
        )

    async def upsert(
        self,
        *,
        types: Iterable[entity_type_upsert_params.Type],
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
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
        converges to the same state. An upsert of an archived entity type restores it.

        Args:
          types: Entity types to upsert (1–100 per request)

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
        return await self._put(
            "/api/v1/entity-types",
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
        self.archive = to_raw_response_wrapper(
            entity_types.archive,
        )
        self.check_active_entities = to_raw_response_wrapper(
            entity_types.check_active_entities,
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
        self.archive = async_to_raw_response_wrapper(
            entity_types.archive,
        )
        self.check_active_entities = async_to_raw_response_wrapper(
            entity_types.check_active_entities,
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
        self.archive = to_streamed_response_wrapper(
            entity_types.archive,
        )
        self.check_active_entities = to_streamed_response_wrapper(
            entity_types.check_active_entities,
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
        self.archive = async_to_streamed_response_wrapper(
            entity_types.archive,
        )
        self.check_active_entities = async_to_streamed_response_wrapper(
            entity_types.check_active_entities,
        )
        self.upsert = async_to_streamed_response_wrapper(
            entity_types.upsert,
        )
