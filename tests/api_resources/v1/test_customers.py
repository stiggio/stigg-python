# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1 import (
    CustomerResponse,
    CustomerListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Stigg) -> None:
        customer = client.v1.customers.create(
            email="dev@stainless.com",
            external_id="externalId",
            name="name",
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Stigg) -> None:
        customer = client.v1.customers.create(
            email="dev@stainless.com",
            external_id="externalId",
            name="name",
            default_payment_method={
                "billing_id": "billingId",
                "card_expiry_month": 0,
                "card_expiry_year": 0,
                "card_last4_digits": "cardLast4Digits",
                "type": "CARD",
            },
            integrations=[
                {
                    "id": "id",
                    "synced_entity_id": "syncedEntityId",
                    "vendor_identifier": "AUTH0",
                }
            ],
            metadata={"foo": "string"},
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stigg) -> None:
        response = client.v1.customers.with_raw_response.create(
            email="dev@stainless.com",
            external_id="externalId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stigg) -> None:
        with client.v1.customers.with_streaming_response.create(
            email="dev@stainless.com",
            external_id="externalId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Stigg) -> None:
        customer = client.v1.customers.retrieve(
            "x",
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Stigg) -> None:
        response = client.v1.customers.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Stigg) -> None:
        with client.v1.customers.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.customers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Stigg) -> None:
        customer = client.v1.customers.update(
            id="x",
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Stigg) -> None:
        customer = client.v1.customers.update(
            id="x",
            email="dev@stainless.com",
            integrations=[
                {
                    "id": "id",
                    "synced_entity_id": "syncedEntityId",
                    "vendor_identifier": "AUTH0",
                }
            ],
            metadata={"foo": "string"},
            name="name",
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Stigg) -> None:
        response = client.v1.customers.with_raw_response.update(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Stigg) -> None:
        with client.v1.customers.with_streaming_response.update(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.customers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        customer = client.v1.customers.list()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        customer = client.v1.customers.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerListResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_archive(self, client: Stigg) -> None:
        customer = client.v1.customers.archive(
            "x",
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Stigg) -> None:
        response = client.v1.customers.with_raw_response.archive(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Stigg) -> None:
        with client.v1.customers.with_streaming_response.archive(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.customers.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unarchive(self, client: Stigg) -> None:
        customer = client.v1.customers.unarchive(
            "x",
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unarchive(self, client: Stigg) -> None:
        response = client.v1.customers.with_raw_response.unarchive(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unarchive(self, client: Stigg) -> None:
        with client.v1.customers.with_streaming_response.unarchive(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unarchive(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.customers.with_raw_response.unarchive(
                "",
            )


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStigg) -> None:
        customer = await async_client.v1.customers.create(
            email="dev@stainless.com",
            external_id="externalId",
            name="name",
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStigg) -> None:
        customer = await async_client.v1.customers.create(
            email="dev@stainless.com",
            external_id="externalId",
            name="name",
            default_payment_method={
                "billing_id": "billingId",
                "card_expiry_month": 0,
                "card_expiry_year": 0,
                "card_last4_digits": "cardLast4Digits",
                "type": "CARD",
            },
            integrations=[
                {
                    "id": "id",
                    "synced_entity_id": "syncedEntityId",
                    "vendor_identifier": "AUTH0",
                }
            ],
            metadata={"foo": "string"},
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.with_raw_response.create(
            email="dev@stainless.com",
            external_id="externalId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.with_streaming_response.create(
            email="dev@stainless.com",
            external_id="externalId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStigg) -> None:
        customer = await async_client.v1.customers.retrieve(
            "x",
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.customers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncStigg) -> None:
        customer = await async_client.v1.customers.update(
            id="x",
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStigg) -> None:
        customer = await async_client.v1.customers.update(
            id="x",
            email="dev@stainless.com",
            integrations=[
                {
                    "id": "id",
                    "synced_entity_id": "syncedEntityId",
                    "vendor_identifier": "AUTH0",
                }
            ],
            metadata={"foo": "string"},
            name="name",
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.with_raw_response.update(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.with_streaming_response.update(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.customers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        customer = await async_client.v1.customers.list()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        customer = await async_client.v1.customers.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerListResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncStigg) -> None:
        customer = await async_client.v1.customers.archive(
            "x",
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.with_raw_response.archive(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.with_streaming_response.archive(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.customers.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unarchive(self, async_client: AsyncStigg) -> None:
        customer = await async_client.v1.customers.unarchive(
            "x",
        )
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.with_raw_response.unarchive(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.with_streaming_response.unarchive(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.customers.with_raw_response.unarchive(
                "",
            )
