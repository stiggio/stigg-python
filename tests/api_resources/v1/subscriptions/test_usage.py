# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.types.v1.subscriptions import UsageSyncUsageResponse, UsageChargeUsageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_charge_usage(self, client: Stigg) -> None:
        usage = client.v1.subscriptions.usage.charge_usage(
            id="x",
        )
        assert_matches_type(UsageChargeUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_charge_usage_with_all_params(self, client: Stigg) -> None:
        usage = client.v1.subscriptions.usage.charge_usage(
            id="x",
            until_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(UsageChargeUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_charge_usage(self, client: Stigg) -> None:
        response = client.v1.subscriptions.usage.with_raw_response.charge_usage(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageChargeUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_charge_usage(self, client: Stigg) -> None:
        with client.v1.subscriptions.usage.with_streaming_response.charge_usage(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageChargeUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_charge_usage(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.usage.with_raw_response.charge_usage(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_sync_usage(self, client: Stigg) -> None:
        usage = client.v1.subscriptions.usage.sync_usage(
            "x",
        )
        assert_matches_type(UsageSyncUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_sync_usage(self, client: Stigg) -> None:
        response = client.v1.subscriptions.usage.with_raw_response.sync_usage(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageSyncUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_sync_usage(self, client: Stigg) -> None:
        with client.v1.subscriptions.usage.with_streaming_response.sync_usage(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageSyncUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_sync_usage(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.usage.with_raw_response.sync_usage(
                "",
            )


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_charge_usage(self, async_client: AsyncStigg) -> None:
        usage = await async_client.v1.subscriptions.usage.charge_usage(
            id="x",
        )
        assert_matches_type(UsageChargeUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_charge_usage_with_all_params(self, async_client: AsyncStigg) -> None:
        usage = await async_client.v1.subscriptions.usage.charge_usage(
            id="x",
            until_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(UsageChargeUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_charge_usage(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.usage.with_raw_response.charge_usage(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageChargeUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_charge_usage(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.usage.with_streaming_response.charge_usage(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageChargeUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_charge_usage(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.usage.with_raw_response.charge_usage(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_sync_usage(self, async_client: AsyncStigg) -> None:
        usage = await async_client.v1.subscriptions.usage.sync_usage(
            "x",
        )
        assert_matches_type(UsageSyncUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_sync_usage(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.usage.with_raw_response.sync_usage(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageSyncUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_sync_usage(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.usage.with_streaming_response.sync_usage(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageSyncUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_sync_usage(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.usage.with_raw_response.sync_usage(
                "",
            )
