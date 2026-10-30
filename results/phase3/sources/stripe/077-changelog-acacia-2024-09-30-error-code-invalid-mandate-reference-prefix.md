# Adds new error code for invalid mandate prefixes to Bacs Direct Debit and SEPA Direct Debit payments

## What’s new

Adds the `invalid_mandate_reference_prefix_format` [error code](https://docs.stripe.com/error-codes.md) as an enum value to the following resources: [Payment Intents](https://docs.stripe.com/api/payment_intents.md?api-version=2024-09-30.acacia), [Setup Attempts](https://docs.stripe.com/api/setup_attempts.md?api-version=2024-09-30.acacia), [Setup Intents](https://docs.stripe.com/api/setup_intents.md?api-version=2024-09-30.acacia) and [Errors](https://docs.stripe.com/api/errors.md?api-version=2024-09-30.acacia). This allows you to test your integration and more easily discover any issues with the format of reference prefixes in [Mandates](https://docs.stripe.com/api/mandates.md?api-version=2024-09-30.acacia) related to [Bacs Direct Debit](https://docs.stripe.com/payments/bacs-debit.md) and [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit.md) payments.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `mandate_options` | Added | [PaymentIntent#confirm.payment_method_options.bacs_debit](/api/payment_intents/confirm?api-version=2024-09-30.acacia#confirm_payment_intent-payment_method_options-bacs_debit), [PaymentIntent#create.payment_method_options.bacs_debit](/api/payment_intents/create?api-version=2024-09-30.acacia#create_payment_intent-payment_method_options-bacs_debit), [PaymentIntent#update.payment_method_options.bacs_debit](/api/payment_intents/update?api-version=2024-09-30.acacia#update_payment_intent-payment_method_options-bacs_debit), [PaymentIntent.payment_method_options.bacs_debit](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-payment_method_options-bacs_debit) |
| `bacs_debit` | Added | [SetupIntent#confirm.payment_method_options](/api/setup_intents/confirm?api-version=2024-09-30.acacia#confirm_setup_intent-payment_method_options), [SetupIntent#create.payment_method_options](/api/setup_intents/create?api-version=2024-09-30.acacia#create_setup_intent-payment_method_options), [SetupIntent#update.payment_method_options](/api/setup_intents/update?api-version=2024-09-30.acacia#update_setup_intent-payment_method_options), [SetupIntent.payment_method_options](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-payment_method_options) |

| Value | Change | Enums |
| --- | --- | --- |
| `invalid_mandate_reference_prefix_format` | Added | [Invoice.last_finalization_error.code](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-last_finalization_error-code), [PaymentIntent.last_payment_error.code](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-last_payment_error-code), [SetupAttempt.setup_error.code](/api/setup_attempts/object?api-version=2024-09-30.acacia#setup_attempt_object-setup_error-code), [SetupIntent.last_setup_error.code](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-last_setup_error-code), [StripeError.code](/api/errors?api-version=2024-09-30.acacia#errors-code) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

This change doesn’t affect the Python SDK.

#### PHP

| Value | Change | Enum |
| --- | --- | --- |
| `invalid_mandate_reference_prefix_format` | Added | [StripeError.code](/api/errors?api-version=2024-09-30.acacia#errors-code) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mandate_options` | Added | [PaymentIntent.payment_method_options.bacs_debit](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-payment_method_options-bacs_debit), [PaymentIntentConfirmParams.payment_method_options.bacs_debit](/api/payment_intents/confirm?api-version=2024-09-30.acacia#confirm_payment_intent-payment_method_options-bacs_debit), [PaymentIntentCreateParams.payment_method_options.bacs_debit](/api/payment_intents/create?api-version=2024-09-30.acacia#create_payment_intent-payment_method_options-bacs_debit), [PaymentIntentUpdateParams.payment_method_options.bacs_debit](/api/payment_intents/update?api-version=2024-09-30.acacia#update_payment_intent-payment_method_options-bacs_debit) |
| `bacs_debit` | Added | [SetupIntent.payment_method_options](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-payment_method_options), [SetupIntentConfirmParams.payment_method_options](/api/setup_intents/confirm?api-version=2024-09-30.acacia#confirm_setup_intent-payment_method_options), [SetupIntentCreateParams.payment_method_options](/api/setup_intents/create?api-version=2024-09-30.acacia#create_setup_intent-payment_method_options), [SetupIntentUpdateParams.payment_method_options](/api/setup_intents/update?api-version=2024-09-30.acacia#update_setup_intent-payment_method_options) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mandate_options` | Added | [PaymentIntent.payment_method_options.bacs_debit](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-payment_method_options-bacs_debit), [PaymentIntentConfirmParams.payment_method_options.bacs_debit](/api/payment_intents/confirm?api-version=2024-09-30.acacia#confirm_payment_intent-payment_method_options-bacs_debit), [PaymentIntentCreateParams.payment_method_options.bacs_debit](/api/payment_intents/create?api-version=2024-09-30.acacia#create_payment_intent-payment_method_options-bacs_debit), [PaymentIntentUpdateParams.payment_method_options.bacs_debit](/api/payment_intents/update?api-version=2024-09-30.acacia#update_payment_intent-payment_method_options-bacs_debit) |
| `bacs_debit` | Added | [SetupIntent.payment_method_options](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-payment_method_options), [SetupIntentConfirmParams.payment_method_options](/api/setup_intents/confirm?api-version=2024-09-30.acacia#confirm_setup_intent-payment_method_options), [SetupIntentCreateParams.payment_method_options](/api/setup_intents/create?api-version=2024-09-30.acacia#create_setup_intent-payment_method_options), [SetupIntentUpdateParams.payment_method_options](/api/setup_intents/update?api-version=2024-09-30.acacia#update_setup_intent-payment_method_options) |

| Value | Change | Enums |
| --- | --- | --- |
| `invalid_mandate_reference_prefix_format` | Added | [Invoice.last_finalization_error.code](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-last_finalization_error-code), [PaymentIntent.last_payment_error.code](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-last_payment_error-code), [SetupAttempt.setup_error.code](/api/setup_attempts/object?api-version=2024-09-30.acacia#setup_attempt_object-setup_error-code), [SetupIntent.last_setup_error.code](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-last_setup_error-code), [StripeError.code](/api/errors?api-version=2024-09-30.acacia#errors-code) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `MandateOptions` | Added | [PaymentIntentConfirmPaymentMethodOptionsBacsDebitParams](/api/payment_intents/confirm?api-version=2024-09-30.acacia#confirm_payment_intent-payment_method_options-bacs_debit), [PaymentIntentPaymentMethodOptionsBacsDebitParams](/api/payment_intents/create?api-version=2024-09-30.acacia#create_payment_intent-payment_method_options-bacs_debit), [PaymentIntentPaymentMethodOptionsBacsDebit](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-payment_method_options-bacs_debit) |
| `BACSDebit` | Added | [SetupIntentConfirmPaymentMethodOptionsParams](/api/setup_intents/confirm?api-version=2024-09-30.acacia#confirm_setup_intent-payment_method_options), [SetupIntentPaymentMethodOptionsParams](/api/setup_intents/create?api-version=2024-09-30.acacia#create_setup_intent-payment_method_options), [SetupIntentPaymentMethodOptions](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-payment_method_options) |

| Value | Change | Enums |
| --- | --- | --- |
| `invalid_mandate_reference_prefix_format` | Added | [InvoiceLastFinalizationErrorCode](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-last_finalization_error-code), [PaymentIntentLastPaymentErrorCode](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-last_payment_error-code), [SetupAttemptSetupErrorCode](/api/setup_attempts/object?api-version=2024-09-30.acacia#setup_attempt_object-setup_error-code), [SetupIntentLastSetupErrorCode](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-last_setup_error-code), [StripeErrorCode](/api/errors?api-version=2024-09-30.acacia#errors-code) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `MandateOptions` | Added | [PaymentIntentPaymentMethodOptionsBacsDebitOptions](/api/payment_intents/create?api-version=2024-09-30.acacia#create_payment_intent-payment_method_options-bacs_debit), [PaymentIntentPaymentMethodOptionsBacsDebit](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-payment_method_options-bacs_debit) |
| `BacsDebit` | Added | [SetupIntentPaymentMethodOptionsOptions](/api/setup_intents/create?api-version=2024-09-30.acacia#create_setup_intent-payment_method_options), [SetupIntentPaymentMethodOptions](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-payment_method_options) |

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

- [Adds error code for exceeded transaction limits](https://docs.stripe.com/changelog/acacia/2024-09-30/error-code-transaction-limit.md)
