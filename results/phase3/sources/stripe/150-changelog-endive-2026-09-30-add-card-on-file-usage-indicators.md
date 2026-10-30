# Adds support for specifying card-on-file usage when saving and charging saved cards

## What’s new

Introduces new [payment_method_options.card](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-09-30.preview#payment_intent_object-payment_method_options-card) parameters:

- [setup_credential_usage](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-09-30.preview#payment_intent_object-payment_method_options-card-setup_credential_usage): Set this to declare how you intend to use a customer’s saved card on a [Setup Intent](https://docs.stripe.com/api/setup_intents.md?api-version=2026-09-30.preview) or a [Payment Intent](https://docs.stripe.com/api/payment_intents.md?api-version=2026-09-30.preview) that uses [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-card-setup_future_usage).
- [stored_credential_usage](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-09-30.preview#payment_intent_object-payment_method_options-card-stored_credential_usage): Set this when you charge a saved card off-session, to declare the usage type of the subsequent charge. The value is also returned on the resulting [Charge](https://docs.stripe.com/api/charges/object.md?api-version=2026-09-30.preview#charge_object-payment_method_details-card-stored_credential_usage).

Learn [how to save a card and charge it later](https://docs.stripe.com/payments/cards/save-and-reuse.md).

## Impact

Credential-on-file is a card network requirement for businesses that store a customer’s card and charge it in future transactions with a specific usage type. You can now declare that usage type directly through two card payment method options.

Learn [how to save a card and charge it later](https://docs.stripe.com/payments/cards/save-and-reuse.md).

We use this information as an input when determining how to represent the transaction to card networks, which helps support network compliance. Existing integrations are not affected unless they adopt these parameters.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `setup_credential_usage`, `stored_credential_usage` | Added | [Charge.payment_method_details.card](/api/charges/object?api-version=2026-09-30.preview#charge_object-payment_method_details-card), [PaymentIntent#confirm.payment_method_options.card](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-card), [PaymentIntent#create.payment_method_options.card](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-card), [PaymentIntent#update.payment_method_options.card](/api/payment_intents/update?api-version=2026-09-30.preview#update_payment_intent-payment_method_options-card), [PaymentIntent.payment_method_options.card](/api/payment_intents/object?api-version=2026-09-30.preview#payment_intent_object-payment_method_options-card) |
| `setup_credential_usage` | Added | [SetupIntent#confirm.payment_method_options.card](/api/setup_intents/confirm?api-version=2026-09-30.preview#confirm_setup_intent-payment_method_options-card), [SetupIntent#create.payment_method_options.card](/api/setup_intents/create?api-version=2026-09-30.preview#create_setup_intent-payment_method_options-card), [SetupIntent#update.payment_method_options.card](/api/setup_intents/update?api-version=2026-09-30.preview#update_setup_intent-payment_method_options-card), [SetupIntent.payment_method_options.card](/api/setup_intents/object?api-version=2026-09-30.preview#setup_intent_object-payment_method_options-card) |
| `stored_credential_usage` | Added | [PaymentAttemptRecord.payment_method_details.card](/api/payment-attempt-record/object?api-version=2026-09-30.preview#payment_attempt_record_object-payment_method_details-card), [PaymentRecord.payment_method_details.card](/api/payment-record/object?api-version=2026-09-30.preview#payment_record_object-payment_method_details-card) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setup_credential_usage`, `stored_credential_usage` | Added | [Charge::PaymentMethodDetail::Card](/api/charges/object?api-version=2026-09-30.preview#charge_object-payment_method_details-card), [PaymentIntent::PaymentMethodOption::Card](/api/payment_intents/object?api-version=2026-09-30.preview#payment_intent_object-payment_method_options-card), [PaymentIntentConfirmParams::PaymentMethodOption::Card](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-card), [PaymentIntentCreateParams::PaymentMethodOption::Card](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-card), [PaymentIntentUpdateParams::PaymentMethodOption::Card](/api/payment_intents/update?api-version=2026-09-30.preview#update_payment_intent-payment_method_options-card) |
| `setup_credential_usage` | Added | [SetupIntent::PaymentMethodOption::Card](/api/setup_intents/object?api-version=2026-09-30.preview#setup_intent_object-payment_method_options-card), [SetupIntentConfirmParams::PaymentMethodOption::Card](/api/setup_intents/confirm?api-version=2026-09-30.preview#confirm_setup_intent-payment_method_options-card), [SetupIntentCreateParams::PaymentMethodOption::Card](/api/setup_intents/create?api-version=2026-09-30.preview#create_setup_intent-payment_method_options-card), [SetupIntentUpdateParams::PaymentMethodOption::Card](/api/setup_intents/update?api-version=2026-09-30.preview#update_setup_intent-payment_method_options-card) |
| `stored_credential_usage` | Added | [PaymentAttemptRecord::PaymentMethodDetail::Card](/api/payment-attempt-record/object?api-version=2026-09-30.preview#payment_attempt_record_object-payment_method_details-card), [PaymentRecord::PaymentMethodDetail::Card](/api/payment-record/object?api-version=2026-09-30.preview#payment_record_object-payment_method_details-card) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setup_credential_usage`, `stored_credential_usage` | Added | [Charge.PaymentMethodDetail.Card](/api/charges/object?api-version=2026-09-30.preview#charge_object-payment_method_details-card), [PaymentIntent.PaymentMethodOption.Card](/api/payment_intents/object?api-version=2026-09-30.preview#payment_intent_object-payment_method_options-card), [PaymentIntentConfirmParamsPaymentMethodOptionCard](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-card), [PaymentIntentCreateParamsPaymentMethodOptionCard](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-card), [PaymentIntentModifyParamsPaymentMethodOptionCard](/api/payment_intents/update?api-version=2026-09-30.preview#update_payment_intent-payment_method_options-card) |
| `setup_credential_usage` | Added | [SetupIntent.PaymentMethodOption.Card](/api/setup_intents/object?api-version=2026-09-30.preview#setup_intent_object-payment_method_options-card), [SetupIntentConfirmParamsPaymentMethodOptionCard](/api/setup_intents/confirm?api-version=2026-09-30.preview#confirm_setup_intent-payment_method_options-card), [SetupIntentCreateParamsPaymentMethodOptionCard](/api/setup_intents/create?api-version=2026-09-30.preview#create_setup_intent-payment_method_options-card), [SetupIntentModifyParamsPaymentMethodOptionCard](/api/setup_intents/update?api-version=2026-09-30.preview#update_setup_intent-payment_method_options-card) |
| `stored_credential_usage` | Added | [PaymentAttemptRecord.PaymentMethodDetail.Card](/api/payment-attempt-record/object?api-version=2026-09-30.preview#payment_attempt_record_object-payment_method_details-card), [PaymentRecord.PaymentMethodDetail.Card](/api/payment-record/object?api-version=2026-09-30.preview#payment_record_object-payment_method_details-card) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setup_credential_usage`, `stored_credential_usage` | Added | [Charge.payment_method_details.card](/api/charges/object?api-version=2026-09-30.preview#charge_object-payment_method_details-card), [PaymentIntent.confirm().$params.payment_method_option.card](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-card), [PaymentIntent.create().$params.payment_method_option.card](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-card), [PaymentIntent.payment_method_options.card](/api/payment_intents/object?api-version=2026-09-30.preview#payment_intent_object-payment_method_options-card), [PaymentIntent.update().$params.payment_method_option.card](/api/payment_intents/update?api-version=2026-09-30.preview#update_payment_intent-payment_method_options-card) |
| `setup_credential_usage` | Added | [SetupIntent.confirm().$params.payment_method_option.card](/api/setup_intents/confirm?api-version=2026-09-30.preview#confirm_setup_intent-payment_method_options-card), [SetupIntent.create().$params.payment_method_option.card](/api/setup_intents/create?api-version=2026-09-30.preview#create_setup_intent-payment_method_options-card), [SetupIntent.payment_method_options.card](/api/setup_intents/object?api-version=2026-09-30.preview#setup_intent_object-payment_method_options-card), [SetupIntent.update().$params.payment_method_option.card](/api/setup_intents/update?api-version=2026-09-30.preview#update_setup_intent-payment_method_options-card) |
| `stored_credential_usage` | Added | [PaymentAttemptRecord.payment_method_details.card](/api/payment-attempt-record/object?api-version=2026-09-30.preview#payment_attempt_record_object-payment_method_details-card), [PaymentRecord.payment_method_details.card](/api/payment-record/object?api-version=2026-09-30.preview#payment_record_object-payment_method_details-card) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setupCredentialUsage`, `storedCredentialUsage` | Added | [Charge.payment_method_details.card](/api/charges/object?api-version=2026-09-30.preview#charge_object-payment_method_details-card), [PaymentIntent.payment_method_options.card](/api/payment_intents/object?api-version=2026-09-30.preview#payment_intent_object-payment_method_options-card), [PaymentIntentConfirmParams.payment_method_options.card](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-card), [PaymentIntentCreateParams.payment_method_options.card](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-card), [PaymentIntentUpdateParams.payment_method_options.card](/api/payment_intents/update?api-version=2026-09-30.preview#update_payment_intent-payment_method_options-card) |
| `setupCredentialUsage` | Added | [SetupIntent.payment_method_options.card](/api/setup_intents/object?api-version=2026-09-30.preview#setup_intent_object-payment_method_options-card), [SetupIntentConfirmParams.payment_method_options.card](/api/setup_intents/confirm?api-version=2026-09-30.preview#confirm_setup_intent-payment_method_options-card), [SetupIntentCreateParams.payment_method_options.card](/api/setup_intents/create?api-version=2026-09-30.preview#create_setup_intent-payment_method_options-card), [SetupIntentUpdateParams.payment_method_options.card](/api/setup_intents/update?api-version=2026-09-30.preview#update_setup_intent-payment_method_options-card) |
| `storedCredentialUsage` | Added | [PaymentAttemptRecord.payment_method_details.card](/api/payment-attempt-record/object?api-version=2026-09-30.preview#payment_attempt_record_object-payment_method_details-card), [PaymentRecord.payment_method_details.card](/api/payment-record/object?api-version=2026-09-30.preview#payment_record_object-payment_method_details-card) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setup_credential_usage`, `stored_credential_usage` | Added | [Charge.payment_method_details.card](/api/charges/object?api-version=2026-09-30.preview#charge_object-payment_method_details-card), [PaymentIntent.payment_method_options.card](/api/payment_intents/object?api-version=2026-09-30.preview#payment_intent_object-payment_method_options-card), [PaymentIntentConfirmParams.payment_method_options.card](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-card), [PaymentIntentCreateParams.payment_method_options.card](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-card), [PaymentIntentUpdateParams.payment_method_options.card](/api/payment_intents/update?api-version=2026-09-30.preview#update_payment_intent-payment_method_options-card) |
| `setup_credential_usage` | Added | [SetupIntent.payment_method_options.card](/api/setup_intents/object?api-version=2026-09-30.preview#setup_intent_object-payment_method_options-card), [SetupIntentConfirmParams.payment_method_options.card](/api/setup_intents/confirm?api-version=2026-09-30.preview#confirm_setup_intent-payment_method_options-card), [SetupIntentCreateParams.payment_method_options.card](/api/setup_intents/create?api-version=2026-09-30.preview#create_setup_intent-payment_method_options-card), [SetupIntentUpdateParams.payment_method_options.card](/api/setup_intents/update?api-version=2026-09-30.preview#update_setup_intent-payment_method_options-card) |
| `stored_credential_usage` | Added | [PaymentAttemptRecord.payment_method_details.card](/api/payment-attempt-record/object?api-version=2026-09-30.preview#payment_attempt_record_object-payment_method_details-card), [PaymentRecord.payment_method_details.card](/api/payment-record/object?api-version=2026-09-30.preview#payment_record_object-payment_method_details-card) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `SetupCredentialUsage`, `StoredCredentialUsage` | Added | [ChargePaymentMethodDetailsCard](/api/charges/object?api-version=2026-09-30.preview#charge_object-payment_method_details-card), [PaymentIntentConfirmPaymentMethodOptionsCardParams](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-card), [PaymentIntentPaymentMethodOptionsCard](/api/payment_intents/object?api-version=2026-09-30.preview#payment_intent_object-payment_method_options-card), [PaymentIntentPaymentMethodOptionsCardParams](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-card) |
| `SetupCredentialUsage` | Added | [SetupIntentConfirmPaymentMethodOptionsCardParams](/api/setup_intents/confirm?api-version=2026-09-30.preview#confirm_setup_intent-payment_method_options-card), [SetupIntentPaymentMethodOptionsCard](/api/setup_intents/object?api-version=2026-09-30.preview#setup_intent_object-payment_method_options-card), [SetupIntentPaymentMethodOptionsCardParams](/api/setup_intents/create?api-version=2026-09-30.preview#create_setup_intent-payment_method_options-card) |
| `StoredCredentialUsage` | Added | [PaymentAttemptRecordPaymentMethodDetailsCard](/api/payment-attempt-record/object?api-version=2026-09-30.preview#payment_attempt_record_object-payment_method_details-card), [PaymentRecordPaymentMethodDetailsCard](/api/payment-record/object?api-version=2026-09-30.preview#payment_record_object-payment_method_details-card) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `SetupCredentialUsage`, `StoredCredentialUsage` | Added | [Charge.PaymentMethodDetails.Card](/api/charges/object?api-version=2026-09-30.preview#charge_object-payment_method_details-card), [PaymentIntent.PaymentMethodOptions.Card](/api/payment_intents/object?api-version=2026-09-30.preview#payment_intent_object-payment_method_options-card), [PaymentIntentPaymentMethodOptionsCardOptions](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-card) |
| `SetupCredentialUsage` | Added | [SetupIntent.PaymentMethodOptions.Card](/api/setup_intents/object?api-version=2026-09-30.preview#setup_intent_object-payment_method_options-card), [SetupIntentPaymentMethodOptionsCardOptions](/api/setup_intents/create?api-version=2026-09-30.preview#create_setup_intent-payment_method_options-card) |
| `StoredCredentialUsage` | Added | [PaymentAttemptRecord.PaymentMethodDetails.Card](/api/payment-attempt-record/object?api-version=2026-09-30.preview#payment_attempt_record_object-payment_method_details-card), [PaymentRecord.PaymentMethodDetails.Card](/api/payment-record/object?api-version=2026-09-30.preview#payment_record_object-payment_method_details-card) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.preview`
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

- [Adds page limit validation for dispute evidence](https://docs.stripe.com/changelog/endive/2026-09-30/page-limit-validation-for-dispute-evidence.md)
- [Removes the capture method parameter for PayPay payments](https://docs.stripe.com/changelog/endive/2026-09-30/removes-capture-method-parameter-for-paypay-payments.md)
- [Adds the ability to update payment intent data on Checkout Sessions](https://docs.stripe.com/changelog/endive/2026-09-30/update-payment-intent-data-on-checkout-sessions.md)
- [Adds support for submitting evidence to appeal a dispute decision](https://docs.stripe.com/changelog/endive/2026-09-30/submit-evidence-to-appeal-dispute-decision.md)
