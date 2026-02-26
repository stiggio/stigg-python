# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1.events.addons import (
    AddonPackageEntitlement,
    EntitlementListResponse,
    EntitlementCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntitlements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Stigg) -> None:
        entitlement = client.v1.events.addons.entitlements.create(
            addon_id="addonId",
            entitlements=[{}],
        )
        assert_matches_type(EntitlementCreateResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stigg) -> None:
        response = client.v1.events.addons.entitlements.with_raw_response.create(
            addon_id="addonId",
            entitlements=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = response.parse()
        assert_matches_type(EntitlementCreateResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stigg) -> None:
        with client.v1.events.addons.entitlements.with_streaming_response.create(
            addon_id="addonId",
            entitlements=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = response.parse()
            assert_matches_type(EntitlementCreateResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addon_id` but received ''"):
            client.v1.events.addons.entitlements.with_raw_response.create(
                addon_id="",
                entitlements=[{}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Stigg) -> None:
        entitlement = client.v1.events.addons.entitlements.update(
            id="id",
            addon_id="addonId",
        )
        assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Stigg) -> None:
        entitlement = client.v1.events.addons.entitlements.update(
            id="id",
            addon_id="addonId",
            credit={
                "amount": 1,
                "behavior": "Increment",
                "cadence": "MONTH",
                "description": "description",
                "display_name_override": "displayNameOverride",
                "hidden_from_widgets": ["PAYWALL"],
                "is_custom": True,
                "is_granted": True,
                "order": 0,
            },
            feature={
                "behavior": "Increment",
                "description": "description",
                "display_name_override": "displayNameOverride",
                "enum_values": ["string"],
                "has_soft_limit": True,
                "has_unlimited_usage": True,
                "hidden_from_widgets": ["PAYWALL"],
                "is_custom": True,
                "is_granted": True,
                "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                "order": 0,
                "reset_period": "YEAR",
                "usage_limit": 0,
                "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
            },
        )
        assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Stigg) -> None:
        response = client.v1.events.addons.entitlements.with_raw_response.update(
            id="id",
            addon_id="addonId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = response.parse()
        assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Stigg) -> None:
        with client.v1.events.addons.entitlements.with_streaming_response.update(
            id="id",
            addon_id="addonId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = response.parse()
            assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addon_id` but received ''"):
            client.v1.events.addons.entitlements.with_raw_response.update(
                id="id",
                addon_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.addons.entitlements.with_raw_response.update(
                id="",
                addon_id="addonId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        entitlement = client.v1.events.addons.entitlements.list(
            "addonId",
        )
        assert_matches_type(EntitlementListResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1.events.addons.entitlements.with_raw_response.list(
            "addonId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = response.parse()
        assert_matches_type(EntitlementListResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1.events.addons.entitlements.with_streaming_response.list(
            "addonId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = response.parse()
            assert_matches_type(EntitlementListResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addon_id` but received ''"):
            client.v1.events.addons.entitlements.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Stigg) -> None:
        entitlement = client.v1.events.addons.entitlements.delete(
            id="id",
            addon_id="addonId",
        )
        assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Stigg) -> None:
        response = client.v1.events.addons.entitlements.with_raw_response.delete(
            id="id",
            addon_id="addonId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = response.parse()
        assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Stigg) -> None:
        with client.v1.events.addons.entitlements.with_streaming_response.delete(
            id="id",
            addon_id="addonId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = response.parse()
            assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addon_id` but received ''"):
            client.v1.events.addons.entitlements.with_raw_response.delete(
                id="id",
                addon_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.addons.entitlements.with_raw_response.delete(
                id="",
                addon_id="addonId",
            )


class TestAsyncEntitlements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStigg) -> None:
        entitlement = await async_client.v1.events.addons.entitlements.create(
            addon_id="addonId",
            entitlements=[{}],
        )
        assert_matches_type(EntitlementCreateResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.addons.entitlements.with_raw_response.create(
            addon_id="addonId",
            entitlements=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = await response.parse()
        assert_matches_type(EntitlementCreateResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.addons.entitlements.with_streaming_response.create(
            addon_id="addonId",
            entitlements=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = await response.parse()
            assert_matches_type(EntitlementCreateResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addon_id` but received ''"):
            await async_client.v1.events.addons.entitlements.with_raw_response.create(
                addon_id="",
                entitlements=[{}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncStigg) -> None:
        entitlement = await async_client.v1.events.addons.entitlements.update(
            id="id",
            addon_id="addonId",
        )
        assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStigg) -> None:
        entitlement = await async_client.v1.events.addons.entitlements.update(
            id="id",
            addon_id="addonId",
            credit={
                "amount": 1,
                "behavior": "Increment",
                "cadence": "MONTH",
                "description": "description",
                "display_name_override": "displayNameOverride",
                "hidden_from_widgets": ["PAYWALL"],
                "is_custom": True,
                "is_granted": True,
                "order": 0,
            },
            feature={
                "behavior": "Increment",
                "description": "description",
                "display_name_override": "displayNameOverride",
                "enum_values": ["string"],
                "has_soft_limit": True,
                "has_unlimited_usage": True,
                "hidden_from_widgets": ["PAYWALL"],
                "is_custom": True,
                "is_granted": True,
                "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                "order": 0,
                "reset_period": "YEAR",
                "usage_limit": 0,
                "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
            },
        )
        assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.addons.entitlements.with_raw_response.update(
            id="id",
            addon_id="addonId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = await response.parse()
        assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.addons.entitlements.with_streaming_response.update(
            id="id",
            addon_id="addonId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = await response.parse()
            assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addon_id` but received ''"):
            await async_client.v1.events.addons.entitlements.with_raw_response.update(
                id="id",
                addon_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.addons.entitlements.with_raw_response.update(
                id="",
                addon_id="addonId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        entitlement = await async_client.v1.events.addons.entitlements.list(
            "addonId",
        )
        assert_matches_type(EntitlementListResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.addons.entitlements.with_raw_response.list(
            "addonId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = await response.parse()
        assert_matches_type(EntitlementListResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.addons.entitlements.with_streaming_response.list(
            "addonId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = await response.parse()
            assert_matches_type(EntitlementListResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addon_id` but received ''"):
            await async_client.v1.events.addons.entitlements.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncStigg) -> None:
        entitlement = await async_client.v1.events.addons.entitlements.delete(
            id="id",
            addon_id="addonId",
        )
        assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.addons.entitlements.with_raw_response.delete(
            id="id",
            addon_id="addonId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = await response.parse()
        assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.addons.entitlements.with_streaming_response.delete(
            id="id",
            addon_id="addonId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = await response.parse()
            assert_matches_type(AddonPackageEntitlement, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addon_id` but received ''"):
            await async_client.v1.events.addons.entitlements.with_raw_response.delete(
                id="id",
                addon_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.addons.entitlements.with_raw_response.delete(
                id="",
                addon_id="addonId",
            )
