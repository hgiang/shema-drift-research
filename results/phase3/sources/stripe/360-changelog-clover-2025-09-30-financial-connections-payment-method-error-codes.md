# Adds new error codes for failures when creating Payment Methods from Financial Connections Accounts

## What’s new

When you create a `us_bank_account` [Payment Method](https://docs.stripe.com/api/payment_methods.md?api-version=2025-09-30.clover) from a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md?api-version=2025-09-30.clover) using the [financial_connections_account](https://docs.stripe.com/api/payment_methods/create.md?api-version=2025-09-30.clover#create_payment_method-us_bank_account-financial_connections_account) parameter, the account might not yet have account or routing numbers or Stripe might still be retrieving them. In these cases, Stripe returns one of the following error codes:

- `financial_connections_account_pending_account_numbers`: If you receive this error, retry the request later.
- `financial_connections_account_unavailable_account_numbers`: If you receive this error, prompt your user to link a different bank account.

## Impact

Previously, this error didn’t include a specific error code and appeared as an invalid request. Use the new error code to decide whether to retry creating the `PaymentMethod`.

## Changes

#### REST API

| Codes | Change |  |
| --- | --- | --- |
| `financial_connections_account_pending_account_numbers`, `financial_connections_account_unavailable_account_numbers` | Added | [Invoice.last_finalization_error](/api/invoices/object?api-version=2025-09-30.clover#invoice_object-last_finalization_error), [PaymentIntent.last_payment_error](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-last_payment_error), [SetupAttempt.setup_error](/api/setup_attempts/object?api-version=2025-09-30.clover#setup_attempt_object-setup_error), [SetupIntent.last_setup_error](/api/setup_intents/object?api-version=2025-09-30.clover#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2025-09-30.clover) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Codes | Change |  |
| --- | --- | --- |
| `financial_connections_account_pending_account_numbers`, `financial_connections_account_unavailable_account_numbers` | Added | [Invoice.LastFinalizationError](/api/invoices/object?api-version=2025-09-30.clover#invoice_object-last_finalization_error), [PaymentIntent.LastPaymentError](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-last_payment_error), [SetupAttempt.SetupError](/api/setup_attempts/object?api-version=2025-09-30.clover#setup_attempt_object-setup_error), [SetupIntent.LastSetupError](/api/setup_intents/object?api-version=2025-09-30.clover#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2025-09-30.clover) |

#### PHP

| Codes | Change |  |
| --- | --- | --- |
| `financial_connections_account_pending_account_numbers`, `financial_connections_account_unavailable_account_numbers` | Added | [Invoice.last_finalization_error](/api/invoices/object?api-version=2025-09-30.clover#invoice_object-last_finalization_error), [PaymentIntent.last_payment_error](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-last_payment_error), [SetupAttempt.setup_error](/api/setup_attempts/object?api-version=2025-09-30.clover#setup_attempt_object-setup_error), [SetupIntent.last_setup_error](/api/setup_intents/object?api-version=2025-09-30.clover#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2025-09-30.clover) |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Codes | Change |  |
| --- | --- | --- |
| `financial_connections_account_pending_account_numbers`, `financial_connections_account_unavailable_account_numbers` | Added | [Invoice.last_finalization_error](/api/invoices/object?api-version=2025-09-30.clover#invoice_object-last_finalization_error), [PaymentIntent.last_payment_error](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-last_payment_error), [SetupAttempt.setup_error](/api/setup_attempts/object?api-version=2025-09-30.clover#setup_attempt_object-setup_error), [SetupIntent.last_setup_error](/api/setup_intents/object?api-version=2025-09-30.clover#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2025-09-30.clover) |

#### Go

| Codes | Change |  |
| --- | --- | --- |
| `financial_connections_account_pending_account_numbers`, `financial_connections_account_unavailable_account_numbers` | Added | [Error](/api/errors?api-version=2025-09-30.clover), [InvoiceLastFinalizationError](/api/invoices/object?api-version=2025-09-30.clover#invoice_object-last_finalization_error), [PaymentIntentLastPaymentError](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-last_payment_error), [SetupAttemptSetupError](/api/setup_attempts/object?api-version=2025-09-30.clover#setup_attempt_object-setup_error), [SetupIntentLastSetupError](/api/setup_intents/object?api-version=2025-09-30.clover#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2025-09-30.clover) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-09-30.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v16.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.0.1](https://github.com/stripe/stripe-python/releases/tag/v13.0.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.0.0](https://github.com/stripe/stripe-php/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.0.0](https://github.com/stripe/stripe-java/releases/tag/v30.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.1.0](https://github.com/stripe/stripe-node/releases/tag/v19.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.0.0](https://github.com/stripe/stripe-go/releases/tag/v83.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
