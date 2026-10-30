# Adds the ability to opt out of strict arithmetic validation for Payment Line Items

## What’s new

You can now opt out of strict arithmetic validation for Payment Line Items on a per-request basis by using the [amount_details.enforce_arithmetic_validation](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-01-28.clover#create_payment_intent-amount_details-enforce_arithmetic_validation) parameter.

## Impact

By default, Stripe validates that your line item data passed as part of the [Payment Line Items](https://docs.stripe.com/payments/payment-line-items.md) feature adds up correctly. When the sum of line items doesn’t match the total amount, Stripe returns a 400 error so you can correct discrepancies before processing the payment.

You can now opt out of this strict validation on a per-request basis by setting [amount_details.enforce_arithmetic_validation](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-01-28.clover#create_payment_intent-amount_details-enforce_arithmetic_validation) to `false`. When you do this:

- The request proceeds even if line item amounts don’t match the total.
- Stripe returns validation error details in the [amount_details.error](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-01-28.clover#payment_intent_object-amount_details-error) field in the response.
- For card payments, Stripe doesn’t send line item data with arithmetic errors to card networks, preventing the transaction from qualifying for L2/L3 interchange savings.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `enforce_arithmetic_validation` | Added | [PaymentIntent#capture.amount_details](/api/payment_intents/capture?api-version=2026-01-28.clover#capture_payment_intent-amount_details), [PaymentIntent#confirm.amount_details](/api/payment_intents/confirm?api-version=2026-01-28.clover#confirm_payment_intent-amount_details), [PaymentIntent#create.amount_details](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-amount_details), [PaymentIntent#increment_authorization.amount_details](/api/payment_intents/increment_authorization?api-version=2026-01-28.clover#increment_payment_intent-amount_details), [PaymentIntent#update.amount_details](/api/payment_intents/update?api-version=2026-01-28.clover#update_payment_intent-amount_details) |
| `error` | Added | [PaymentIntent.amount_details](/api/payment_intents/object?api-version=2026-01-28.clover#payment_intent_object-amount_details) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `enforce_arithmetic_validation` | Added | [PaymentIntentCaptureParams::AmountDetail](/api/payment_intents/capture?api-version=2026-01-28.clover#capture_payment_intent-amount_details), [PaymentIntentConfirmParams::AmountDetail](/api/payment_intents/confirm?api-version=2026-01-28.clover#confirm_payment_intent-amount_details), [PaymentIntentCreateParams::AmountDetail](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-amount_details), [PaymentIntentIncrementAuthorizationParams::AmountDetail](/api/payment_intents/increment_authorization?api-version=2026-01-28.clover#increment_payment_intent-amount_details), [PaymentIntentUpdateParams::AmountDetail](/api/payment_intents/update?api-version=2026-01-28.clover#update_payment_intent-amount_details) |
| `error` | Added | [PaymentIntent::AmountDetail](/api/payment_intents/object?api-version=2026-01-28.clover#payment_intent_object-amount_details) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `enforce_arithmetic_validation` | Added | [PaymentIntentCaptureParamsAmountDetail](/api/payment_intents/capture?api-version=2026-01-28.clover#capture_payment_intent-amount_details), [PaymentIntentConfirmParamsAmountDetail](/api/payment_intents/confirm?api-version=2026-01-28.clover#confirm_payment_intent-amount_details), [PaymentIntentCreateParamsAmountDetail](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-amount_details), [PaymentIntentIncrementAuthorizationParamsAmountDetail](/api/payment_intents/increment_authorization?api-version=2026-01-28.clover#increment_payment_intent-amount_details), [PaymentIntentModifyParamsAmountDetail](/api/payment_intents/update?api-version=2026-01-28.clover#update_payment_intent-amount_details) |
| `error` | Added | [PaymentIntent.AmountDetail](/api/payment_intents/object?api-version=2026-01-28.clover#payment_intent_object-amount_details) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `enforce_arithmetic_validation` | Added | [PaymentIntent.capture().$params.amount_detail](/api/payment_intents/capture?api-version=2026-01-28.clover#capture_payment_intent-amount_details), [PaymentIntent.confirm().$params.amount_detail](/api/payment_intents/confirm?api-version=2026-01-28.clover#confirm_payment_intent-amount_details), [PaymentIntent.create().$params.amount_detail](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-amount_details), [PaymentIntent.increment_authorization().$params.amount_detail](/api/payment_intents/increment_authorization?api-version=2026-01-28.clover#increment_payment_intent-amount_details), [PaymentIntent.update().$params.amount_detail](/api/payment_intents/update?api-version=2026-01-28.clover#update_payment_intent-amount_details) |
| `error` | Added | [PaymentIntent.amount_details](/api/payment_intents/object?api-version=2026-01-28.clover#payment_intent_object-amount_details) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `enforceArithmeticValidation` | Added | [PaymentIntentCaptureParams.amount_details](/api/payment_intents/capture?api-version=2026-01-28.clover#capture_payment_intent-amount_details), [PaymentIntentConfirmParams.amount_details](/api/payment_intents/confirm?api-version=2026-01-28.clover#confirm_payment_intent-amount_details), [PaymentIntentCreateParams.amount_details](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-amount_details), [PaymentIntentIncrementAuthorizationParams.amount_details](/api/payment_intents/increment_authorization?api-version=2026-01-28.clover#increment_payment_intent-amount_details), [PaymentIntentUpdateParams.amount_details](/api/payment_intents/update?api-version=2026-01-28.clover#update_payment_intent-amount_details) |
| `error` | Added | [PaymentIntent.amount_details](/api/payment_intents/object?api-version=2026-01-28.clover#payment_intent_object-amount_details) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `enforce_arithmetic_validation` | Added | [PaymentIntentCaptureParams.amount_details](/api/payment_intents/capture?api-version=2026-01-28.clover#capture_payment_intent-amount_details), [PaymentIntentConfirmParams.amount_details](/api/payment_intents/confirm?api-version=2026-01-28.clover#confirm_payment_intent-amount_details), [PaymentIntentCreateParams.amount_details](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-amount_details), [PaymentIntentIncrementAuthorizationParams.amount_details](/api/payment_intents/increment_authorization?api-version=2026-01-28.clover#increment_payment_intent-amount_details), [PaymentIntentUpdateParams.amount_details](/api/payment_intents/update?api-version=2026-01-28.clover#update_payment_intent-amount_details) |
| `error` | Added | [PaymentIntent.amount_details](/api/payment_intents/object?api-version=2026-01-28.clover#payment_intent_object-amount_details) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `EnforceArithmeticValidation` | Added | [PaymentIntentAmountDetailsParams](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-amount_details), [PaymentIntentCaptureAmountDetailsParams](/api/payment_intents/capture?api-version=2026-01-28.clover#capture_payment_intent-amount_details), [PaymentIntentConfirmAmountDetailsParams](/api/payment_intents/confirm?api-version=2026-01-28.clover#confirm_payment_intent-amount_details), [PaymentIntentIncrementAuthorizationAmountDetailsParams](/api/payment_intents/increment_authorization?api-version=2026-01-28.clover#increment_payment_intent-amount_details) |
| `Error` | Added | [PaymentIntentAmountDetails](/api/payment_intents/object?api-version=2026-01-28.clover#payment_intent_object-amount_details) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `EnforceArithmeticValidation` | Added | [PaymentIntentAmountDetailsOptions](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-amount_details) |
| `Error` | Added | [PaymentIntent.AmountDetails](/api/payment_intents/object?api-version=2026-01-28.clover#payment_intent_object-amount_details) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-01-28.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v18.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v18.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v14.2.0](https://github.com/stripe/stripe-python/releases/tag/v14.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v19.2.0](https://github.com/stripe/stripe-php/releases/tag/v19.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v31.2.0](https://github.com/stripe/stripe-java/releases/tag/v31.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v20.2.0](https://github.com/stripe/stripe-node/releases/tag/v20.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v84.2.0](https://github.com/stripe/stripe-go/releases/tag/v84.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v50.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v50.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds support for 3D Secure versions 2.3.0 and 2.3.1](https://docs.stripe.com/changelog/clover/2026-01-28/3d-secure-version-support.md)
- [Adds the ability to monitor reserve activity on Balance Transactions and reconcile Risk Reserved balance changes](https://docs.stripe.com/changelog/clover/2026-01-28/monitor-reserve-activity-on-balance-transactions.md)
- [Adds Adyen as an issuer for iDEAL payments](https://docs.stripe.com/changelog/clover/2026-01-28/adds-adyen-as-an-issuer-for-ideal-payments.md)
- [Adds adjustable quantity to the line items response](https://docs.stripe.com/changelog/clover/2026-01-28/line-items-adjustable-quantity.md)
