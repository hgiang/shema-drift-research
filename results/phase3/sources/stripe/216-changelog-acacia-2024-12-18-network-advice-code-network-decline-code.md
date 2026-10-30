# Adds network advice and decline codes

## What’s new

When a charge is declined, two new error codes are now part of the response. The `network_decline_code` provides more information from the card network about why the charge was declined. The `network_advice_code` provides more information about how to handle the decline.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `network_advice_code`, `network_decline_code` | Added | [Charge.outcome](/api/charges/object?api-version=2024-12-18.acacia#charge_object-outcome), [Invoice.last_finalization_error](/api/invoices/object?api-version=2024-12-18.acacia#invoice_object-last_finalization_error), [PaymentIntent.last_payment_error](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-last_payment_error), [SetupAttempt.setup_error](/api/setup_attempts/object?api-version=2024-12-18.acacia#setup_attempt_object-setup_error), [SetupIntent.last_setup_error](/api/setup_intents/object?api-version=2024-12-18.acacia#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2024-12-18.acacia) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `network_advice_code` | Added | [stripe.Charge.Outcome](/api/charges/object?api-version=2024-12-18.acacia#charge_object-outcome), [stripe.Invoice.LastFinalizationError](/api/invoices/object?api-version=2024-12-18.acacia#invoice_object-last_finalization_error), [stripe.PaymentIntent.LastPaymentError](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-last_payment_error), [stripe.SetupAttempt.SetupError](/api/setup_attempts/object?api-version=2024-12-18.acacia#setup_attempt_object-setup_error), [stripe.SetupIntent.LastSetupError](/api/setup_intents/object?api-version=2024-12-18.acacia#setup_intent_object-last_setup_error) |
| `network_decline_code` | Added | [stripe.Charge.Outcome](/api/charges/object?api-version=2024-12-18.acacia#charge_object-outcome), [stripe.Invoice.LastFinalizationError](/api/invoices/object?api-version=2024-12-18.acacia#invoice_object-last_finalization_error), [stripe.PaymentIntent.LastPaymentError](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-last_payment_error), [stripe.SetupAttempt.SetupError](/api/setup_attempts/object?api-version=2024-12-18.acacia#setup_attempt_object-setup_error), [stripe.SetupIntent.LastSetupError](/api/setup_intents/object?api-version=2024-12-18.acacia#setup_intent_object-last_setup_error) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `network_advice_code`, `network_decline_code` | Added | [StripeError](/api/errors?api-version=2024-12-18.acacia) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `network_advice_code`, `network_decline_code` | Added | [Charge.outcome](/api/charges/object?api-version=2024-12-18.acacia#charge_object-outcome), [Invoice.last_finalization_error](/api/invoices/object?api-version=2024-12-18.acacia#invoice_object-last_finalization_error), [PaymentIntent.last_payment_error](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-last_payment_error), [SetupAttempt.setup_error](/api/setup_attempts/object?api-version=2024-12-18.acacia#setup_attempt_object-setup_error), [SetupIntent.last_setup_error](/api/setup_intents/object?api-version=2024-12-18.acacia#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2024-12-18.acacia) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `network_advice_code`, `network_decline_code` | Added | [Charge.outcome](/api/charges/object?api-version=2024-12-18.acacia#charge_object-outcome), [Invoice.last_finalization_error](/api/invoices/object?api-version=2024-12-18.acacia#invoice_object-last_finalization_error), [PaymentIntent.last_payment_error](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-last_payment_error), [SetupAttempt.setup_error](/api/setup_attempts/object?api-version=2024-12-18.acacia#setup_attempt_object-setup_error), [SetupIntent.last_setup_error](/api/setup_intents/object?api-version=2024-12-18.acacia#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2024-12-18.acacia) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `NetworkAdviceCode`, `NetworkDeclineCode` | Added | [ChargeOutcome](/api/charges/object?api-version=2024-12-18.acacia#charge_object-outcome), [InvoiceLastFinalizationError](/api/invoices/object?api-version=2024-12-18.acacia#invoice_object-last_finalization_error), [PaymentIntentLastPaymentError](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-last_payment_error), [SetupAttemptSetupError](/api/setup_attempts/object?api-version=2024-12-18.acacia#setup_attempt_object-setup_error), [SetupIntentLastSetupError](/api/setup_intents/object?api-version=2024-12-18.acacia#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2024-12-18.acacia) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `NetworkAdviceCode`, `NetworkDeclineCode` | Added | [ChargeOutcome](/api/charges/object?api-version=2024-12-18.acacia#charge_object-outcome), [InvoiceLastFinalizationError](/api/invoices/object?api-version=2024-12-18.acacia#invoice_object-last_finalization_error), [PaymentIntentLastPaymentError](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-last_payment_error), [SetupAttemptSetupError](/api/setup_attempts/object?api-version=2024-12-18.acacia#setup_attempt_object-setup_error), [SetupIntentLastSetupError](/api/setup_intents/object?api-version=2024-12-18.acacia#setup_intent_object-last_setup_error), [StripeError](/api/errors?api-version=2024-12-18.acacia) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-12-18.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.3.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.4.0](https://github.com/stripe/stripe-python/releases/tag/v11.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.4.0](https://github.com/stripe/stripe-php/releases/tag/v16.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.2.0](https://github.com/stripe/stripe-java/releases/tag/v28.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.5.0](https://github.com/stripe/stripe-node/releases/tag/v17.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.2.0](https://github.com/stripe/stripe-go/releases/tag/v81.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
