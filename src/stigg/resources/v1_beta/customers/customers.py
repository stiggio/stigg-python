# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .entities import (
    EntitiesResource,
    AsyncEntitiesResource,
    EntitiesResourceWithRawResponse,
    AsyncEntitiesResourceWithRawResponse,
    EntitiesResourceWithStreamingResponse,
    AsyncEntitiesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from .assignments import (
    AssignmentsResource,
    AsyncAssignmentsResource,
    AssignmentsResourceWithRawResponse,
    AsyncAssignmentsResourceWithRawResponse,
    AssignmentsResourceWithStreamingResponse,
    AsyncAssignmentsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .entitlements import (
    EntitlementsResource,
    AsyncEntitlementsResource,
    EntitlementsResourceWithRawResponse,
    AsyncEntitlementsResourceWithRawResponse,
    EntitlementsResourceWithStreamingResponse,
    AsyncEntitlementsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.v1_beta import customer_retrieve_governance_params
from ....types.v1_beta.customer_retrieve_governance_response import CustomerRetrieveGovernanceResponse

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def entitlements(self) -> EntitlementsResource:
        return EntitlementsResource(self._client)

    @cached_property
    def entities(self) -> EntitiesResource:
        return EntitiesResource(self._client)

    @cached_property
    def assignments(self) -> AssignmentsResource:
        return AssignmentsResource(self._client)

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

    def retrieve_governance(
        self,
        id: str,
        *,
        after: str | Omit = omit,
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
    ) -> CustomerRetrieveGovernanceResponse:
        """
        Queries the customer's governance hierarchy tree, returning a cursor-paginated
        list of nodes with their usage configuration (limit, cadence, scope) and current
        usage, sortable and filterable by usage. Each node carries `parentId` so the
        tree can be rebuilt client-side. Usage is read from a periodically-refreshed
        read model and never gates access.

        Args:
          after: Return items that come after this cursor

          currency_ids: Currency ids to include, repeated per value (e.g. `?currencyIds=credits`). Omit
              both featureIds and currencyIds for tree mode.

          entity_id_search: Case-insensitive substring match on the entity id (`%`/`_` matched literally).

          entity_type_ids: Filter to one or more entity types, repeated per value (e.g.
              `?entityTypeIds=team&entityTypeIds=user`).

          feature_ids: Feature ids to include, repeated per value (e.g.
              `?featureIds=ai-tokens&featureIds=seats`). Omit both featureIds and currencyIds
              for tree mode — every node in the hierarchy with no usage configuration
              attached.

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
        return self._get(
            path_template("/api/v1-beta/customers/{id}/governance", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
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
                    customer_retrieve_governance_params.CustomerRetrieveGovernanceParams,
                ),
            ),
            cast_to=CustomerRetrieveGovernanceResponse,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def entitlements(self) -> AsyncEntitlementsResource:
        return AsyncEntitlementsResource(self._client)

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        return AsyncEntitiesResource(self._client)

    @cached_property
    def assignments(self) -> AsyncAssignmentsResource:
        return AsyncAssignmentsResource(self._client)

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

    async def retrieve_governance(
        self,
        id: str,
        *,
        after: str | Omit = omit,
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
    ) -> CustomerRetrieveGovernanceResponse:
        """
        Queries the customer's governance hierarchy tree, returning a cursor-paginated
        list of nodes with their usage configuration (limit, cadence, scope) and current
        usage, sortable and filterable by usage. Each node carries `parentId` so the
        tree can be rebuilt client-side. Usage is read from a periodically-refreshed
        read model and never gates access.

        Args:
          after: Return items that come after this cursor

          currency_ids: Currency ids to include, repeated per value (e.g. `?currencyIds=credits`). Omit
              both featureIds and currencyIds for tree mode.

          entity_id_search: Case-insensitive substring match on the entity id (`%`/`_` matched literally).

          entity_type_ids: Filter to one or more entity types, repeated per value (e.g.
              `?entityTypeIds=team&entityTypeIds=user`).

          feature_ids: Feature ids to include, repeated per value (e.g.
              `?featureIds=ai-tokens&featureIds=seats`). Omit both featureIds and currencyIds
              for tree mode — every node in the hierarchy with no usage configuration
              attached.

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
        return await self._get(
            path_template("/api/v1-beta/customers/{id}/governance", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
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
                    customer_retrieve_governance_params.CustomerRetrieveGovernanceParams,
                ),
            ),
            cast_to=CustomerRetrieveGovernanceResponse,
        )


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.retrieve_governance = to_raw_response_wrapper(
            customers.retrieve_governance,
        )

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithRawResponse:
        return EntitlementsResourceWithRawResponse(self._customers.entitlements)

    @cached_property
    def entities(self) -> EntitiesResourceWithRawResponse:
        return EntitiesResourceWithRawResponse(self._customers.entities)

    @cached_property
    def assignments(self) -> AssignmentsResourceWithRawResponse:
        return AssignmentsResourceWithRawResponse(self._customers.assignments)


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.retrieve_governance = async_to_raw_response_wrapper(
            customers.retrieve_governance,
        )

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithRawResponse:
        return AsyncEntitlementsResourceWithRawResponse(self._customers.entitlements)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithRawResponse:
        return AsyncEntitiesResourceWithRawResponse(self._customers.entities)

    @cached_property
    def assignments(self) -> AsyncAssignmentsResourceWithRawResponse:
        return AsyncAssignmentsResourceWithRawResponse(self._customers.assignments)


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.retrieve_governance = to_streamed_response_wrapper(
            customers.retrieve_governance,
        )

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithStreamingResponse:
        return EntitlementsResourceWithStreamingResponse(self._customers.entitlements)

    @cached_property
    def entities(self) -> EntitiesResourceWithStreamingResponse:
        return EntitiesResourceWithStreamingResponse(self._customers.entities)

    @cached_property
    def assignments(self) -> AssignmentsResourceWithStreamingResponse:
        return AssignmentsResourceWithStreamingResponse(self._customers.assignments)


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.retrieve_governance = async_to_streamed_response_wrapper(
            customers.retrieve_governance,
        )

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithStreamingResponse:
        return AsyncEntitlementsResourceWithStreamingResponse(self._customers.entitlements)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithStreamingResponse:
        return AsyncEntitiesResourceWithStreamingResponse(self._customers.entities)

    @cached_property
    def assignments(self) -> AsyncAssignmentsResourceWithStreamingResponse:
        return AsyncAssignmentsResourceWithStreamingResponse(self._customers.assignments)
