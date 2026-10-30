# Adds support for 3D Secure versions 2.3.0 and 2.3.1

## What’s new

You can now import [3D Secure](https://docs.stripe.com/payments/3d-secure.md) authentication results that use versions 2.3.0 and 2.3.1 of the 3D Secure protocol. The [version](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-01-28.clover#create_payment_intent-payment_method_options-card-three_d_secure-version) parameter in [payment_method_options.card.three_d_secure](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-01-28.clover#create_payment_intent-payment_method_options-card-three_d_secure) now accepts `"2.3.0"` and `"2.3.1"` as valid values, in addition to the previously supported versions `"1.0.2"`, `"2.1.0"`, and `"2.2.0"`.

This enhancement applies to [Payment Intents](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-01-28.clover#create_payment_intent-payment_method_options-card-three_d_secure-version) and [Setup Intents](https://docs.stripe.com/api/setup_intents/create.md?api-version=2026-01-28.clover#create_setup_intent-payment_method_options-card-three_d_secure-version) when you use the [3D Secure Import](https://docs.stripe.com/payments/payment-intents/three-d-secure-import.md) feature to import authentication results from external 3D Secure providers.

## Impact

If you’re using 3D Secure Import and your 3D Secure provider returns authentication results using version 2.3.0 or 2.3.1, you can now successfully import these results into Stripe. Previously, attempting to import results from these newer protocol versions would fail validation. This change ensures compatibility with 3D Secure providers that have adopted the latest EMVCo specifications published in 2021 (v2.3.0) and 2023 (v2.3.1).

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `2.3.0`, `2.3.1` | Added | [Charge.payment_method_details.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-card-three_d_secure-version), [PaymentIntent#create.payment_method_options.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [PaymentIntent#update.payment_method_options.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [PaymentIntent#confirm.payment_method_options.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [SetupAttempt.payment_method_details.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-card-three_d_secure-version), [SetupIntent#create.payment_method_options.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [SetupIntent#update.payment_method_options.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [SetupIntent#confirm.payment_method_options.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `2.3.0`, `2.3.1` | Added | [Charge.PaymentMethodDetail.Card.ThreeDSecure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-card-three_d_secure-version), [PaymentIntentCreateParamsPaymentMethodOptionCardThreeDSecure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [PaymentIntentModifyParamsPaymentMethodOptionCardThreeDSecure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [PaymentIntentConfirmParamsPaymentMethodOptionCardThreeDSecure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [SetupAttempt.PaymentMethodDetail.Card.ThreeDSecure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-card-three_d_secure-version), [SetupIntentCreateParamsPaymentMethodOptionCardThreeDSecure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [SetupIntentModifyParamsPaymentMethodOptionCardThreeDSecure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [SetupIntentConfirmParamsPaymentMethodOptionCardThreeDSecure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version) |

#### PHP

| Values | Change | Enums |
| --- | --- | --- |
| `2.3.0`, `2.3.1` | Added | [Charge.payment_method_details.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-card-three_d_secure-version), [SetupAttempt.payment_method_details.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-card-three_d_secure-version) |

#### Java

| Values | Change | Enums |
| --- | --- | --- |
| `2.3.0`, `2.3.1` | Added | [PaymentIntentCreateParams.payment_method_options.card.three_d_secure](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-payment_method_options-card-three_d_secure-version), [PaymentIntentUpdateParams.payment_method_options.card.three_d_secure](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-payment_method_options-card-three_d_secure-version), [PaymentIntentConfirmParams.payment_method_options.card.three_d_secure](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-payment_method_options-card-three_d_secure-version), [SetupIntentCreateParams.payment_method_options.card.three_d_secure](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-payment_method_options-card-three_d_secure-version), [SetupIntentUpdateParams.payment_method_options.card.three_d_secure](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-payment_method_options-card-three_d_secure-version), [SetupIntentConfirmParams.payment_method_options.card.three_d_secure](/api/payment_intents/create?api-version=2026-01-28.clover#create_payment_intent-payment_method_options-card-three_d_secure-version) |

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `2.3.0`, `2.3.1` | Added | [Charge.payment_method_details.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-card-three_d_secure-version), [PaymentIntentCreateParams.payment_method_options.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [PaymentIntentUpdateParams.payment_method_options.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [PaymentIntentConfirmParams.payment_method_options.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [SetupAttempt.payment_method_details.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-card-three_d_secure-version), [SetupIntentCreateParams.payment_method_options.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [SetupIntentUpdateParams.payment_method_options.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version), [SetupIntentConfirmParams.payment_method_options.card.three_d_secure](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_options-card-three_d_secure-version) |

#### Go

This change doesn’t affect the Go SDK.

#### .NET

This change doesn’t affect the .NET SDK.

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

- [Adds the ability to monitor reserve activity on Balance Transactions and reconcile Risk Reserved balance changes](https://docs.stripe.com/changelog/clover/2026-01-28/monitor-reserve-activity-on-balance-transactions.md)
- [Adds the ability to opt out of strict arithmetic validation for Payment Line Items](https://docs.stripe.com/changelog/clover/2026-01-28/loosen-arithmetic-validation-for-payment-line-items.md)
- [Adds Adyen as an issuer for iDEAL payments](https://docs.stripe.com/changelog/clover/2026-01-28/adds-adyen-as-an-issuer-for-ideal-payments.md)
- [Adds adjustable quantity to the line items response](https://docs.stripe.com/changelog/clover/2026-01-28/line-items-adjustable-quantity.md)
