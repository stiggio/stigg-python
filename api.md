# V1

## Customers

Types:

```python
from stigg.types.v1 import (
    CustomerResponse,
    CustomerListResponse,
    CustomerImportResponse,
    CustomerListResourcesResponse,
)
```

Methods:

- <code title="get /api/v1/customers/{id}">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="patch /api/v1/customers/{id}">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">update</a>(id, \*\*<a href="src/stigg/types/v1/customer_update_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="get /api/v1/customers">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">list</a>(\*\*<a href="src/stigg/types/v1/customer_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_list_response.py">SyncMyCursorIDPage[CustomerListResponse]</a></code>
- <code title="post /api/v1/customers/{id}/archive">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">archive</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="post /api/v1/customers/import">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">import\_</a>(\*\*<a href="src/stigg/types/v1/customer_import_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_import_response.py">CustomerImportResponse</a></code>
- <code title="get /api/v1/customers/{id}/resources">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">list_resources</a>(id, \*\*<a href="src/stigg/types/v1/customer_list_resources_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_list_resources_response.py">SyncMyCursorIDPage[CustomerListResourcesResponse]</a></code>
- <code title="post /api/v1/customers">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">provision</a>(\*\*<a href="src/stigg/types/v1/customer_provision_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="post /api/v1/customers/{id}/unarchive">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">unarchive</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>

### PaymentMethod

Methods:

- <code title="post /api/v1/customers/{id}/payment-method">client.v1.customers.payment_method.<a href="./src/stigg/resources/v1/customers/payment_method.py">attach</a>(id, \*\*<a href="src/stigg/types/v1/customers/payment_method_attach_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="delete /api/v1/customers/{id}/payment-method">client.v1.customers.payment_method.<a href="./src/stigg/resources/v1/customers/payment_method.py">detach</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>

### PromotionalEntitlements

Types:

```python
from stigg.types.v1.customers import (
    PromotionalEntitlementCreateResponse,
    PromotionalEntitlementListResponse,
    PromotionalEntitlementRevokeResponse,
)
```

Methods:

- <code title="post /api/v1/customers/{id}/promotional-entitlements">client.v1.customers.promotional_entitlements.<a href="./src/stigg/resources/v1/customers/promotional_entitlements.py">create</a>(id, \*\*<a href="src/stigg/types/v1/customers/promotional_entitlement_create_params.py">params</a>) -> <a href="./src/stigg/types/v1/customers/promotional_entitlement_create_response.py">PromotionalEntitlementCreateResponse</a></code>
- <code title="get /api/v1/customers/{id}/promotional-entitlements">client.v1.customers.promotional_entitlements.<a href="./src/stigg/resources/v1/customers/promotional_entitlements.py">list</a>(id, \*\*<a href="src/stigg/types/v1/customers/promotional_entitlement_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/customers/promotional_entitlement_list_response.py">SyncMyCursorIDPage[PromotionalEntitlementListResponse]</a></code>
- <code title="delete /api/v1/customers/{id}/promotional-entitlements/{featureId}">client.v1.customers.promotional_entitlements.<a href="./src/stigg/resources/v1/customers/promotional_entitlements.py">revoke</a>(feature_id, \*, id) -> <a href="./src/stigg/types/v1/customers/promotional_entitlement_revoke_response.py">PromotionalEntitlementRevokeResponse</a></code>

## Subscriptions

Types:

```python
from stigg.types.v1 import (
    Subscription,
    SubscriptionListResponse,
    SubscriptionImportResponse,
    SubscriptionPreviewResponse,
    SubscriptionProvisionResponse,
)
```

Methods:

- <code title="get /api/v1/subscriptions/{id}">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/subscription.py">Subscription</a></code>
- <code title="patch /api/v1/subscriptions/{id}">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">update</a>(id, \*\*<a href="src/stigg/types/v1/subscription_update_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription.py">Subscription</a></code>
- <code title="get /api/v1/subscriptions">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">list</a>(\*\*<a href="src/stigg/types/v1/subscription_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_list_response.py">SyncMyCursorIDPage[SubscriptionListResponse]</a></code>
- <code title="post /api/v1/subscriptions/{id}/cancel">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">cancel</a>(id, \*\*<a href="src/stigg/types/v1/subscription_cancel_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription.py">Subscription</a></code>
- <code title="post /api/v1/subscriptions/{id}/delegate">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">delegate</a>(id, \*\*<a href="src/stigg/types/v1/subscription_delegate_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription.py">Subscription</a></code>
- <code title="post /api/v1/subscriptions/import">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">import\_</a>(\*\*<a href="src/stigg/types/v1/subscription_import_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_import_response.py">SubscriptionImportResponse</a></code>
- <code title="post /api/v1/subscriptions/{id}/migrate">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">migrate</a>(id, \*\*<a href="src/stigg/types/v1/subscription_migrate_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription.py">Subscription</a></code>
- <code title="post /api/v1/subscriptions/preview">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">preview</a>(\*\*<a href="src/stigg/types/v1/subscription_preview_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_preview_response.py">SubscriptionPreviewResponse</a></code>
- <code title="post /api/v1/subscriptions">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">provision</a>(\*\*<a href="src/stigg/types/v1/subscription_provision_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_provision_response.py">SubscriptionProvisionResponse</a></code>
- <code title="post /api/v1/subscriptions/{id}/transfer">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">transfer</a>(id, \*\*<a href="src/stigg/types/v1/subscription_transfer_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription.py">Subscription</a></code>

### FutureUpdate

Types:

```python
from stigg.types.v1.subscriptions import CancelSubscription
```

Methods:

- <code title="delete /api/v1/subscriptions/{id}/future-update/pending-payment">client.v1.subscriptions.future_update.<a href="./src/stigg/resources/v1/subscriptions/future_update.py">cancel_pending_payment</a>(id) -> <a href="./src/stigg/types/v1/subscriptions/cancel_subscription.py">CancelSubscription</a></code>
- <code title="delete /api/v1/subscriptions/{id}/future-update/schedule">client.v1.subscriptions.future_update.<a href="./src/stigg/resources/v1/subscriptions/future_update.py">cancel_schedule</a>(id) -> <a href="./src/stigg/types/v1/subscriptions/cancel_subscription.py">CancelSubscription</a></code>

### Usage

Types:

```python
from stigg.types.v1.subscriptions import UsageChargeUsageResponse, UsageSyncResponse
```

Methods:

- <code title="post /api/v1/subscriptions/{id}/usage/charge">client.v1.subscriptions.usage.<a href="./src/stigg/resources/v1/subscriptions/usage.py">charge_usage</a>(id, \*\*<a href="src/stigg/types/v1/subscriptions/usage_charge_usage_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscriptions/usage_charge_usage_response.py">UsageChargeUsageResponse</a></code>
- <code title="post /api/v1/subscriptions/{id}/usage/sync">client.v1.subscriptions.usage.<a href="./src/stigg/resources/v1/subscriptions/usage.py">sync</a>(id) -> <a href="./src/stigg/types/v1/subscriptions/usage_sync_response.py">UsageSyncResponse</a></code>

### Invoice

Types:

```python
from stigg.types.v1.subscriptions import InvoiceMarkAsPaidResponse
```

Methods:

- <code title="post /api/v1/subscriptions/{id}/invoice/paid">client.v1.subscriptions.invoice.<a href="./src/stigg/resources/v1/subscriptions/invoice.py">mark_as_paid</a>(id) -> <a href="./src/stigg/types/v1/subscriptions/invoice_mark_as_paid_response.py">InvoiceMarkAsPaidResponse</a></code>

## Coupons

Types:

```python
from stigg.types.v1 import Coupon, CouponListResponse
```

Methods:

- <code title="post /api/v1/coupons">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">create</a>(\*\*<a href="src/stigg/types/v1/coupon_create_params.py">params</a>) -> <a href="./src/stigg/types/v1/coupon.py">Coupon</a></code>
- <code title="get /api/v1/coupons/{id}">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/coupon.py">Coupon</a></code>
- <code title="get /api/v1/coupons">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">list</a>(\*\*<a href="src/stigg/types/v1/coupon_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/coupon_list_response.py">SyncMyCursorIDPage[CouponListResponse]</a></code>
- <code title="post /api/v1/coupons/{id}/archive">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">archive_coupon</a>(id) -> <a href="./src/stigg/types/v1/coupon.py">Coupon</a></code>
- <code title="patch /api/v1/coupons/{id}">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">update_coupon</a>(id, \*\*<a href="src/stigg/types/v1/coupon_update_coupon_params.py">params</a>) -> <a href="./src/stigg/types/v1/coupon.py">Coupon</a></code>

## Events

Types:

```python
from stigg.types.v1 import EventReportResponse
```

Methods:

- <code title="post /api/v1/events">client.v1.events.<a href="./src/stigg/resources/v1/events.py">report</a>(\*\*<a href="src/stigg/types/v1/event_report_params.py">params</a>) -> <a href="./src/stigg/types/v1/event_report_response.py">EventReportResponse</a></code>

## Features

Types:

```python
from stigg.types.v1 import Feature, FeatureListFeaturesResponse
```

Methods:

- <code title="post /api/v1/features/{id}/archive">client.v1.features.<a href="./src/stigg/resources/v1/features.py">archive_feature</a>(id) -> <a href="./src/stigg/types/v1/feature.py">Feature</a></code>
- <code title="post /api/v1/features">client.v1.features.<a href="./src/stigg/resources/v1/features.py">create_feature</a>(\*\*<a href="src/stigg/types/v1/feature_create_feature_params.py">params</a>) -> <a href="./src/stigg/types/v1/feature.py">Feature</a></code>
- <code title="get /api/v1/features">client.v1.features.<a href="./src/stigg/resources/v1/features.py">list_features</a>(\*\*<a href="src/stigg/types/v1/feature_list_features_params.py">params</a>) -> <a href="./src/stigg/types/v1/feature_list_features_response.py">SyncMyCursorIDPage[FeatureListFeaturesResponse]</a></code>
- <code title="get /api/v1/features/{id}">client.v1.features.<a href="./src/stigg/resources/v1/features.py">retrieve_feature</a>(id) -> <a href="./src/stigg/types/v1/feature.py">Feature</a></code>
- <code title="post /api/v1/features/{id}/unarchive">client.v1.features.<a href="./src/stigg/resources/v1/features.py">unarchive_feature</a>(id) -> <a href="./src/stigg/types/v1/feature.py">Feature</a></code>
- <code title="patch /api/v1/features/{id}">client.v1.features.<a href="./src/stigg/resources/v1/features.py">update_feature</a>(id, \*\*<a href="src/stigg/types/v1/feature_update_feature_params.py">params</a>) -> <a href="./src/stigg/types/v1/feature.py">Feature</a></code>

## Addons

Types:

```python
from stigg.types.v1 import (
    Addon,
    SetPackagePricing,
    SetPackagePricingResponse,
    AddonListResponse,
    AddonPublishResponse,
    AddonRemoveDraftResponse,
)
```

Methods:

- <code title="post /api/v1/addons">client.v1.addons.<a href="./src/stigg/resources/v1/addons/addons.py">create</a>(\*\*<a href="src/stigg/types/v1/addon_create_params.py">params</a>) -> <a href="./src/stigg/types/v1/addon.py">Addon</a></code>
- <code title="get /api/v1/addons/{id}">client.v1.addons.<a href="./src/stigg/resources/v1/addons/addons.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/addon.py">Addon</a></code>
- <code title="patch /api/v1/addons/{id}">client.v1.addons.<a href="./src/stigg/resources/v1/addons/addons.py">update</a>(id, \*\*<a href="src/stigg/types/v1/addon_update_params.py">params</a>) -> <a href="./src/stigg/types/v1/addon.py">Addon</a></code>
- <code title="get /api/v1/addons">client.v1.addons.<a href="./src/stigg/resources/v1/addons/addons.py">list</a>(\*\*<a href="src/stigg/types/v1/addon_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/addon_list_response.py">SyncMyCursorIDPage[AddonListResponse]</a></code>
- <code title="post /api/v1/addons/{id}/archive">client.v1.addons.<a href="./src/stigg/resources/v1/addons/addons.py">archive</a>(id) -> <a href="./src/stigg/types/v1/addon.py">Addon</a></code>
- <code title="post /api/v1/addons/{id}/draft">client.v1.addons.<a href="./src/stigg/resources/v1/addons/addons.py">create_draft</a>(id) -> <a href="./src/stigg/types/v1/addon.py">Addon</a></code>
- <code title="post /api/v1/addons/{id}/publish">client.v1.addons.<a href="./src/stigg/resources/v1/addons/addons.py">publish</a>(id, \*\*<a href="src/stigg/types/v1/addon_publish_params.py">params</a>) -> <a href="./src/stigg/types/v1/addon_publish_response.py">AddonPublishResponse</a></code>
- <code title="delete /api/v1/addons/{id}/draft">client.v1.addons.<a href="./src/stigg/resources/v1/addons/addons.py">remove_draft</a>(id) -> <a href="./src/stigg/types/v1/addon_remove_draft_response.py">AddonRemoveDraftResponse</a></code>
- <code title="put /api/v1/addons/{id}/charges">client.v1.addons.<a href="./src/stigg/resources/v1/addons/addons.py">set_pricing</a>(id, \*\*<a href="src/stigg/types/v1/addon_set_pricing_params.py">params</a>) -> <a href="./src/stigg/types/v1/set_package_pricing_response.py">SetPackagePricingResponse</a></code>

### Entitlements

Types:

```python
from stigg.types.v1.addons import (
    AddonPackageEntitlement,
    EntitlementCreateResponse,
    EntitlementListResponse,
)
```

Methods:

- <code title="post /api/v1/addons/{addonId}/entitlements">client.v1.addons.entitlements.<a href="./src/stigg/resources/v1/addons/entitlements.py">create</a>(addon_id, \*\*<a href="src/stigg/types/v1/addons/entitlement_create_params.py">params</a>) -> <a href="./src/stigg/types/v1/addons/entitlement_create_response.py">EntitlementCreateResponse</a></code>
- <code title="patch /api/v1/addons/{addonId}/entitlements/{id}">client.v1.addons.entitlements.<a href="./src/stigg/resources/v1/addons/entitlements.py">update</a>(id, \*, addon_id, \*\*<a href="src/stigg/types/v1/addons/entitlement_update_params.py">params</a>) -> <a href="./src/stigg/types/v1/addons/addon_package_entitlement.py">AddonPackageEntitlement</a></code>
- <code title="get /api/v1/addons/{addonId}/entitlements">client.v1.addons.entitlements.<a href="./src/stigg/resources/v1/addons/entitlements.py">list</a>(addon_id) -> <a href="./src/stigg/types/v1/addons/entitlement_list_response.py">EntitlementListResponse</a></code>
- <code title="delete /api/v1/addons/{addonId}/entitlements/{id}">client.v1.addons.entitlements.<a href="./src/stigg/resources/v1/addons/entitlements.py">delete</a>(id, \*, addon_id) -> <a href="./src/stigg/types/v1/addons/addon_package_entitlement.py">AddonPackageEntitlement</a></code>

## Plans

Types:

```python
from stigg.types.v1 import Plan, PlanListResponse, PlanPublishResponse, PlanRemoveDraftResponse
```

Methods:

- <code title="post /api/v1/plans">client.v1.plans.<a href="./src/stigg/resources/v1/plans/plans.py">create</a>(\*\*<a href="src/stigg/types/v1/plan_create_params.py">params</a>) -> <a href="./src/stigg/types/v1/plan.py">Plan</a></code>
- <code title="get /api/v1/plans/{id}">client.v1.plans.<a href="./src/stigg/resources/v1/plans/plans.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/plan.py">Plan</a></code>
- <code title="patch /api/v1/plans/{id}">client.v1.plans.<a href="./src/stigg/resources/v1/plans/plans.py">update</a>(id, \*\*<a href="src/stigg/types/v1/plan_update_params.py">params</a>) -> <a href="./src/stigg/types/v1/plan.py">Plan</a></code>
- <code title="get /api/v1/plans">client.v1.plans.<a href="./src/stigg/resources/v1/plans/plans.py">list</a>(\*\*<a href="src/stigg/types/v1/plan_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/plan_list_response.py">SyncMyCursorIDPage[PlanListResponse]</a></code>
- <code title="post /api/v1/plans/{id}/archive">client.v1.plans.<a href="./src/stigg/resources/v1/plans/plans.py">archive</a>(id) -> <a href="./src/stigg/types/v1/plan.py">Plan</a></code>
- <code title="post /api/v1/plans/{id}/draft">client.v1.plans.<a href="./src/stigg/resources/v1/plans/plans.py">create_draft</a>(id) -> <a href="./src/stigg/types/v1/plan.py">Plan</a></code>
- <code title="post /api/v1/plans/{id}/publish">client.v1.plans.<a href="./src/stigg/resources/v1/plans/plans.py">publish</a>(id, \*\*<a href="src/stigg/types/v1/plan_publish_params.py">params</a>) -> <a href="./src/stigg/types/v1/plan_publish_response.py">PlanPublishResponse</a></code>
- <code title="delete /api/v1/plans/{id}/draft">client.v1.plans.<a href="./src/stigg/resources/v1/plans/plans.py">remove_draft</a>(id) -> <a href="./src/stigg/types/v1/plan_remove_draft_response.py">PlanRemoveDraftResponse</a></code>
- <code title="put /api/v1/plans/{id}/charges">client.v1.plans.<a href="./src/stigg/resources/v1/plans/plans.py">set_pricing</a>(id, \*\*<a href="src/stigg/types/v1/plan_set_pricing_params.py">params</a>) -> <a href="./src/stigg/types/v1/set_package_pricing_response.py">SetPackagePricingResponse</a></code>

### Entitlements

Types:

```python
from stigg.types.v1.plans import PlanEntitlement, EntitlementCreateResponse, EntitlementListResponse
```

Methods:

- <code title="post /api/v1/plans/{planId}/entitlements">client.v1.plans.entitlements.<a href="./src/stigg/resources/v1/plans/entitlements.py">create</a>(plan_id, \*\*<a href="src/stigg/types/v1/plans/entitlement_create_params.py">params</a>) -> <a href="./src/stigg/types/v1/plans/entitlement_create_response.py">EntitlementCreateResponse</a></code>
- <code title="patch /api/v1/plans/{planId}/entitlements/{id}">client.v1.plans.entitlements.<a href="./src/stigg/resources/v1/plans/entitlements.py">update</a>(id, \*, plan_id, \*\*<a href="src/stigg/types/v1/plans/entitlement_update_params.py">params</a>) -> <a href="./src/stigg/types/v1/plans/plan_entitlement.py">PlanEntitlement</a></code>
- <code title="get /api/v1/plans/{planId}/entitlements">client.v1.plans.entitlements.<a href="./src/stigg/resources/v1/plans/entitlements.py">list</a>(plan_id) -> <a href="./src/stigg/types/v1/plans/entitlement_list_response.py">EntitlementListResponse</a></code>
- <code title="delete /api/v1/plans/{planId}/entitlements/{id}">client.v1.plans.entitlements.<a href="./src/stigg/resources/v1/plans/entitlements.py">delete</a>(id, \*, plan_id) -> <a href="./src/stigg/types/v1/plans/plan_entitlement.py">PlanEntitlement</a></code>

## Usage

Types:

```python
from stigg.types.v1 import UsageHistoryResponse, UsageReportResponse
```

Methods:

- <code title="get /api/v1/usage/{customerId}/history/{featureId}">client.v1.usage.<a href="./src/stigg/resources/v1/usage.py">history</a>(feature_id, \*, customer_id, \*\*<a href="src/stigg/types/v1/usage_history_params.py">params</a>) -> <a href="./src/stigg/types/v1/usage_history_response.py">UsageHistoryResponse</a></code>
- <code title="post /api/v1/usage">client.v1.usage.<a href="./src/stigg/resources/v1/usage.py">report</a>(\*\*<a href="src/stigg/types/v1/usage_report_params.py">params</a>) -> <a href="./src/stigg/types/v1/usage_report_response.py">UsageReportResponse</a></code>

## Products

Types:

```python
from stigg.types.v1 import Product, ProductListProductsResponse
```

Methods:

- <code title="post /api/v1/products/{id}/archive">client.v1.products.<a href="./src/stigg/resources/v1/products.py">archive_product</a>(id) -> <a href="./src/stigg/types/v1/product.py">Product</a></code>
- <code title="post /api/v1/products">client.v1.products.<a href="./src/stigg/resources/v1/products.py">create_product</a>(\*\*<a href="src/stigg/types/v1/product_create_product_params.py">params</a>) -> <a href="./src/stigg/types/v1/product.py">Product</a></code>
- <code title="post /api/v1/products/{id}/duplicate">client.v1.products.<a href="./src/stigg/resources/v1/products.py">duplicate_product</a>(path_id, \*\*<a href="src/stigg/types/v1/product_duplicate_product_params.py">params</a>) -> <a href="./src/stigg/types/v1/product.py">Product</a></code>
- <code title="get /api/v1/products">client.v1.products.<a href="./src/stigg/resources/v1/products.py">list_products</a>(\*\*<a href="src/stigg/types/v1/product_list_products_params.py">params</a>) -> <a href="./src/stigg/types/v1/product_list_products_response.py">SyncMyCursorIDPage[ProductListProductsResponse]</a></code>
- <code title="post /api/v1/products/{id}/unarchive">client.v1.products.<a href="./src/stigg/resources/v1/products.py">unarchive_product</a>(id) -> <a href="./src/stigg/types/v1/product.py">Product</a></code>
- <code title="patch /api/v1/products/{id}">client.v1.products.<a href="./src/stigg/resources/v1/products.py">update_product</a>(id, \*\*<a href="src/stigg/types/v1/product_update_product_params.py">params</a>) -> <a href="./src/stigg/types/v1/product.py">Product</a></code>
