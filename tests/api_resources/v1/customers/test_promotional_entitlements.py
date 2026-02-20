# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from stigg.types.v1.customers import (
    PromotionalEntitlementListResponse,
    PromotionalEntitlementCreateResponse,
    PromotionalEntitlementRevokeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPromotionalEntitlements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Stigg) -> None:
        promotional_entitlement = client.v1.customers.promotional_entitlements.create(
            id="x",
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
        assert_matches_type(PromotionalEntitlementCreateResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stigg) -> None:
        response = client.v1.customers.promotional_entitlements.with_raw_response.create(
            id="x",
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
        assert_matches_type(PromotionalEntitlementCreateResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stigg) -> None:
        with client.v1.customers.promotional_entitlements.with_streaming_response.create(
            id="x",
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
            assert_matches_type(PromotionalEntitlementCreateResponse, promotional_entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.customers.promotional_entitlements.with_raw_response.create(
                id="",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        promotional_entitlement = client.v1.customers.promotional_entitlements.list(
            id="x",
        )
        assert_matches_type(
            SyncMyCursorIDPage[PromotionalEntitlementListResponse], promotional_entitlement, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        promotional_entitlement = client.v1.customers.promotional_entitlements.list(
            id="x",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            limit=1,
            status="status",
        )
        assert_matches_type(
            SyncMyCursorIDPage[PromotionalEntitlementListResponse], promotional_entitlement, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1.customers.promotional_entitlements.with_raw_response.list(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotional_entitlement = response.parse()
        assert_matches_type(
            SyncMyCursorIDPage[PromotionalEntitlementListResponse], promotional_entitlement, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1.customers.promotional_entitlements.with_streaming_response.list(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotional_entitlement = response.parse()
            assert_matches_type(
                SyncMyCursorIDPage[PromotionalEntitlementListResponse], promotional_entitlement, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.customers.promotional_entitlements.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke(self, client: Stigg) -> None:
        promotional_entitlement = client.v1.customers.promotional_entitlements.revoke(
            feature_id="featureId",
            id="id",
        )
        assert_matches_type(PromotionalEntitlementRevokeResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: Stigg) -> None:
        response = client.v1.customers.promotional_entitlements.with_raw_response.revoke(
            feature_id="featureId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotional_entitlement = response.parse()
        assert_matches_type(PromotionalEntitlementRevokeResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: Stigg) -> None:
        with client.v1.customers.promotional_entitlements.with_streaming_response.revoke(
            feature_id="featureId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotional_entitlement = response.parse()
            assert_matches_type(PromotionalEntitlementRevokeResponse, promotional_entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_revoke(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.customers.promotional_entitlements.with_raw_response.revoke(
                feature_id="featureId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            client.v1.customers.promotional_entitlements.with_raw_response.revoke(
                feature_id="",
                id="id",
            )


class TestAsyncPromotionalEntitlements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStigg) -> None:
        promotional_entitlement = await async_client.v1.customers.promotional_entitlements.create(
            id="x",
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
        assert_matches_type(PromotionalEntitlementCreateResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.promotional_entitlements.with_raw_response.create(
            id="x",
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
        assert_matches_type(PromotionalEntitlementCreateResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.promotional_entitlements.with_streaming_response.create(
            id="x",
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
            assert_matches_type(PromotionalEntitlementCreateResponse, promotional_entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.customers.promotional_entitlements.with_raw_response.create(
                id="",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        promotional_entitlement = await async_client.v1.customers.promotional_entitlements.list(
            id="x",
        )
        assert_matches_type(
            AsyncMyCursorIDPage[PromotionalEntitlementListResponse], promotional_entitlement, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        promotional_entitlement = await async_client.v1.customers.promotional_entitlements.list(
            id="x",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            limit=1,
            status="status",
        )
        assert_matches_type(
            AsyncMyCursorIDPage[PromotionalEntitlementListResponse], promotional_entitlement, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.promotional_entitlements.with_raw_response.list(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotional_entitlement = await response.parse()
        assert_matches_type(
            AsyncMyCursorIDPage[PromotionalEntitlementListResponse], promotional_entitlement, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.promotional_entitlements.with_streaming_response.list(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotional_entitlement = await response.parse()
            assert_matches_type(
                AsyncMyCursorIDPage[PromotionalEntitlementListResponse], promotional_entitlement, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.customers.promotional_entitlements.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncStigg) -> None:
        promotional_entitlement = await async_client.v1.customers.promotional_entitlements.revoke(
            feature_id="featureId",
            id="id",
        )
        assert_matches_type(PromotionalEntitlementRevokeResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.promotional_entitlements.with_raw_response.revoke(
            feature_id="featureId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotional_entitlement = await response.parse()
        assert_matches_type(PromotionalEntitlementRevokeResponse, promotional_entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.promotional_entitlements.with_streaming_response.revoke(
            feature_id="featureId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotional_entitlement = await response.parse()
            assert_matches_type(PromotionalEntitlementRevokeResponse, promotional_entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.customers.promotional_entitlements.with_raw_response.revoke(
                feature_id="featureId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            await async_client.v1.customers.promotional_entitlements.with_raw_response.revoke(
                feature_id="",
                id="id",
            )
