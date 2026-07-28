# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.types.v1 import (
    ContractListResponse,
    ContractCreateResponse,
    ContractDeleteResponse,
    ContractUpdateResponse,
    ContractRetrieveResponse,
)
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContracts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Stigg) -> None:
        contract = client.v1.contracts.create(
            customer_id="customerId",
            subscriptions=[{}],
        )
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Stigg) -> None:
        contract = client.v1.contracts.create(
            customer_id="customerId",
            subscriptions=[
                {
                    "existing_subscription_id": "existingSubscriptionId",
                    "new_subscription": {
                        "customer_id": "customerId",
                        "plan_id": "planId",
                        "id": "id",
                        "addons": [
                            {
                                "id": "id",
                                "quantity": 0,
                            }
                        ],
                        "applied_coupon": {
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
                        "await_payment_confirmation": True,
                        "billing_country_code": "billingCountryCode",
                        "billing_cycle_anchor": "UNCHANGED",
                        "billing_id": "billingId",
                        "billing_information": {
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
                        "billing_period": "MONTHLY",
                        "budget": {
                            "has_soft_limit": True,
                            "limit": 0,
                        },
                        "cancellation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "charges": [
                            {
                                "id": "id",
                                "quantity": 0,
                                "type": "FEATURE",
                            }
                        ],
                        "checkout_options": {
                            "cancel_url": "https://example.com",
                            "success_url": "https://example.com",
                            "allow_promo_codes": True,
                            "allow_tax_id_collection": True,
                            "collect_billing_address": True,
                            "collect_phone_number": True,
                            "reference_id": "referenceId",
                        },
                        "entitlements": [
                            {
                                "id": "id",
                                "type": "FEATURE",
                                "has_soft_limit": True,
                                "has_unlimited_usage": True,
                                "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                                "reset_period": "YEAR",
                                "usage_limit": 0,
                                "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                                "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                            }
                        ],
                        "metadata": {"foo": "string"},
                        "minimum_spend": {
                            "amount": 0,
                            "currency": "usd",
                        },
                        "paying_customer_id": "payingCustomerId",
                        "payment_collection_method": "CHARGE",
                        "price_overrides": [
                            {
                                "addon_id": "addonId",
                                "amount": 0,
                                "base_charge": True,
                                "billing_country_code": "billingCountryCode",
                                "block_size": 0,
                                "credit_grant_cadence": "BEGINNING_OF_BILLING_PERIOD",
                                "credit_rate": {
                                    "amount": 1,
                                    "currency_id": "currencyId",
                                    "cost_formula": "costFormula",
                                },
                                "currency": "usd",
                                "feature_id": "featureId",
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
                        "resource_id": "resourceId",
                        "salesforce_id": "salesforceId",
                        "schedule_strategy": "END_OF_BILLING_PERIOD",
                        "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "trial_override_configuration": {
                            "is_trial": True,
                            "trial_end_behavior": "CONVERT_TO_PAID",
                            "trial_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        "unit_quantity": 0,
                    },
                }
            ],
            activation_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            activation_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            po_number="poNumber",
            setup_billing=True,
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stigg) -> None:
        response = client.v1.contracts.with_raw_response.create(
            customer_id="customerId",
            subscriptions=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stigg) -> None:
        with client.v1.contracts.with_streaming_response.create(
            customer_id="customerId",
            subscriptions=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractCreateResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Stigg) -> None:
        contract = client.v1.contracts.retrieve(
            id="x",
        )
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Stigg) -> None:
        contract = client.v1.contracts.retrieve(
            id="x",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Stigg) -> None:
        response = client.v1.contracts.with_raw_response.retrieve(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Stigg) -> None:
        with client.v1.contracts.with_streaming_response.retrieve(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.contracts.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Stigg) -> None:
        contract = client.v1.contracts.update(
            id="x",
        )
        assert_matches_type(ContractUpdateResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Stigg) -> None:
        contract = client.v1.contracts.update(
            id="x",
            activation_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            activation_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            po_number="poNumber",
            setup_billing=True,
            subscription_ids=["NxI"],
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ContractUpdateResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Stigg) -> None:
        response = client.v1.contracts.with_raw_response.update(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractUpdateResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Stigg) -> None:
        with client.v1.contracts.with_streaming_response.update(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractUpdateResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.contracts.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        contract = client.v1.contracts.list()
        assert_matches_type(SyncMyCursorIDPage[ContractListResponse], contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        contract = client.v1.contracts.list(
            after="after",
            before="before",
            customer_external_id="customerExternalId",
            limit=1,
            name="name",
            state="state",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(SyncMyCursorIDPage[ContractListResponse], contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1.contracts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(SyncMyCursorIDPage[ContractListResponse], contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1.contracts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(SyncMyCursorIDPage[ContractListResponse], contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Stigg) -> None:
        contract = client.v1.contracts.delete(
            id="x",
        )
        assert_matches_type(ContractDeleteResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Stigg) -> None:
        contract = client.v1.contracts.delete(
            id="x",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ContractDeleteResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Stigg) -> None:
        response = client.v1.contracts.with_raw_response.delete(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractDeleteResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Stigg) -> None:
        with client.v1.contracts.with_streaming_response.delete(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractDeleteResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.contracts.with_raw_response.delete(
                id="",
            )


class TestAsyncContracts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStigg) -> None:
        contract = await async_client.v1.contracts.create(
            customer_id="customerId",
            subscriptions=[{}],
        )
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStigg) -> None:
        contract = await async_client.v1.contracts.create(
            customer_id="customerId",
            subscriptions=[
                {
                    "existing_subscription_id": "existingSubscriptionId",
                    "new_subscription": {
                        "customer_id": "customerId",
                        "plan_id": "planId",
                        "id": "id",
                        "addons": [
                            {
                                "id": "id",
                                "quantity": 0,
                            }
                        ],
                        "applied_coupon": {
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
                        "await_payment_confirmation": True,
                        "billing_country_code": "billingCountryCode",
                        "billing_cycle_anchor": "UNCHANGED",
                        "billing_id": "billingId",
                        "billing_information": {
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
                        "billing_period": "MONTHLY",
                        "budget": {
                            "has_soft_limit": True,
                            "limit": 0,
                        },
                        "cancellation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "charges": [
                            {
                                "id": "id",
                                "quantity": 0,
                                "type": "FEATURE",
                            }
                        ],
                        "checkout_options": {
                            "cancel_url": "https://example.com",
                            "success_url": "https://example.com",
                            "allow_promo_codes": True,
                            "allow_tax_id_collection": True,
                            "collect_billing_address": True,
                            "collect_phone_number": True,
                            "reference_id": "referenceId",
                        },
                        "entitlements": [
                            {
                                "id": "id",
                                "type": "FEATURE",
                                "has_soft_limit": True,
                                "has_unlimited_usage": True,
                                "monthly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                                "reset_period": "YEAR",
                                "usage_limit": 0,
                                "weekly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                                "yearly_reset_period_configuration": {"according_to": "SubscriptionStart"},
                            }
                        ],
                        "metadata": {"foo": "string"},
                        "minimum_spend": {
                            "amount": 0,
                            "currency": "usd",
                        },
                        "paying_customer_id": "payingCustomerId",
                        "payment_collection_method": "CHARGE",
                        "price_overrides": [
                            {
                                "addon_id": "addonId",
                                "amount": 0,
                                "base_charge": True,
                                "billing_country_code": "billingCountryCode",
                                "block_size": 0,
                                "credit_grant_cadence": "BEGINNING_OF_BILLING_PERIOD",
                                "credit_rate": {
                                    "amount": 1,
                                    "currency_id": "currencyId",
                                    "cost_formula": "costFormula",
                                },
                                "currency": "usd",
                                "feature_id": "featureId",
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
                        "resource_id": "resourceId",
                        "salesforce_id": "salesforceId",
                        "schedule_strategy": "END_OF_BILLING_PERIOD",
                        "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "trial_override_configuration": {
                            "is_trial": True,
                            "trial_end_behavior": "CONVERT_TO_PAID",
                            "trial_end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        "unit_quantity": 0,
                    },
                }
            ],
            activation_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            activation_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            po_number="poNumber",
            setup_billing=True,
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.contracts.with_raw_response.create(
            customer_id="customerId",
            subscriptions=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.contracts.with_streaming_response.create(
            customer_id="customerId",
            subscriptions=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractCreateResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStigg) -> None:
        contract = await async_client.v1.contracts.retrieve(
            id="x",
        )
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncStigg) -> None:
        contract = await async_client.v1.contracts.retrieve(
            id="x",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.contracts.with_raw_response.retrieve(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.contracts.with_streaming_response.retrieve(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.contracts.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncStigg) -> None:
        contract = await async_client.v1.contracts.update(
            id="x",
        )
        assert_matches_type(ContractUpdateResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStigg) -> None:
        contract = await async_client.v1.contracts.update(
            id="x",
            activation_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            activation_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            po_number="poNumber",
            setup_billing=True,
            subscription_ids=["NxI"],
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ContractUpdateResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.contracts.with_raw_response.update(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractUpdateResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.contracts.with_streaming_response.update(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractUpdateResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.contracts.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        contract = await async_client.v1.contracts.list()
        assert_matches_type(AsyncMyCursorIDPage[ContractListResponse], contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        contract = await async_client.v1.contracts.list(
            after="after",
            before="before",
            customer_external_id="customerExternalId",
            limit=1,
            name="name",
            state="state",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(AsyncMyCursorIDPage[ContractListResponse], contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.contracts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[ContractListResponse], contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.contracts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[ContractListResponse], contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncStigg) -> None:
        contract = await async_client.v1.contracts.delete(
            id="x",
        )
        assert_matches_type(ContractDeleteResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncStigg) -> None:
        contract = await async_client.v1.contracts.delete(
            id="x",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ContractDeleteResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.contracts.with_raw_response.delete(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractDeleteResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.contracts.with_streaming_response.delete(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractDeleteResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.contracts.with_raw_response.delete(
                id="",
            )
