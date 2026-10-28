# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from stigg.types.v1_beta.customers import GovernanceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGovernance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        governance = client.v1_beta.customers.governance.list(
            id="id",
        )
        assert_matches_type(SyncMyCursorIDPage[GovernanceListResponse], governance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        governance = client.v1_beta.customers.governance.list(
            id="id",
            after="after",
            before="before",
            currency_ids=["string"],
            entity_id_search="x",
            entity_type_ids=["string"],
            feature_ids=["string"],
            limit=1,
            min_utilization=0,
            order="asc",
            scope="all",
            sort_by="utilization",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(SyncMyCursorIDPage[GovernanceListResponse], governance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1_beta.customers.governance.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        governance = response.parse()
        assert_matches_type(SyncMyCursorIDPage[GovernanceListResponse], governance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1_beta.customers.governance.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            governance = response.parse()
            assert_matches_type(SyncMyCursorIDPage[GovernanceListResponse], governance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1_beta.customers.governance.with_raw_response.list(
                id="",
            )


class TestAsyncGovernance:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        governance = await async_client.v1_beta.customers.governance.list(
            id="id",
        )
        assert_matches_type(AsyncMyCursorIDPage[GovernanceListResponse], governance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        governance = await async_client.v1_beta.customers.governance.list(
            id="id",
            after="after",
            before="before",
            currency_ids=["string"],
            entity_id_search="x",
            entity_type_ids=["string"],
            feature_ids=["string"],
            limit=1,
            min_utilization=0,
            order="asc",
            scope="all",
            sort_by="utilization",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(AsyncMyCursorIDPage[GovernanceListResponse], governance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1_beta.customers.governance.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        governance = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[GovernanceListResponse], governance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1_beta.customers.governance.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            governance = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[GovernanceListResponse], governance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1_beta.customers.governance.with_raw_response.list(
                id="",
            )
