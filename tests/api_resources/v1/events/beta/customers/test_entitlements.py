# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1.events.beta.customers import EntitlementCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntitlements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check(self, client: Stigg) -> None:
        entitlement = client.v1.events.beta.customers.entitlements.check(
            id="x",
        )
        assert_matches_type(EntitlementCheckResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_with_all_params(self, client: Stigg) -> None:
        entitlement = client.v1.events.beta.customers.entitlements.check(
            id="x",
            currency_id="x",
            dimensions={"foo": "string"},
            feature_id="x",
            requested_usage=0,
            requested_values=["string"],
            resource_id="x",
        )
        assert_matches_type(EntitlementCheckResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check(self, client: Stigg) -> None:
        response = client.v1.events.beta.customers.entitlements.with_raw_response.check(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = response.parse()
        assert_matches_type(EntitlementCheckResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check(self, client: Stigg) -> None:
        with client.v1.events.beta.customers.entitlements.with_streaming_response.check(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = response.parse()
            assert_matches_type(EntitlementCheckResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_check(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.beta.customers.entitlements.with_raw_response.check(
                id="",
            )


class TestAsyncEntitlements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check(self, async_client: AsyncStigg) -> None:
        entitlement = await async_client.v1.events.beta.customers.entitlements.check(
            id="x",
        )
        assert_matches_type(EntitlementCheckResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_with_all_params(self, async_client: AsyncStigg) -> None:
        entitlement = await async_client.v1.events.beta.customers.entitlements.check(
            id="x",
            currency_id="x",
            dimensions={"foo": "string"},
            feature_id="x",
            requested_usage=0,
            requested_values=["string"],
            resource_id="x",
        )
        assert_matches_type(EntitlementCheckResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.beta.customers.entitlements.with_raw_response.check(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = await response.parse()
        assert_matches_type(EntitlementCheckResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.beta.customers.entitlements.with_streaming_response.check(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = await response.parse()
            assert_matches_type(EntitlementCheckResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_check(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.beta.customers.entitlements.with_raw_response.check(
                id="",
            )
