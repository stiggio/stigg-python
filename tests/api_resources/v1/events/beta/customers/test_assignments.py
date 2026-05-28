# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from stigg.types.v1.events.beta.customers import (
    AssignmentListResponse,
    AssignmentUpsertResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssignments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        assignment = client.v1.events.beta.customers.assignments.list(
            id="id",
        )
        assert_matches_type(SyncMyCursorIDPage[AssignmentListResponse], assignment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        assignment = client.v1.events.beta.customers.assignments.list(
            id="id",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            capability_id="capabilityId",
            entity_id="entityId",
            limit=1,
        )
        assert_matches_type(SyncMyCursorIDPage[AssignmentListResponse], assignment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1.events.beta.customers.assignments.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignment = response.parse()
        assert_matches_type(SyncMyCursorIDPage[AssignmentListResponse], assignment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1.events.beta.customers.assignments.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignment = response.parse()
            assert_matches_type(SyncMyCursorIDPage[AssignmentListResponse], assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.beta.customers.assignments.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Stigg) -> None:
        assignment = client.v1.events.beta.customers.assignments.upsert(
            id="id",
            assignments=[
                {
                    "capability_id": "compute-minutes",
                    "entity_id": "workspace-001",
                },
                {
                    "capability_id": "compute-minutes",
                    "entity_id": "workspace-002",
                },
            ],
        )
        assert_matches_type(AssignmentUpsertResponse, assignment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Stigg) -> None:
        response = client.v1.events.beta.customers.assignments.with_raw_response.upsert(
            id="id",
            assignments=[
                {
                    "capability_id": "compute-minutes",
                    "entity_id": "workspace-001",
                },
                {
                    "capability_id": "compute-minutes",
                    "entity_id": "workspace-002",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignment = response.parse()
        assert_matches_type(AssignmentUpsertResponse, assignment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Stigg) -> None:
        with client.v1.events.beta.customers.assignments.with_streaming_response.upsert(
            id="id",
            assignments=[
                {
                    "capability_id": "compute-minutes",
                    "entity_id": "workspace-001",
                },
                {
                    "capability_id": "compute-minutes",
                    "entity_id": "workspace-002",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignment = response.parse()
            assert_matches_type(AssignmentUpsertResponse, assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.beta.customers.assignments.with_raw_response.upsert(
                id="",
                assignments=[
                    {
                        "capability_id": "compute-minutes",
                        "entity_id": "workspace-001",
                    },
                    {
                        "capability_id": "compute-minutes",
                        "entity_id": "workspace-002",
                    },
                ],
            )


class TestAsyncAssignments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        assignment = await async_client.v1.events.beta.customers.assignments.list(
            id="id",
        )
        assert_matches_type(AsyncMyCursorIDPage[AssignmentListResponse], assignment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        assignment = await async_client.v1.events.beta.customers.assignments.list(
            id="id",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            capability_id="capabilityId",
            entity_id="entityId",
            limit=1,
        )
        assert_matches_type(AsyncMyCursorIDPage[AssignmentListResponse], assignment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.beta.customers.assignments.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignment = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[AssignmentListResponse], assignment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.beta.customers.assignments.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignment = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[AssignmentListResponse], assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.beta.customers.assignments.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncStigg) -> None:
        assignment = await async_client.v1.events.beta.customers.assignments.upsert(
            id="id",
            assignments=[
                {
                    "capability_id": "compute-minutes",
                    "entity_id": "workspace-001",
                },
                {
                    "capability_id": "compute-minutes",
                    "entity_id": "workspace-002",
                },
            ],
        )
        assert_matches_type(AssignmentUpsertResponse, assignment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.beta.customers.assignments.with_raw_response.upsert(
            id="id",
            assignments=[
                {
                    "capability_id": "compute-minutes",
                    "entity_id": "workspace-001",
                },
                {
                    "capability_id": "compute-minutes",
                    "entity_id": "workspace-002",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignment = await response.parse()
        assert_matches_type(AssignmentUpsertResponse, assignment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.beta.customers.assignments.with_streaming_response.upsert(
            id="id",
            assignments=[
                {
                    "capability_id": "compute-minutes",
                    "entity_id": "workspace-001",
                },
                {
                    "capability_id": "compute-minutes",
                    "entity_id": "workspace-002",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignment = await response.parse()
            assert_matches_type(AssignmentUpsertResponse, assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.beta.customers.assignments.with_raw_response.upsert(
                id="",
                assignments=[
                    {
                        "capability_id": "compute-minutes",
                        "entity_id": "workspace-001",
                    },
                    {
                        "capability_id": "compute-minutes",
                        "entity_id": "workspace-002",
                    },
                ],
            )
