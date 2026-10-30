# Adds surcharge configuration options for card-not-present payments

## What’s new

Adds the ability to configure surcharge validation for card-not-present payments using the new [amount_details.surcharge.enforce_validation](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-03-25.preview#create_payment_intent-amount_details-surcharge-enforce_validation) parameter on Payment Intents. It can have the following values:

- `automatic`: Validation is enforced, but can be changed. If you don’t specify a value, this behaviour is the default.
- `disabled`: Validation isn’t enforced. You can’t change this value.
- `enabled`: Validation is enforced. You can’t change this value.

Also adds the [amount_details.surcharge.amount](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-03-25.preview#payment_intent_object-amount_details-surcharge-amount) property.

When creating Payment Intents for payments with surcharges, you pass the total amount inclusive of the surcharge rather than calculating it separately. Surcharge parameters are available on the [create](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-03-25.preview), [update](https://docs.stripe.com/api/payment_intents/update.md?api-version=2026-03-25.preview), [confirm](https://docs.stripe.com/api/payment_intents/confirm.md?api-version=2026-03-25.preview), and [capture](https://docs.stripe.com/api/payment_intents/capture.md?api-version=2026-03-25.preview) methods.

## Impact

When you create, update, confirm or capture a Payment Intent and specify a surcharge, include the surcharge amount in the total amount and identify the surcharge amount in the [amount_details.surcharge.amount](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-03-25.preview#payment_intent_object-amount_details-surcharge-amount) parameter.

You can also now configure validation enforcement for card-not-present payments with surcharges by specifying the [amount_details.surcharge.enforce_validation](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-03-25.preview#payment_intent_object-amount_details-surcharge-enforce_validation) parameter. If you set the parameter to `enabled` or `disabled`, you can’t change it. Setting it to `automatic` enables validation enforcement, but can be changed.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `surcharge` | Added | [PaymentIntent#capture.amount_details](/api/payment_intents/capture?api-version=2026-03-25.preview#capture_payment_intent-amount_details), [PaymentIntent#confirm.amount_details](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-amount_details), [PaymentIntent#create.amount_details](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-amount_details), [PaymentIntent#update.amount_details](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-amount_details), [PaymentIntent.amount_details](/api/payment_intents/object?api-version=2026-03-25.preview#payment_intent_object-amount_details) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `surcharge` | Added | [PaymentIntent::AmountDetail](/api/payment_intents/object?api-version=2026-03-25.preview#payment_intent_object-amount_details), [PaymentIntentCaptureParams::AmountDetail](/api/payment_intents/capture?api-version=2026-03-25.preview#capture_payment_intent-amount_details), [PaymentIntentConfirmParams::AmountDetail](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-amount_details), [PaymentIntentCreateParams::AmountDetail](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-amount_details), [PaymentIntentUpdateParams::AmountDetail](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-amount_details) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `surcharge` | Added | [PaymentIntent.AmountDetail](/api/payment_intents/object?api-version=2026-03-25.preview#payment_intent_object-amount_details), [PaymentIntentCaptureParamsAmountDetail](/api/payment_intents/capture?api-version=2026-03-25.preview#capture_payment_intent-amount_details), [PaymentIntentConfirmParamsAmountDetail](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-amount_details), [PaymentIntentCreateParamsAmountDetail](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-amount_details), [PaymentIntentModifyParamsAmountDetail](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-amount_details) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `surcharge` | Added | [PaymentIntent.amount_details](/api/payment_intents/object?api-version=2026-03-25.preview#payment_intent_object-amount_details), [PaymentIntent.capture().$params.amount_detail](/api/payment_intents/capture?api-version=2026-03-25.preview#capture_payment_intent-amount_details), [PaymentIntent.confirm().$params.amount_detail](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-amount_details), [PaymentIntent.create().$params.amount_detail](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-amount_details), [PaymentIntent.update().$params.amount_detail](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-amount_details) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `surcharge` | Added | [PaymentIntent.amount_details](/api/payment_intents/object?api-version=2026-03-25.preview#payment_intent_object-amount_details), [PaymentIntentCaptureParams.amount_details](/api/payment_intents/capture?api-version=2026-03-25.preview#capture_payment_intent-amount_details), [PaymentIntentConfirmParams.amount_details](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-amount_details), [PaymentIntentCreateParams.amount_details](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-amount_details), [PaymentIntentUpdateParams.amount_details](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-amount_details) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `surcharge` | Added | [PaymentIntent.amount_details](/api/payment_intents/object?api-version=2026-03-25.preview#payment_intent_object-amount_details), [PaymentIntentCaptureParams.amount_details](/api/payment_intents/capture?api-version=2026-03-25.preview#capture_payment_intent-amount_details), [PaymentIntentConfirmParams.amount_details](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-amount_details), [PaymentIntentCreateParams.amount_details](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-amount_details), [PaymentIntentUpdateParams.amount_details](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-amount_details) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Surcharge` | Added | [PaymentIntentAmountDetails](/api/payment_intents/object?api-version=2026-03-25.preview#payment_intent_object-amount_details), [PaymentIntentAmountDetailsParams](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-amount_details), [PaymentIntentCaptureAmountDetailsParams](/api/payment_intents/capture?api-version=2026-03-25.preview#capture_payment_intent-amount_details), [PaymentIntentConfirmAmountDetailsParams](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-amount_details), [PaymentIntentUpdateAmountDetailsParams](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-amount_details) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Surcharge` | Added | [PaymentIntent.AmountDetail](/api/payment_intents/object?api-version=2026-03-25.preview#payment_intent_object-amount_details), [PaymentIntentCaptureParamsAmountDetail](/api/payment_intents/capture?api-version=2026-03-25.preview#capture_payment_intent-amount_details), [PaymentIntentConfirmParamsAmountDetail](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-amount_details), [PaymentIntentCreateParamsAmountDetail](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-amount_details), [PaymentIntentModifyParamsAmountDetail](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-amount_details) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-03-25.preview`
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

- [Removes the source type property from Stripe balance payment methods](https://docs.stripe.com/changelog/dahlia/2026-03-25/stripe-balance-payment-method-source-type.md)
- [Adds Risk Reserved Balance to the Balances API](https://docs.stripe.com/changelog/dahlia/2026-03-25/adds-risk-reserved-balance-to-the-balances-api.md)
