# Adds BUUT as a supported bank when using iDEAL

## What’s new

Adds support for the bank BUUT when using [iDEAL payments](https://docs.stripe.com/payments/ideal.md).

## Impact

You can specify BUUT as a bank when you use the iDEAL payment method with [Payment Intents](https://docs.stripe.com/api/payment_intents/object.md?api-version=2025-06-30.basil) and [Setup Intents](https://docs.stripe.com/api/setup_intents/object.md?api-version=2025-06-30.basil).

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `buut` | Added | [Charge.payment_method_details.ideal.bank](/api/charges/object?api-version=2025-06-30.basil), [ConfirmationToken.payment_method_preview.ideal.bank](/api/confirmation_tokens/object?api-version=2025-06-30.basil), [ConfirmationToken.testHelpers#create.payment_method_data.ideal.bank](/api/confirmation_tokens/object?api-version=2025-06-30.basil), [PaymentIntent#confirm.payment_method_data.ideal.bank](/api/payment_intents/object?api-version=2025-06-30.basil), [PaymentIntent#create.payment_method_data.ideal.bank](/api/payment_intents/object?api-version=2025-06-30.basil), [PaymentIntent#update.payment_method_data.ideal.bank](/api/payment_intents/object?api-version=2025-06-30.basil), [PaymentMethod#create.ideal.bank](/api/payment_methods/object?api-version=2025-06-30.basil), [PaymentMethod.ideal.bank](/api/payment_methods/object?api-version=2025-06-30.basil), [SetupAttempt.payment_method_details.ideal.bank](/api/setup_intents/object?api-version=2025-06-30.basil), [SetupIntent#confirm.payment_method_data.ideal.bank](/api/setup_intents/object?api-version=2025-06-30.basil), [SetupIntent#create.payment_method_data.ideal.bank](/api/setup_intents/object?api-version=2025-06-30.basil), [SetupIntent#update.payment_method_data.ideal.bank](/api/setup_intents/object?api-version=2025-06-30.basil) |
| `BUUTNL2A` | Added | [Charge.payment_method_details.ideal.bic](/api/charges/object?api-version=2025-06-30.basil), [ConfirmationToken.payment_method_preview.ideal.bic](/api/confirmation_tokens/object?api-version=2025-06-30.basil), [PaymentMethod.ideal.bic](/api/payment_methods/object?api-version=2025-06-30.basil), [SetupAttempt.payment_method_details.ideal.bic](/api/setup_intents/object?api-version=2025-06-30.basil) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `buut` | Added | [Charge.PaymentMethodDetail.Ideal.bank](/api/charges/object?api-version=2025-06-30.basil), [ConfirmationToken.CreateParamsPaymentMethodDatumIdeal.bank](/api/confirmation_tokens/object?api-version=2025-06-30.basil), [ConfirmationToken.PaymentMethodPreview.Ideal.bank](/api/confirmation_tokens/object?api-version=2025-06-30.basil), [PaymentIntent.ConfirmParamsPaymentMethodDatumIdeal.bank](/api/payment_intents/object?api-version=2025-06-30.basil), [PaymentIntent.CreateParamsPaymentMethodDatumIdeal.bank](/api/payment_intents/object?api-version=2025-06-30.basil), [PaymentIntent.ModifyParamsPaymentMethodDatumIdeal.bank](/api/payment_intents/object?api-version=2025-06-30.basil), [PaymentMethod.CreateParamsIdeal.bank](/api/payment_methods/object?api-version=2025-06-30.basil), [PaymentMethod.Ideal.bank](/api/payment_methods/object?api-version=2025-06-30.basil), [SetupAttempt.PaymentMethodDetail.Ideal.bank](/api/setup_intents/object?api-version=2025-06-30.basil), [SetupIntent.ConfirmParamsPaymentMethodDatumIdeal.bank](/api/setup_intents/object?api-version=2025-06-30.basil), [SetupIntent.CreateParamsPaymentMethodDatumIdeal.bank](/api/setup_intents/object?api-version=2025-06-30.basil), [SetupIntent.ModifyParamsPaymentMethodDatumIdeal.bank](/api/setup_intents/object?api-version=2025-06-30.basil) |
| `BUUTNL2A` | Added | [Charge.PaymentMethodDetail.Ideal.bic](/api/charges/object?api-version=2025-06-30.basil), [ConfirmationToken.PaymentMethodPreview.Ideal.bic](/api/confirmation_tokens/object?api-version=2025-06-30.basil), [PaymentMethod.Ideal.bic](/api/payment_methods/object?api-version=2025-06-30.basil), [SetupAttempt.PaymentMethodDetail.Ideal.bic](/api/setup_intents/object?api-version=2025-06-30.basil) |

#### PHP

| Values | Change | Enums |
| --- | --- | --- |
| `buut` | Added | [PaymentMethod.ideal.bank](/api/payment_methods/object?api-version=2025-06-30.basil) |
| `BUUTNL2A` | Added | [PaymentMethod.ideal.bic](/api/payment_methods/object?api-version=2025-06-30.basil) |

#### Java

| Value | Change | Enums |
| --- | --- | --- |
| `buut` | Added | [ConfirmationTokenCreateParams.payment_method_data.ideal.bank](/api/confirmation_tokens/object?api-version=2025-06-30.basil), [PaymentIntentConfirmParams.payment_method_data.ideal.bank](/api/payment_intents/object?api-version=2025-06-30.basil), [PaymentIntentCreateParams.payment_method_data.ideal.bank](/api/payment_intents/object?api-version=2025-06-30.basil), [PaymentIntentUpdateParams.payment_method_data.ideal.bank](/api/payment_intents/object?api-version=2025-06-30.basil), [PaymentMethodCreateParams.ideal.bank](/api/payment_methods/object?api-version=2025-06-30.basil), [SetupIntentConfirmParams.payment_method_data.ideal.bank](/api/setup_intents/object?api-version=2025-06-30.basil), [SetupIntentCreateParams.payment_method_data.ideal.bank](/api/setup_intents/object?api-version=2025-06-30.basil), [SetupIntentUpdateParams.payment_method_data.ideal.bank](/api/setup_intents/object?api-version=2025-06-30.basil) |

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `buut` | Added | [Charge.payment_method_details.ideal.bank](/api/charges/object?api-version=2025-06-30.basil), [ConfirmationToken.payment_method_preview.ideal.bank](/api/confirmation_tokens/object?api-version=2025-06-30.basil), [ConfirmationTokenCreateParams.testHelpers.payment_method_data.ideal.bank](/api/confirmation_tokens/object?api-version=2025-06-30.basil), [PaymentIntentConfirmParams.payment_method_data.ideal.bank](/api/payment_intents/object?api-version=2025-06-30.basil), [PaymentIntentCreateParams.payment_method_data.ideal.bank](/api/payment_intents/object?api-version=2025-06-30.basil), [PaymentIntentUpdateParams.payment_method_data.ideal.bank](/api/payment_intents/object?api-version=2025-06-30.basil), [PaymentMethod.ideal.bank](/api/payment_methods/object?api-version=2025-06-30.basil), [PaymentMethodCreateParams.ideal.bank](/api/payment_methods/object?api-version=2025-06-30.basil), [SetupAttempt.payment_method_details.ideal.bank](/api/setup_intents/object?api-version=2025-06-30.basil), [SetupIntentConfirmParams.payment_method_data.ideal.bank](/api/setup_intents/object?api-version=2025-06-30.basil), [SetupIntentCreateParams.payment_method_data.ideal.bank](/api/setup_intents/object?api-version=2025-06-30.basil), [SetupIntentUpdateParams.payment_method_data.ideal.bank](/api/setup_intents/object?api-version=2025-06-30.basil) |
| `BUUTNL2A` | Added | [Charge.payment_method_details.ideal.bic](/api/charges/object?api-version=2025-06-30.basil), [ConfirmationToken.payment_method_preview.ideal.bic](/api/confirmation_tokens/object?api-version=2025-06-30.basil), [PaymentMethod.ideal.bic](/api/payment_methods/object?api-version=2025-06-30.basil), [SetupAttempt.payment_method_details.ideal.bic](/api/setup_intents/object?api-version=2025-06-30.basil) |

#### Go

| Values | Change | Enums |
| --- | --- | --- |
| `buut` | Added | [ConfirmationTokenPaymentMethodPreviewIdeal.Bank](/api/confirmation_tokens/object?api-version=2025-06-30.basil) |
| `BUUTNL2A` | Added | [ConfirmationTokenPaymentMethodPreviewIdeal.BIC](/api/confirmation_tokens/object?api-version=2025-06-30.basil) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-06-30.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.3.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.3.0](https://github.com/stripe/stripe-python/releases/tag/v12.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.4.0](https://github.com/stripe/stripe-php/releases/tag/v17.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.3.0](https://github.com/stripe/stripe-java/releases/tag/v29.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.3.0](https://github.com/stripe/stripe-node/releases/tag/v18.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.3.0](https://github.com/stripe/stripe-go/releases/tag/v82.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.3.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds new plan types for Japan instalments](https://docs.stripe.com/changelog/basil/2025-06-30/add_jp_installments_plan_types.md)
- [Adds support for saving Klarna payment methods](https://docs.stripe.com/changelog/basil/2025-06-30/klarna-saved-payment-methods.md)
- [Adds support for crypto payment method](https://docs.stripe.com/changelog/basil/2025-06-30/crypto-payment-method.md)
