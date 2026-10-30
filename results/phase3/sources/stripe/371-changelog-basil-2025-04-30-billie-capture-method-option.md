# Adds capture method option to Billie payments

## What’s new

Adds support for specifying the [capture_method](https://docs.stripe.com/api/payment_intents/object.md?api-version=2025-04-30.basil#payment_intent_object-capture_method) for [Billie](https://docs.stripe.com/payments/billie.md) as a payment method option.

## Impact

You can now accept [Billie](https://docs.stripe.com/payments/billie.md) payments if your integration relies on supplying `capture_method` as a payment method option on a per-payment method basis.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `billie` | Added | [PaymentIntent#confirm.payment_method_options](/api/payment_intents/confirm?api-version=2025-04-30.basil#confirm_payment_intent-payment_method_options), [PaymentIntent#create.payment_method_options](/api/payment_intents/create?api-version=2025-04-30.basil#create_payment_intent-payment_method_options), [PaymentIntent#update.payment_method_options](/api/payment_intents/update?api-version=2025-04-30.basil#update_payment_intent-payment_method_options), [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-payment_method_options) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billie` | Added | `PaymentIntent::ConfirmParams::PaymentMethodOption`, `PaymentIntent::CreateParams::PaymentMethodOption`, `PaymentIntent::PaymentMethodOption`, `PaymentIntent::UpdateParams::PaymentMethodOption` |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billie` | Added | `PaymentIntent.ConfirmParamsPaymentMethodOption`, `PaymentIntent.CreateParamsPaymentMethodOption`, `PaymentIntent.PaymentMethodOption`, `PaymentIntent.UpdateParamsPaymentMethodOption` |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billie` | Added | [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-payment_method_options), [PaymentIntentConfirmParams.payment_method_options](/api/payment_intents/confirm?api-version=2025-04-30.basil#confirm_payment_intent-payment_method_options), [PaymentIntentCreateParams.payment_method_options](/api/payment_intents/create?api-version=2025-04-30.basil#create_payment_intent-payment_method_options), [PaymentIntentUpdateParams.payment_method_options](/api/payment_intents/update?api-version=2025-04-30.basil#update_payment_intent-payment_method_options) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billie` | Added | [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-payment_method_options), [PaymentIntentConfirmParams.payment_method_options](/api/payment_intents/confirm?api-version=2025-04-30.basil#confirm_payment_intent-payment_method_options), [PaymentIntentCreateParams.payment_method_options](/api/payment_intents/create?api-version=2025-04-30.basil#create_payment_intent-payment_method_options), [PaymentIntentUpdateParams.payment_method_options](/api/payment_intents/update?api-version=2025-04-30.basil#update_payment_intent-payment_method_options) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Billie` | Added | [PaymentIntentConfirmPaymentMethodOptionsParams](/api/payment_intents/confirm?api-version=2025-04-30.basil#confirm_payment_intent-payment_method_options), [PaymentIntentPaymentMethodOptionsParams](/api/payment_intents/create?api-version=2025-04-30.basil#create_payment_intent-payment_method_options), [PaymentIntentPaymentMethodOptions](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-payment_method_options) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Billie` | Added | [PaymentIntentPaymentMethodOptionsOptions](/api/payment_intents/create?api-version=2025-04-30.basil#create_payment_intent-payment_method_options), [PaymentIntentPaymentMethodOptions](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-payment_method_options) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-04-30.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.1.0](https://github.com/stripe/stripe-python/releases/tag/v12.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.2.0](https://github.com/stripe/stripe-php/releases/tag/v17.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.1.0](https://github.com/stripe/stripe-java/releases/tag/v29.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.1.0](https://github.com/stripe/stripe-node/releases/tag/v18.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.1.0](https://github.com/stripe/stripe-go/releases/tag/v82.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds Affirm as a supported payment method for one-off invoices and subscriptions](https://docs.stripe.com/changelog/basil/2025-04-30/affirm-send-invoice.md)
- [Adds tax ID to Payment Method billing details](https://docs.stripe.com/changelog/basil/2025-04-30/add-tax-id-to-billing-details.md)
- [Adds Pix to payment method configurations](https://docs.stripe.com/changelog/basil/2025-04-30/add_pix_to_payment_method_configuration.md)
