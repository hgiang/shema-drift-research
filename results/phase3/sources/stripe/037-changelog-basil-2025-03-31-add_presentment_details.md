# Adds presentment details for Adaptive Pricing

## What’s new

Adds a [presentment_details](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-03-31.basil#checkout_session_object-presentment_details) object to the Checkout Session to provide information about the currency and amount presented to customers when Adaptive Pricing was used on a Checkout Session.

## Impact

A [recent update](https://support.stripe.com/questions/adaptive-pricing-product-improvements) to Adaptive Pricing maintains Checkout Session [currency](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-03-31.basil#checkout_session_object-currency) in the same currency as your Stripe integration, with context about the customer’s choice now available under Checkout Session [presentment_details](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-03-31.basil#checkout_session_object-presentment_details) when Adaptive Pricing is used. Previously, [currency](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-03-31.basil#checkout_session_object-currency) was the customer’s choice of currency and the currency of your Stripe integration was described under [currency_conversion](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-03-31.basil#checkout_session_object-currency_conversion).

We plan to remove the legacy [currency_conversion](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-03-31.basil#checkout_session_object-currency-conversion) field from the Checkout Session resource in a future release. To prepare, update your integration by replacing references to [currency_conversion.source_currency](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-03-31.basil#checkout_session_object-currency_conversion-source_currency) with Checkout Session [currency](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-03-31.basil#checkout_session_object-currency), and [currency_conversion.amount_total](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-03-31.basil#checkout_session_object-currency_conversion-amount_total) with Checkout Session [amount_total](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-03-31.basil#checkout_session_object-amount_total). For information about the currency selected by your customer, see [presentment_details](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-03-31.basil#checkout_session_object-presentment_details).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `presentment_details` | Added | [Charge](/api/charges/object?api-version=2025-03-31.basil), [Checkout.Session](/api/checkout/sessions/object?api-version=2025-03-31.basil), [PaymentIntent](/api/payment_intents/object?api-version=2025-03-31.basil), `Refund` |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `presentment_details` | Added | [Charge](/api/charges/object?api-version=2025-03-31.basil), `CheckoutSession`, [PaymentIntent](/api/payment_intents/object?api-version=2025-03-31.basil), `Refund` |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `presentment_details` | Added | [Charge](/api/charges/object?api-version=2025-03-31.basil), [Checkout.Session](/api/checkout/sessions/object?api-version=2025-03-31.basil), [PaymentIntent](/api/payment_intents/object?api-version=2025-03-31.basil), `Refund` |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `presentmentDetails` | Added | [Charge](/api/charges/object?api-version=2025-03-31.basil), [Checkout.Session](/api/checkout/sessions/object?api-version=2025-03-31.basil), [PaymentIntent](/api/payment_intents/object?api-version=2025-03-31.basil), `Refund` |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `presentment_details` | Added | [Charge](/api/charges/object?api-version=2025-03-31.basil), [Checkout.Session](/api/checkout/sessions/object?api-version=2025-03-31.basil), [PaymentIntent](/api/payment_intents/object?api-version=2025-03-31.basil), `Refund` |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PresentmentDetails` | Added | [Charge](/api/charges/object?api-version=2025-03-31.basil), [CheckoutSession](/api/checkout/sessions/object?api-version=2025-03-31.basil), [PaymentIntent](/api/payment_intents/object?api-version=2025-03-31.basil), `Refund` |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PresentmentDetails` | Added | [Charge](/api/charges/object?api-version=2025-03-31.basil), [CheckoutSession](/api/checkout/sessions/object?api-version=2025-03-31.basil), [PaymentIntent](/api/payment_intents/object?api-version=2025-03-31.basil), `Refund` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-03-31.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.0.0](https://github.com/stripe/stripe-python/releases/tag/v12.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.0.0](https://github.com/stripe/stripe-php/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.0.0](https://github.com/stripe/stripe-java/releases/tag/v29.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.0.0](https://github.com/stripe/stripe-node/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.0.0](https://github.com/stripe/stripe-go/releases/tag/v82.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
