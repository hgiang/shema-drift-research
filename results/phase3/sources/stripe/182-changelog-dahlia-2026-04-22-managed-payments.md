# Adds support for Managed Payments, Stripe's merchant of record solution

## What’s new

Adds support for [Managed Payments](https://docs.stripe.com/payments/managed-payments.md), Stripe’s merchant of record solution, to [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md?api-version=2026-04-22.dahlia) and [Payment Links](https://docs.stripe.com/api/payment-link.md?api-version=2026-04-22.dahlia). When you set [managed_payments.enabled](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-04-22.dahlia#create_checkout_session-managed_payments-enabled) to `true`, Stripe handles indirect tax compliance (in more than 80 countries), fraud prevention, dispute management and transaction-level customer support.

## Impact

You can now enable [Managed Payments](https://docs.stripe.com/payments/managed-payments.md) when selling digital products such as SaaS, software, and digital content or downloads. Managed Payments handles indirect tax compliance, fraud prevention, dispute management, and transaction-level customer support.

When you enable Managed Payments, Stripe automatically manages [certain parameters](https://docs.stripe.com/payments/managed-payments/update-checkout.md#remove-unsupported-parameters) related to Connect, tax configuration, and shipping. You can’t manually specify those parameters.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `managed_payments` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object), [PaymentLink#create](/api/payment-link/create?api-version=2026-04-22.dahlia#create_payment_link), [Checkout.Session#create](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session), [PaymentIntent](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object), [PaymentLink](/api/payment-link/object?api-version=2026-04-22.dahlia#payment_link_object), [Subscription](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object), [SetupIntent](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `managed_payments` | Added | [Checkout::SessionCreateParams](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session), [SetupIntent](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object), [PaymentLinkCreateParams](/api/payment-link/create?api-version=2026-04-22.dahlia#create_payment_link), [Subscription](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object), [PaymentIntent](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object), [PaymentLink](/api/payment-link/object?api-version=2026-04-22.dahlia#payment_link_object), [Checkout::Session](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `managed_payments` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object), [checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session), [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object), [PaymentLink](/api/payment-link/object?api-version=2026-04-22.dahlia#payment_link_object), [Subscription](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object), [SetupIntent](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object), [PaymentLinkCreateParams](/api/payment-link/create?api-version=2026-04-22.dahlia#create_payment_link) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `managed_payments` | Added | [PaymentLink](/api/payment-link/object?api-version=2026-04-22.dahlia#payment_link_object), [SetupIntent](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object), [Checkout\Session.create().$params](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session), [Subscription](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object), [PaymentIntent](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object), [PaymentLink.create().$params](/api/payment-link/create?api-version=2026-04-22.dahlia#create_payment_link), [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `managedPayments` | Added | [checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object), [Subscription](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object), [PaymentLink](/api/payment-link/object?api-version=2026-04-22.dahlia#payment_link_object), [checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session), [PaymentIntent](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object), [SetupIntent](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object), [PaymentLinkCreateParams](/api/payment-link/create?api-version=2026-04-22.dahlia#create_payment_link) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `managed_payments` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object), [SetupIntent](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object), [Checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session), [PaymentLink](/api/payment-link/object?api-version=2026-04-22.dahlia#payment_link_object), [Subscription](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object), [PaymentIntent](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object), [PaymentLinkCreateParams](/api/payment-link/create?api-version=2026-04-22.dahlia#create_payment_link) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `ManagedPayments` | Added | [CheckoutSession](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object), [PaymentLink](/api/payment-link/object?api-version=2026-04-22.dahlia#payment_link_object), [CheckoutSessionParams](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session), [PaymentLinkParams](/api/payment-link/create?api-version=2026-04-22.dahlia#create_payment_link), [Subscription](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object), [SetupIntent](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object), [PaymentIntent](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `ManagedPayments` | Added | [PaymentLinkCreateOptions](/api/payment-link/create?api-version=2026-04-22.dahlia#create_payment_link), [PaymentIntent](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object), [Checkout.SessionCreateOptions](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session), [SetupIntent](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object), [PaymentLink](/api/payment-link/object?api-version=2026-04-22.dahlia#payment_link_object), [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object), [Subscription](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-04-22.dahlia`
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

- [Adds support for Sunbit, a Buy Now, Pay Later payment method](https://docs.stripe.com/changelog/dahlia/2026-04-22/sunbit-buy-now-pay-later-support.md)
- [Adds support for Pix recurring payments](https://docs.stripe.com/changelog/dahlia/2026-04-22/pix-recurring-payments-support.md)
- [Adds the moto property to Setup Attempt payment method details for cards](https://docs.stripe.com/changelog/dahlia/2026-04-22/setup-attempt-payment-method-details-for-cards-moto.md)
- [Adds QR code support for Klarna payments with Terminal readers](https://docs.stripe.com/changelog/dahlia/2026-04-22/klarna-payments-with-terminal-readers-qr-code-support.md)
