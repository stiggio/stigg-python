# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from stigg.types.v1.events.beta import (
    EntityTypeListResponse,
    EntityTypeUpsertResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntityTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        entity_type = client.v1.events.beta.entity_types.list()
        assert_matches_type(SyncMyCursorIDPage[EntityTypeListResponse], entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        entity_type = client.v1.events.beta.entity_types.list(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(SyncMyCursorIDPage[EntityTypeListResponse], entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1.events.beta.entity_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = response.parse()
        assert_matches_type(SyncMyCursorIDPage[EntityTypeListResponse], entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1.events.beta.entity_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = response.parse()
            assert_matches_type(SyncMyCursorIDPage[EntityTypeListResponse], entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Stigg) -> None:
        entity_type = client.v1.events.beta.entity_types.upsert(
            types=[
                {
                    "id": "org",
                    "attribution_keys": ["organizationId"],
                    "display_name": "Organization",
                },
                {
                    "id": "team",
                    "attribution_keys": ["teamId"],
                    "display_name": "Team",
                },
            ],
        )
        assert_matches_type(EntityTypeUpsertResponse, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: Stigg) -> None:
        entity_type = client.v1.events.beta.entity_types.upsert(
            types=[
                {
                    "id": "org",
                    "attribution_keys": ["organizationId"],
                    "display_name": "Organization",
                },
                {
                    "id": "team",
                    "attribution_keys": ["teamId"],
                    "display_name": "Team",
                },
            ],
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(EntityTypeUpsertResponse, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Stigg) -> None:
        response = client.v1.events.beta.entity_types.with_raw_response.upsert(
            types=[
                {
                    "id": "org",
                    "attribution_keys": ["organizationId"],
                    "display_name": "Organization",
                },
                {
                    "id": "team",
                    "attribution_keys": ["teamId"],
                    "display_name": "Team",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = response.parse()
        assert_matches_type(EntityTypeUpsertResponse, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Stigg) -> None:
        with client.v1.events.beta.entity_types.with_streaming_response.upsert(
            types=[
                {
                    "id": "org",
                    "attribution_keys": ["organizationId"],
                    "display_name": "Organization",
                },
                {
                    "id": "team",
                    "attribution_keys": ["teamId"],
                    "display_name": "Team",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = response.parse()
            assert_matches_type(EntityTypeUpsertResponse, entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEntityTypes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        entity_type = await async_client.v1.events.beta.entity_types.list()
        assert_matches_type(AsyncMyCursorIDPage[EntityTypeListResponse], entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        entity_type = await async_client.v1.events.beta.entity_types.list(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(AsyncMyCursorIDPage[EntityTypeListResponse], entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.beta.entity_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[EntityTypeListResponse], entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.beta.entity_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[EntityTypeListResponse], entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncStigg) -> None:
        entity_type = await async_client.v1.events.beta.entity_types.upsert(
            types=[
                {
                    "id": "org",
                    "attribution_keys": ["organizationId"],
                    "display_name": "Organization",
                },
                {
                    "id": "team",
                    "attribution_keys": ["teamId"],
                    "display_name": "Team",
                },
            ],
        )
        assert_matches_type(EntityTypeUpsertResponse, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncStigg) -> None:
        entity_type = await async_client.v1.events.beta.entity_types.upsert(
            types=[
                {
                    "id": "org",
                    "attribution_keys": ["organizationId"],
                    "display_name": "Organization",
                },
                {
                    "id": "team",
                    "attribution_keys": ["teamId"],
                    "display_name": "Team",
                },
            ],
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(EntityTypeUpsertResponse, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.beta.entity_types.with_raw_response.upsert(
            types=[
                {
                    "id": "org",
                    "attribution_keys": ["organizationId"],
                    "display_name": "Organization",
                },
                {
                    "id": "team",
                    "attribution_keys": ["teamId"],
                    "display_name": "Team",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = await response.parse()
        assert_matches_type(EntityTypeUpsertResponse, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.beta.entity_types.with_streaming_response.upsert(
            types=[
                {
                    "id": "org",
                    "attribution_keys": ["organizationId"],
                    "display_name": "Organization",
                },
                {
                    "id": "team",
                    "attribution_keys": ["teamId"],
                    "display_name": "Team",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = await response.parse()
            assert_matches_type(EntityTypeUpsertResponse, entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True
