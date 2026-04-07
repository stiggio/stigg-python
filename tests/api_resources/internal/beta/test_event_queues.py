# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.internal.beta import (
    EventQueueResponse,
    EventQueueListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEventQueues:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Stigg) -> None:
        event_queue = client.internal.beta.event_queues.retrieve(
            "x",
        )
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Stigg) -> None:
        response = client.internal.beta.event_queues.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_queue = response.parse()
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Stigg) -> None:
        with client.internal.beta.event_queues.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_queue = response.parse()
            assert_matches_type(EventQueueResponse, event_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_name` but received ''"):
            client.internal.beta.event_queues.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Stigg) -> None:
        event_queue = client.internal.beta.event_queues.update(
            queue_name="x",
        )
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Stigg) -> None:
        event_queue = client.internal.beta.event_queues.update(
            queue_name="x",
            allowed_assume_role_arns=["string"],
            create_low_priority_queues=True,
            event_types=["MEMBER_INVITED"],
        )
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Stigg) -> None:
        response = client.internal.beta.event_queues.with_raw_response.update(
            queue_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_queue = response.parse()
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Stigg) -> None:
        with client.internal.beta.event_queues.with_streaming_response.update(
            queue_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_queue = response.parse()
            assert_matches_type(EventQueueResponse, event_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_name` but received ''"):
            client.internal.beta.event_queues.with_raw_response.update(
                queue_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        event_queue = client.internal.beta.event_queues.list()
        assert_matches_type(EventQueueListResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.internal.beta.event_queues.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_queue = response.parse()
        assert_matches_type(EventQueueListResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.internal.beta.event_queues.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_queue = response.parse()
            assert_matches_type(EventQueueListResponse, event_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Stigg) -> None:
        event_queue = client.internal.beta.event_queues.delete(
            "x",
        )
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Stigg) -> None:
        response = client.internal.beta.event_queues.with_raw_response.delete(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_queue = response.parse()
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Stigg) -> None:
        with client.internal.beta.event_queues.with_streaming_response.delete(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_queue = response.parse()
            assert_matches_type(EventQueueResponse, event_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_name` but received ''"):
            client.internal.beta.event_queues.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_provision(self, client: Stigg) -> None:
        event_queue = client.internal.beta.event_queues.provision(
            region="us-east-1",
        )
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_provision_with_all_params(self, client: Stigg) -> None:
        event_queue = client.internal.beta.event_queues.provision(
            region="us-east-1",
            allowed_assume_role_arns=["string"],
            create_low_priority_queues=True,
            event_types=["MEMBER_INVITED"],
            suffix="suffix",
        )
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_provision(self, client: Stigg) -> None:
        response = client.internal.beta.event_queues.with_raw_response.provision(
            region="us-east-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_queue = response.parse()
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_provision(self, client: Stigg) -> None:
        with client.internal.beta.event_queues.with_streaming_response.provision(
            region="us-east-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_queue = response.parse()
            assert_matches_type(EventQueueResponse, event_queue, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEventQueues:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStigg) -> None:
        event_queue = await async_client.internal.beta.event_queues.retrieve(
            "x",
        )
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStigg) -> None:
        response = await async_client.internal.beta.event_queues.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_queue = await response.parse()
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStigg) -> None:
        async with async_client.internal.beta.event_queues.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_queue = await response.parse()
            assert_matches_type(EventQueueResponse, event_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_name` but received ''"):
            await async_client.internal.beta.event_queues.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncStigg) -> None:
        event_queue = await async_client.internal.beta.event_queues.update(
            queue_name="x",
        )
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStigg) -> None:
        event_queue = await async_client.internal.beta.event_queues.update(
            queue_name="x",
            allowed_assume_role_arns=["string"],
            create_low_priority_queues=True,
            event_types=["MEMBER_INVITED"],
        )
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStigg) -> None:
        response = await async_client.internal.beta.event_queues.with_raw_response.update(
            queue_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_queue = await response.parse()
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStigg) -> None:
        async with async_client.internal.beta.event_queues.with_streaming_response.update(
            queue_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_queue = await response.parse()
            assert_matches_type(EventQueueResponse, event_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_name` but received ''"):
            await async_client.internal.beta.event_queues.with_raw_response.update(
                queue_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        event_queue = await async_client.internal.beta.event_queues.list()
        assert_matches_type(EventQueueListResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.internal.beta.event_queues.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_queue = await response.parse()
        assert_matches_type(EventQueueListResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.internal.beta.event_queues.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_queue = await response.parse()
            assert_matches_type(EventQueueListResponse, event_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncStigg) -> None:
        event_queue = await async_client.internal.beta.event_queues.delete(
            "x",
        )
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStigg) -> None:
        response = await async_client.internal.beta.event_queues.with_raw_response.delete(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_queue = await response.parse()
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStigg) -> None:
        async with async_client.internal.beta.event_queues.with_streaming_response.delete(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_queue = await response.parse()
            assert_matches_type(EventQueueResponse, event_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_name` but received ''"):
            await async_client.internal.beta.event_queues.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_provision(self, async_client: AsyncStigg) -> None:
        event_queue = await async_client.internal.beta.event_queues.provision(
            region="us-east-1",
        )
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_provision_with_all_params(self, async_client: AsyncStigg) -> None:
        event_queue = await async_client.internal.beta.event_queues.provision(
            region="us-east-1",
            allowed_assume_role_arns=["string"],
            create_low_priority_queues=True,
            event_types=["MEMBER_INVITED"],
            suffix="suffix",
        )
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_provision(self, async_client: AsyncStigg) -> None:
        response = await async_client.internal.beta.event_queues.with_raw_response.provision(
            region="us-east-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_queue = await response.parse()
        assert_matches_type(EventQueueResponse, event_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_provision(self, async_client: AsyncStigg) -> None:
        async with async_client.internal.beta.event_queues.with_streaming_response.provision(
            region="us-east-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_queue = await response.parse()
            assert_matches_type(EventQueueResponse, event_queue, path=["response"])

        assert cast(Any, response.is_closed) is True
