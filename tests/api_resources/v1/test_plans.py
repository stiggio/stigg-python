# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.types.v1 import (
    Plan,
    PlanListResponse,
    PlanPublishResponse,
    PlanRemoveDraftResponse,
    SetPackagePricingResponse,
)
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Stigg) -> None:
        plan = client.v1.plans.create(
            id="id",
            display_name="displayName",
            product_id="productId",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Stigg) -> None:
        plan = client.v1.plans.create(
            id="id",
            display_name="displayName",
            product_id="productId",
            billing_id="billingId",
            default_trial_config={
                "duration": 0,
                "units": "DAY",
                "budget": {
                    "has_soft_limit": True,
                    "limit": 0,
                },
                "trial_end_behavior": "CONVERT_TO_PAID",
            },
            description="description",
            metadata={"foo": "string"},
            parent_plan_id="parentPlanId",
            pricing_type="FREE",
            status="DRAFT",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stigg) -> None:
        response = client.v1.plans.with_raw_response.create(
            id="id",
            display_name="displayName",
            product_id="productId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stigg) -> None:
        with client.v1.plans.with_streaming_response.create(
            id="id",
            display_name="displayName",
            product_id="productId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Stigg) -> None:
        plan = client.v1.plans.retrieve(
            "x",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Stigg) -> None:
        response = client.v1.plans.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Stigg) -> None:
        with client.v1.plans.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.plans.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Stigg) -> None:
        plan = client.v1.plans.update(
            id="x",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Stigg) -> None:
        plan = client.v1.plans.update(
            id="x",
            billing_id="billingId",
            compatible_addon_ids=["string"],
            default_trial_config={
                "duration": 0,
                "units": "DAY",
                "budget": {
                    "has_soft_limit": True,
                    "limit": 0,
                },
                "trial_end_behavior": "CONVERT_TO_PAID",
            },
            description="description",
            display_name="displayName",
            metadata={"foo": "string"},
            parent_plan_id="parentPlanId",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Stigg) -> None:
        response = client.v1.plans.with_raw_response.update(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Stigg) -> None:
        with client.v1.plans.with_streaming_response.update(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.plans.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        plan = client.v1.plans.list()
        assert_matches_type(SyncMyCursorIDPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        plan = client.v1.plans.list(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            limit=1,
            product_id="productId",
            status="status",
        )
        assert_matches_type(SyncMyCursorIDPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SyncMyCursorIDPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SyncMyCursorIDPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Stigg) -> None:
        plan = client.v1.plans.archive(
            "x",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Stigg) -> None:
        response = client.v1.plans.with_raw_response.archive(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Stigg) -> None:
        with client.v1.plans.with_streaming_response.archive(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.plans.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_draft(self, client: Stigg) -> None:
        plan = client.v1.plans.create_draft(
            "x",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_draft(self, client: Stigg) -> None:
        response = client.v1.plans.with_raw_response.create_draft(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_draft(self, client: Stigg) -> None:
        with client.v1.plans.with_streaming_response.create_draft(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_draft(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.plans.with_raw_response.create_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish(self, client: Stigg) -> None:
        plan = client.v1.plans.publish(
            id="x",
            migration_type="NEW_CUSTOMERS",
        )
        assert_matches_type(PlanPublishResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_publish(self, client: Stigg) -> None:
        response = client.v1.plans.with_raw_response.publish(
            id="x",
            migration_type="NEW_CUSTOMERS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanPublishResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_publish(self, client: Stigg) -> None:
        with client.v1.plans.with_streaming_response.publish(
            id="x",
            migration_type="NEW_CUSTOMERS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanPublishResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_publish(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.plans.with_raw_response.publish(
                id="",
                migration_type="NEW_CUSTOMERS",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_draft(self, client: Stigg) -> None:
        plan = client.v1.plans.remove_draft(
            "x",
        )
        assert_matches_type(PlanRemoveDraftResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_draft(self, client: Stigg) -> None:
        response = client.v1.plans.with_raw_response.remove_draft(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanRemoveDraftResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_draft(self, client: Stigg) -> None:
        with client.v1.plans.with_streaming_response.remove_draft(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanRemoveDraftResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_draft(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.plans.with_raw_response.remove_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_pricing(self, client: Stigg) -> None:
        plan = client.v1.plans.set_pricing(
            id="x",
            pricing_type="FREE",
        )
        assert_matches_type(SetPackagePricingResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_pricing_with_all_params(self, client: Stigg) -> None:
        plan = client.v1.plans.set_pricing(
            id="x",
            pricing_type="FREE",
            billing_id="billingId",
            minimum_spend=[
                {
                    "billing_period": "MONTHLY",
                    "minimum": {
                        "amount": 0,
                        "currency": "usd",
                    },
                }
            ],
            overage_billing_period="ON_SUBSCRIPTION_RENEWAL",
            overage_pricing_models=[
                {
                    "billing_model": "FLAT_FEE",
                    "price_periods": [
                        {
                            "billing_period": "MONTHLY",
                            "billing_country_code": "billingCountryCode",
                            "block_size": 0,
                            "credit_grant_cadence": "BEGINNING_OF_BILLING_PERIOD",
                            "credit_rate": {
                                "amount": 1,
                                "currency_id": "currencyId",
                                "cost_formula": "costFormula",
                            },
                            "price": {
                                "amount": 0,
                                "currency": "usd",
                            },
                            "tiers": [
                                {
                                    "flat_price": {
                                        "amount": 0,
                                        "currency": "usd",
                                    },
                                    "unit_price": {
                                        "amount": 0,
                                        "currency": "usd",
                                    },
                                    "up_to": 0,
                                }
                            ],
                        }
                    ],
                    "billing_cadence": "RECURRING",
                    "entitlement": {
                        "feature_id": "featureId",
                        "has_soft_limit": True,
                        "has_unlimited_usage": True,
                        "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                        "reset_period": "YEAR",
                        "usage_limit": 0,
                        "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                        "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    },
                    "feature_id": "featureId",
                    "top_up_custom_currency_id": "topUpCustomCurrencyId",
                }
            ],
            pricing_models=[
                {
                    "billing_model": "FLAT_FEE",
                    "price_periods": [
                        {
                            "billing_period": "MONTHLY",
                            "billing_country_code": "billingCountryCode",
                            "block_size": 0,
                            "credit_grant_cadence": "BEGINNING_OF_BILLING_PERIOD",
                            "credit_rate": {
                                "amount": 1,
                                "currency_id": "currencyId",
                                "cost_formula": "costFormula",
                            },
                            "price": {
                                "amount": 0,
                                "currency": "usd",
                            },
                            "tiers": [
                                {
                                    "flat_price": {
                                        "amount": 0,
                                        "currency": "usd",
                                    },
                                    "unit_price": {
                                        "amount": 0,
                                        "currency": "usd",
                                    },
                                    "up_to": 0,
                                }
                            ],
                        }
                    ],
                    "billing_cadence": "RECURRING",
                    "feature_id": "featureId",
                    "max_unit_quantity": 1,
                    "min_unit_quantity": 1,
                    "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "reset_period": "YEAR",
                    "tiers_mode": "VOLUME",
                    "top_up_custom_currency_id": "topUpCustomCurrencyId",
                    "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                }
            ],
        )
        assert_matches_type(SetPackagePricingResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_pricing(self, client: Stigg) -> None:
        response = client.v1.plans.with_raw_response.set_pricing(
            id="x",
            pricing_type="FREE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SetPackagePricingResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_pricing(self, client: Stigg) -> None:
        with client.v1.plans.with_streaming_response.set_pricing(
            id="x",
            pricing_type="FREE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SetPackagePricingResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_pricing(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.plans.with_raw_response.set_pricing(
                id="",
                pricing_type="FREE",
            )


class TestAsyncPlans:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStigg) -> None:
        plan = await async_client.v1.plans.create(
            id="id",
            display_name="displayName",
            product_id="productId",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStigg) -> None:
        plan = await async_client.v1.plans.create(
            id="id",
            display_name="displayName",
            product_id="productId",
            billing_id="billingId",
            default_trial_config={
                "duration": 0,
                "units": "DAY",
                "budget": {
                    "has_soft_limit": True,
                    "limit": 0,
                },
                "trial_end_behavior": "CONVERT_TO_PAID",
            },
            description="description",
            metadata={"foo": "string"},
            parent_plan_id="parentPlanId",
            pricing_type="FREE",
            status="DRAFT",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.plans.with_raw_response.create(
            id="id",
            display_name="displayName",
            product_id="productId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.plans.with_streaming_response.create(
            id="id",
            display_name="displayName",
            product_id="productId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStigg) -> None:
        plan = await async_client.v1.plans.retrieve(
            "x",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.plans.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.plans.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.plans.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncStigg) -> None:
        plan = await async_client.v1.plans.update(
            id="x",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStigg) -> None:
        plan = await async_client.v1.plans.update(
            id="x",
            billing_id="billingId",
            compatible_addon_ids=["string"],
            default_trial_config={
                "duration": 0,
                "units": "DAY",
                "budget": {
                    "has_soft_limit": True,
                    "limit": 0,
                },
                "trial_end_behavior": "CONVERT_TO_PAID",
            },
            description="description",
            display_name="displayName",
            metadata={"foo": "string"},
            parent_plan_id="parentPlanId",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.plans.with_raw_response.update(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.plans.with_streaming_response.update(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.plans.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        plan = await async_client.v1.plans.list()
        assert_matches_type(AsyncMyCursorIDPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        plan = await async_client.v1.plans.list(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            limit=1,
            product_id="productId",
            status="status",
        )
        assert_matches_type(AsyncMyCursorIDPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncStigg) -> None:
        plan = await async_client.v1.plans.archive(
            "x",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.plans.with_raw_response.archive(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.plans.with_streaming_response.archive(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.plans.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_draft(self, async_client: AsyncStigg) -> None:
        plan = await async_client.v1.plans.create_draft(
            "x",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_draft(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.plans.with_raw_response.create_draft(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_draft(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.plans.with_streaming_response.create_draft(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_draft(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.plans.with_raw_response.create_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish(self, async_client: AsyncStigg) -> None:
        plan = await async_client.v1.plans.publish(
            id="x",
            migration_type="NEW_CUSTOMERS",
        )
        assert_matches_type(PlanPublishResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.plans.with_raw_response.publish(
            id="x",
            migration_type="NEW_CUSTOMERS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanPublishResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.plans.with_streaming_response.publish(
            id="x",
            migration_type="NEW_CUSTOMERS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanPublishResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_publish(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.plans.with_raw_response.publish(
                id="",
                migration_type="NEW_CUSTOMERS",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_draft(self, async_client: AsyncStigg) -> None:
        plan = await async_client.v1.plans.remove_draft(
            "x",
        )
        assert_matches_type(PlanRemoveDraftResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_draft(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.plans.with_raw_response.remove_draft(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanRemoveDraftResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_draft(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.plans.with_streaming_response.remove_draft(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanRemoveDraftResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_draft(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.plans.with_raw_response.remove_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_pricing(self, async_client: AsyncStigg) -> None:
        plan = await async_client.v1.plans.set_pricing(
            id="x",
            pricing_type="FREE",
        )
        assert_matches_type(SetPackagePricingResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_pricing_with_all_params(self, async_client: AsyncStigg) -> None:
        plan = await async_client.v1.plans.set_pricing(
            id="x",
            pricing_type="FREE",
            billing_id="billingId",
            minimum_spend=[
                {
                    "billing_period": "MONTHLY",
                    "minimum": {
                        "amount": 0,
                        "currency": "usd",
                    },
                }
            ],
            overage_billing_period="ON_SUBSCRIPTION_RENEWAL",
            overage_pricing_models=[
                {
                    "billing_model": "FLAT_FEE",
                    "price_periods": [
                        {
                            "billing_period": "MONTHLY",
                            "billing_country_code": "billingCountryCode",
                            "block_size": 0,
                            "credit_grant_cadence": "BEGINNING_OF_BILLING_PERIOD",
                            "credit_rate": {
                                "amount": 1,
                                "currency_id": "currencyId",
                                "cost_formula": "costFormula",
                            },
                            "price": {
                                "amount": 0,
                                "currency": "usd",
                            },
                            "tiers": [
                                {
                                    "flat_price": {
                                        "amount": 0,
                                        "currency": "usd",
                                    },
                                    "unit_price": {
                                        "amount": 0,
                                        "currency": "usd",
                                    },
                                    "up_to": 0,
                                }
                            ],
                        }
                    ],
                    "billing_cadence": "RECURRING",
                    "entitlement": {
                        "feature_id": "featureId",
                        "has_soft_limit": True,
                        "has_unlimited_usage": True,
                        "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                        "reset_period": "YEAR",
                        "usage_limit": 0,
                        "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                        "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    },
                    "feature_id": "featureId",
                    "top_up_custom_currency_id": "topUpCustomCurrencyId",
                }
            ],
            pricing_models=[
                {
                    "billing_model": "FLAT_FEE",
                    "price_periods": [
                        {
                            "billing_period": "MONTHLY",
                            "billing_country_code": "billingCountryCode",
                            "block_size": 0,
                            "credit_grant_cadence": "BEGINNING_OF_BILLING_PERIOD",
                            "credit_rate": {
                                "amount": 1,
                                "currency_id": "currencyId",
                                "cost_formula": "costFormula",
                            },
                            "price": {
                                "amount": 0,
                                "currency": "usd",
                            },
                            "tiers": [
                                {
                                    "flat_price": {
                                        "amount": 0,
                                        "currency": "usd",
                                    },
                                    "unit_price": {
                                        "amount": 0,
                                        "currency": "usd",
                                    },
                                    "up_to": 0,
                                }
                            ],
                        }
                    ],
                    "billing_cadence": "RECURRING",
                    "feature_id": "featureId",
                    "max_unit_quantity": 1,
                    "min_unit_quantity": 1,
                    "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "reset_period": "YEAR",
                    "tiers_mode": "VOLUME",
                    "top_up_custom_currency_id": "topUpCustomCurrencyId",
                    "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                }
            ],
        )
        assert_matches_type(SetPackagePricingResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_pricing(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.plans.with_raw_response.set_pricing(
            id="x",
            pricing_type="FREE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(SetPackagePricingResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_pricing(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.plans.with_streaming_response.set_pricing(
            id="x",
            pricing_type="FREE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(SetPackagePricingResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_pricing(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.plans.with_raw_response.set_pricing(
                id="",
                pricing_type="FREE",
            )
