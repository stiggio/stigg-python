# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from ......_base_client import AsyncPaginator, make_request_options
from ......types.v1.events.beta.customers import assignment_list_params, assignment_upsert_params
from ......types.v1.events.beta.customers.assignment_list_response import AssignmentListResponse
from ......types.v1.events.beta.customers.assignment_upsert_response import AssignmentUpsertResponse

__all__ = ["AssignmentsResource", "AsyncAssignmentsResource"]


class AssignmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AssignmentsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        capability_id: str | Omit = omit,
        entity_id: str | Omit = omit,
        limit: int | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[AssignmentListResponse]:
        """Returns a cursor-paginated list of capability assignments for the given
        customer.

        An assignment ties an entity to a capability with a usage limit and
        reset cadence.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          capability_id: Filter assignments to a specific capability refId

          entity_id: Filter assignments to a specific entity refId

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
            path_template("/api/v1-beta/customers/{id}/assignments", id=id),
            page=SyncMyCursorIDPage[AssignmentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "capability_id": capability_id,
                        "entity_id": entity_id,
                        "limit": limit,
                    },
                    assignment_list_params.AssignmentListParams,
                ),
            ),
            model=AssignmentListResponse,
        )

    def upsert(
        self,
        id: str,
        *,
        assignments: Iterable[assignment_upsert_params.Assignment],
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssignmentUpsertResponse:
        """Batched create-or-update of capability assignments.

        Existing assignments matched
        by (entityId, capabilityId) are updated; new pairs are created. On update,
        omitted fields (usageLimit, cadence) are preserved; on create both are required
        by the governance service.

        Args:
          assignments: Assignments to upsert (1–100 per request)

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
            path_template("/api/v1-beta/customers/{id}/assignments", id=id),
            body=maybe_transform({"assignments": assignments}, assignment_upsert_params.AssignmentUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssignmentUpsertResponse,
        )


class AsyncAssignmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncAssignmentsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        capability_id: str | Omit = omit,
        entity_id: str | Omit = omit,
        limit: int | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AssignmentListResponse, AsyncMyCursorIDPage[AssignmentListResponse]]:
        """Returns a cursor-paginated list of capability assignments for the given
        customer.

        An assignment ties an entity to a capability with a usage limit and
        reset cadence.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          capability_id: Filter assignments to a specific capability refId

          entity_id: Filter assignments to a specific entity refId

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
            path_template("/api/v1-beta/customers/{id}/assignments", id=id),
            page=AsyncMyCursorIDPage[AssignmentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "capability_id": capability_id,
                        "entity_id": entity_id,
                        "limit": limit,
                    },
                    assignment_list_params.AssignmentListParams,
                ),
            ),
            model=AssignmentListResponse,
        )

    async def upsert(
        self,
        id: str,
        *,
        assignments: Iterable[assignment_upsert_params.Assignment],
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssignmentUpsertResponse:
        """Batched create-or-update of capability assignments.

        Existing assignments matched
        by (entityId, capabilityId) are updated; new pairs are created. On update,
        omitted fields (usageLimit, cadence) are preserved; on create both are required
        by the governance service.

        Args:
          assignments: Assignments to upsert (1–100 per request)

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
            path_template("/api/v1-beta/customers/{id}/assignments", id=id),
            body=await async_maybe_transform(
                {"assignments": assignments}, assignment_upsert_params.AssignmentUpsertParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssignmentUpsertResponse,
        )


class AssignmentsResourceWithRawResponse:
    def __init__(self, assignments: AssignmentsResource) -> None:
        self._assignments = assignments

        self.list = to_raw_response_wrapper(
            assignments.list,
        )
        self.upsert = to_raw_response_wrapper(
            assignments.upsert,
        )


class AsyncAssignmentsResourceWithRawResponse:
    def __init__(self, assignments: AsyncAssignmentsResource) -> None:
        self._assignments = assignments

        self.list = async_to_raw_response_wrapper(
            assignments.list,
        )
        self.upsert = async_to_raw_response_wrapper(
            assignments.upsert,
        )


class AssignmentsResourceWithStreamingResponse:
    def __init__(self, assignments: AssignmentsResource) -> None:
        self._assignments = assignments

        self.list = to_streamed_response_wrapper(
            assignments.list,
        )
        self.upsert = to_streamed_response_wrapper(
            assignments.upsert,
        )


class AsyncAssignmentsResourceWithStreamingResponse:
    def __init__(self, assignments: AsyncAssignmentsResource) -> None:
        self._assignments = assignments

        self.list = async_to_streamed_response_wrapper(
            assignments.list,
        )
        self.upsert = async_to_streamed_response_wrapper(
            assignments.upsert,
        )
