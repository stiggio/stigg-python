# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.types.v1 import UsageReportResponse, UsageHistoryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_history(self, client: Stigg) -> None:
        usage = client.v1.usage.history(
            feature_id="featureId",
            customer_id="customerId",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(UsageHistoryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_history_with_all_params(self, client: Stigg) -> None:
        usage = client.v1.usage.history(
            feature_id="featureId",
            customer_id="customerId",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            group_by="groupBy",
            resource_id="resourceId",
        )
        assert_matches_type(UsageHistoryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_history(self, client: Stigg) -> None:
        response = client.v1.usage.with_raw_response.history(
            feature_id="featureId",
            customer_id="customerId",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageHistoryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_history(self, client: Stigg) -> None:
        with client.v1.usage.with_streaming_response.history(
            feature_id="featureId",
            customer_id="customerId",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageHistoryResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_history(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.usage.with_raw_response.history(
                feature_id="featureId",
                customer_id="",
                start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            client.v1.usage.with_raw_response.history(
                feature_id="",
                customer_id="customerId",
                start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report(self, client: Stigg) -> None:
        usage = client.v1.usage.report(
            usages=[
                {
                    "customer_id": "customerId",
                    "feature_id": "featureId",
                    "value": -9007199254740991,
                }
            ],
        )
        assert_matches_type(UsageReportResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_report(self, client: Stigg) -> None:
        response = client.v1.usage.with_raw_response.report(
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
        usage = response.parse()
        assert_matches_type(UsageReportResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_report(self, client: Stigg) -> None:
        with client.v1.usage.with_streaming_response.report(
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

            usage = response.parse()
            assert_matches_type(UsageReportResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_history(self, async_client: AsyncStigg) -> None:
        usage = await async_client.v1.usage.history(
            feature_id="featureId",
            customer_id="customerId",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(UsageHistoryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncStigg) -> None:
        usage = await async_client.v1.usage.history(
            feature_id="featureId",
            customer_id="customerId",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            group_by="groupBy",
            resource_id="resourceId",
        )
        assert_matches_type(UsageHistoryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_history(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.usage.with_raw_response.history(
            feature_id="featureId",
            customer_id="customerId",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageHistoryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.usage.with_streaming_response.history(
            feature_id="featureId",
            customer_id="customerId",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageHistoryResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_history(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.usage.with_raw_response.history(
                feature_id="featureId",
                customer_id="",
                start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            await async_client.v1.usage.with_raw_response.history(
                feature_id="",
                customer_id="customerId",
                start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report(self, async_client: AsyncStigg) -> None:
        usage = await async_client.v1.usage.report(
            usages=[
                {
                    "customer_id": "customerId",
                    "feature_id": "featureId",
                    "value": -9007199254740991,
                }
            ],
        )
        assert_matches_type(UsageReportResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_report(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.usage.with_raw_response.report(
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
        usage = await response.parse()
        assert_matches_type(UsageReportResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_report(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.usage.with_streaming_response.report(
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

            usage = await response.parse()
            assert_matches_type(UsageReportResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True
