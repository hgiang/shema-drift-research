# Adds Support for Twint as a Payment method for Recurring payments

## What’s new

Adds support for Twint as a payment method for recurring payments to the following:

- [Stripe Billing](https://docs.stripe.com/billing.md): Use Twint for [Subscriptions](https://docs.stripe.com/api/subscriptions.md?api-version=2026-05-27.dahlia) and [Invoices](https://docs.stripe.com/api/invoices.md?api-version=2026-05-27.dahlia).
- [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md?api-version=2026-05-27.dahlia): Use Twint in `setup` and `subscription` modes.
- [PaymentIntents](https://docs.stripe.com/api/payment_intents.md?api-version=2026-05-27.dahlia): Set [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-05-27.dahlia#create_payment_intent-payment_method_options-twint-setup_future_usage) to `off_session` to save Twint as a payment method for future use.
- [SetupIntents](https://docs.stripe.com/api/setup_intents.md?api-version=2026-05-27.dahlia): Create a [Mandate](https://docs.stripe.com/api/mandates.md?api-version=2026-05-27.dahlia) without an initial payment.
- The [Charge](https://docs.stripe.com/api/charges.md?api-version=2026-05-27.dahlia) object now includes a [mandate](https://docs.stripe.com/api/charges/object.md?api-version=2026-05-27.dahlia#charge_object-payment_method_details-twint-mandate) property in `payment_method_details.twint` that contains the ID of the mandate used for off-session payments.
- For client-side integrations, you can use the new [stripe.confirmTwintSetup](https://docs.stripe.com/js/setup_intents/confirm_twint_setup) API method in Stripe.js to confirm SetupIntents with Twint payment methods.

## Impact

You can now offer your customers Twint as a payment method for subscriptions, future purchases, recurring billing and off-session payments. [Learn how to set up future payments with Twint](https://docs.stripe.com/payments/twint/set-up-future-payments.md).

Twint allows only one active mandate per merchant-customer pair. If you try to create a new mandate when one already exists, the API returns a `payment_intent_mandate_revoked_mandate_collision` error. To learn how to handle this error, see [support](https://support.stripe.com/questions/fix-failed-twint-payments-from-revoked-mandates).

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `mandate` | Added | [Charge.payment_method_details.twint](/api/charges/object?api-version=2026-05-27.dahlia#charge_object-payment_method_details-twint), [PaymentAttemptRecord.payment_method_details.twint](/api/payment-attempt-record/object?api-version=2026-05-27.dahlia#payment_attempt_record_object-payment_method_details-twint), [PaymentRecord.payment_method_details.twint](/api/payment-record/object?api-version=2026-05-27.dahlia#payment_record_object-payment_method_details-twint) |
| `twint` | Added | [Mandate.payment_method_details](/api/mandates/object?api-version=2026-05-27.dahlia#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-05-27.dahlia#setup_attempt_object-payment_method_details) |

| Value | Change | Enums |
| --- | --- | --- |
| `twint` | Added | [Invoice#update.payment_settings](/api/invoices/update?api-version=2026-05-27.dahlia#update_invoice-payment_settings-payment_method_types), [Invoice#create.payment_settings](/api/invoices/create?api-version=2026-05-27.dahlia#create-payment_settings-payment_method_types), [Invoice.payment_settings](/api/invoices/object?api-version=2026-05-27.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription#update.payment_settings](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription-payment_settings-payment_method_types), [Subscription#create.payment_settings](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription-payment_settings-payment_method_types), [Subscription.payment_settings](/api/subscriptions/object?api-version=2026-05-27.dahlia#subscription_object-payment_settings-payment_method_types) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Checkout.Session#create.payment_method_options.twint.setup_future_usage`, `Checkout.Session.payment_method_options.twint.setup_future_usage`, `PaymentIntent#confirm.payment_method_options.twint.setup_future_usage`, `PaymentIntent#create.payment_method_options.twint.setup_future_usage`, `PaymentIntent#update.payment_method_options.twint.setup_future_usage`, `PaymentIntent.payment_method_options.twint.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mandate` | Added | [Charge::PaymentMethodDetail::Twint](/api/charges/object?api-version=2026-05-27.dahlia#charge_object-payment_method_details-twint), [PaymentAttemptRecord::PaymentMethodDetail::Twint](/api/payment-attempt-record/object?api-version=2026-05-27.dahlia#payment_attempt_record_object-payment_method_details-twint), [PaymentRecord::PaymentMethodDetail::Twint](/api/payment-record/object?api-version=2026-05-27.dahlia#payment_record_object-payment_method_details-twint) |
| `twint` | Added | [Mandate::PaymentMethodDetail](/api/mandates/object?api-version=2026-05-27.dahlia#mandate_object-payment_method_details), [SetupAttempt::PaymentMethodDetail](/api/setup_attempts/object?api-version=2026-05-27.dahlia#setup_attempt_object-payment_method_details) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Checkout::Session::PaymentMethodOption::Twint.setup_future_usage`, `Checkout::SessionCreateParams::PaymentMethodOption::Twint.setup_future_usage`, `PaymentIntent::PaymentMethodOption::Twint.setup_future_usage`, `PaymentIntentConfirmParams::PaymentMethodOption::Twint.setup_future_usage`, `PaymentIntentCreateParams::PaymentMethodOption::Twint.setup_future_usage`, `PaymentIntentUpdateParams::PaymentMethodOption::Twint.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mandate` | Added | [Charge.PaymentMethodDetail.Twint](/api/charges/object?api-version=2026-05-27.dahlia#charge_object-payment_method_details-twint), [PaymentAttemptRecord.PaymentMethodDetail.Twint](/api/payment-attempt-record/object?api-version=2026-05-27.dahlia#payment_attempt_record_object-payment_method_details-twint), [PaymentRecord.PaymentMethodDetail.Twint](/api/payment-record/object?api-version=2026-05-27.dahlia#payment_record_object-payment_method_details-twint) |
| `twint` | Added | [Mandate.PaymentMethodDetail](/api/mandates/object?api-version=2026-05-27.dahlia#mandate_object-payment_method_details), [SetupAttempt.PaymentMethodDetail](/api/setup_attempts/object?api-version=2026-05-27.dahlia#setup_attempt_object-payment_method_details) |

| Value | Change | Enums |
| --- | --- | --- |
| `twint` | Added | [InvoiceModifyParamsPaymentSetting](/api/invoices/update?api-version=2026-05-27.dahlia#update_invoice-payment_settings-payment_method_types), [InvoiceCreateParamsPaymentSetting](/api/invoices/create?api-version=2026-05-27.dahlia#create-payment_settings-payment_method_types), [Invoice.PaymentSetting](/api/invoices/object?api-version=2026-05-27.dahlia#invoice_object-payment_settings-payment_method_types), [SubscriptionModifyParamsPaymentSetting](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription-payment_settings-payment_method_types), [SubscriptionCreateParamsPaymentSetting](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription-payment_settings-payment_method_types), [Subscription.PaymentSetting](/api/subscriptions/object?api-version=2026-05-27.dahlia#subscription_object-payment_settings-payment_method_types) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Checkout.Session.PaymentMethodOption.Twint.setup_future_usage`, `PaymentIntent.PaymentMethodOption.Twint.setup_future_usage`, `PaymentIntentConfirmParamsPaymentMethodOptionTwint.setup_future_usage`, `PaymentIntentCreateParamsPaymentMethodOptionTwint.setup_future_usage`, `PaymentIntentModifyParamsPaymentMethodOptionTwint.setup_future_usage`, `checkout.SessionCreateParamsPaymentMethodOptionTwint.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mandate` | Added | [Charge.payment_method_details.twint](/api/charges/object?api-version=2026-05-27.dahlia#charge_object-payment_method_details-twint), [PaymentAttemptRecord.payment_method_details.twint](/api/payment-attempt-record/object?api-version=2026-05-27.dahlia#payment_attempt_record_object-payment_method_details-twint), [PaymentRecord.payment_method_details.twint](/api/payment-record/object?api-version=2026-05-27.dahlia#payment_record_object-payment_method_details-twint) |
| `twint` | Added | [Mandate.payment_method_details](/api/mandates/object?api-version=2026-05-27.dahlia#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-05-27.dahlia#setup_attempt_object-payment_method_details) |

| Value | Change | Enums |
| --- | --- | --- |
| `twint` | Added | [Invoice.payment_settings](/api/invoices/object?api-version=2026-05-27.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription.payment_settings](/api/subscriptions/object?api-version=2026-05-27.dahlia#subscription_object-payment_settings-payment_method_types) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Checkout.Session.payment_method_options.twint.setup_future_usage`, `Checkout\Session.create().$params.payment_method_option.twint.setup_future_usage`, `PaymentIntent.confirm().$params.payment_method_option.twint.setup_future_usage`, `PaymentIntent.create().$params.payment_method_option.twint.setup_future_usage`, `PaymentIntent.payment_method_options.twint.setup_future_usage`, `PaymentIntent.update().$params.payment_method_option.twint.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mandate` | Added | [Charge.payment_method_details.twint](/api/charges/object?api-version=2026-05-27.dahlia#charge_object-payment_method_details-twint), [PaymentAttemptRecord.payment_method_details.twint](/api/payment-attempt-record/object?api-version=2026-05-27.dahlia#payment_attempt_record_object-payment_method_details-twint), [PaymentRecord.payment_method_details.twint](/api/payment-record/object?api-version=2026-05-27.dahlia#payment_record_object-payment_method_details-twint) |
| `twint` | Added | [Mandate.payment_method_details](/api/mandates/object?api-version=2026-05-27.dahlia#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-05-27.dahlia#setup_attempt_object-payment_method_details) |

| Value | Change | Enums |
| --- | --- | --- |
| `twint` | Added | [InvoiceUpdateParams.payment_settings](/api/invoices/update?api-version=2026-05-27.dahlia#update_invoice-payment_settings-paymentMethodTypes), [InvoiceCreateParams.payment_settings](/api/invoices/create?api-version=2026-05-27.dahlia#create-payment_settings-paymentMethodTypes), [SubscriptionUpdateParams.payment_settings](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription-payment_settings-paymentMethodTypes), [SubscriptionCreateParams.payment_settings](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription-payment_settings-paymentMethodTypes) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentIntent.payment_method_options.twint.setupFutureUsage`, `PaymentIntentConfirmParams.payment_method_options.twint.setupFutureUsage`, `PaymentIntentCreateParams.payment_method_options.twint.setupFutureUsage`, `PaymentIntentUpdateParams.payment_method_options.twint.setupFutureUsage`, `checkout.Session.payment_method_options.twint.setupFutureUsage`, `checkout.SessionCreateParams.payment_method_options.twint.setupFutureUsage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mandate` | Added | [Charge.payment_method_details.twint](/api/charges/object?api-version=2026-05-27.dahlia#charge_object-payment_method_details-twint), [PaymentAttemptRecord.payment_method_details.twint](/api/payment-attempt-record/object?api-version=2026-05-27.dahlia#payment_attempt_record_object-payment_method_details-twint), [PaymentRecord.payment_method_details.twint](/api/payment-record/object?api-version=2026-05-27.dahlia#payment_record_object-payment_method_details-twint) |
| `twint` | Added | [Mandate.payment_method_details](/api/mandates/object?api-version=2026-05-27.dahlia#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-05-27.dahlia#setup_attempt_object-payment_method_details) |

| Value | Change | Enums |
| --- | --- | --- |
| `twint` | Added | [InvoiceUpdateParams.payment_settings](/api/invoices/update?api-version=2026-05-27.dahlia#update_invoice-payment_settings-payment_method_types), [InvoiceCreateParams.payment_settings](/api/invoices/create?api-version=2026-05-27.dahlia#create-payment_settings-payment_method_types), [Invoice.payment_settings](/api/invoices/object?api-version=2026-05-27.dahlia#invoice_object-payment_settings-payment_method_types), [SubscriptionUpdateParams.payment_settings](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription-payment_settings-payment_method_types), [SubscriptionCreateParams.payment_settings](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription-payment_settings-payment_method_types), [Subscription.payment_settings](/api/subscriptions/object?api-version=2026-05-27.dahlia#subscription_object-payment_settings-payment_method_types) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Checkout.Session.payment_method_options.twint.setup_future_usage`, `Checkout.SessionCreateParams.payment_method_options.twint.setup_future_usage`, `PaymentIntent.payment_method_options.twint.setup_future_usage`, `PaymentIntentConfirmParams.payment_method_options.twint.setup_future_usage`, `PaymentIntentCreateParams.payment_method_options.twint.setup_future_usage`, `PaymentIntentUpdateParams.payment_method_options.twint.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Mandate` | Added | [ChargePaymentMethodDetailsTwint](/api/charges/object?api-version=2026-05-27.dahlia#charge_object-payment_method_details-twint), [PaymentAttemptRecordPaymentMethodDetailsTwint](/api/payment-attempt-record/object?api-version=2026-05-27.dahlia#payment_attempt_record_object-payment_method_details-twint), [PaymentRecordPaymentMethodDetailsTwint](/api/payment-record/object?api-version=2026-05-27.dahlia#payment_record_object-payment_method_details-twint) |
| `TWINT` | Added | [MandatePaymentMethodDetails](/api/mandates/object?api-version=2026-05-27.dahlia#mandate_object-payment_method_details), [SetupAttemptPaymentMethodDetails](/api/setup_attempts/object?api-version=2026-05-27.dahlia#setup_attempt_object-payment_method_details) |

| Value | Change | Enums |
| --- | --- | --- |
| `twint` | Added | [InvoicePaymentSettings](/api/invoices/object?api-version=2026-05-27.dahlia#invoice_object-payment_settings-PaymentMethodTypes), [SubscriptionPaymentSettings](/api/subscriptions/object?api-version=2026-05-27.dahlia#subscription_object-payment_settings-PaymentMethodTypes) |

| Fields | Change | From → to |
| --- | --- | --- |
| `CheckoutSessionPaymentMethodOptionsTwint.SetupFutureUsage`, `CheckoutSessionPaymentMethodOptionsTwintParams.SetupFutureUsage`, `PaymentIntentConfirmPaymentMethodOptionsTwintParams.SetupFutureUsage`, `PaymentIntentPaymentMethodOptionsTwint.SetupFutureUsage`, `PaymentIntentPaymentMethodOptionsTwintParams.SetupFutureUsage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Mandate` | Added | [Charge.PaymentMethodDetails.Twint](/api/charges/object?api-version=2026-05-27.dahlia#charge_object-payment_method_details-twint), [PaymentAttemptRecord.PaymentMethodDetails.Twint](/api/payment-attempt-record/object?api-version=2026-05-27.dahlia#payment_attempt_record_object-payment_method_details-twint), [PaymentRecord.PaymentMethodDetails.Twint](/api/payment-record/object?api-version=2026-05-27.dahlia#payment_record_object-payment_method_details-twint) |
| `Twint` | Added | [Mandate.PaymentMethodDetails](/api/mandates/object?api-version=2026-05-27.dahlia#mandate_object-payment_method_details), [SetupAttempt.PaymentMethodDetails](/api/setup_attempts/object?api-version=2026-05-27.dahlia#setup_attempt_object-payment_method_details) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Checkout.Session.PaymentMethodOptions.Twint.SetupFutureUsage`, `CheckoutSessionPaymentMethodOptionsTwintOptions.SetupFutureUsage`, `PaymentIntent.PaymentMethodOptions.Twint.SetupFutureUsage`, `PaymentIntentPaymentMethodOptionsTwintOptions.SetupFutureUsage` | Changed | `literal('none') → enum('none'|'off_session')` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-05-27.dahlia`
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

- [Adds destination payment description and metadata support to transfer data](https://docs.stripe.com/changelog/dahlia/2026-05-27/transfer-data-destination-payment-description-and-metadata.md)
- [Adds active status filtering to payment method configurations](https://docs.stripe.com/changelog/dahlia/2026-05-27/payment-method-configurations-active-status-filtering.md)
- [Adds card brand restrictions to Payment Links](https://docs.stripe.com/changelog/dahlia/2026-05-27/adds-card-brand-restrictions-to-payment-links.md)
- [Adds support for Scalapay payments](https://docs.stripe.com/changelog/dahlia/2026-05-27/scalapay-payments.md)
