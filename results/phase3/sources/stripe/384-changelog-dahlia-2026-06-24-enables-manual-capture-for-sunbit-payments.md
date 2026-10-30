# Enables manual capture for Sunbit payments

## What’s new

Adds support for manual capture for [Sunbit](https://docs.stripe.com/payments/sunbit.md) payments. You can now set the [capture_method](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-06-24.dahlia#create_payment_intent-capture_method) parameter to `manual` when creating a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md?api-version=2026-06-24.dahlia) that uses Sunbit as the payment method. This allows you to authorise the payment first and capture it at a later time, giving you more control over when funds are collected from your customer.

Previously, Sunbit payments only supported automatic capture, where funds were collected immediately upon authorisation.

## Impact

You can now use manual capture workflows with Sunbit payments, enabling use cases such as:

- Authorising payments before shipping products
- Implementing delayed capture for marketplace scenarios
- Managing inventory and fulfilment processes before collecting funds

To use manual capture, set the `capture_method` parameter to `manual` when creating the `PaymentIntent`, then call the [capture endpoint](https://docs.stripe.com/api/payment_intents/capture.md?api-version=2026-06-24.dahlia) when you’re ready to collect the funds. Alternatively, you can set `payment_method_options.sunbit.capture_method` to `manual` when creating a `PaymentIntent` to use manual capture only if Sunbit is selected. To use manual capture in a Checkout Session, set the `payment_intent_data.capture_method` to `manual` when calling the [create endpoint](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-05-27.dahlia#create_checkout_session-payment_intent_data-capture_method), then call the capture endpoint when you’re ready to collect the funds.

Manual capture must occur within the payment method’s authorisation window.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `sunbit` | Added | [PaymentIntent#confirm.payment_method_options](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options), [PaymentIntent#create.payment_method_options](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options), [PaymentIntent#update.payment_method_options](/api/payment_intents/update?api-version=2026-06-24.dahlia#update_payment_intent-payment_method_options), [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sunbit` | Added | [PaymentIntent::PaymentMethodOption](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options), [PaymentIntentConfirmParams::PaymentMethodOption](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options), [PaymentIntentCreateParams::PaymentMethodOption](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options), [PaymentIntentUpdateParams::PaymentMethodOption](/api/payment_intents/update?api-version=2026-06-24.dahlia#update_payment_intent-payment_method_options) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sunbit` | Added | [PaymentIntent.PaymentMethodOption](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options), [PaymentIntentConfirmParamsPaymentMethodOption](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options), [PaymentIntentCreateParamsPaymentMethodOption](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options), [PaymentIntentModifyParamsPaymentMethodOption](/api/payment_intents/update?api-version=2026-06-24.dahlia#update_payment_intent-payment_method_options) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sunbit` | Added | [PaymentIntent.confirm().$params.payment_method_option](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options), [PaymentIntent.create().$params.payment_method_option](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options), [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options), [PaymentIntent.update().$params.payment_method_option](/api/payment_intents/update?api-version=2026-06-24.dahlia#update_payment_intent-payment_method_options) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sunbit` | Added | [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options), [PaymentIntentConfirmParams.payment_method_options](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options), [PaymentIntentCreateParams.payment_method_options](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options), [PaymentIntentUpdateParams.payment_method_options](/api/payment_intents/update?api-version=2026-06-24.dahlia#update_payment_intent-payment_method_options) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sunbit` | Added | [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options), [PaymentIntentConfirmParams.payment_method_options](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options), [PaymentIntentCreateParams.payment_method_options](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options), [PaymentIntentUpdateParams.payment_method_options](/api/payment_intents/update?api-version=2026-06-24.dahlia#update_payment_intent-payment_method_options) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Sunbit` | Added | [PaymentIntentConfirmPaymentMethodOptionsParams](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options), [PaymentIntentPaymentMethodOptions](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options), [PaymentIntentPaymentMethodOptionsParams](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Sunbit` | Added | [PaymentIntent.PaymentMethodOptions](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options), [PaymentIntentPaymentMethodOptionsOptions](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-06-24.dahlia`
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

- [Adds buyer ID support for Bizum payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/bizum-payments-buyer-id.md)
- [Adds buyer ID support for BLIK payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/blik-payments-buyer-id.md)
- [Adds a fingerprint to Pix payment method details](https://docs.stripe.com/changelog/dahlia/2026-06-24/pix-fingerprint-payment-method-details.md)
- [Adds transaction link ID to card payment method details for Mastercard and Maestro transactions](https://docs.stripe.com/changelog/dahlia/2026-06-24/card-payment-method-details-transaction-link-id.md)
- [Adds payment method options for Sunbit in Checkout Sessions](https://docs.stripe.com/changelog/dahlia/2026-06-24/sunbit-checkout-pmo.md)
- [Adds support for the Sui network and USDsui token for crypto payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/sui-network-and-usdsui-token-support.md)
- [Adds support for Mastercard compliance disputes](https://docs.stripe.com/changelog/dahlia/2026-06-24/mastercard-compliance-disputes.md)
- [Adds support for recurring payments with Satispay](https://docs.stripe.com/changelog/dahlia/2026-06-24/satispay-recurring-payments.md)
