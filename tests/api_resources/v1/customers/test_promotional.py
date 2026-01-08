# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.types.v1.customers import PromotionalCreateResponse, PromotionalRevokeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPromotional:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Stigg) -> None:
        promotional = client.v1.customers.promotional.create(
            customer_id="customerId",
            promotional_entitlements=[
                {
                    "custom_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "enum_values": ["string"],
                    "feature_id": "featureId",
                    "has_soft_limit": True,
                    "has_unlimited_usage": True,
                    "is_visible": True,
                    "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "period": "1 week",
                    "reset_period": "YEAR",
                    "usage_limit": -9007199254740991,
                    "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                }
            ],
        )
        assert_matches_type(PromotionalCreateResponse, promotional, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stigg) -> None:
        response = client.v1.customers.promotional.with_raw_response.create(
            customer_id="customerId",
            promotional_entitlements=[
                {
                    "custom_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "enum_values": ["string"],
                    "feature_id": "featureId",
                    "has_soft_limit": True,
                    "has_unlimited_usage": True,
                    "is_visible": True,
                    "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "period": "1 week",
                    "reset_period": "YEAR",
                    "usage_limit": -9007199254740991,
                    "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotional = response.parse()
        assert_matches_type(PromotionalCreateResponse, promotional, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stigg) -> None:
        with client.v1.customers.promotional.with_streaming_response.create(
            customer_id="customerId",
            promotional_entitlements=[
                {
                    "custom_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "enum_values": ["string"],
                    "feature_id": "featureId",
                    "has_soft_limit": True,
                    "has_unlimited_usage": True,
                    "is_visible": True,
                    "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "period": "1 week",
                    "reset_period": "YEAR",
                    "usage_limit": -9007199254740991,
                    "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotional = response.parse()
            assert_matches_type(PromotionalCreateResponse, promotional, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.promotional.with_raw_response.create(
                customer_id="",
                promotional_entitlements=[
                    {
                        "custom_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "enum_values": ["string"],
                        "feature_id": "featureId",
                        "has_soft_limit": True,
                        "has_unlimited_usage": True,
                        "is_visible": True,
                        "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                        "period": "1 week",
                        "reset_period": "YEAR",
                        "usage_limit": -9007199254740991,
                        "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                        "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_revoke(self, client: Stigg) -> None:
        promotional = client.v1.customers.promotional.revoke(
            feature_id="featureId",
            customer_id="customerId",
        )
        assert_matches_type(PromotionalRevokeResponse, promotional, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: Stigg) -> None:
        response = client.v1.customers.promotional.with_raw_response.revoke(
            feature_id="featureId",
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotional = response.parse()
        assert_matches_type(PromotionalRevokeResponse, promotional, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: Stigg) -> None:
        with client.v1.customers.promotional.with_streaming_response.revoke(
            feature_id="featureId",
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotional = response.parse()
            assert_matches_type(PromotionalRevokeResponse, promotional, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_revoke(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.promotional.with_raw_response.revoke(
                feature_id="featureId",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            client.v1.customers.promotional.with_raw_response.revoke(
                feature_id="",
                customer_id="customerId",
            )


class TestAsyncPromotional:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStigg) -> None:
        promotional = await async_client.v1.customers.promotional.create(
            customer_id="customerId",
            promotional_entitlements=[
                {
                    "custom_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "enum_values": ["string"],
                    "feature_id": "featureId",
                    "has_soft_limit": True,
                    "has_unlimited_usage": True,
                    "is_visible": True,
                    "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "period": "1 week",
                    "reset_period": "YEAR",
                    "usage_limit": -9007199254740991,
                    "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                }
            ],
        )
        assert_matches_type(PromotionalCreateResponse, promotional, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.promotional.with_raw_response.create(
            customer_id="customerId",
            promotional_entitlements=[
                {
                    "custom_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "enum_values": ["string"],
                    "feature_id": "featureId",
                    "has_soft_limit": True,
                    "has_unlimited_usage": True,
                    "is_visible": True,
                    "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "period": "1 week",
                    "reset_period": "YEAR",
                    "usage_limit": -9007199254740991,
                    "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotional = await response.parse()
        assert_matches_type(PromotionalCreateResponse, promotional, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.promotional.with_streaming_response.create(
            customer_id="customerId",
            promotional_entitlements=[
                {
                    "custom_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "enum_values": ["string"],
                    "feature_id": "featureId",
                    "has_soft_limit": True,
                    "has_unlimited_usage": True,
                    "is_visible": True,
                    "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "period": "1 week",
                    "reset_period": "YEAR",
                    "usage_limit": -9007199254740991,
                    "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotional = await response.parse()
            assert_matches_type(PromotionalCreateResponse, promotional, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.promotional.with_raw_response.create(
                customer_id="",
                promotional_entitlements=[
                    {
                        "custom_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "enum_values": ["string"],
                        "feature_id": "featureId",
                        "has_soft_limit": True,
                        "has_unlimited_usage": True,
                        "is_visible": True,
                        "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                        "period": "1 week",
                        "reset_period": "YEAR",
                        "usage_limit": -9007199254740991,
                        "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                        "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncStigg) -> None:
        promotional = await async_client.v1.customers.promotional.revoke(
            feature_id="featureId",
            customer_id="customerId",
        )
        assert_matches_type(PromotionalRevokeResponse, promotional, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.promotional.with_raw_response.revoke(
            feature_id="featureId",
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotional = await response.parse()
        assert_matches_type(PromotionalRevokeResponse, promotional, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.promotional.with_streaming_response.revoke(
            feature_id="featureId",
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotional = await response.parse()
            assert_matches_type(PromotionalRevokeResponse, promotional, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.promotional.with_raw_response.revoke(
                feature_id="featureId",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            await async_client.v1.customers.promotional.with_raw_response.revoke(
                feature_id="",
                customer_id="customerId",
            )
