# Adds error code for exceeded transaction limits

## What’s new

Adds the `charge_exceeds_transaction_limit` [error code](https://docs.stripe.com/error-codes.md#charge-exceeds-source-limit) as an enum value to the following resources: [Invoices](https://docs.stripe.com/api/invoices.md?api-version=2024-09-30.acacia), [Payment Intents](https://docs.stripe.com/api/payment_intents.md?api-version=2024-09-30.acacia), [Setup Attempts](https://docs.stripe.com/api/setup_attempts.md?api-version=2024-09-30.acacia), [Setup Intents](https://docs.stripe.com/api/setup_intents.md?api-version=2024-09-30.acacia) and [Errors](https://docs.stripe.com/api/errors.md?api-version=2024-09-30.acacia).

This error occurs when the amount of a transaction that uses a [bank debit](https://docs.stripe.com/payments/bank-debits.md) payment method causes the merchant to exceed their transaction volume limit.

## Impact

This allows you to [test your integration](https://docs.stripe.com/testing.md) and more easily discover any issues with transaction or weekly volume limits.

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `charge_exceeds_transaction_limit` | Added | [Invoice.last_finalization_error.code](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-last_finalization_error-code), [PaymentIntent.last_payment_error.code](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-last_payment_error-code), [SetupAttempt.setup_error.code](/api/setup_attempts/object?api-version=2024-09-30.acacia#setup_attempt_object-setup_error-code), [SetupIntent.last_setup_error.code](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-last_setup_error-code), [StripeError.code](/api/errors?api-version=2024-09-30.acacia#errors-code) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enums |
| --- | --- | --- |
| `charge_exceeds_transaction_limit` | Added | [stripe.Invoice.LastFinalizationError.code](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-last_finalization_error-code), [stripe.PaymentIntent.LastPaymentError.code](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-last_payment_error-code), [stripe.SetupAttempt.SetupError.code](/api/setup_attempts/object?api-version=2024-09-30.acacia#setup_attempt_object-setup_error-code) |

#### PHP

| Value | Change | Enum |
| --- | --- | --- |
| `charge_exceeds_transaction_limit` | Added | [StripeError.code](/api/errors?api-version=2024-09-30.acacia#errors-code) |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `charge_exceeds_transaction_limit` | Added | [Invoice.last_finalization_error.code](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-last_finalization_error-code), [PaymentIntent.last_payment_error.code](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-last_payment_error-code), [SetupAttempt.setup_error.code](/api/setup_attempts/object?api-version=2024-09-30.acacia#setup_attempt_object-setup_error-code), [SetupIntent.last_setup_error.code](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-last_setup_error-code), [StripeError.code](/api/errors?api-version=2024-09-30.acacia#errors-code) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `charge_exceeds_transaction_limit` | Added | [InvoiceLastFinalizationErrorCode](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-last_finalization_error-code), [PaymentIntentLastPaymentErrorCode](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-last_payment_error-code), [SetupAttemptSetupErrorCode](/api/setup_attempts/object?api-version=2024-09-30.acacia#setup_attempt_object-setup_error-code), [SetupIntentLastSetupErrorCode](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-last_setup_error-code), [StripeErrorCode](/api/errors?api-version=2024-09-30.acacia#errors-code) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-09-30.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.0.0](https://github.com/stripe/stripe-python/releases/tag/v11.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.0.0](https://github.com/stripe/stripe-php/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v27.0.0](https://github.com/stripe/stripe-java/releases/tag/v27.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.0.0](https://github.com/stripe/stripe-node/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v80.0.0](https://github.com/stripe/stripe-go/releases/tag/v80.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v46.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v46.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds new error code for invalid mandate prefixes to Bacs Direct Debit and SEPA Direct Debit payments](https://docs.stripe.com/changelog/acacia/2024-09-30/error-code-invalid-mandate-reference-prefix.md)
