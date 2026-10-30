# Removes the source type property from Stripe balance payment methods

## What’s new

Removes the `source_type` property from API resources that reference a Payment Method with a [type](https://docs.stripe.com/api/payment_methods/object.md?api-version=2026-03-25.preview#payment_method_object-type) of `stripe_balance`.

The `source_type` property can appear in different hashes, depending on the resource. For example, in the Payment Record object, the removed property is [payment_method_details.stripe_balance.source_type](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-02-25.preview#payment_record_object-payment_method_details-stripe_balance-source_type), and in the create `/v1/payment_methods` method, the removed parameter is [stripe_balance.source_type](https://docs.stripe.com/api/payment_methods/create.md?api-version=2026-02-25.preview#create_payment_method-stripe_balance-source_type).

## Why is this a breaking change?

Stripe balance payment methods no longer support the `source_type` property. If your integration references the `source_type` property for Stripe balance payments, you must remove it from your code.

- Requests that include the `source_type` parameter for Stripe balance payments now fail with a `parameter_unknown` error.
- Responses and objects for Stripe balance payments no longer include the `source_type` property.

## Impact

This change only affects integrations using [Stripe balance payments](https://docs.stripe.com/payments/pay-with-balance.md). It removes the `source_type` property from the following resources when they represent Stripe balance payments:

- [Charges](https://docs.stripe.com/api/charges.md?api-version=2026-03-25.preview)
- [Confirmation Tokens](https://docs.stripe.com/api/confirmation_tokens.md?api-version=2026-03-25.preview)
- [Payment Attempt Records](https://docs.stripe.com/api/payment-attempt-record.md?api-version=2026-03-25.preview)
- [Payment Intents](https://docs.stripe.com/api/payment_intents.md?api-version=2026-03-25.preview)
- [Payment Methods](https://docs.stripe.com/api/payment_methods.md?api-version=2026-03-25.preview)
- [Payment Records](https://docs.stripe.com/api/payment-record.md?api-version=2026-03-25.preview)
- [Setup Intents](https://docs.stripe.com/api/setup_intents.md?api-version=2026-03-25.preview)

You can no longer include the `source_type` parameter when calling any endpoints of the affected resources for a Stripe balance payment. You can no longer reference the `source_type` property in objects or responses of the affected resources when they’re associated with a Stripe balance payment.

No action is needed if you don’t use the `stripe_balance` payment method.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `source_type` | Removed | [Charge.payment_method_details.stripe_balance](/api/charges/object?api-version=2026-03-25.preview#charge_object-payment_method_details-stripe_balance), [ConfirmationToken.payment_method_preview.stripe_balance](/api/confirmation_tokens/object?api-version=2026-03-25.preview#confirmation_token_object-payment_method_preview-stripe_balance), [ConfirmationToken.testHelpers#create.payment_method_data.stripe_balance](/api/confirmation_tokens/test_create?api-version=2026-03-25.preview#test_create-payment_method_data-stripe_balance), [PaymentAttemptRecord.payment_method_details.stripe_balance](/api/payment-attempt-record/object?api-version=2026-03-25.preview#payment_attempt_record_object-payment_method_details-stripe_balance), [PaymentIntent#confirm.payment_method_data.stripe_balance](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-payment_method_data-stripe_balance), [PaymentIntent#create.payment_method_data.stripe_balance](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-payment_method_data-stripe_balance), [PaymentIntent#update.payment_method_data.stripe_balance](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-payment_method_data-stripe_balance), [PaymentMethod#create.stripe_balance](/api/payment_methods/create?api-version=2026-03-25.preview#create_payment_method-stripe_balance), [PaymentMethod.stripe_balance](/api/payment_methods/object?api-version=2026-03-25.preview#payment_method_object-stripe_balance), [PaymentRecord.payment_method_details.stripe_balance](/api/payment-record/object?api-version=2026-03-25.preview#payment_record_object-payment_method_details-stripe_balance), [SetupIntent#confirm.payment_method_data.stripe_balance](/api/setup_intents/confirm?api-version=2026-03-25.preview#confirm_setup_intent-payment_method_data-stripe_balance), [SetupIntent#create.payment_method_data.stripe_balance](/api/setup_intents/create?api-version=2026-03-25.preview#create_setup_intent-payment_method_data-stripe_balance), [SetupIntent#update.payment_method_data.stripe_balance](/api/setup_intents/update?api-version=2026-03-25.preview#update_setup_intent-payment_method_data-stripe_balance) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `source_type` | Removed | [Charge::PaymentMethodDetail::StripeBalance](/api/charges/object?api-version=2026-03-25.preview#charge_object-payment_method_details-stripe_balance), [ConfirmationToken::PaymentMethodPreview::StripeBalance](/api/confirmation_tokens/object?api-version=2026-03-25.preview#confirmation_token_object-payment_method_preview-stripe_balance), [ConfirmationTokenCreateParams::PaymentMethodDatum::StripeBalance](/api/confirmation_tokens/test_create?api-version=2026-03-25.preview#test_create-payment_method_data-stripe_balance), [PaymentAttemptRecord::PaymentMethodDetail::StripeBalance](/api/payment-attempt-record/object?api-version=2026-03-25.preview#payment_attempt_record_object-payment_method_details-stripe_balance), [PaymentIntentConfirmParams::PaymentMethodDatum::StripeBalance](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-payment_method_data-stripe_balance), [PaymentIntentCreateParams::PaymentMethodDatum::StripeBalance](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-payment_method_data-stripe_balance), [PaymentIntentUpdateParams::PaymentMethodDatum::StripeBalance](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-payment_method_data-stripe_balance), [PaymentMethod::StripeBalance](/api/payment_methods/object?api-version=2026-03-25.preview#payment_method_object-stripe_balance), [PaymentMethodCreateParams::StripeBalance](/api/payment_methods/create?api-version=2026-03-25.preview#create_payment_method-stripe_balance), [PaymentRecord::PaymentMethodDetail::StripeBalance](/api/payment-record/object?api-version=2026-03-25.preview#payment_record_object-payment_method_details-stripe_balance), [SetupIntentConfirmParams::PaymentMethodDatum::StripeBalance](/api/setup_intents/confirm?api-version=2026-03-25.preview#confirm_setup_intent-payment_method_data-stripe_balance), [SetupIntentCreateParams::PaymentMethodDatum::StripeBalance](/api/setup_intents/create?api-version=2026-03-25.preview#create_setup_intent-payment_method_data-stripe_balance), [SetupIntentUpdateParams::PaymentMethodDatum::StripeBalance](/api/setup_intents/update?api-version=2026-03-25.preview#update_setup_intent-payment_method_data-stripe_balance) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `source_type` | Removed | [Charge.PaymentMethodDetail.StripeBalance](/api/charges/object?api-version=2026-03-25.preview#charge_object-payment_method_details-stripe_balance), [ConfirmationToken.PaymentMethodPreview.StripeBalance](/api/confirmation_tokens/object?api-version=2026-03-25.preview#confirmation_token_object-payment_method_preview-stripe_balance), [ConfirmationTokenCreateParamsPaymentMethodDatumStripeBalance](/api/confirmation_tokens/test_create?api-version=2026-03-25.preview#test_create-payment_method_data-stripe_balance), [PaymentAttemptRecord.PaymentMethodDetail.StripeBalance](/api/payment-attempt-record/object?api-version=2026-03-25.preview#payment_attempt_record_object-payment_method_details-stripe_balance), [PaymentIntentConfirmParamsPaymentMethodDatumStripeBalance](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-payment_method_data-stripe_balance), [PaymentIntentCreateParamsPaymentMethodDatumStripeBalance](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-payment_method_data-stripe_balance), [PaymentIntentModifyParamsPaymentMethodDatumStripeBalance](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-payment_method_data-stripe_balance), [PaymentMethod.StripeBalance](/api/payment_methods/object?api-version=2026-03-25.preview#payment_method_object-stripe_balance), [PaymentMethodCreateParamsStripeBalance](/api/payment_methods/create?api-version=2026-03-25.preview#create_payment_method-stripe_balance), [PaymentRecord.PaymentMethodDetail.StripeBalance](/api/payment-record/object?api-version=2026-03-25.preview#payment_record_object-payment_method_details-stripe_balance), [SetupIntentConfirmParamsPaymentMethodDatumStripeBalance](/api/setup_intents/confirm?api-version=2026-03-25.preview#confirm_setup_intent-payment_method_data-stripe_balance), [SetupIntentCreateParamsPaymentMethodDatumStripeBalance](/api/setup_intents/create?api-version=2026-03-25.preview#create_setup_intent-payment_method_data-stripe_balance), [SetupIntentModifyParamsPaymentMethodDatumStripeBalance](/api/setup_intents/update?api-version=2026-03-25.preview#update_setup_intent-payment_method_data-stripe_balance) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `source_type` | Removed | [Charge.payment_method_details.stripe_balance](/api/charges/object?api-version=2026-03-25.preview#charge_object-payment_method_details-stripe_balance), [ConfirmationToken.create().$params.payment_method_datum.stripe_balance](/api/confirmation_tokens/test_create?api-version=2026-03-25.preview#test_create-payment_method_data-stripe_balance), [ConfirmationToken.payment_method_preview.stripe_balance](/api/confirmation_tokens/object?api-version=2026-03-25.preview#confirmation_token_object-payment_method_preview-stripe_balance), [PaymentAttemptRecord.payment_method_details.stripe_balance](/api/payment-attempt-record/object?api-version=2026-03-25.preview#payment_attempt_record_object-payment_method_details-stripe_balance), [PaymentIntent.confirm().$params.payment_method_datum.stripe_balance](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-payment_method_data-stripe_balance), [PaymentIntent.create().$params.payment_method_datum.stripe_balance](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-payment_method_data-stripe_balance), [PaymentIntent.update().$params.payment_method_datum.stripe_balance](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-payment_method_data-stripe_balance), [PaymentMethod.create().$params.stripe_balance](/api/payment_methods/create?api-version=2026-03-25.preview#create_payment_method-stripe_balance), [PaymentMethod.stripe_balance](/api/payment_methods/object?api-version=2026-03-25.preview#payment_method_object-stripe_balance), [PaymentRecord.payment_method_details.stripe_balance](/api/payment-record/object?api-version=2026-03-25.preview#payment_record_object-payment_method_details-stripe_balance), [SetupIntent.confirm().$params.payment_method_datum.stripe_balance](/api/setup_intents/confirm?api-version=2026-03-25.preview#confirm_setup_intent-payment_method_data-stripe_balance), [SetupIntent.create().$params.payment_method_datum.stripe_balance](/api/setup_intents/create?api-version=2026-03-25.preview#create_setup_intent-payment_method_data-stripe_balance), [SetupIntent.update().$params.payment_method_datum.stripe_balance](/api/setup_intents/update?api-version=2026-03-25.preview#update_setup_intent-payment_method_data-stripe_balance) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sourceType` | Removed | [Charge.payment_method_details.stripe_balance](/api/charges/object?api-version=2026-03-25.preview#charge_object-payment_method_details-stripe_balance), [ConfirmationToken.payment_method_preview.stripe_balance](/api/confirmation_tokens/object?api-version=2026-03-25.preview#confirmation_token_object-payment_method_preview-stripe_balance), [ConfirmationTokenCreateParams.payment_method_data.stripe_balance](/api/confirmation_tokens/test_create?api-version=2026-03-25.preview#test_create-payment_method_data-stripe_balance), [PaymentAttemptRecord.payment_method_details.stripe_balance](/api/payment-attempt-record/object?api-version=2026-03-25.preview#payment_attempt_record_object-payment_method_details-stripe_balance), [PaymentIntentConfirmParams.payment_method_data.stripe_balance](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-payment_method_data-stripe_balance), [PaymentIntentCreateParams.payment_method_data.stripe_balance](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-payment_method_data-stripe_balance), [PaymentIntentUpdateParams.payment_method_data.stripe_balance](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-payment_method_data-stripe_balance), [PaymentMethod.stripe_balance](/api/payment_methods/object?api-version=2026-03-25.preview#payment_method_object-stripe_balance), [PaymentMethodCreateParams.stripe_balance](/api/payment_methods/create?api-version=2026-03-25.preview#create_payment_method-stripe_balance), [PaymentRecord.payment_method_details.stripe_balance](/api/payment-record/object?api-version=2026-03-25.preview#payment_record_object-payment_method_details-stripe_balance), [SetupIntentConfirmParams.payment_method_data.stripe_balance](/api/setup_intents/confirm?api-version=2026-03-25.preview#confirm_setup_intent-payment_method_data-stripe_balance), [SetupIntentCreateParams.payment_method_data.stripe_balance](/api/setup_intents/create?api-version=2026-03-25.preview#create_setup_intent-payment_method_data-stripe_balance), [SetupIntentUpdateParams.payment_method_data.stripe_balance](/api/setup_intents/update?api-version=2026-03-25.preview#update_setup_intent-payment_method_data-stripe_balance) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `source_type` | Removed | [Charge.payment_method_details.stripe_balance](/api/charges/object?api-version=2026-03-25.preview#charge_object-payment_method_details-stripe_balance), [ConfirmationToken.payment_method_preview.stripe_balance](/api/confirmation_tokens/object?api-version=2026-03-25.preview#confirmation_token_object-payment_method_preview-stripe_balance), [ConfirmationTokenCreateParams.testHelpers.payment_method_data.stripe_balance](/api/confirmation_tokens/test_create?api-version=2026-03-25.preview#test_create-payment_method_data-stripe_balance), [PaymentAttemptRecord.payment_method_details.stripe_balance](/api/payment-attempt-record/object?api-version=2026-03-25.preview#payment_attempt_record_object-payment_method_details-stripe_balance), [PaymentIntentConfirmParams.payment_method_data.stripe_balance](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-payment_method_data-stripe_balance), [PaymentIntentCreateParams.payment_method_data.stripe_balance](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-payment_method_data-stripe_balance), [PaymentIntentUpdateParams.payment_method_data.stripe_balance](/api/payment_intents/update?api-version=2026-03-25.preview#update_payment_intent-payment_method_data-stripe_balance), [PaymentMethod.stripe_balance](/api/payment_methods/object?api-version=2026-03-25.preview#payment_method_object-stripe_balance), [PaymentMethodCreateParams.stripe_balance](/api/payment_methods/create?api-version=2026-03-25.preview#create_payment_method-stripe_balance), [PaymentRecord.payment_method_details.stripe_balance](/api/payment-record/object?api-version=2026-03-25.preview#payment_record_object-payment_method_details-stripe_balance), [SetupIntentConfirmParams.payment_method_data.stripe_balance](/api/setup_intents/confirm?api-version=2026-03-25.preview#confirm_setup_intent-payment_method_data-stripe_balance), [SetupIntentCreateParams.payment_method_data.stripe_balance](/api/setup_intents/create?api-version=2026-03-25.preview#create_setup_intent-payment_method_data-stripe_balance), [SetupIntentUpdateParams.payment_method_data.stripe_balance](/api/setup_intents/update?api-version=2026-03-25.preview#update_setup_intent-payment_method_data-stripe_balance) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SourceType` | Removed | [ChargePaymentMethodDetailsStripeBalance](/api/charges/object?api-version=2026-03-25.preview#charge_object-payment_method_details-stripe_balance), [ConfirmationTokenPaymentMethodDataStripeBalanceParams](/api/confirmation_tokens/test_create?api-version=2026-03-25.preview#test_create-payment_method_data-stripe_balance), [ConfirmationTokenPaymentMethodPreviewStripeBalance](/api/confirmation_tokens/object?api-version=2026-03-25.preview#confirmation_token_object-payment_method_preview-stripe_balance), [PaymentAttemptRecordPaymentMethodDetailsStripeBalance](/api/payment-attempt-record/object?api-version=2026-03-25.preview#payment_attempt_record_object-payment_method_details-stripe_balance), [PaymentIntentConfirmPaymentMethodDataStripeBalanceParams](/api/payment_intents/confirm?api-version=2026-03-25.preview#confirm_payment_intent-payment_method_data-stripe_balance), [PaymentIntentPaymentMethodDataStripeBalanceParams](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-payment_method_data-stripe_balance), [PaymentMethodStripeBalance](/api/payment_methods/object?api-version=2026-03-25.preview#payment_method_object-stripe_balance), [PaymentMethodStripeBalanceParams](/api/payment_methods/create?api-version=2026-03-25.preview#create_payment_method-stripe_balance), [PaymentRecordPaymentMethodDetailsStripeBalance](/api/payment-record/object?api-version=2026-03-25.preview#payment_record_object-payment_method_details-stripe_balance), [SetupIntentConfirmPaymentMethodDataStripeBalanceParams](/api/setup_intents/confirm?api-version=2026-03-25.preview#confirm_setup_intent-payment_method_data-stripe_balance), [SetupIntentPaymentMethodDataStripeBalanceParams](/api/setup_intents/create?api-version=2026-03-25.preview#create_setup_intent-payment_method_data-stripe_balance) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SourceType` | Removed | [Charge.PaymentMethodDetails.StripeBalance](/api/charges/object?api-version=2026-03-25.preview#charge_object-payment_method_details-stripe_balance), [ConfirmationToken.PaymentMethodPreview.StripeBalance](/api/confirmation_tokens/object?api-version=2026-03-25.preview#confirmation_token_object-payment_method_preview-stripe_balance), [ConfirmationTokenPaymentMethodDataStripeBalanceOptions](/api/confirmation_tokens/test_create?api-version=2026-03-25.preview#test_create-payment_method_data-stripe_balance), [PaymentAttemptRecord.PaymentMethodDetails.StripeBalance](/api/payment-attempt-record/object?api-version=2026-03-25.preview#payment_attempt_record_object-payment_method_details-stripe_balance), [PaymentIntentPaymentMethodDataStripeBalanceOptions](/api/payment_intents/create?api-version=2026-03-25.preview#create_payment_intent-payment_method_data-stripe_balance), [PaymentMethod.StripeBalance](/api/payment_methods/object?api-version=2026-03-25.preview#payment_method_object-stripe_balance), [PaymentMethodStripeBalanceOptions](/api/payment_methods/create?api-version=2026-03-25.preview#create_payment_method-stripe_balance), [PaymentRecord.PaymentMethodDetails.StripeBalance](/api/payment-record/object?api-version=2026-03-25.preview#payment_record_object-payment_method_details-stripe_balance), [SetupIntentPaymentMethodDataStripeBalanceOptions](/api/setup_intents/create?api-version=2026-03-25.preview#create_setup_intent-payment_method_data-stripe_balance) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-03-25.preview`
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

- [Adds surcharge configuration options for card-not-present payments](https://docs.stripe.com/changelog/dahlia/2026-03-25/card-not-present-payments-surcharge-configuration-options.md)
- [Adds Risk Reserved Balance to the Balances API](https://docs.stripe.com/changelog/dahlia/2026-03-25/adds-risk-reserved-balance-to-the-balances-api.md)
