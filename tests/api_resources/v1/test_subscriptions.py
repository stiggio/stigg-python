# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.types.v1 import (
    SubscriptionListResponse,
    SubscriptionCreateResponse,
    SubscriptionMigrateResponse,
    SubscriptionPreviewResponse,
    SubscriptionDelegateResponse,
    SubscriptionRetrieveResponse,
    SubscriptionTransferResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.create(
            customer_id="customerId",
            plan_id="planId",
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.create(
            customer_id="customerId",
            plan_id="planId",
            id="id",
            await_payment_confirmation=True,
            billing_period="MONTHLY",
            checkout_options={
                "cancel_url": "https://example.com",
                "success_url": "https://example.com",
                "allow_promo_codes": True,
                "allow_tax_id_collection": True,
                "collect_billing_address": True,
                "collect_phone_number": True,
                "reference_id": "referenceId",
            },
            metadata={"foo": "string"},
            paying_customer_id="payingCustomerId",
            resource_id="resourceId",
            trial_override_configuration={
                "is_trial": True,
                "trial_end_behavior": "CONVERT_TO_PAID",
                "trial_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.create(
            customer_id="customerId",
            plan_id="planId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.create(
            customer_id="customerId",
            plan_id="planId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.retrieve(
            "x",
        )
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.list()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.list(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="customerId",
            limit=1,
            status="status",
        )
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delegate(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.delegate(
            id="x",
            target_customer_id="targetCustomerId",
        )
        assert_matches_type(SubscriptionDelegateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delegate(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.delegate(
            id="x",
            target_customer_id="targetCustomerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionDelegateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delegate(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.delegate(
            id="x",
            target_customer_id="targetCustomerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionDelegateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delegate(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.with_raw_response.delegate(
                id="",
                target_customer_id="targetCustomerId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_migrate(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.migrate(
            id="x",
        )
        assert_matches_type(SubscriptionMigrateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_migrate_with_all_params(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.migrate(
            id="x",
            subscription_migration_time="END_OF_BILLING_PERIOD",
        )
        assert_matches_type(SubscriptionMigrateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_migrate(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.migrate(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionMigrateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_migrate(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.migrate(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionMigrateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_migrate(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.with_raw_response.migrate(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_preview(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.preview(
            customer_id="customerId",
            plan_id="planId",
        )
        assert_matches_type(SubscriptionPreviewResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_preview_with_all_params(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.preview(
            customer_id="customerId",
            plan_id="planId",
            addons=[
                {
                    "addon_id": "addonId",
                    "quantity": 1,
                }
            ],
            applied_coupon={
                "billing_coupon_id": "billingCouponId",
                "configuration": {"start_date": parse_datetime("2019-12-27T18:11:19.117Z")},
                "coupon_id": "couponId",
                "discount": {
                    "amounts_off": [
                        {
                            "amount": 0,
                            "currency": "usd",
                        }
                    ],
                    "description": "description",
                    "duration_in_months": 1,
                    "name": "name",
                    "percent_off": 1,
                },
                "promotion_code": "promotionCode",
            },
            billable_features=[
                {
                    "feature_id": "featureId",
                    "quantity": 1,
                }
            ],
            billing_country_code="billingCountryCode",
            billing_information={
                "billing_address": {
                    "city": "city",
                    "country": "country",
                    "line1": "line1",
                    "line2": "line2",
                    "postal_code": "postalCode",
                    "state": "state",
                },
                "charge_on_behalf_of_account": "chargeOnBehalfOfAccount",
                "integration_id": "integrationId",
                "invoice_days_until_due": 0,
                "is_backdated": True,
                "is_invoice_paid": True,
                "metadata": {},
                "proration_behavior": "INVOICE_IMMEDIATELY",
                "tax_ids": [
                    {
                        "type": "type",
                        "value": "value",
                    }
                ],
                "tax_percentage": 0,
                "tax_rate_ids": ["string"],
            },
            billing_period="MONTHLY",
            charges=[
                {
                    "id": "id",
                    "quantity": 1,
                    "type": "FEATURE",
                }
            ],
            paying_customer_id="payingCustomerId",
            resource_id="resourceId",
            schedule_strategy="END_OF_BILLING_PERIOD",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            trial_override_configuration={
                "is_trial": True,
                "trial_end_behavior": "CONVERT_TO_PAID",
                "trial_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            unit_quantity=1,
        )
        assert_matches_type(SubscriptionPreviewResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_preview(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.preview(
            customer_id="customerId",
            plan_id="planId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionPreviewResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_preview(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.preview(
            customer_id="customerId",
            plan_id="planId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionPreviewResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_transfer(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.transfer(
            id="x",
            destination_resource_id="destinationResourceId",
        )
        assert_matches_type(SubscriptionTransferResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_transfer(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.transfer(
            id="x",
            destination_resource_id="destinationResourceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionTransferResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_transfer(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.transfer(
            id="x",
            destination_resource_id="destinationResourceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionTransferResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_transfer(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.with_raw_response.transfer(
                id="",
                destination_resource_id="destinationResourceId",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.create(
            customer_id="customerId",
            plan_id="planId",
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.create(
            customer_id="customerId",
            plan_id="planId",
            id="id",
            await_payment_confirmation=True,
            billing_period="MONTHLY",
            checkout_options={
                "cancel_url": "https://example.com",
                "success_url": "https://example.com",
                "allow_promo_codes": True,
                "allow_tax_id_collection": True,
                "collect_billing_address": True,
                "collect_phone_number": True,
                "reference_id": "referenceId",
            },
            metadata={"foo": "string"},
            paying_customer_id="payingCustomerId",
            resource_id="resourceId",
            trial_override_configuration={
                "is_trial": True,
                "trial_end_behavior": "CONVERT_TO_PAID",
                "trial_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.create(
            customer_id="customerId",
            plan_id="planId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.create(
            customer_id="customerId",
            plan_id="planId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.retrieve(
            "x",
        )
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.list()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.list(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="customerId",
            limit=1,
            status="status",
        )
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delegate(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.delegate(
            id="x",
            target_customer_id="targetCustomerId",
        )
        assert_matches_type(SubscriptionDelegateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delegate(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.delegate(
            id="x",
            target_customer_id="targetCustomerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionDelegateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delegate(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.delegate(
            id="x",
            target_customer_id="targetCustomerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionDelegateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delegate(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.with_raw_response.delegate(
                id="",
                target_customer_id="targetCustomerId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_migrate(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.migrate(
            id="x",
        )
        assert_matches_type(SubscriptionMigrateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_migrate_with_all_params(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.migrate(
            id="x",
            subscription_migration_time="END_OF_BILLING_PERIOD",
        )
        assert_matches_type(SubscriptionMigrateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_migrate(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.migrate(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionMigrateResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_migrate(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.migrate(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionMigrateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_migrate(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.with_raw_response.migrate(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_preview(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.preview(
            customer_id="customerId",
            plan_id="planId",
        )
        assert_matches_type(SubscriptionPreviewResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_preview_with_all_params(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.preview(
            customer_id="customerId",
            plan_id="planId",
            addons=[
                {
                    "addon_id": "addonId",
                    "quantity": 1,
                }
            ],
            applied_coupon={
                "billing_coupon_id": "billingCouponId",
                "configuration": {"start_date": parse_datetime("2019-12-27T18:11:19.117Z")},
                "coupon_id": "couponId",
                "discount": {
                    "amounts_off": [
                        {
                            "amount": 0,
                            "currency": "usd",
                        }
                    ],
                    "description": "description",
                    "duration_in_months": 1,
                    "name": "name",
                    "percent_off": 1,
                },
                "promotion_code": "promotionCode",
            },
            billable_features=[
                {
                    "feature_id": "featureId",
                    "quantity": 1,
                }
            ],
            billing_country_code="billingCountryCode",
            billing_information={
                "billing_address": {
                    "city": "city",
                    "country": "country",
                    "line1": "line1",
                    "line2": "line2",
                    "postal_code": "postalCode",
                    "state": "state",
                },
                "charge_on_behalf_of_account": "chargeOnBehalfOfAccount",
                "integration_id": "integrationId",
                "invoice_days_until_due": 0,
                "is_backdated": True,
                "is_invoice_paid": True,
                "metadata": {},
                "proration_behavior": "INVOICE_IMMEDIATELY",
                "tax_ids": [
                    {
                        "type": "type",
                        "value": "value",
                    }
                ],
                "tax_percentage": 0,
                "tax_rate_ids": ["string"],
            },
            billing_period="MONTHLY",
            charges=[
                {
                    "id": "id",
                    "quantity": 1,
                    "type": "FEATURE",
                }
            ],
            paying_customer_id="payingCustomerId",
            resource_id="resourceId",
            schedule_strategy="END_OF_BILLING_PERIOD",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            trial_override_configuration={
                "is_trial": True,
                "trial_end_behavior": "CONVERT_TO_PAID",
                "trial_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            unit_quantity=1,
        )
        assert_matches_type(SubscriptionPreviewResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.preview(
            customer_id="customerId",
            plan_id="planId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionPreviewResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.preview(
            customer_id="customerId",
            plan_id="planId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionPreviewResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_transfer(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.transfer(
            id="x",
            destination_resource_id="destinationResourceId",
        )
        assert_matches_type(SubscriptionTransferResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_transfer(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.transfer(
            id="x",
            destination_resource_id="destinationResourceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionTransferResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_transfer(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.transfer(
            id="x",
            destination_resource_id="destinationResourceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionTransferResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_transfer(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.with_raw_response.transfer(
                id="",
                destination_resource_id="destinationResourceId",
            )
