# Adds explicit session configuration options for Financial Connections

## What’s new

You can now use explicit, composable configuration parameters to control which accounts are collected and how the Financial Connections authentication flow behaves. Previously, account holder type implicitly determined session behaviour.

The following parameters are now available:

- [filters.require_payment_method_support](https://docs.stripe.com/api/financial_connections/sessions/create.md?api-version=2026-07-29.dahlia#financial_connections_create_session-filters-require_payment_method_support): Restricts account selection to payment-eligible accounts. Set to `all` to make every linked account payment-eligible, `at_least_one` to make at least one a payment account while allowing others, or `none` for no restriction.
- [limits.accounts](https://docs.stripe.com/api/financial_connections/sessions/create.md?api-version=2026-07-29.dahlia#financial_connections_create_session-limits-accounts): Sets the maximum number of accounts a user can link in a session.
- [manual_entry.mode](https://docs.stripe.com/api/financial_connections/sessions/create.md?api-version=2026-07-29.dahlia#financial_connections_create_session-manual_entry-mode): Controls whether the manual bank account entry fallback is shown during authentication. Set to `automatic` for Stripe to manage it, or `disabled` to remove the option entirely.

This change also adds a new property on the returned Session object:

- [bank_account_token](https://docs.stripe.com/api/financial_connections/sessions/object.md?api-version=2026-07-29.dahlia#financial_connections_session_object-bank_account_token): Returned when a user completes manual entry.

## Impact

Previously, Financial Connections session behaviour was implicitly tied to account holder type, rather than the user’s actual use case. Advanced session configurability replaces this with explicit, composable API parameters, making it easier for platforms to build the exact experience they need without workarounds.

You can also subscribe to [financial_connections.account.supported_payment_method_types_updated](https://docs.stripe.com/api/events/types.md?api-version=2026-07-29.dahlia#event_types-financial_connections.account.supported_payment_method_types_updated) to be notified when an account’s payment eligibility is confirmed after account number retrieval.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `limits`, `manual_entry` | Added | [FinancialConnections.Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object), [FinancialConnections.Session#create](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session) |
| `require_payment_method_support` | Added | [FinancialConnections.Session#create.filters](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session-filters), [FinancialConnections.Session.filters](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object-filters) |
| `bank_account_token` | Added | [FinancialConnections.Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object) |

| Value | Change | Enums |
| --- | --- | --- |
| `financial_connections.account.supported_payment_method_types_updated` | Added | [Event.type](/api/events/object?api-version=2026-07-29.dahlia#event_object-type), [WebhookEndpoint#update.enabled_events](/api/webhook_endpoints/update?api-version=2026-07-29.dahlia#update_webhook_endpoint-enabled_events), [WebhookEndpoint#create.enabled_events](/api/webhook_endpoints/create?api-version=2026-07-29.dahlia#create_webhook_endpoint-enabled_events) |

|  | Change | Event type |
| --- | --- | --- |
| `financial_connections.account.supported_payment_method_types_updated` | Added | `FinancialConnections.Account` |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `limits`, `manual_entry` | Added | [FinancialConnections::Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object), [FinancialConnections::SessionCreateParams](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session) |
| `require_payment_method_support` | Added | [FinancialConnections::Session::Filter](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object-filters), [FinancialConnections::SessionCreateParams::Filter](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session-filters) |
| `bank_account_token` | Added | [FinancialConnections::Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `limits`, `manual_entry` | Added | [FinancialConnections.Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object), [financial_connections.SessionCreateParams](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session) |
| `require_payment_method_support` | Added | [FinancialConnections.Session.Filter](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object-filters), [financial_connections.SessionCreateParamsFilter](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session-filters) |
| `bank_account_token` | Added | [FinancialConnections.Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object) |

| Value | Change | Enums |
| --- | --- | --- |
| `financial_connections.account.supported_payment_method_types_updated` | Added | [Event.type](/api/events/object?api-version=2026-07-29.dahlia#event_object-type), [WebhookEndpointModifyParams.enabled_events](/api/webhook_endpoints/update?api-version=2026-07-29.dahlia#update_webhook_endpoint-enabled_events), [WebhookEndpointCreateParams.enabled_events](/api/webhook_endpoints/create?api-version=2026-07-29.dahlia#create_webhook_endpoint-enabled_events) |

|  | Change | Event type |
| --- | --- | --- |
| `financial_connections.account.supported_payment_method_types_updated` | Added | `financial_connections.Account` |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `limits`, `manual_entry` | Added | [FinancialConnections.Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object), [FinancialConnections\Session.create().$params](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session) |
| `require_payment_method_support` | Added | [FinancialConnections.Session.filters](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object-filters), [FinancialConnections\Session.create().$params.filters](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session-filters) |
| `bank_account_token` | Added | [FinancialConnections.Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object) |

| Value | Change | Enum |
| --- | --- | --- |
| `financial_connections.account.supported_payment_method_types_updated` | Added | [Event.type](/api/events/object?api-version=2026-07-29.dahlia#event_object-type) |

|  | Change | Event type |
| --- | --- | --- |
| `FINANCIAL_CONNECTIONS_ACCOUNT_SUPPORTED_PAYMENT_METHOD_TYPES_UPDATED` | Added | `FinancialConnections.Account` |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `limits`, `manualEntry` | Added | [financialconnections.Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object), [financialconnections.SessionCreateParams](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session) |
| `requirePaymentMethodSupport` | Added | [financialconnections.Session.filters](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object-filters), [financialconnections.SessionCreateParams.filters](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session-filters) |
| `bankAccountToken` | Added | [financialconnections.Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object) |

| Value | Change | Enums |
| --- | --- | --- |
| `financial_connections.account.supported_payment_method_types_updated` | Added | [WebhookEndpointUpdateParams.enabledEvents](/api/webhook_endpoints/update?api-version=2026-07-29.dahlia#update_webhook_endpoint-enabledEvents), [WebhookEndpointCreateParams.enabledEvents](/api/webhook_endpoints/create?api-version=2026-07-29.dahlia#create_webhook_endpoint-enabledEvents) |

|  | Change | Event type |
| --- | --- | --- |
| `financial_connections.account.supported_payment_method_types_updated` | Added | `financialconnections.Account` |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `limits`, `manual_entry` | Added | [FinancialConnections.Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object), [FinancialConnections.SessionCreateParams](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session) |
| `require_payment_method_support` | Added | [FinancialConnections.Session.filters](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object-filters), [FinancialConnections.SessionCreateParams.filters](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session-filters) |
| `bank_account_token` | Added | [FinancialConnections.Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object) |

| Value | Change | Enums |
| --- | --- | --- |
| `financial_connections.account.supported_payment_method_types_updated` | Added | [Event.type](/api/events/object?api-version=2026-07-29.dahlia#event_object-type), [WebhookEndpointUpdateParams.enabled_events](/api/webhook_endpoints/update?api-version=2026-07-29.dahlia#update_webhook_endpoint-enabled_events), [WebhookEndpointCreateParams.enabled_events](/api/webhook_endpoints/create?api-version=2026-07-29.dahlia#create_webhook_endpoint-enabled_events) |

|  | Change | Event type |
| --- | --- | --- |
| `FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent` | Added | `FinancialConnections.Account` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Limits`, `ManualEntry` | Added | [FinancialConnectionsSession](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object), [FinancialConnectionsSessionParams](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session) |
| `RequirePaymentMethodSupport` | Added | [FinancialConnectionsSessionFilters](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object-filters), [FinancialConnectionsSessionFiltersParams](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session-filters) |
| `BankAccountToken` | Added | [FinancialConnectionsSession](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object) |

| Value | Change | Enum |
| --- | --- | --- |
| `financial_connections.account.supported_payment_method_types_updated` | Added | [Event.Type](/api/events/object?api-version=2026-07-29.dahlia#event_object-Type) |

|  | Change | Event type |
| --- | --- | --- |
| `EventTypeFinancialConnectionsAccountSupportedPaymentMethodTypesUpdated` | Added | `FinancialConnectionsAccount` |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Limits`, `ManualEntry` | Added | [FinancialConnections.Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object), [FinancialConnections.SessionCreateOptions](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session) |
| `RequirePaymentMethodSupport` | Added | [FinancialConnections.Session.Filters](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object-filters), [FinancialConnectionsSessionFiltersOptions](/api/financial_connections/sessions/create?api-version=2026-07-29.dahlia#financial_connections_create_session-filters) |
| `BankAccountToken` | Added | [FinancialConnections.Session](/api/financial_connections/sessions/object?api-version=2026-07-29.dahlia#financial_connections_session_object) |

|  | Change | Event type |
| --- | --- | --- |
| `FinancialConnectionsAccountSupportedPaymentMethodTypesUpdated` | Added | `FinancialConnections.Account` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-07-29.dahlia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds deactivation event notifications for Financial Connections accounts and authorisations](https://docs.stripe.com/changelog/dahlia/2026-07-29/financial-connections-deactivation-event-notifications.md)
