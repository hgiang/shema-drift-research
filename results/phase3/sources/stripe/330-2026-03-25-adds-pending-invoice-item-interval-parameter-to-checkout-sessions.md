# Adds pending invoice item interval parameter to create Checkout Sessions

## What’s new

Adds the [pending_invoice_item_interval](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-03-25.dahlia#create_checkout_session-subscription_data-pending_invoice_item_interval) parameter to the [create CheckoutSession](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-03-25.dahlia) endpoint. Use it to specify the billing frequency for [pending invoice items](https://docs.stripe.com/billing/invoices/subscription.md#Customize) when using [Checkout](https://docs.stripe.com/payments/checkout.md) with [subscriptions](https://docs.stripe.com/subscriptions.md). You can specify `day`, `week`, `month`, or `year`.

## Impact

You can now configure the billing interval for pending invoice items when creating subscription-based payments in [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md?api-version=2026-03-25.dahlia). That allows you to invoice pending items on a different schedule than the subscription cycle without needing to [update the Subscription](https://docs.stripe.com/api/subscriptions/update.md?api-version=2026-03-25.dahlia#update_subscription-pending_invoice_item_interval) after the Checkout Session completes.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `pending_invoice_item_interval` | Added | [Checkout.Session#create.subscription_data](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-subscription_data) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pending_invoice_item_interval` | Added | [Checkout::SessionCreateParams::SubscriptionDatum](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-subscription_data) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pending_invoice_item_interval` | Added | [checkout.SessionCreateParamsSubscriptionDatum](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-subscription_data) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pending_invoice_item_interval` | Added | [Checkout\Session.create().$params.subscription_datum](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-subscription_data) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pendingInvoiceItemInterval` | Added | [checkout.SessionCreateParams.subscription_data](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-subscription_data) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pending_invoice_item_interval` | Added | [Checkout.SessionCreateParams.subscription_data](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-subscription_data) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PendingInvoiceItemInterval` | Added | [CheckoutSessionSubscriptionDataParams](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-subscription_data) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PendingInvoiceItemInterval` | Added | [CheckoutSessionSubscriptionDataOptions](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-subscription_data) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-03-25.dahlia`
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

- [Updates Checkout Session UI mode enum values](https://docs.stripe.com/changelog/dahlia/2026-03-25/updates-available-checkout-session-ui-modes.md)
- [Adds integration identifier parameter to Checkout Sessions](https://docs.stripe.com/changelog/dahlia/2026-03-25/adds-integration-identifier-parameter-to-checkout-sessions.md)
