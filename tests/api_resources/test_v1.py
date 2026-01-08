# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from stigg.types import V1CreateEventResponse, V1CreateUsageResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_event(self, client: Stigg) -> None:
        v1 = client.v1.create_event(
            events=[
                {
                    "customer_id": "customerId",
                    "event_name": "x",
                    "idempotency_key": "x",
                }
            ],
        )
        assert_matches_type(V1CreateEventResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_event(self, client: Stigg) -> None:
        response = client.v1.with_raw_response.create_event(
            events=[
                {
                    "customer_id": "customerId",
                    "event_name": "x",
                    "idempotency_key": "x",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1CreateEventResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_event(self, client: Stigg) -> None:
        with client.v1.with_streaming_response.create_event(
            events=[
                {
                    "customer_id": "customerId",
                    "event_name": "x",
                    "idempotency_key": "x",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1CreateEventResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_usage(self, client: Stigg) -> None:
        v1 = client.v1.create_usage(
            usages=[
                {
                    "customer_id": "customerId",
                    "feature_id": "featureId",
                    "value": -9007199254740991,
                }
            ],
        )
        assert_matches_type(V1CreateUsageResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_usage(self, client: Stigg) -> None:
        response = client.v1.with_raw_response.create_usage(
            usages=[
                {
                    "customer_id": "customerId",
                    "feature_id": "featureId",
                    "value": -9007199254740991,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1CreateUsageResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_usage(self, client: Stigg) -> None:
        with client.v1.with_streaming_response.create_usage(
            usages=[
                {
                    "customer_id": "customerId",
                    "feature_id": "featureId",
                    "value": -9007199254740991,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1CreateUsageResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_event(self, async_client: AsyncStigg) -> None:
        v1 = await async_client.v1.create_event(
            events=[
                {
                    "customer_id": "customerId",
                    "event_name": "x",
                    "idempotency_key": "x",
                }
            ],
        )
        assert_matches_type(V1CreateEventResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_event(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.with_raw_response.create_event(
            events=[
                {
                    "customer_id": "customerId",
                    "event_name": "x",
                    "idempotency_key": "x",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1CreateEventResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_event(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.with_streaming_response.create_event(
            events=[
                {
                    "customer_id": "customerId",
                    "event_name": "x",
                    "idempotency_key": "x",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1CreateEventResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_usage(self, async_client: AsyncStigg) -> None:
        v1 = await async_client.v1.create_usage(
            usages=[
                {
                    "customer_id": "customerId",
                    "feature_id": "featureId",
                    "value": -9007199254740991,
                }
            ],
        )
        assert_matches_type(V1CreateUsageResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_usage(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.with_raw_response.create_usage(
            usages=[
                {
                    "customer_id": "customerId",
                    "feature_id": "featureId",
                    "value": -9007199254740991,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1CreateUsageResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_usage(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.with_streaming_response.create_usage(
            usages=[
                {
                    "customer_id": "customerId",
                    "feature_id": "featureId",
                    "value": -9007199254740991,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1CreateUsageResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
