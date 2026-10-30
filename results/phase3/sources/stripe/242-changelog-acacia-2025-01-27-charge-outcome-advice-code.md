# Adds advice code to Charges

## What’s new

Adds the [advice_code](https://docs.stripe.com/api/charges/object.md?api-version=2025-01-27.acacia#charge_object-outcome-advice_code) property to the [Charge](https://docs.stripe.com/api/charges/object.md?api-version=2025-01-27.acacia) object. The `advice_code` is an enumerated value that provides more details about unsuccessful transactions.

## Impact

You can use the `advice_code` to understand [how to proceed with an error](https://docs.stripe.com/declines.md#issuer-declines) if a transaction is unsuccessful.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `advice_code` | Added | [Charge.outcome](/api/charges/object?api-version=2025-01-27.acacia#charge_object-outcome) |
| `advice_code` | Added | [Invoice.last_finalization_error](/api/invoices/object?api-version=2025-01-27.acacia#invoice_object-last_finalization_error), [PaymentIntent.last_payment_error](/api/payment_intents/object?api-version=2025-01-27.acacia#payment_intent_object-last_payment_error), [SetupAttempt.setup_error](/api/setup_attempts/object?api-version=2025-01-27.acacia#setup_attempt_object-setup_error), [SetupIntent.last_setup_error](/api/setup_intents/object?api-version=2025-01-27.acacia#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2025-01-27.acacia) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `advice_code` | Added | [stripe.Charge.Outcome](/api/charges/object?api-version=2025-01-27.acacia#charge_object-outcome) |
| `advice_code` | Added | [stripe.Invoice.LastFinalizationError](/api/invoices/object?api-version=2025-01-27.acacia#invoice_object-last_finalization_error), [stripe.PaymentIntent.LastPaymentError](/api/payment_intents/object?api-version=2025-01-27.acacia#payment_intent_object-last_payment_error), [stripe.SetupAttempt.SetupError](/api/setup_attempts/object?api-version=2025-01-27.acacia#setup_attempt_object-setup_error), [stripe.SetupIntent.LastSetupError](/api/setup_intents/object?api-version=2025-01-27.acacia#setup_intent_object-last_setup_error) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `advice_code` | Added | [StripeError](/api/errors?api-version=2025-01-27.acacia) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `advice_code` | Added | [Charge.outcome](/api/charges/object?api-version=2025-01-27.acacia#charge_object-outcome) |
| `advice_code` | Added | [Invoice.last_finalization_error](/api/invoices/object?api-version=2025-01-27.acacia#invoice_object-last_finalization_error), [PaymentIntent.last_payment_error](/api/payment_intents/object?api-version=2025-01-27.acacia#payment_intent_object-last_payment_error), [SetupAttempt.setup_error](/api/setup_attempts/object?api-version=2025-01-27.acacia#setup_attempt_object-setup_error), [SetupIntent.last_setup_error](/api/setup_intents/object?api-version=2025-01-27.acacia#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2025-01-27.acacia) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `advice_code` | Added | [Charge.outcome](/api/charges/object?api-version=2025-01-27.acacia#charge_object-outcome) |
| `advice_code` | Added | [Invoice.last_finalization_error](/api/invoices/object?api-version=2025-01-27.acacia#invoice_object-last_finalization_error), [PaymentIntent.last_payment_error](/api/payment_intents/object?api-version=2025-01-27.acacia#payment_intent_object-last_payment_error), [SetupAttempt.setup_error](/api/setup_attempts/object?api-version=2025-01-27.acacia#setup_attempt_object-setup_error), [SetupIntent.last_setup_error](/api/setup_intents/object?api-version=2025-01-27.acacia#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2025-01-27.acacia) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AdviceCode` | Added | [ChargeOutcome](/api/charges/object?api-version=2025-01-27.acacia#charge_object-outcome) |
| `AdviceCode` | Added | [InvoiceLastFinalizationError](/api/invoices/object?api-version=2025-01-27.acacia#invoice_object-last_finalization_error), [PaymentIntentLastPaymentError](/api/payment_intents/object?api-version=2025-01-27.acacia#payment_intent_object-last_payment_error), [SetupAttemptSetupError](/api/setup_attempts/object?api-version=2025-01-27.acacia#setup_attempt_object-setup_error), [SetupIntentLastSetupError](/api/setup_intents/object?api-version=2025-01-27.acacia#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2025-01-27.acacia) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AdviceCode` | Added | [ChargeOutcome](/api/charges/object?api-version=2025-01-27.acacia#charge_object-outcome) |
| `AdviceCode` | Added | [InvoiceLastFinalizationError](/api/invoices/object?api-version=2025-01-27.acacia#invoice_object-last_finalization_error), [PaymentIntentLastPaymentError](/api/payment_intents/object?api-version=2025-01-27.acacia#payment_intent_object-last_payment_error), [SetupAttemptSetupError](/api/setup_attempts/object?api-version=2025-01-27.acacia#setup_attempt_object-setup_error), [SetupIntentLastSetupError](/api/setup_intents/object?api-version=2025-01-27.acacia#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2025-01-27.acacia) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-01-27.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.4.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.5.0](https://github.com/stripe/stripe-python/releases/tag/v11.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.5.0](https://github.com/stripe/stripe-php/releases/tag/v16.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.3.0](https://github.com/stripe/stripe-java/releases/tag/v28.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.6.0](https://github.com/stripe/stripe-node/releases/tag/v17.6.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.3.0](https://github.com/stripe/stripe-go/releases/tag/v81.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.3.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
