# Adds the ability to specify the capture method for card present payments with Payment Intents

## What’s new

Adds the ability to specify the [capture_method](https://docs.stripe.com/api/payment_intents/object.md?api-version=2025-11-17.clover#payment_intent_object-payment_method_options-card_present-capture_method) in the [payment_method_options](https://docs.stripe.com/api/payment_intents/object.md?api-version=2025-11-17.clover#payment_intent_object-payment_method_options-card_present-capture_method) for card present payments using [Payment Intents](https://docs.stripe.com/api/payment_intents.md?api-version=2025-11-17.clover).

You can optionally set the capture method to one of these values:

- `manual` directs Stripe to place the funds on hold and explicitly capture the payment after authorisation. For example, you might want to wait until the order is fulfilled before capturing funds.
- `manual_preferred` directs Stripe to prioritise `manual` capture, but use `automatic` behaviour if appropriate based on the presented card’s supported network. This supports manual capturing when possible without declining when it’s not.

## Impact

You can now specify the behaviour for capturing card present payments for Payment Intents. The `capture_method` controls when to capture the funds from the customer’s account.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `capture_method` | Added | [PaymentIntent#confirm.payment_method_options.card_present](/api/payment_intents/confirm?api-version=2025-11-17.clover#confirm_payment_intent-payment_method_options-card_present), [PaymentIntent#create.payment_method_options.card_present](/api/payment_intents/create?api-version=2025-11-17.clover#create_payment_intent-payment_method_options-card_present), [PaymentIntent#update.payment_method_options.card_present](/api/payment_intents/update?api-version=2025-11-17.clover#update_payment_intent-payment_method_options-card_present), [PaymentIntent.payment_method_options.card_present](/api/payment_intents/object?api-version=2025-11-17.clover#payment_intent_object-payment_method_options-card_present) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `capture_method` | Added | [PaymentIntent::PaymentMethodOption::CardPresent](/api/payment_intents/object?api-version=2025-11-17.clover#payment_intent_object-payment_method_options-card_present), [PaymentIntentConfirmParams::PaymentMethodOption::CardPresent](/api/payment_intents/confirm?api-version=2025-11-17.clover#confirm_payment_intent-payment_method_options-card_present), [PaymentIntentCreateParams::PaymentMethodOption::CardPresent](/api/payment_intents/create?api-version=2025-11-17.clover#create_payment_intent-payment_method_options-card_present), [PaymentIntentUpdateParams::PaymentMethodOption::CardPresent](/api/payment_intents/update?api-version=2025-11-17.clover#update_payment_intent-payment_method_options-card_present) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `capture_method` | Added | [PaymentIntent.PaymentMethodOption.CardPresent](/api/payment_intents/object?api-version=2025-11-17.clover#payment_intent_object-payment_method_options-card_present), [PaymentIntentConfirmParamsPaymentMethodOptionCardPresent](/api/payment_intents/confirm?api-version=2025-11-17.clover#confirm_payment_intent-payment_method_options-card_present), [PaymentIntentCreateParamsPaymentMethodOptionCardPresent](/api/payment_intents/create?api-version=2025-11-17.clover#create_payment_intent-payment_method_options-card_present), [PaymentIntentModifyParamsPaymentMethodOptionCardPresent](/api/payment_intents/update?api-version=2025-11-17.clover#update_payment_intent-payment_method_options-card_present) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `capture_method` | Added | [PaymentIntent.confirm().$params.payment_method_option.card_present](/api/payment_intents/confirm?api-version=2025-11-17.clover#confirm_payment_intent-payment_method_options-card_present), [PaymentIntent.create().$params.payment_method_option.card_present](/api/payment_intents/create?api-version=2025-11-17.clover#create_payment_intent-payment_method_options-card_present), [PaymentIntent.payment_method_options.card_present](/api/payment_intents/object?api-version=2025-11-17.clover#payment_intent_object-payment_method_options-card_present), [PaymentIntent.update().$params.payment_method_option.card_present](/api/payment_intents/update?api-version=2025-11-17.clover#update_payment_intent-payment_method_options-card_present) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `captureMethod` | Added | [PaymentIntent.payment_method_options.card_present](/api/payment_intents/object?api-version=2025-11-17.clover#payment_intent_object-payment_method_options-card_present), [PaymentIntentConfirmParams.payment_method_options.card_present](/api/payment_intents/confirm?api-version=2025-11-17.clover#confirm_payment_intent-payment_method_options-card_present), [PaymentIntentCreateParams.payment_method_options.card_present](/api/payment_intents/create?api-version=2025-11-17.clover#create_payment_intent-payment_method_options-card_present), [PaymentIntentUpdateParams.payment_method_options.card_present](/api/payment_intents/update?api-version=2025-11-17.clover#update_payment_intent-payment_method_options-card_present) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `capture_method` | Added | [PaymentIntent.payment_method_options.card_present](/api/payment_intents/object?api-version=2025-11-17.clover#payment_intent_object-payment_method_options-card_present), [PaymentIntentConfirmParams.payment_method_options.card_present](/api/payment_intents/confirm?api-version=2025-11-17.clover#confirm_payment_intent-payment_method_options-card_present), [PaymentIntentCreateParams.payment_method_options.card_present](/api/payment_intents/create?api-version=2025-11-17.clover#create_payment_intent-payment_method_options-card_present), [PaymentIntentUpdateParams.payment_method_options.card_present](/api/payment_intents/update?api-version=2025-11-17.clover#update_payment_intent-payment_method_options-card_present) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CaptureMethod` | Added | [PaymentIntentConfirmPaymentMethodOptionsCardPresentParams](/api/payment_intents/confirm?api-version=2025-11-17.clover#confirm_payment_intent-payment_method_options-card_present), [PaymentIntentPaymentMethodOptionsCardPresent](/api/payment_intents/object?api-version=2025-11-17.clover#payment_intent_object-payment_method_options-card_present), [PaymentIntentPaymentMethodOptionsCardPresentParams](/api/payment_intents/create?api-version=2025-11-17.clover#create_payment_intent-payment_method_options-card_present) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CaptureMethod` | Added | [PaymentIntent.PaymentMethodOptions.CardPresent](/api/payment_intents/object?api-version=2025-11-17.clover#payment_intent_object-payment_method_options-card_present), [PaymentIntentPaymentMethodOptionsCardPresentOptions](/api/payment_intents/create?api-version=2025-11-17.clover#create_payment_intent-payment_method_options-card_present) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-11-17.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v17.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v17.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.2.0](https://github.com/stripe/stripe-python/releases/tag/v13.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.2.0](https://github.com/stripe/stripe-php/releases/tag/v18.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.2.0](https://github.com/stripe/stripe-java/releases/tag/v30.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.3.0](https://github.com/stripe/stripe-node/releases/tag/v19.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.2.0](https://github.com/stripe/stripe-go/releases/tag/v83.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds the transaction ID to iDEAL payment method details](https://docs.stripe.com/changelog/clover/2025-11-17/ideal-transaction-id.md)
- [Adds MB WAY and TWINT to destination details for refunds](https://docs.stripe.com/changelog/clover/2025-11-17/mb-way-twint-destination-details-for-refunds.md)
- [Adds Finom as a supported iDEAL issuer](https://docs.stripe.com/changelog/clover/2025-11-17/ideal-payments-finom.md)
