# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from stigg.types.v1_beta import (
    EntityListResponse,
    EntityUpsertResponse,
    EntityArchiveResponse,
    EntityRetrieveResponse,
    EntityUnarchiveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Stigg) -> None:
        entity = client.v1_beta.entities.retrieve(
            entity_id="x",
            id="id",
        )
        assert_matches_type(EntityRetrieveResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Stigg) -> None:
        response = client.v1_beta.entities.with_raw_response.retrieve(
            entity_id="x",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityRetrieveResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Stigg) -> None:
        with client.v1_beta.entities.with_streaming_response.retrieve(
            entity_id="x",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityRetrieveResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1_beta.entities.with_raw_response.retrieve(
                entity_id="x",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.v1_beta.entities.with_raw_response.retrieve(
                entity_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        entity = client.v1_beta.entities.list(
            id="id",
        )
        assert_matches_type(SyncMyCursorIDPage[EntityListResponse], entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        entity = client.v1_beta.entities.list(
            id="id",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_archived="true",
            limit=1,
            type_ref_id="typeRefId",
        )
        assert_matches_type(SyncMyCursorIDPage[EntityListResponse], entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1_beta.entities.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(SyncMyCursorIDPage[EntityListResponse], entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1_beta.entities.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(SyncMyCursorIDPage[EntityListResponse], entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1_beta.entities.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Stigg) -> None:
        entity = client.v1_beta.entities.archive(
            id="id",
            ids=["user-7f3a0c1d", "user-c4d1b2e9"],
        )
        assert_matches_type(EntityArchiveResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Stigg) -> None:
        response = client.v1_beta.entities.with_raw_response.archive(
            id="id",
            ids=["user-7f3a0c1d", "user-c4d1b2e9"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityArchiveResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Stigg) -> None:
        with client.v1_beta.entities.with_streaming_response.archive(
            id="id",
            ids=["user-7f3a0c1d", "user-c4d1b2e9"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityArchiveResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1_beta.entities.with_raw_response.archive(
                id="",
                ids=["user-7f3a0c1d", "user-c4d1b2e9"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unarchive(self, client: Stigg) -> None:
        entity = client.v1_beta.entities.unarchive(
            id="id",
            ids=["user-7f3a0c1d", "user-c4d1b2e9"],
        )
        assert_matches_type(EntityUnarchiveResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unarchive(self, client: Stigg) -> None:
        response = client.v1_beta.entities.with_raw_response.unarchive(
            id="id",
            ids=["user-7f3a0c1d", "user-c4d1b2e9"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityUnarchiveResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unarchive(self, client: Stigg) -> None:
        with client.v1_beta.entities.with_streaming_response.unarchive(
            id="id",
            ids=["user-7f3a0c1d", "user-c4d1b2e9"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityUnarchiveResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unarchive(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1_beta.entities.with_raw_response.unarchive(
                id="",
                ids=["user-7f3a0c1d", "user-c4d1b2e9"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Stigg) -> None:
        entity = client.v1_beta.entities.upsert(
            id="id",
            entities=[{"id": "user-7f3a0c1d"}, {"id": "user-c4d1b2e9"}],
        )
        assert_matches_type(EntityUpsertResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Stigg) -> None:
        response = client.v1_beta.entities.with_raw_response.upsert(
            id="id",
            entities=[{"id": "user-7f3a0c1d"}, {"id": "user-c4d1b2e9"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityUpsertResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Stigg) -> None:
        with client.v1_beta.entities.with_streaming_response.upsert(
            id="id",
            entities=[{"id": "user-7f3a0c1d"}, {"id": "user-c4d1b2e9"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityUpsertResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1_beta.entities.with_raw_response.upsert(
                id="",
                entities=[{"id": "user-7f3a0c1d"}, {"id": "user-c4d1b2e9"}],
            )


class TestAsyncEntities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStigg) -> None:
        entity = await async_client.v1_beta.entities.retrieve(
            entity_id="x",
            id="id",
        )
        assert_matches_type(EntityRetrieveResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1_beta.entities.with_raw_response.retrieve(
            entity_id="x",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityRetrieveResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStigg) -> None:
        async with async_client.v1_beta.entities.with_streaming_response.retrieve(
            entity_id="x",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityRetrieveResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1_beta.entities.with_raw_response.retrieve(
                entity_id="x",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.v1_beta.entities.with_raw_response.retrieve(
                entity_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        entity = await async_client.v1_beta.entities.list(
            id="id",
        )
        assert_matches_type(AsyncMyCursorIDPage[EntityListResponse], entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        entity = await async_client.v1_beta.entities.list(
            id="id",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_archived="true",
            limit=1,
            type_ref_id="typeRefId",
        )
        assert_matches_type(AsyncMyCursorIDPage[EntityListResponse], entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1_beta.entities.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[EntityListResponse], entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1_beta.entities.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[EntityListResponse], entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1_beta.entities.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncStigg) -> None:
        entity = await async_client.v1_beta.entities.archive(
            id="id",
            ids=["user-7f3a0c1d", "user-c4d1b2e9"],
        )
        assert_matches_type(EntityArchiveResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1_beta.entities.with_raw_response.archive(
            id="id",
            ids=["user-7f3a0c1d", "user-c4d1b2e9"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityArchiveResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncStigg) -> None:
        async with async_client.v1_beta.entities.with_streaming_response.archive(
            id="id",
            ids=["user-7f3a0c1d", "user-c4d1b2e9"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityArchiveResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1_beta.entities.with_raw_response.archive(
                id="",
                ids=["user-7f3a0c1d", "user-c4d1b2e9"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unarchive(self, async_client: AsyncStigg) -> None:
        entity = await async_client.v1_beta.entities.unarchive(
            id="id",
            ids=["user-7f3a0c1d", "user-c4d1b2e9"],
        )
        assert_matches_type(EntityUnarchiveResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1_beta.entities.with_raw_response.unarchive(
            id="id",
            ids=["user-7f3a0c1d", "user-c4d1b2e9"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityUnarchiveResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncStigg) -> None:
        async with async_client.v1_beta.entities.with_streaming_response.unarchive(
            id="id",
            ids=["user-7f3a0c1d", "user-c4d1b2e9"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityUnarchiveResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1_beta.entities.with_raw_response.unarchive(
                id="",
                ids=["user-7f3a0c1d", "user-c4d1b2e9"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncStigg) -> None:
        entity = await async_client.v1_beta.entities.upsert(
            id="id",
            entities=[{"id": "user-7f3a0c1d"}, {"id": "user-c4d1b2e9"}],
        )
        assert_matches_type(EntityUpsertResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1_beta.entities.with_raw_response.upsert(
            id="id",
            entities=[{"id": "user-7f3a0c1d"}, {"id": "user-c4d1b2e9"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityUpsertResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncStigg) -> None:
        async with async_client.v1_beta.entities.with_streaming_response.upsert(
            id="id",
            entities=[{"id": "user-7f3a0c1d"}, {"id": "user-c4d1b2e9"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityUpsertResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1_beta.entities.with_raw_response.upsert(
                id="",
                entities=[{"id": "user-7f3a0c1d"}, {"id": "user-c4d1b2e9"}],
            )
