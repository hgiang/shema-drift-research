# Partially capturing or cancelling payments no longer creates a Refund

## What’s new

The following flows no longer result in a `Refund` object created and linked to the payment:

- Partial capture
- Payment cancellation (both manual and automated)

## Why is this a breaking change?

This change might break your integration in the following scenarios:

- If your integration expects a partial capture or payment cancellation to create a refund object.
- If your integration expects a partial capture to create two balance transactions.

For more details about possible effects on your integration, see the following breakdown.

## Impact

This change affects your integration if you depend on the `Refund` object or any related fields for capture reversals or for payment cancellation. Removal of the `Refund` object affects the following fields or objects.

### Refund object

- A `Refund` object representing the cancellation or capture reversal will no longer be created.
- It won’t be returned when calling to get all refunds associated with the payment intent or charge.
- It won’t be present in any webhook events.
- It won’t be present on the `Charge` object in any API response.
- It won’t be visible on the Dashboard.

### PaymentIntent Object

- A new `cancellation_reason` value called `expired` will be introduced. This new value represents payments cancelled because of authorisation expiry. It replaces the formerly used value of `automatic`.

### Charge object

- `amount_captured` will be 0 instead of `nil` in payment cancellation flows.
- `amount_refunded` will no longer be updated by these actions.
- `refunded` will no longer be `true` for payment cancellation flows.

### Balance transactions

- There will only be a single balance transaction for partial captures. There will no longer be a balance transaction representing the amount and fees reversed.
- The balance transaction representing the capture will show the amount captured instead of the amount authorised for the related payment.

### Webhooks

- We’ll no longer send `charge.refunded` and `charge.refund.updated` events.
- We’ll still send `charge.expired`, `charge.captured`, and `payment_intent.canceled` events for their respective flows.

### Radar payment review

- If applicable, a Radar payment review will be closed upon payment cancellation with the reason `canceled` instead of `refunded`.

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `canceled` | Added | [Review.closed_reason](/api/radar/reviews/object?api-version=2025-03-31.basil#review_object-closed_reason) |
| `expired` | Added | [PaymentIntent.cancellation_reason](/api/payment_intents/cancel?api-version=2025-03-31.basil#cancel_payment_intent-cancellation_reason) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `canceled` | Added | [Review.closed_reason](/api/radar/reviews/object?api-version=2025-03-31.basil#review_object-closed_reason) |
| `expired` | Added | [PaymentIntent.cancellation_reason](/api/payment_intents/cancel?api-version=2025-03-31.basil#cancel_payment_intent-cancellation_reason) |

#### PHP

| Values | Change | Enums |
| --- | --- | --- |
| `canceled` | Added | [Review.closed_reason](/api/radar/reviews/object?api-version=2025-03-31.basil#review_object-closed_reason) |
| `expired` | Added | [PaymentIntent.cancellation_reason](/api/payment_intents/cancel?api-version=2025-03-31.basil#cancel_payment_intent-cancellation_reason) |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `canceled` | Added | [Review.closed_reason](/api/radar/reviews/object?api-version=2025-03-31.basil#review_object-closed_reason) |
| `expired` | Added | [PaymentIntent.cancellation_reason](/api/payment_intents/cancel?api-version=2025-03-31.basil#cancel_payment_intent-cancellation_reason) |

#### Go

| Values | Change | Enums |
| --- | --- | --- |
| `canceled` | Added | [Review.ClosedReason](/api/radar/reviews/object?api-version=2025-03-31.basil#review_object-closed_reason) |
| `expired` | Added | [PaymentIntent.CancellationReason](/api/payment_intents/cancel?api-version=2025-03-31.basil#cancel_payment_intent-cancellation_reason) |

#### .NET

This change doesn’t affect the .NET SDK.

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

## Related changes

- [Updates the Vault and Forward API to return a 402 status code for upstream request timeouts](https://docs.stripe.com/changelog/basil/2025-03-31/vault-forward-api-returns-402.md)
- [Removes manual capture method for Interac cards](https://docs.stripe.com/changelog/basil/2025-03-31/deprecate-interac-present-manual-capture-method.md)
- [Payment Methods won’t allow modifying fields for Naver Pay after the object is first created](https://docs.stripe.com/changelog/basil/2025-03-31/naver-pay-payment-method.md)
- [Adds support for Klarna in the hosted invoice page](https://docs.stripe.com/changelog/basil/2025-03-31/klarna-send-invoice.md)
- [Adds ability to configure saved payment methods for one-time payments on the hosted invoice page](https://docs.stripe.com/changelog/basil/2025-03-31/hosted-payment-method-save.md)
- [Adds support for saving and reusing Naver Pay payment methods](https://docs.stripe.com/changelog/basil/2025-03-31/naver-pay-recurring.md)
- [Adds support for the Billie local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/add-billie.md)
- [Adds support for the Satispay local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/satispay-lpm.md)
- [Makes the client parameter optional for WeChat Pay until confirmation](https://docs.stripe.com/changelog/basil/2025-03-31/lient-param-optional-wechatpay-before-confirmation.md)
- [Adds support for the New Zealand BECS Direct Debit local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/nz-bank-account.md)
