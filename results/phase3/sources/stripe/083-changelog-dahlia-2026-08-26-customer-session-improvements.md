# Adds the ability to query entitlements and launch the customer portal in Customer Sessions

## What’s new

Expands the [Customer Session](https://docs.stripe.com/api/customer_sessions.md?api-version=2026-08-26.dahlia) object to support the following new components:

- `customer_portal`: Redirects a customer to their customer portal from the session so they can manage their subscriptions and payments.
- `active_entitlements`: Shows a customer their active entitlements within the customer session.

## Impact

You can now create a [Customer Session](https://docs.stripe.com/api/customer_sessions/create.md?api-version=2026-08-26.dahlia) on your server with the `customer_portal` or `active_entitlements` components enabled, then pass its `client_secret` to your client application. A client that holds the `client_secret` can:

- Retrieve the customer’s [active Entitlements](https://docs.stripe.com/api/entitlements/active-entitlement.md?api-version=2026-08-26.dahlia) to gate access to features in your application.
- Open the Stripe-hosted [customer portal](https://docs.stripe.com/customer-management/integrate-customer-portal.md) for that customer so they can manage their subscriptions, payment methods and billing information. Your application presents the portal as an in-app sheet or in a browser, and the customer returns to your application when they’re done.

These components don’t change the behaviour of the Payment Element. To get started, see [Manage subscriptions on iOS](https://docs.stripe.com/billing/subscriptions/manage-ios.md).

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `customer_portal` | Added | [CustomerSession#create.components](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components), [CustomerSession.components](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components) |
| `active_entitlements` | Added | [CustomerSession#create.components](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components), [CustomerSession.components](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customer_portal` | Added | [CustomerSession::Component](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSession::CreateParams::Component](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |
| `active_entitlements` | Added | [CustomerSession::Component](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSession::CreateParams::Component](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customer_portal` | Added | [CustomerSession.Component](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSession.CreateParamsComponent](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |
| `active_entitlements` | Added | [CustomerSession.Component](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSession.CreateParamsComponent](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customer_portal` | Added | [CustomerSession.components](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSession.create().$params.component](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |
| `active_entitlements` | Added | [CustomerSession.components](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSession.create().$params.component](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customerPortal` | Added | [CustomerSession.components](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSessionCreateParams.components](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |
| `activeEntitlements` | Added | [CustomerSession.components](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSessionCreateParams.components](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customer_portal` | Added | [CustomerSession.components](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSessionCreateParams.components](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |
| `active_entitlements` | Added | [CustomerSession.components](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSessionCreateParams.components](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CustomerPortal` | Added | [CustomerSessionComponents](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSessionComponentsParams](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |
| `ActiveEntitlements` | Added | [CustomerSessionComponents](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSessionComponentsParams](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CustomerPortal` | Added | [CustomerSession.Components](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSessionComponentsOptions](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |
| `ActiveEntitlements` | Added | [CustomerSession.Components](/api/customer_sessions/object?api-version=2026-08-26.dahlia#customer_session_object-components), [CustomerSessionComponentsOptions](/api/customer_sessions/create?api-version=2026-08-26.dahlia#create_customer_session-components) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-08-26.dahlia`
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

- [Adds a customer update deep link for billing portal sessions](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-a-customer-update-deep-link-for-billing-portal-sessions.md)
- [Adds frozen fields property to Invoice Items](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-frozen-fields-property-to-invoice-items.md)
- [Adds support for the Billie payment method for invoices and subscriptions](https://docs.stripe.com/changelog/dahlia/2026-08-26/billie-support-for-invoices-and-subscriptions.md)
- [Increases the subscription item limit](https://docs.stripe.com/changelog/dahlia/2026-08-26/flexible-subscription-item-limits.md)
