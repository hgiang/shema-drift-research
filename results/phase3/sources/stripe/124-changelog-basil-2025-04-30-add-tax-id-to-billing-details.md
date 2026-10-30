# Adds tax ID to Payment Method billing details

## What’s new

Adds support for buyers in Latin American countries to provide their tax identifier when transacting with sellers outside Latin America, as required by local regulations.

## Impact

Many central banks in Latin America require Latin American buyers to provide their tax identifier when transacting with sellers outside Latin America. Stripe now uses the `tax_id` field on the Payment Method `billing_details` hash to collect and store a Latin American buyer’s tax identifier. [Checkout](https://docs.stripe.com/payments/checkout.md) and the [Payment Element](https://docs.stripe.com/payments/payment-element.md) collect the `tax_id` automatically. If your integration uses a different payment flow, you need to handle this requirement.

If the country of your Stripe account is the US, and you accept Pix payments, you must collect the buyer’s `tax_id` on the Payment Method `billing_details` hash. Populating this field is prohibited in all other circumstances. If you set the `tax_id` value for a transaction that doesn’t require it, the API returns the `tax_id_prohibited` error.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `tax_id` | Added | [Charge.billing_details](/api/charges/object?api-version=2025-04-30.basil#charge_object-billing_details), [ConfirmationToken.payment_method_preview.billing_details](/api/confirmation_tokens/object?api-version=2025-04-30.basil#confirmation_token_object-payment_method_preview-billing_details), [ConfirmationToken.testHelpers#create.payment_method_data.billing_details](/api/confirmation_tokens/object?api-version=2025-04-30.basil#create_confirmation_token-test_helpers-payment_method_data-billing_details), [PaymentIntent#confirm.payment_method_data.billing_details](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-confirm-payment_method_data-billing_details), [PaymentIntent#create.payment_method_data.billing_details](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-create-payment_method_data-billing_details), [PaymentIntent#update.payment_method_data.billing_details](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-update-payment_method_data-billing_details), [PaymentMethod#create.billing_details](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-create-billing_details), [PaymentMethod#update.billing_details](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-update-billing_details), [PaymentMethod.billing_details](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-billing_details), [SetupIntent#confirm.payment_method_data.billing_details](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-confirm-payment_method_data-billing_details), [SetupIntent#create.payment_method_data.billing_details](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-create-payment_method_data-billing_details), [SetupIntent#update.payment_method_data.billing_details](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-update-payment_method_data-billing_details) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `tax_id` | Added | [Charge::BillingDetail](/api/charges/object?api-version=2025-04-30.basil#charge_object-billing_details), [ConfirmationToken::CreateParams::PaymentMethodDatum::BillingDetail](/api/confirmation_tokens/object?api-version=2025-04-30.basil#create_confirmation_token-test_helpers-payment_method_data-billing_details), [ConfirmationToken::PaymentMethodPreview::BillingDetail](/api/confirmation_tokens/object?api-version=2025-04-30.basil#confirmation_token_object-payment_method_preview-billing_details), [PaymentIntent::ConfirmParams::PaymentMethodDatum::BillingDetail](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-confirm-payment_method_data-billing_details), [PaymentIntent::CreateParams::PaymentMethodDatum::BillingDetail](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-create-payment_method_data-billing_details), [PaymentIntent::UpdateParams::PaymentMethodDatum::BillingDetail](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-update-payment_method_data-billing_details), [PaymentMethod::BillingDetail](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-billing_details), [PaymentMethod::CreateParams::BillingDetail](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-create-billing_details), [PaymentMethod::UpdateParams::BillingDetail](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-update-billing_details), [SetupIntent::ConfirmParams::PaymentMethodDatum::BillingDetail](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-confirm-payment_method_data-billing_details), [SetupIntent::CreateParams::PaymentMethodDatum::BillingDetail](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-create-payment_method_data-billing_details), [SetupIntent::UpdateParams::PaymentMethodDatum::BillingDetail](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-update-payment_method_data-billing_details) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `tax_id` | Added | [Charge.BillingDetail](/api/charges/object?api-version=2025-04-30.basil#charge_object-billing_details), [ConfirmationToken.CreateParamsPaymentMethodDatumBillingDetail](/api/confirmation_tokens/object?api-version=2025-04-30.basil#create_confirmation_token-test_helpers-payment_method_data-billing_details), [ConfirmationToken.PaymentMethodPreview.BillingDetail](/api/confirmation_tokens/object?api-version=2025-04-30.basil#confirmation_token_object-payment_method_preview-billing_details), [PaymentIntent.ConfirmParamsPaymentMethodDatumBillingDetail](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-confirm-payment_method_data-billing_details), [PaymentIntent.CreateParamsPaymentMethodDatumBillingDetail](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-create-payment_method_data-billing_details), [PaymentIntent.UpdateParamsPaymentMethodDatumBillingDetail](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-update-payment_method_data-billing_details), [PaymentMethod.BillingDetail](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-billing_details), [PaymentMethod.CreateParamsBillingDetail](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-create-billing_details), [PaymentMethod.UpdateParamsBillingDetail](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-update-billing_details), [SetupIntent.ConfirmParamsPaymentMethodDatumBillingDetail](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-confirm-payment_method_data-billing_details), [SetupIntent.CreateParamsPaymentMethodDatumBillingDetail](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-create-payment_method_data-billing_details), [SetupIntent.UpdateParamsPaymentMethodDatumBillingDetail](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-update-payment_method_data-billing_details) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `taxId` | Added | [Charge.billing_details](/api/charges/object?api-version=2025-04-30.basil#charge_object-billing_details), [ConfirmationToken.payment_method_preview.billing_details](/api/confirmation_tokens/object?api-version=2025-04-30.basil#confirmation_token_object-payment_method_preview-billing_details), [ConfirmationTokenCreateParams.payment_method_data.billing_details](/api/confirmation_tokens/object?api-version=2025-04-30.basil#create_confirmation_token-test_helpers-payment_method_data-billing_details), [PaymentIntentConfirmParams.payment_method_data.billing_details](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-confirm-payment_method_data-billing_details), [PaymentIntentCreateParams.payment_method_data.billing_details](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-create-payment_method_data-billing_details), [PaymentIntentUpdateParams.payment_method_data.billing_details](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-update-payment_method_data-billing_details), [PaymentMethod.billing_details](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-billing_details), [PaymentMethodCreateParams.billing_details](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-create-billing_details), [PaymentMethodUpdateParams.billing_details](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-update-billing_details), [SetupIntentConfirmParams.payment_method_data.billing_details](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-confirm-payment_method_data-billing_details), [SetupIntentCreateParams.payment_method_data.billing_details](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-create-payment_method_data-billing_details), [SetupIntentUpdateParams.payment_method_data.billing_details](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-update-payment_method_data-billing_details) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `tax_id` | Added | [Charge.billing_details](/api/charges/object?api-version=2025-04-30.basil#charge_object-billing_details), [ConfirmationToken.payment_method_preview.billing_details](/api/confirmation_tokens/object?api-version=2025-04-30.basil#confirmation_token_object-payment_method_preview-billing_details), [ConfirmationTokenCreateParams.testHelpers.payment_method_data.billing_details](/api/confirmation_tokens/object?api-version=2025-04-30.basil#create_confirmation_token-test_helpers-payment_method_data-billing_details), [PaymentIntentConfirmParams.payment_method_data.billing_details](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-confirm-payment_method_data-billing_details), [PaymentIntentCreateParams.payment_method_data.billing_details](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-create-payment_method_data-billing_details), [PaymentIntentUpdateParams.payment_method_data.billing_details](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-update-payment_method_data-billing_details), [PaymentMethod.billing_details](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-billing_details), [PaymentMethodCreateParams.billing_details](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-create-billing_details), [PaymentMethodUpdateParams.billing_details](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-update-billing_details), [SetupIntentConfirmParams.payment_method_data.billing_details](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-confirm-payment_method_data-billing_details), [SetupIntentCreateParams.payment_method_data.billing_details](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-create-payment_method_data-billing_details), [SetupIntentUpdateParams.payment_method_data.billing_details](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-update-payment_method_data-billing_details) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `TaxID` | Added | [ChargeBillingDetails](/api/charges/object?api-version=2025-04-30.basil#charge_object-billing_details), [ConfirmationTokenPaymentMethodDataBillingDetailsParams](/api/confirmation_tokens/object?api-version=2025-04-30.basil#create_confirmation_token-test_helpers-payment_method_data-billing_details), [ConfirmationTokenPaymentMethodPreviewBillingDetails](/api/confirmation_tokens/object?api-version=2025-04-30.basil#confirmation_token_object-payment_method_preview-billing_details), [PaymentIntentConfirmPaymentMethodDataBillingDetailsParams](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-confirm-payment_method_data-billing_details), [PaymentIntentPaymentMethodDataBillingDetailsParams](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-create-payment_method_data-billing_details), [PaymentMethodBillingDetailsParams](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-create-billing_details), [PaymentMethodBillingDetails](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-billing_details), [SetupIntentConfirmPaymentMethodDataBillingDetailsParams](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-confirm-payment_method_data-billing_details), [SetupIntentPaymentMethodDataBillingDetailsParams](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-create-payment_method_data-billing_details) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `TaxId` | Added | [ChargeBillingDetails](/api/charges/object?api-version=2025-04-30.basil#charge_object-billing_details), [ConfirmationTokenPaymentMethodDataBillingDetailsOptions](/api/confirmation_tokens/object?api-version=2025-04-30.basil#create_confirmation_token-test_helpers-payment_method_data-billing_details), [ConfirmationTokenPaymentMethodPreviewBillingDetails](/api/confirmation_tokens/object?api-version=2025-04-30.basil#confirmation_token_object-payment_method_preview-billing_details), [PaymentIntentPaymentMethodDataBillingDetailsOptions](/api/payment_intents/object?api-version=2025-04-30.basil#payment_intent_object-create-payment_method_data-billing_details), [PaymentMethodBillingDetailsOptions](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-create-billing_details), [PaymentMethodBillingDetails](/api/payment_methods/object?api-version=2025-04-30.basil#payment_method_object-billing_details), [SetupIntentPaymentMethodDataBillingDetailsOptions](/api/setup_intents/object?api-version=2025-04-30.basil#setup_intent_object-create-payment_method_data-billing_details) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-04-30.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.1.0](https://github.com/stripe/stripe-python/releases/tag/v12.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.2.0](https://github.com/stripe/stripe-php/releases/tag/v17.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.1.0](https://github.com/stripe/stripe-java/releases/tag/v29.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.1.0](https://github.com/stripe/stripe-node/releases/tag/v18.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.1.0](https://github.com/stripe/stripe-go/releases/tag/v82.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds Affirm as a supported payment method for one-off invoices and subscriptions](https://docs.stripe.com/changelog/basil/2025-04-30/affirm-send-invoice.md)
- [Adds Pix to payment method configurations](https://docs.stripe.com/changelog/basil/2025-04-30/add_pix_to_payment_method_configuration.md)
- [Adds capture method option to Billie payments](https://docs.stripe.com/changelog/basil/2025-04-30/billie-capture-method-option.md)
