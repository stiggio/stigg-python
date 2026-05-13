# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from stigg.types.v1.events.credits import GrantListResponse, CreditGrantResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGrants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Stigg) -> None:
        grant = client.v1.events.credits.grants.create(
            amount=0,
            currency_id="currencyId",
            customer_id="customerId",
            display_name="displayName",
            grant_type="PAID",
        )
        assert_matches_type(CreditGrantResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Stigg) -> None:
        grant = client.v1.events.credits.grants.create(
            amount=0,
            currency_id="currencyId",
            customer_id="customerId",
            display_name="displayName",
            grant_type="PAID",
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
                "invoice_days_until_due": 0,
                "is_invoice_paid": True,
            },
            comment="comment",
            cost={
                "amount": 0,
                "currency": "usd",
            },
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "string"},
            payment_collection_method="CHARGE",
            priority=0,
            resource_id="resourceId",
        )
        assert_matches_type(CreditGrantResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stigg) -> None:
        response = client.v1.events.credits.grants.with_raw_response.create(
            amount=0,
            currency_id="currencyId",
            customer_id="customerId",
            display_name="displayName",
            grant_type="PAID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = response.parse()
        assert_matches_type(CreditGrantResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stigg) -> None:
        with client.v1.events.credits.grants.with_streaming_response.create(
            amount=0,
            currency_id="currencyId",
            customer_id="customerId",
            display_name="displayName",
            grant_type="PAID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = response.parse()
            assert_matches_type(CreditGrantResponse, grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        grant = client.v1.events.credits.grants.list(
            customer_id="customerId",
        )
        assert_matches_type(SyncMyCursorIDPage[GrantListResponse], grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        grant = client.v1.events.credits.grants.list(
            customer_id="customerId",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            currency_id="currencyId",
            limit=1,
            resource_id="resourceId",
        )
        assert_matches_type(SyncMyCursorIDPage[GrantListResponse], grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1.events.credits.grants.with_raw_response.list(
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = response.parse()
        assert_matches_type(SyncMyCursorIDPage[GrantListResponse], grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1.events.credits.grants.with_streaming_response.list(
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = response.parse()
            assert_matches_type(SyncMyCursorIDPage[GrantListResponse], grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_void(self, client: Stigg) -> None:
        grant = client.v1.events.credits.grants.void(
            "x",
        )
        assert_matches_type(CreditGrantResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_void(self, client: Stigg) -> None:
        response = client.v1.events.credits.grants.with_raw_response.void(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = response.parse()
        assert_matches_type(CreditGrantResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_void(self, client: Stigg) -> None:
        with client.v1.events.credits.grants.with_streaming_response.void(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = response.parse()
            assert_matches_type(CreditGrantResponse, grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_void(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.credits.grants.with_raw_response.void(
                "",
            )


class TestAsyncGrants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStigg) -> None:
        grant = await async_client.v1.events.credits.grants.create(
            amount=0,
            currency_id="currencyId",
            customer_id="customerId",
            display_name="displayName",
            grant_type="PAID",
        )
        assert_matches_type(CreditGrantResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStigg) -> None:
        grant = await async_client.v1.events.credits.grants.create(
            amount=0,
            currency_id="currencyId",
            customer_id="customerId",
            display_name="displayName",
            grant_type="PAID",
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
                "invoice_days_until_due": 0,
                "is_invoice_paid": True,
            },
            comment="comment",
            cost={
                "amount": 0,
                "currency": "usd",
            },
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "string"},
            payment_collection_method="CHARGE",
            priority=0,
            resource_id="resourceId",
        )
        assert_matches_type(CreditGrantResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.credits.grants.with_raw_response.create(
            amount=0,
            currency_id="currencyId",
            customer_id="customerId",
            display_name="displayName",
            grant_type="PAID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = await response.parse()
        assert_matches_type(CreditGrantResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.credits.grants.with_streaming_response.create(
            amount=0,
            currency_id="currencyId",
            customer_id="customerId",
            display_name="displayName",
            grant_type="PAID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = await response.parse()
            assert_matches_type(CreditGrantResponse, grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        grant = await async_client.v1.events.credits.grants.list(
            customer_id="customerId",
        )
        assert_matches_type(AsyncMyCursorIDPage[GrantListResponse], grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        grant = await async_client.v1.events.credits.grants.list(
            customer_id="customerId",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            currency_id="currencyId",
            limit=1,
            resource_id="resourceId",
        )
        assert_matches_type(AsyncMyCursorIDPage[GrantListResponse], grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.credits.grants.with_raw_response.list(
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[GrantListResponse], grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.credits.grants.with_streaming_response.list(
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[GrantListResponse], grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_void(self, async_client: AsyncStigg) -> None:
        grant = await async_client.v1.events.credits.grants.void(
            "x",
        )
        assert_matches_type(CreditGrantResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_void(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.credits.grants.with_raw_response.void(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = await response.parse()
        assert_matches_type(CreditGrantResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_void(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.credits.grants.with_streaming_response.void(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = await response.parse()
            assert_matches_type(CreditGrantResponse, grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_void(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.credits.grants.with_raw_response.void(
                "",
            )
