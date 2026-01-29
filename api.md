# V1

## Customers

Types:

```python
from stigg.types.v1 import CustomerResponse, CustomerListResponse, CustomerImportResponse
```

Methods:

- <code title="get /api/v1/customers/{id}">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="patch /api/v1/customers/{id}">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">update</a>(id, \*\*<a href="src/stigg/types/v1/customer_update_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="get /api/v1/customers">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">list</a>(\*\*<a href="src/stigg/types/v1/customer_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_list_response.py">SyncMyCursorIDPage[CustomerListResponse]</a></code>
- <code title="post /api/v1/customers/{id}/archive">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">archive</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="post /api/v1/customers/import">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">import\_</a>(\*\*<a href="src/stigg/types/v1/customer_import_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_import_response.py">CustomerImportResponse</a></code>
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
    PromotionalEntitlementGrantResponse,
    PromotionalEntitlementRevokeResponse,
)
```

Methods:

- <code title="post /api/v1/customers/{customerId}/promotional">client.v1.customers.promotional_entitlements.<a href="./src/stigg/resources/v1/customers/promotional_entitlements.py">grant</a>(customer_id, \*\*<a href="src/stigg/types/v1/customers/promotional_entitlement_grant_params.py">params</a>) -> <a href="./src/stigg/types/v1/customers/promotional_entitlement_grant_response.py">PromotionalEntitlementGrantResponse</a></code>
- <code title="delete /api/v1/customers/{customerId}/promotional/{featureId}">client.v1.customers.promotional_entitlements.<a href="./src/stigg/resources/v1/customers/promotional_entitlements.py">revoke</a>(feature_id, \*, customer_id) -> <a href="./src/stigg/types/v1/customers/promotional_entitlement_revoke_response.py">PromotionalEntitlementRevokeResponse</a></code>

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

## Coupons

Types:

```python
from stigg.types.v1 import Coupon, CouponListResponse
```

Methods:

- <code title="post /api/v1/coupons">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">create</a>(\*\*<a href="src/stigg/types/v1/coupon_create_params.py">params</a>) -> <a href="./src/stigg/types/v1/coupon.py">Coupon</a></code>
- <code title="get /api/v1/coupons/{id}">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/coupon.py">Coupon</a></code>
- <code title="get /api/v1/coupons">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">list</a>(\*\*<a href="src/stigg/types/v1/coupon_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/coupon_list_response.py">SyncMyCursorIDPage[CouponListResponse]</a></code>

## Events

Types:

```python
from stigg.types.v1 import EventReportResponse
```

Methods:

- <code title="post /api/v1/events">client.v1.events.<a href="./src/stigg/resources/v1/events.py">report</a>(\*\*<a href="src/stigg/types/v1/event_report_params.py">params</a>) -> <a href="./src/stigg/types/v1/event_report_response.py">EventReportResponse</a></code>

## Usage

Types:

```python
from stigg.types.v1 import UsageHistoryResponse, UsageReportResponse
```

Methods:

- <code title="get /api/v1/usage/{customerId}/history/{featureId}">client.v1.usage.<a href="./src/stigg/resources/v1/usage.py">history</a>(feature_id, \*, customer_id, \*\*<a href="src/stigg/types/v1/usage_history_params.py">params</a>) -> <a href="./src/stigg/types/v1/usage_history_response.py">UsageHistoryResponse</a></code>
- <code title="post /api/v1/usage">client.v1.usage.<a href="./src/stigg/resources/v1/usage.py">report</a>(\*\*<a href="src/stigg/types/v1/usage_report_params.py">params</a>) -> <a href="./src/stigg/types/v1/usage_report_response.py">UsageReportResponse</a></code>
