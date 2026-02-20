# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.types.v1 import (
    Subscription,
    SubscriptionListResponse,
    SubscriptionImportResponse,
    SubscriptionPreviewResponse,
    SubscriptionProvisionResponse,
)
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.retrieve(
            "x",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.update(
            id="x",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.update(
            id="x",
            addons=[
                {
                    "addon_id": "addonId",
                    "quantity": 0,
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
            await_payment_confirmation=True,
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
                "coupon_id": "couponId",
                "integration_id": "integrationId",
                "invoice_days_until_due": 0,
                "is_backdated": True,
                "is_invoice_paid": True,
                "metadata": {"foo": "bar"},
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
            budget={
                "has_soft_limit": True,
                "limit": 0,
            },
            charges=[
                {
                    "id": "id",
                    "quantity": 1,
                    "type": "FEATURE",
                }
            ],
            metadata={"foo": "string"},
            minimum_spend={
                "minimum": {
                    "amount": 0,
                    "currency": "usd",
                }
            },
            price_overrides=[
                {
                    "addon_id": "addonId",
                    "base_charge": True,
                    "currency_id": "currencyId",
                    "feature_id": "featureId",
                    "price": {
                        "amount": 0,
                        "currency": "usd",
                    },
                }
            ],
            promotion_code="promotionCode",
            schedule_strategy="END_OF_BILLING_PERIOD",
            subscription_entitlements=[
                {
                    "id": "id",
                    "feature_id": "featureId",
                    "has_soft_limit": True,
                    "has_unlimited_usage": True,
                    "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "reset_period": "YEAR",
                    "usage_limit": 0,
                    "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                }
            ],
            trial_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.update(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.update(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.list()
        assert_matches_type(SyncMyCursorIDPage[SubscriptionListResponse], subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.list(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            customer_id="customerId",
            limit=1,
            plan_id="planId",
            pricing_type="pricingType",
            resource_id="resourceId",
            status="status",
        )
        assert_matches_type(SyncMyCursorIDPage[SubscriptionListResponse], subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncMyCursorIDPage[SubscriptionListResponse], subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SyncMyCursorIDPage[SubscriptionListResponse], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.cancel(
            id="x",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.cancel(
            id="x",
            cancellation_action="DEFAULT",
            cancellation_time="END_OF_BILLING_PERIOD",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            prorate=True,
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.cancel(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.cancel(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.with_raw_response.cancel(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delegate(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.delegate(
            id="x",
            target_customer_id="targetCustomerId",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delegate(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.delegate(
            id="x",
            target_customer_id="targetCustomerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delegate(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.delegate(
            id="x",
            target_customer_id="targetCustomerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delegate(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.with_raw_response.delegate(
                id="",
                target_customer_id="targetCustomerId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.import_(
            subscriptions=[
                {
                    "id": "id",
                    "customer_id": "customerId",
                    "plan_id": "planId",
                }
            ],
        )
        assert_matches_type(SubscriptionImportResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import_with_all_params(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.import_(
            subscriptions=[
                {
                    "id": "id",
                    "customer_id": "customerId",
                    "plan_id": "planId",
                    "billing_id": "billingId",
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "metadata": {"foo": "string"},
                    "resource_id": "resourceId",
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            integration_id="integrationId",
        )
        assert_matches_type(SubscriptionImportResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_import(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.import_(
            subscriptions=[
                {
                    "id": "id",
                    "customer_id": "customerId",
                    "plan_id": "planId",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionImportResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_import(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.import_(
            subscriptions=[
                {
                    "id": "id",
                    "customer_id": "customerId",
                    "plan_id": "planId",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionImportResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_migrate(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.migrate(
            id="x",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_migrate_with_all_params(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.migrate(
            id="x",
            subscription_migration_time="END_OF_BILLING_PERIOD",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_migrate(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.migrate(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_migrate(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.migrate(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_migrate(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.with_raw_response.migrate(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_preview(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.preview(
            customer_id="customerId",
            plan_id="planId",
        )
        assert_matches_type(SubscriptionPreviewResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_provision(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.provision(
            customer_id="customerId",
            plan_id="planId",
        )
        assert_matches_type(SubscriptionProvisionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_provision_with_all_params(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.provision(
            customer_id="customerId",
            plan_id="planId",
            id="id",
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
            await_payment_confirmation=True,
            billing_country_code="billingCountryCode",
            billing_id="billingId",
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
                "metadata": {"foo": "string"},
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
            budget={
                "has_soft_limit": True,
                "limit": 0,
            },
            charges=[
                {
                    "id": "id",
                    "quantity": 1,
                    "type": "FEATURE",
                }
            ],
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
            minimum_spend={
                "minimum": {
                    "amount": 0,
                    "billing_country_code": "billingCountryCode",
                    "currency": "usd",
                }
            },
            paying_customer_id="payingCustomerId",
            payment_collection_method="CHARGE",
            price_overrides=[
                {
                    "addon_id": "addonId",
                    "base_charge": True,
                    "block_size": 0,
                    "credit_grant_cadence": "BEGINNING_OF_BILLING_PERIOD",
                    "credit_rate": {
                        "amount": 1,
                        "currency_id": "currencyId",
                        "cost_formula": "costFormula",
                    },
                    "feature_id": "featureId",
                    "price": {
                        "amount": 0,
                        "billing_country_code": "billingCountryCode",
                        "currency": "usd",
                    },
                    "tiers": [
                        {
                            "flat_price": {
                                "amount": 0,
                                "billing_country_code": "billingCountryCode",
                                "currency": "usd",
                            },
                            "unit_price": {
                                "amount": 0,
                                "billing_country_code": "billingCountryCode",
                                "currency": "usd",
                            },
                            "up_to": 0,
                        }
                    ],
                }
            ],
            resource_id="resourceId",
            salesforce_id="salesforceId",
            schedule_strategy="END_OF_BILLING_PERIOD",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            subscription_entitlements=[
                {
                    "feature_id": "featureId",
                    "usage_limit": 0,
                    "is_granted": True,
                }
            ],
            trial_override_configuration={
                "is_trial": True,
                "trial_end_behavior": "CONVERT_TO_PAID",
                "trial_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            unit_quantity=1,
        )
        assert_matches_type(SubscriptionProvisionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_provision(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.provision(
            customer_id="customerId",
            plan_id="planId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionProvisionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_provision(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.provision(
            customer_id="customerId",
            plan_id="planId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionProvisionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_transfer(self, client: Stigg) -> None:
        subscription = client.v1.subscriptions.transfer(
            id="x",
            destination_resource_id="destinationResourceId",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_transfer(self, client: Stigg) -> None:
        response = client.v1.subscriptions.with_raw_response.transfer(
            id="x",
            destination_resource_id="destinationResourceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_transfer(self, client: Stigg) -> None:
        with client.v1.subscriptions.with_streaming_response.transfer(
            id="x",
            destination_resource_id="destinationResourceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.retrieve(
            "x",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.update(
            id="x",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.update(
            id="x",
            addons=[
                {
                    "addon_id": "addonId",
                    "quantity": 0,
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
            await_payment_confirmation=True,
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
                "coupon_id": "couponId",
                "integration_id": "integrationId",
                "invoice_days_until_due": 0,
                "is_backdated": True,
                "is_invoice_paid": True,
                "metadata": {"foo": "bar"},
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
            budget={
                "has_soft_limit": True,
                "limit": 0,
            },
            charges=[
                {
                    "id": "id",
                    "quantity": 1,
                    "type": "FEATURE",
                }
            ],
            metadata={"foo": "string"},
            minimum_spend={
                "minimum": {
                    "amount": 0,
                    "currency": "usd",
                }
            },
            price_overrides=[
                {
                    "addon_id": "addonId",
                    "base_charge": True,
                    "currency_id": "currencyId",
                    "feature_id": "featureId",
                    "price": {
                        "amount": 0,
                        "currency": "usd",
                    },
                }
            ],
            promotion_code="promotionCode",
            schedule_strategy="END_OF_BILLING_PERIOD",
            subscription_entitlements=[
                {
                    "id": "id",
                    "feature_id": "featureId",
                    "has_soft_limit": True,
                    "has_unlimited_usage": True,
                    "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "reset_period": "YEAR",
                    "usage_limit": 0,
                    "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                    "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                }
            ],
            trial_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.update(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.update(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.list()
        assert_matches_type(AsyncMyCursorIDPage[SubscriptionListResponse], subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.list(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            customer_id="customerId",
            limit=1,
            plan_id="planId",
            pricing_type="pricingType",
            resource_id="resourceId",
            status="status",
        )
        assert_matches_type(AsyncMyCursorIDPage[SubscriptionListResponse], subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[SubscriptionListResponse], subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[SubscriptionListResponse], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.cancel(
            id="x",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.cancel(
            id="x",
            cancellation_action="DEFAULT",
            cancellation_time="END_OF_BILLING_PERIOD",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            prorate=True,
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.cancel(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.cancel(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.with_raw_response.cancel(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delegate(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.delegate(
            id="x",
            target_customer_id="targetCustomerId",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delegate(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.delegate(
            id="x",
            target_customer_id="targetCustomerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delegate(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.delegate(
            id="x",
            target_customer_id="targetCustomerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delegate(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.with_raw_response.delegate(
                id="",
                target_customer_id="targetCustomerId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.import_(
            subscriptions=[
                {
                    "id": "id",
                    "customer_id": "customerId",
                    "plan_id": "planId",
                }
            ],
        )
        assert_matches_type(SubscriptionImportResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.import_(
            subscriptions=[
                {
                    "id": "id",
                    "customer_id": "customerId",
                    "plan_id": "planId",
                    "billing_id": "billingId",
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "metadata": {"foo": "string"},
                    "resource_id": "resourceId",
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            integration_id="integrationId",
        )
        assert_matches_type(SubscriptionImportResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_import(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.import_(
            subscriptions=[
                {
                    "id": "id",
                    "customer_id": "customerId",
                    "plan_id": "planId",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionImportResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.import_(
            subscriptions=[
                {
                    "id": "id",
                    "customer_id": "customerId",
                    "plan_id": "planId",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionImportResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_migrate(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.migrate(
            id="x",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_migrate_with_all_params(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.migrate(
            id="x",
            subscription_migration_time="END_OF_BILLING_PERIOD",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_migrate(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.migrate(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_migrate(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.migrate(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_migrate(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.with_raw_response.migrate(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_preview(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.preview(
            customer_id="customerId",
            plan_id="planId",
        )
        assert_matches_type(SubscriptionPreviewResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_provision(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.provision(
            customer_id="customerId",
            plan_id="planId",
        )
        assert_matches_type(SubscriptionProvisionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_provision_with_all_params(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.provision(
            customer_id="customerId",
            plan_id="planId",
            id="id",
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
            await_payment_confirmation=True,
            billing_country_code="billingCountryCode",
            billing_id="billingId",
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
                "metadata": {"foo": "string"},
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
            budget={
                "has_soft_limit": True,
                "limit": 0,
            },
            charges=[
                {
                    "id": "id",
                    "quantity": 1,
                    "type": "FEATURE",
                }
            ],
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
            minimum_spend={
                "minimum": {
                    "amount": 0,
                    "billing_country_code": "billingCountryCode",
                    "currency": "usd",
                }
            },
            paying_customer_id="payingCustomerId",
            payment_collection_method="CHARGE",
            price_overrides=[
                {
                    "addon_id": "addonId",
                    "base_charge": True,
                    "block_size": 0,
                    "credit_grant_cadence": "BEGINNING_OF_BILLING_PERIOD",
                    "credit_rate": {
                        "amount": 1,
                        "currency_id": "currencyId",
                        "cost_formula": "costFormula",
                    },
                    "feature_id": "featureId",
                    "price": {
                        "amount": 0,
                        "billing_country_code": "billingCountryCode",
                        "currency": "usd",
                    },
                    "tiers": [
                        {
                            "flat_price": {
                                "amount": 0,
                                "billing_country_code": "billingCountryCode",
                                "currency": "usd",
                            },
                            "unit_price": {
                                "amount": 0,
                                "billing_country_code": "billingCountryCode",
                                "currency": "usd",
                            },
                            "up_to": 0,
                        }
                    ],
                }
            ],
            resource_id="resourceId",
            salesforce_id="salesforceId",
            schedule_strategy="END_OF_BILLING_PERIOD",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            subscription_entitlements=[
                {
                    "feature_id": "featureId",
                    "usage_limit": 0,
                    "is_granted": True,
                }
            ],
            trial_override_configuration={
                "is_trial": True,
                "trial_end_behavior": "CONVERT_TO_PAID",
                "trial_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            unit_quantity=1,
        )
        assert_matches_type(SubscriptionProvisionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_provision(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.provision(
            customer_id="customerId",
            plan_id="planId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionProvisionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_provision(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.provision(
            customer_id="customerId",
            plan_id="planId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionProvisionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_transfer(self, async_client: AsyncStigg) -> None:
        subscription = await async_client.v1.subscriptions.transfer(
            id="x",
            destination_resource_id="destinationResourceId",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_transfer(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.with_raw_response.transfer(
            id="x",
            destination_resource_id="destinationResourceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_transfer(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.with_streaming_response.transfer(
            id="x",
            destination_resource_id="destinationResourceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_transfer(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.with_raw_response.transfer(
                id="",
                destination_resource_id="destinationResourceId",
            )
