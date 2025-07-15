# V1

## Customers

Types:

```python
from stigg.types.v1 import CustomerRetrieveResponse
```

Methods:

- <code title="get /api/v1/customers/{refId}">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">retrieve</a>(ref_id) -> <a href="./src/stigg/types/v1/customer_retrieve_response.py">CustomerRetrieveResponse</a></code>

### SubCustomer

Types:

```python
from stigg.types.v1.customers import SubCustomerRetrieveResponse
```

Methods:

- <code title="get /api/v1/customers/{refId}">client.v1.customers.sub_customer.<a href="./src/stigg/resources/v1/customers/sub_customer.py">retrieve</a>(ref_id) -> <a href="./src/stigg/types/v1/customers/sub_customer_retrieve_response.py">SubCustomerRetrieveResponse</a></code>

## Permissions

Types:

```python
from stigg.types.v1 import PermissionCheckResponse
```

Methods:

- <code title="post /api/v1/permissions/check">client.v1.permissions.<a href="./src/stigg/resources/v1/permissions.py">check</a>(\*\*<a href="src/stigg/types/v1/permission_check_params.py">params</a>) -> <a href="./src/stigg/types/v1/permission_check_response.py">PermissionCheckResponse</a></code>

# V2

## Customers

Types:

```python
from stigg.types.v2 import CustomerRetrieveResponse
```

Methods:

- <code title="get /api/v1/customers/{refId}">client.v2.customers.<a href="./src/stigg/resources/v2/customers/customers.py">retrieve</a>(ref_id) -> <a href="./src/stigg/types/v2/customer_retrieve_response.py">CustomerRetrieveResponse</a></code>

### SubCustomer

Types:

```python
from stigg.types.v2.customers import SubCustomerRetrieveResponse
```

Methods:

- <code title="get /api/v1/customers/{refId}">client.v2.customers.sub_customer.<a href="./src/stigg/resources/v2/customers/sub_customer.py">retrieve</a>(ref_id) -> <a href="./src/stigg/types/v2/customers/sub_customer_retrieve_response.py">SubCustomerRetrieveResponse</a></code>

## Permissions

Types:

```python
from stigg.types.v2 import PermissionCheckResponse
```

Methods:

- <code title="post /api/v1/permissions/check">client.v2.permissions.<a href="./src/stigg/resources/v2/permissions.py">check</a>(\*\*<a href="src/stigg/types/v2/permission_check_params.py">params</a>) -> <a href="./src/stigg/types/v2/permission_check_response.py">PermissionCheckResponse</a></code>
