# Adds an amount confirmation parameter to the Payment Intent API

## What’s new

Adds the [amount_to_confirm](https://docs.stripe.com/api/payment_intents/confirm.md?api-version=2026-04-22.preview#confirm_payment_intent-amount_to_confirm) parameter for secret key callers to the [Payment Intents](https://docs.stripe.com/api/payment_intents.md?api-version=2026-04-22.preview) API. This parameter allows you to specify the exact amount to confirm on a PaymentIntent. If not provided, the parameter defaults to the PaymentIntent’s [amount](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-04-22.preview#payment_intent_object-amount) value.

## Impact

You can now reference the `amount_to_confirm` parameter when building integrations that require confirming PaymentIntents with amounts that differ from the original amount. For example, you can [pad the amount with a surcharge](https://docs.stripe.com/payments/cards/surcharge.md#confirm-the-payment-with-a-surcharge) when confirming PaymentIntents.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `amount_to_confirm` | Added | [PaymentIntent#confirm](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `amount_to_confirm` | Added | [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `amount_to_confirm` | Added | [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `amount_to_confirm` | Added | [PaymentIntent.confirm().$params](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `amountToConfirm` | Added | [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `amount_to_confirm` | Added | [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AmountToConfirm` | Added | [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AmountToConfirm` | Added | [PaymentIntentConfirmOptions](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-04-22.preview`
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
