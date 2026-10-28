# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.v1_beta.customers import governance_list_params
from ....types.v1_beta.customers.governance_list_response import GovernanceListResponse

__all__ = ["GovernanceResource", "AsyncGovernanceResource"]


class GovernanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GovernanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return GovernanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GovernanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return GovernanceResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        entity_id_search: str | Omit = omit,
        entity_type_ids: SequenceNotStr[str] | Omit = omit,
        feature_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        min_utilization: float | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        scope: Literal["all", "nodeWide", "scoped"] | Omit = omit,
        sort_by: Literal["utilization", "currentUsage", "usageLimit", "scopeSize", "id", "createdAt"] | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[GovernanceListResponse]:
        """
        Queries the customer's governance hierarchy tree, returning a cursor-paginated
        list of nodes with their usage configuration (limit, cadence, scope) and current
        usage, sortable and filterable by usage. Each node carries `parentId` so the
        tree can be rebuilt client-side. Usage is read from a periodically-refreshed
        read model and never gates access.

        Args:
          after: Opaque cursor from a page’s `next`; returns the page after it. Mutually
              exclusive with `before`.

          before: Opaque cursor from a page’s `prev`; returns the page before it. Mutually
              exclusive with `after`.

          currency_ids: Currency ids to include, comma-separated (e.g. `?currencyIds=credits`), up
              to 100. Omit both featureIds and currencyIds for tree mode.

          entity_id_search: Case-insensitive substring match on the entity id or its display name (`%`/`_`
              matched literally).

          entity_type_ids: Filter to one or more entity types, comma-separated (e.g.
              `?entityTypeIds=team,user`), up to 100.

          feature_ids: Feature ids to include, comma-separated (e.g. `?featureIds=ai-tokens,seats`), up
              to 100. Omit both featureIds and currencyIds for tree mode — every node in the
              hierarchy with no usage configuration attached.

          limit: Maximum number of items to return

          min_utilization: Only nodes with utilization ≥ this value (e.g. 0.8 for ≥80%, 1 for at/over
              limit).

          order: Sort direction: `asc` or `desc` (default `desc`).

          scope: Filter by configuration scope: `all` (default), `nodeWide` (`[]` only), or
              `scoped` (non-empty only).

          sort_by: Sort key: `utilization` (default, cross-capability-safe), `currentUsage`,
              `usageLimit`, `scopeSize`, `id`, or `createdAt`.

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
            path_template("/api/v1-beta/customers/{id}/governance", id=id),
            page=SyncMyCursorIDPage[GovernanceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "currency_ids": currency_ids,
                        "entity_id_search": entity_id_search,
                        "entity_type_ids": entity_type_ids,
                        "feature_ids": feature_ids,
                        "limit": limit,
                        "min_utilization": min_utilization,
                        "order": order,
                        "scope": scope,
                        "sort_by": sort_by,
                    },
                    governance_list_params.GovernanceListParams,
                ),
            ),
            model=GovernanceListResponse,
        )


class AsyncGovernanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGovernanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGovernanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGovernanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncGovernanceResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        entity_id_search: str | Omit = omit,
        entity_type_ids: SequenceNotStr[str] | Omit = omit,
        feature_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        min_utilization: float | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        scope: Literal["all", "nodeWide", "scoped"] | Omit = omit,
        sort_by: Literal["utilization", "currentUsage", "usageLimit", "scopeSize", "id", "createdAt"] | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[GovernanceListResponse, AsyncMyCursorIDPage[GovernanceListResponse]]:
        """
        Queries the customer's governance hierarchy tree, returning a cursor-paginated
        list of nodes with their usage configuration (limit, cadence, scope) and current
        usage, sortable and filterable by usage. Each node carries `parentId` so the
        tree can be rebuilt client-side. Usage is read from a periodically-refreshed
        read model and never gates access.

        Args:
          after: Opaque cursor from a page’s `next`; returns the page after it. Mutually
              exclusive with `before`.

          before: Opaque cursor from a page’s `prev`; returns the page before it. Mutually
              exclusive with `after`.

          currency_ids: Currency ids to include, comma-separated (e.g. `?currencyIds=credits`), up
              to 100. Omit both featureIds and currencyIds for tree mode.

          entity_id_search: Case-insensitive substring match on the entity id or its display name (`%`/`_`
              matched literally).

          entity_type_ids: Filter to one or more entity types, comma-separated (e.g.
              `?entityTypeIds=team,user`), up to 100.

          feature_ids: Feature ids to include, comma-separated (e.g. `?featureIds=ai-tokens,seats`), up
              to 100. Omit both featureIds and currencyIds for tree mode — every node in the
              hierarchy with no usage configuration attached.

          limit: Maximum number of items to return

          min_utilization: Only nodes with utilization ≥ this value (e.g. 0.8 for ≥80%, 1 for at/over
              limit).

          order: Sort direction: `asc` or `desc` (default `desc`).

          scope: Filter by configuration scope: `all` (default), `nodeWide` (`[]` only), or
              `scoped` (non-empty only).

          sort_by: Sort key: `utilization` (default, cross-capability-safe), `currentUsage`,
              `usageLimit`, `scopeSize`, `id`, or `createdAt`.

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
            path_template("/api/v1-beta/customers/{id}/governance", id=id),
            page=AsyncMyCursorIDPage[GovernanceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "currency_ids": currency_ids,
                        "entity_id_search": entity_id_search,
                        "entity_type_ids": entity_type_ids,
                        "feature_ids": feature_ids,
                        "limit": limit,
                        "min_utilization": min_utilization,
                        "order": order,
                        "scope": scope,
                        "sort_by": sort_by,
                    },
                    governance_list_params.GovernanceListParams,
                ),
            ),
            model=GovernanceListResponse,
        )


class GovernanceResourceWithRawResponse:
    def __init__(self, governance: GovernanceResource) -> None:
        self._governance = governance

        self.list = to_raw_response_wrapper(
            governance.list,
        )


class AsyncGovernanceResourceWithRawResponse:
    def __init__(self, governance: AsyncGovernanceResource) -> None:
        self._governance = governance

        self.list = async_to_raw_response_wrapper(
            governance.list,
        )


class GovernanceResourceWithStreamingResponse:
    def __init__(self, governance: GovernanceResource) -> None:
        self._governance = governance

        self.list = to_streamed_response_wrapper(
            governance.list,
        )


class AsyncGovernanceResourceWithStreamingResponse:
    def __init__(self, governance: AsyncGovernanceResource) -> None:
        self._governance = governance

        self.list = async_to_streamed_response_wrapper(
            governance.list,
        )
