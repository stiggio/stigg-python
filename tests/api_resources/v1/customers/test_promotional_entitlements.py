# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.types.v1.customers import (
    PromotionalEntitlementGrantResponse,
    PromotionalEntitlementRevokeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPromotionalEntitlements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_grant(self, client: Stigg) -> None:
        promotional_entitlement = client.v1.customers.promotional_entitlements.grant(
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
        assert_matches_type(PromotionalEntitlementGrantResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_grant(self, client: Stigg) -> None:
        response = client.v1.customers.promotional_entitlements.with_raw_response.grant(
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
        promotional_entitlement = response.parse()
        assert_matches_type(PromotionalEntitlementGrantResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_grant(self, client: Stigg) -> None:
        with client.v1.customers.promotional_entitlements.with_streaming_response.grant(
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

            promotional_entitlement = response.parse()
            assert_matches_type(PromotionalEntitlementGrantResponse, promotional_entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_grant(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.promotional_entitlements.with_raw_response.grant(
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
        promotional_entitlement = client.v1.customers.promotional_entitlements.revoke(
            feature_id="featureId",
            customer_id="customerId",
        )
        assert_matches_type(PromotionalEntitlementRevokeResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: Stigg) -> None:
        response = client.v1.customers.promotional_entitlements.with_raw_response.revoke(
            feature_id="featureId",
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotional_entitlement = response.parse()
        assert_matches_type(PromotionalEntitlementRevokeResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: Stigg) -> None:
        with client.v1.customers.promotional_entitlements.with_streaming_response.revoke(
            feature_id="featureId",
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotional_entitlement = response.parse()
            assert_matches_type(PromotionalEntitlementRevokeResponse, promotional_entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_revoke(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.promotional_entitlements.with_raw_response.revoke(
                feature_id="featureId",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            client.v1.customers.promotional_entitlements.with_raw_response.revoke(
                feature_id="",
                customer_id="customerId",
            )


class TestAsyncPromotionalEntitlements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_grant(self, async_client: AsyncStigg) -> None:
        promotional_entitlement = await async_client.v1.customers.promotional_entitlements.grant(
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
        assert_matches_type(PromotionalEntitlementGrantResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_grant(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.promotional_entitlements.with_raw_response.grant(
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
        promotional_entitlement = await response.parse()
        assert_matches_type(PromotionalEntitlementGrantResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_grant(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.promotional_entitlements.with_streaming_response.grant(
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

            promotional_entitlement = await response.parse()
            assert_matches_type(PromotionalEntitlementGrantResponse, promotional_entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_grant(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.promotional_entitlements.with_raw_response.grant(
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
        promotional_entitlement = await async_client.v1.customers.promotional_entitlements.revoke(
            feature_id="featureId",
            customer_id="customerId",
        )
        assert_matches_type(PromotionalEntitlementRevokeResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.promotional_entitlements.with_raw_response.revoke(
            feature_id="featureId",
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotional_entitlement = await response.parse()
        assert_matches_type(PromotionalEntitlementRevokeResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.promotional_entitlements.with_streaming_response.revoke(
            feature_id="featureId",
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotional_entitlement = await response.parse()
            assert_matches_type(PromotionalEntitlementRevokeResponse, promotional_entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.promotional_entitlements.with_raw_response.revoke(
                feature_id="featureId",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            await async_client.v1.customers.promotional_entitlements.with_raw_response.revoke(
                feature_id="",
                customer_id="customerId",
            )
