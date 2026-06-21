# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1.events import (
    DataExportListModelsResponse,
    DataExportTriggerSyncResponse,
    DataExportMintScopedTokenResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataExport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_models(self, client: Stigg) -> None:
        data_export = client.v1.events.data_export.list_models()
        assert_matches_type(DataExportListModelsResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_models_with_all_params(self, client: Stigg) -> None:
        data_export = client.v1.events.data_export.list_models(
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(DataExportListModelsResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_models(self, client: Stigg) -> None:
        response = client.v1.events.data_export.with_raw_response.list_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = response.parse()
        assert_matches_type(DataExportListModelsResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_models(self, client: Stigg) -> None:
        with client.v1.events.data_export.with_streaming_response.list_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = response.parse()
            assert_matches_type(DataExportListModelsResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mint_scoped_token(self, client: Stigg) -> None:
        data_export = client.v1.events.data_export.mint_scoped_token(
            application_origin="x",
        )
        assert_matches_type(DataExportMintScopedTokenResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mint_scoped_token_with_all_params(self, client: Stigg) -> None:
        data_export = client.v1.events.data_export.mint_scoped_token(
            application_origin="x",
            destination_type="destinationType",
            enabled_models=["x"],
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(DataExportMintScopedTokenResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mint_scoped_token(self, client: Stigg) -> None:
        response = client.v1.events.data_export.with_raw_response.mint_scoped_token(
            application_origin="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = response.parse()
        assert_matches_type(DataExportMintScopedTokenResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mint_scoped_token(self, client: Stigg) -> None:
        with client.v1.events.data_export.with_streaming_response.mint_scoped_token(
            application_origin="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = response.parse()
            assert_matches_type(DataExportMintScopedTokenResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_sync(self, client: Stigg) -> None:
        data_export = client.v1.events.data_export.trigger_sync()
        assert_matches_type(DataExportTriggerSyncResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_sync_with_all_params(self, client: Stigg) -> None:
        data_export = client.v1.events.data_export.trigger_sync(
            destination_id="destinationId",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(DataExportTriggerSyncResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_trigger_sync(self, client: Stigg) -> None:
        response = client.v1.events.data_export.with_raw_response.trigger_sync()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = response.parse()
        assert_matches_type(DataExportTriggerSyncResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_trigger_sync(self, client: Stigg) -> None:
        with client.v1.events.data_export.with_streaming_response.trigger_sync() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = response.parse()
            assert_matches_type(DataExportTriggerSyncResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDataExport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_models(self, async_client: AsyncStigg) -> None:
        data_export = await async_client.v1.events.data_export.list_models()
        assert_matches_type(DataExportListModelsResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_models_with_all_params(self, async_client: AsyncStigg) -> None:
        data_export = await async_client.v1.events.data_export.list_models(
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(DataExportListModelsResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_models(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.data_export.with_raw_response.list_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = await response.parse()
        assert_matches_type(DataExportListModelsResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_models(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.data_export.with_streaming_response.list_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = await response.parse()
            assert_matches_type(DataExportListModelsResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mint_scoped_token(self, async_client: AsyncStigg) -> None:
        data_export = await async_client.v1.events.data_export.mint_scoped_token(
            application_origin="x",
        )
        assert_matches_type(DataExportMintScopedTokenResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mint_scoped_token_with_all_params(self, async_client: AsyncStigg) -> None:
        data_export = await async_client.v1.events.data_export.mint_scoped_token(
            application_origin="x",
            destination_type="destinationType",
            enabled_models=["x"],
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(DataExportMintScopedTokenResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mint_scoped_token(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.data_export.with_raw_response.mint_scoped_token(
            application_origin="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = await response.parse()
        assert_matches_type(DataExportMintScopedTokenResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mint_scoped_token(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.data_export.with_streaming_response.mint_scoped_token(
            application_origin="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = await response.parse()
            assert_matches_type(DataExportMintScopedTokenResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_sync(self, async_client: AsyncStigg) -> None:
        data_export = await async_client.v1.events.data_export.trigger_sync()
        assert_matches_type(DataExportTriggerSyncResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_sync_with_all_params(self, async_client: AsyncStigg) -> None:
        data_export = await async_client.v1.events.data_export.trigger_sync(
            destination_id="destinationId",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(DataExportTriggerSyncResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_trigger_sync(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.data_export.with_raw_response.trigger_sync()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = await response.parse()
        assert_matches_type(DataExportTriggerSyncResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_trigger_sync(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.data_export.with_streaming_response.trigger_sync() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = await response.parse()
            assert_matches_type(DataExportTriggerSyncResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True
