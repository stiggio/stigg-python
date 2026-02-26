# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .usage import (
    UsageResource,
    AsyncUsageResource,
    UsageResourceWithRawResponse,
    AsyncUsageResourceWithRawResponse,
    UsageResourceWithStreamingResponse,
    AsyncUsageResourceWithStreamingResponse,
)
from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .coupons import (
    CouponsResource,
    AsyncCouponsResource,
    CouponsResourceWithRawResponse,
    AsyncCouponsResourceWithRawResponse,
    CouponsResourceWithStreamingResponse,
    AsyncCouponsResourceWithStreamingResponse,
)
from .features import (
    FeaturesResource,
    AsyncFeaturesResource,
    FeaturesResourceWithRawResponse,
    AsyncFeaturesResourceWithRawResponse,
    FeaturesResourceWithStreamingResponse,
    AsyncFeaturesResourceWithStreamingResponse,
)
from .products import (
    ProductsResource,
    AsyncProductsResource,
    ProductsResourceWithRawResponse,
    AsyncProductsResourceWithRawResponse,
    ProductsResourceWithStreamingResponse,
    AsyncProductsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .plans.plans import (
    PlansResource,
    AsyncPlansResource,
    PlansResourceWithRawResponse,
    AsyncPlansResourceWithRawResponse,
    PlansResourceWithStreamingResponse,
    AsyncPlansResourceWithStreamingResponse,
)
from .addons.addons import (
    AddonsResource,
    AsyncAddonsResource,
    AddonsResourceWithRawResponse,
    AsyncAddonsResourceWithRawResponse,
    AddonsResourceWithStreamingResponse,
    AsyncAddonsResourceWithStreamingResponse,
)
from .customers.customers import (
    CustomersResource,
    AsyncCustomersResource,
    CustomersResourceWithRawResponse,
    AsyncCustomersResourceWithRawResponse,
    CustomersResourceWithStreamingResponse,
    AsyncCustomersResourceWithStreamingResponse,
)
from .subscriptions.subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def customers(self) -> CustomersResource:
        return CustomersResource(self._client)

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        return SubscriptionsResource(self._client)

    @cached_property
    def coupons(self) -> CouponsResource:
        return CouponsResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def features(self) -> FeaturesResource:
        return FeaturesResource(self._client)

    @cached_property
    def addons(self) -> AddonsResource:
        return AddonsResource(self._client)

    @cached_property
    def plans(self) -> PlansResource:
        return PlansResource(self._client)

    @cached_property
    def usage(self) -> UsageResource:
        return UsageResource(self._client)

    @cached_property
    def products(self) -> ProductsResource:
        return ProductsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def customers(self) -> AsyncCustomersResource:
        return AsyncCustomersResource(self._client)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def coupons(self) -> AsyncCouponsResource:
        return AsyncCouponsResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def features(self) -> AsyncFeaturesResource:
        return AsyncFeaturesResource(self._client)

    @cached_property
    def addons(self) -> AsyncAddonsResource:
        return AsyncAddonsResource(self._client)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        return AsyncPlansResource(self._client)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        return AsyncUsageResource(self._client)

    @cached_property
    def products(self) -> AsyncProductsResource:
        return AsyncProductsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def customers(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self._v1.customers)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self._v1.subscriptions)

    @cached_property
    def coupons(self) -> CouponsResourceWithRawResponse:
        return CouponsResourceWithRawResponse(self._v1.coupons)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._v1.events)

    @cached_property
    def features(self) -> FeaturesResourceWithRawResponse:
        return FeaturesResourceWithRawResponse(self._v1.features)

    @cached_property
    def addons(self) -> AddonsResourceWithRawResponse:
        return AddonsResourceWithRawResponse(self._v1.addons)

    @cached_property
    def plans(self) -> PlansResourceWithRawResponse:
        return PlansResourceWithRawResponse(self._v1.plans)

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
        return UsageResourceWithRawResponse(self._v1.usage)

    @cached_property
    def products(self) -> ProductsResourceWithRawResponse:
        return ProductsResourceWithRawResponse(self._v1.products)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self._v1.customers)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self._v1.subscriptions)

    @cached_property
    def coupons(self) -> AsyncCouponsResourceWithRawResponse:
        return AsyncCouponsResourceWithRawResponse(self._v1.coupons)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._v1.events)

    @cached_property
    def features(self) -> AsyncFeaturesResourceWithRawResponse:
        return AsyncFeaturesResourceWithRawResponse(self._v1.features)

    @cached_property
    def addons(self) -> AsyncAddonsResourceWithRawResponse:
        return AsyncAddonsResourceWithRawResponse(self._v1.addons)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithRawResponse:
        return AsyncPlansResourceWithRawResponse(self._v1.plans)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        return AsyncUsageResourceWithRawResponse(self._v1.usage)

    @cached_property
    def products(self) -> AsyncProductsResourceWithRawResponse:
        return AsyncProductsResourceWithRawResponse(self._v1.products)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def customers(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self._v1.customers)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self._v1.subscriptions)

    @cached_property
    def coupons(self) -> CouponsResourceWithStreamingResponse:
        return CouponsResourceWithStreamingResponse(self._v1.coupons)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._v1.events)

    @cached_property
    def features(self) -> FeaturesResourceWithStreamingResponse:
        return FeaturesResourceWithStreamingResponse(self._v1.features)

    @cached_property
    def addons(self) -> AddonsResourceWithStreamingResponse:
        return AddonsResourceWithStreamingResponse(self._v1.addons)

    @cached_property
    def plans(self) -> PlansResourceWithStreamingResponse:
        return PlansResourceWithStreamingResponse(self._v1.plans)

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        return UsageResourceWithStreamingResponse(self._v1.usage)

    @cached_property
    def products(self) -> ProductsResourceWithStreamingResponse:
        return ProductsResourceWithStreamingResponse(self._v1.products)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self._v1.customers)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self._v1.subscriptions)

    @cached_property
    def coupons(self) -> AsyncCouponsResourceWithStreamingResponse:
        return AsyncCouponsResourceWithStreamingResponse(self._v1.coupons)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._v1.events)

    @cached_property
    def features(self) -> AsyncFeaturesResourceWithStreamingResponse:
        return AsyncFeaturesResourceWithStreamingResponse(self._v1.features)

    @cached_property
    def addons(self) -> AsyncAddonsResourceWithStreamingResponse:
        return AsyncAddonsResourceWithStreamingResponse(self._v1.addons)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithStreamingResponse:
        return AsyncPlansResourceWithStreamingResponse(self._v1.plans)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        return AsyncUsageResourceWithStreamingResponse(self._v1.usage)

    @cached_property
    def products(self) -> AsyncProductsResourceWithStreamingResponse:
        return AsyncProductsResourceWithStreamingResponse(self._v1.products)
