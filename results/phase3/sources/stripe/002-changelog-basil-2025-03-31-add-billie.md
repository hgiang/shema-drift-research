# Adds support for the Billie local payment method

## What’s new

Adds a new single-use local payment method [Billie](https://docs.stripe.com/payments/billie.md), a leading B2B buy now, pay later method.

## Impact

If your business is located in Austria, France, Germany, the Netherlands, Sweden, or the UK, you can now accept single-use [Billie](https://docs.stripe.com/payments/billie.md) payments from buyers across the European Union.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `billie_payments` | Added | [Account#create.capabilities](/api/accounts/create?api-version=2025-03-31.basil#create_account-capabilities), [Account#update.capabilities](/api/accounts/update?api-version=2025-03-31.basil#update_account-capabilities), [Account.capabilities](/api/accounts/object?api-version=2025-03-31.basil#account_object-capabilities) |
| `billie` | Added | [Charge.payment_method_details](/api/charges/object?api-version=2025-03-31.basil#charge_object-payment_method_details), [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-03-31.basil#confirmation_token_object-payment_method_preview), [ConfirmationToken.testHelpers#create.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-03-31.basil#test_create-payment_method_data), [PaymentIntent#confirm.payment_method_data](/api/payment_intents/confirm?api-version=2025-03-31.basil#confirm_payment_intent-payment_method_data), [PaymentIntent#create.payment_method_data](/api/payment_intents/create?api-version=2025-03-31.basil#create_payment_intent-payment_method_data), [PaymentIntent#update.payment_method_data](/api/payment_intents/update?api-version=2025-03-31.basil#update_payment_intent-payment_method_data), [PaymentMethod#create](/api/payment_methods/create?api-version=2025-03-31.basil), [PaymentMethodConfiguration#create](/api/payment_method_configurations/create?api-version=2025-03-31.basil), [PaymentMethodConfiguration#update](/api/payment_method_configurations/update?api-version=2025-03-31.basil), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-03-31.basil), [PaymentMethod](/api/payment_methods/object?api-version=2025-03-31.basil), [SetupIntent#confirm.payment_method_data](/api/setup_intents/confirm?api-version=2025-03-31.basil#confirm_setup_intent-payment_method_data), [SetupIntent#create.payment_method_data](/api/setup_intents/create?api-version=2025-03-31.basil#create_setup_intent-payment_method_data), [SetupIntent#update.payment_method_data](/api/setup_intents/update?api-version=2025-03-31.basil#update_setup_intent-payment_method_data) |

| Values | Change | Enums |
| --- | --- | --- |
| `billie` | Added | `Checkout.Session#create.payment_method_types` |
| `billie` | Added | [ConfirmationToken.testHelpers#create.payment_method_data.type](/api/confirmation_tokens/test_create?api-version=2025-03-31.basil#test_create-payment_method_data-type), [PaymentIntent#confirm.payment_method_data.type](/api/payment_intents/confirm?api-version=2025-03-31.basil#confirm_payment_intent-payment_method_data-type), [PaymentIntent#create.payment_method_data.type](/api/payment_intents/create?api-version=2025-03-31.basil#create_payment_intent-payment_method_data-type), [PaymentIntent#update.payment_method_data.type](/api/payment_intents/update?api-version=2025-03-31.basil#update_payment_intent-payment_method_data-type), [SetupIntent#confirm.payment_method_data.type](/api/setup_intents/confirm?api-version=2025-03-31.basil#confirm_setup_intent-payment_method_data-type), [SetupIntent#create.payment_method_data.type](/api/setup_intents/create?api-version=2025-03-31.basil#create_setup_intent-payment_method_data-type), [SetupIntent#update.payment_method_data.type](/api/setup_intents/update?api-version=2025-03-31.basil#update_setup_intent-payment_method_data-type) |
| `billie` | Added | [ConfirmationToken.payment_method_preview.type](/api/confirmation_tokens/object?api-version=2025-03-31.basil#confirmation_token_object-payment_method_preview-type), [PaymentMethod.type](/api/payment_methods/object?api-version=2025-03-31.basil#payment_method_object-type) |
| `billie` | Added | [Customer#list_payment_methods.type](/api/payment_methods/customer_list?api-version=2025-03-31.basil#list_customer_payment_methods-type), [PaymentMethod#create.type](/api/payment_methods/create?api-version=2025-03-31.basil#create_payment_method-type), [PaymentMethod#list.type](/api/payment_methods/list?api-version=2025-03-31.basil#list_payment_methods-type) |
| `billie` | Added | `PaymentLink#create.payment_method_types`, `PaymentLink#update.payment_method_types`, `PaymentLink.payment_method_types` |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `billie_payments` | Added | `Account.Capability`, `Account.CreateParamsCapability`, `Account.UpdateParamsCapability` |
| `billie` | Added | `Charge.PaymentMethodDetail`, `ConfirmationToken.CreateParamsPaymentMethodDatum`, `ConfirmationToken.PaymentMethodPreview`, `CustomerPaymentMethod`, `PaymentIntent.ConfirmParamsPaymentMethodDatum`, `PaymentIntent.CreateParamsPaymentMethodDatum`, `PaymentIntent.UpdateParamsPaymentMethodDatum`, `PaymentMethod.CreateParams`, `PaymentMethodConfiguration.CreateParams`, `PaymentMethodConfiguration.UpdateParams`, [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-03-31.basil), [PaymentMethod](/api/payment_methods/object?api-version=2025-03-31.basil), `SetupIntent.ConfirmParamsPaymentMethodDatum`, `SetupIntent.CreateParamsPaymentMethodDatum`, `SetupIntent.UpdateParamsPaymentMethodDatum` |

| Values | Change | Enums |
| --- | --- | --- |
| `billie` | Added | `checkout.Session.CreateParams.payment_method_types` |
| `billie` | Added | `ConfirmationToken.CreateParamsPaymentMethodDatum.type`, `PaymentIntent.ConfirmParamsPaymentMethodDatum.type`, `PaymentIntent.CreateParamsPaymentMethodDatum.type`, `PaymentIntent.UpdateParamsPaymentMethodDatum.type`, `SetupIntent.ConfirmParamsPaymentMethodDatum.type`, `SetupIntent.CreateParamsPaymentMethodDatum.type`, `SetupIntent.UpdateParamsPaymentMethodDatum.type` |
| `billie` | Added | `ConfirmationToken.PaymentMethodPreview.type`, `CustomerPaymentMethod.type`, [PaymentMethod.type](/api/payment_methods/object?api-version=2025-03-31.basil#payment_method_object-type) |
| `billie` | Added | `CustomerPaymentMethod.ListParams.type`, `PaymentMethod.CreateParams.type`, `PaymentMethod.ListParams.type` |
| `billie` | Added | `PaymentLink.CreateParams.payment_method_types`, `PaymentLink.UpdateParams.payment_method_types`, `PaymentLink.payment_method_types` |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billie` | Added | [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-03-31.basil), [PaymentMethod](/api/payment_methods/object?api-version=2025-03-31.basil) |

| Values | Change | Enums |
| --- | --- | --- |
| `billie` | Added | [ConfirmationToken.payment_method_preview.type](/api/confirmation_tokens/object?api-version=2025-03-31.basil#confirmation_token_object-payment_method_preview-type), [PaymentMethod.type](/api/payment_methods/object?api-version=2025-03-31.basil#payment_method_object-type) |
| `billie` | Added | `PaymentLink.payment_method_types` |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `billiePayments` | Added | [Account.capabilities](/api/accounts/object?api-version=2025-03-31.basil#account_object-capabilities), [AccountCreateParams.capabilities](/api/accounts/create?api-version=2025-03-31.basil#create_account-capabilities), [AccountUpdateParams.capabilities](/api/accounts/update?api-version=2025-03-31.basil#update_account-capabilities) |
| `billie` | Added | [Charge.payment_method_details](/api/charges/object?api-version=2025-03-31.basil#charge_object-payment_method_details), [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-03-31.basil#confirmation_token_object-payment_method_preview), [ConfirmationTokenCreateParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-03-31.basil#test_create-payment_method_data), `CustomerPaymentMethod`, [PaymentIntentConfirmParams.payment_method_data](/api/payment_intents/confirm?api-version=2025-03-31.basil#confirm_payment_intent-payment_method_data), [PaymentIntentCreateParams.payment_method_data](/api/payment_intents/create?api-version=2025-03-31.basil#create_payment_intent-payment_method_data), [PaymentIntentUpdateParams.payment_method_data](/api/payment_intents/update?api-version=2025-03-31.basil#update_payment_intent-payment_method_data), [PaymentMethodConfigurationCreateParams](/api/payment_method_configurations/create?api-version=2025-03-31.basil), [PaymentMethodConfigurationUpdateParams](/api/payment_method_configurations/update?api-version=2025-03-31.basil), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-03-31.basil), [PaymentMethodCreateParams](/api/payment_methods/create?api-version=2025-03-31.basil), [PaymentMethod](/api/payment_methods/object?api-version=2025-03-31.basil), [SetupIntentConfirmParams.payment_method_data](/api/setup_intents/confirm?api-version=2025-03-31.basil#confirm_setup_intent-payment_method_data), [SetupIntentCreateParams.payment_method_data](/api/setup_intents/create?api-version=2025-03-31.basil#create_setup_intent-payment_method_data), [SetupIntentUpdateParams.payment_method_data](/api/setup_intents/update?api-version=2025-03-31.basil#update_setup_intent-payment_method_data) |

| Values | Change | Enums |
| --- | --- | --- |
| `billie` | Added | `checkout.SessionCreateParams.paymentMethodTypes` |
| `billie` | Added | [ConfirmationTokenCreateParams.payment_method_data.type](/api/confirmation_tokens/test_create?api-version=2025-03-31.basil#test_create-payment_method_data-type), [PaymentIntentConfirmParams.payment_method_data.type](/api/payment_intents/confirm?api-version=2025-03-31.basil#confirm_payment_intent-payment_method_data-type), [PaymentIntentCreateParams.payment_method_data.type](/api/payment_intents/create?api-version=2025-03-31.basil#create_payment_intent-payment_method_data-type), [PaymentIntentUpdateParams.payment_method_data.type](/api/payment_intents/update?api-version=2025-03-31.basil#update_payment_intent-payment_method_data-type), [SetupIntentConfirmParams.payment_method_data.type](/api/setup_intents/confirm?api-version=2025-03-31.basil#confirm_setup_intent-payment_method_data-type), [SetupIntentCreateParams.payment_method_data.type](/api/setup_intents/create?api-version=2025-03-31.basil#create_setup_intent-payment_method_data-type), [SetupIntentUpdateParams.payment_method_data.type](/api/setup_intents/update?api-version=2025-03-31.basil#update_setup_intent-payment_method_data-type) |
| `billie` | Added | `CustomerPaymentMethodListParams.type`, [PaymentMethodCreateParams.type](/api/payment_methods/create?api-version=2025-03-31.basil#create_payment_method-type), [PaymentMethodListParams.type](/api/payment_methods/list?api-version=2025-03-31.basil#list_payment_methods-type) |
| `billie` | Added | `PaymentLinkCreateParams.paymentMethodTypes`, `PaymentLinkUpdateParams.paymentMethodTypes` |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `billie_payments` | Added | [Account.capabilities](/api/accounts/object?api-version=2025-03-31.basil#account_object-capabilities), [AccountCreateParams.capabilities](/api/accounts/create?api-version=2025-03-31.basil#create_account-capabilities), [AccountUpdateParams.capabilities](/api/accounts/update?api-version=2025-03-31.basil#update_account-capabilities) |
| `billie` | Added | [Charge.payment_method_details](/api/charges/object?api-version=2025-03-31.basil#charge_object-payment_method_details), [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-03-31.basil#confirmation_token_object-payment_method_preview), [ConfirmationTokenCreateParams.testHelpers.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-03-31.basil#test_create-payment_method_data), `CustomerPaymentMethod`, [PaymentIntentConfirmParams.payment_method_data](/api/payment_intents/confirm?api-version=2025-03-31.basil#confirm_payment_intent-payment_method_data), [PaymentIntentCreateParams.payment_method_data](/api/payment_intents/create?api-version=2025-03-31.basil#create_payment_intent-payment_method_data), [PaymentIntentUpdateParams.payment_method_data](/api/payment_intents/update?api-version=2025-03-31.basil#update_payment_intent-payment_method_data), [PaymentMethodConfigurationCreateParams](/api/payment_method_configurations/create?api-version=2025-03-31.basil), [PaymentMethodConfigurationUpdateParams](/api/payment_method_configurations/update?api-version=2025-03-31.basil), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-03-31.basil), [PaymentMethodCreateParams](/api/payment_methods/create?api-version=2025-03-31.basil), [PaymentMethod](/api/payment_methods/object?api-version=2025-03-31.basil), [SetupIntentConfirmParams.payment_method_data](/api/setup_intents/confirm?api-version=2025-03-31.basil#confirm_setup_intent-payment_method_data), [SetupIntentCreateParams.payment_method_data](/api/setup_intents/create?api-version=2025-03-31.basil#create_setup_intent-payment_method_data), [SetupIntentUpdateParams.payment_method_data](/api/setup_intents/update?api-version=2025-03-31.basil#update_setup_intent-payment_method_data) |

| Values | Change | Enums |
| --- | --- | --- |
| `billie` | Added | `Checkout.SessionCreateParams.payment_method_types` |
| `billie` | Added | [ConfirmationTokenCreateParams.testHelpers.payment_method_data.type](/api/confirmation_tokens/test_create?api-version=2025-03-31.basil#test_create-payment_method_data-type), [PaymentIntentConfirmParams.payment_method_data.type](/api/payment_intents/confirm?api-version=2025-03-31.basil#confirm_payment_intent-payment_method_data-type), [PaymentIntentCreateParams.payment_method_data.type](/api/payment_intents/create?api-version=2025-03-31.basil#create_payment_intent-payment_method_data-type), [PaymentIntentUpdateParams.payment_method_data.type](/api/payment_intents/update?api-version=2025-03-31.basil#update_payment_intent-payment_method_data-type), [SetupIntentConfirmParams.payment_method_data.type](/api/setup_intents/confirm?api-version=2025-03-31.basil#confirm_setup_intent-payment_method_data-type), [SetupIntentCreateParams.payment_method_data.type](/api/setup_intents/create?api-version=2025-03-31.basil#create_setup_intent-payment_method_data-type), [SetupIntentUpdateParams.payment_method_data.type](/api/setup_intents/update?api-version=2025-03-31.basil#update_setup_intent-payment_method_data-type) |
| `billie` | Added | [ConfirmationToken.payment_method_preview.type](/api/confirmation_tokens/object?api-version=2025-03-31.basil#confirmation_token_object-payment_method_preview-type), `CustomerPaymentMethod.type`, [PaymentMethod.type](/api/payment_methods/object?api-version=2025-03-31.basil#payment_method_object-type) |
| `billie` | Added | `CustomerPaymentMethodListParams.type`, [PaymentMethodCreateParams.type](/api/payment_methods/create?api-version=2025-03-31.basil#create_payment_method-type), [PaymentMethodListParams.type](/api/payment_methods/list?api-version=2025-03-31.basil#list_payment_methods-type) |
| `billie` | Added | `PaymentLink.payment_method_types`, `PaymentLinkCreateParams.payment_method_types`, `PaymentLinkUpdateParams.payment_method_types` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BilliePayments` | Added | [AccountCapabilitiesParams](/api/accounts/create?api-version=2025-03-31.basil#create_account-capabilities), [AccountCapabilities](/api/accounts/object?api-version=2025-03-31.basil#account_object-capabilities) |
| `Billie` | Added | [ChargePaymentMethodDetails](/api/charges/object?api-version=2025-03-31.basil#charge_object-payment_method_details), [ConfirmationTokenPaymentMethodDataParams](/api/confirmation_tokens/test_create?api-version=2025-03-31.basil#test_create-payment_method_data), [ConfirmationTokenPaymentMethodPreview](/api/confirmation_tokens/object?api-version=2025-03-31.basil#confirmation_token_object-payment_method_preview), [PaymentIntentConfirmPaymentMethodDataParams](/api/payment_intents/confirm?api-version=2025-03-31.basil#confirm_payment_intent-payment_method_data), [PaymentIntentPaymentMethodDataParams](/api/payment_intents/create?api-version=2025-03-31.basil#create_payment_intent-payment_method_data), [PaymentMethodConfigurationParams](/api/payment_method_configurations/create?api-version=2025-03-31.basil), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-03-31.basil), [PaymentMethodParams](/api/payment_methods/create?api-version=2025-03-31.basil), [PaymentMethod](/api/payment_methods/object?api-version=2025-03-31.basil), [SetupIntentConfirmPaymentMethodDataParams](/api/setup_intents/confirm?api-version=2025-03-31.basil#confirm_setup_intent-payment_method_data), [SetupIntentPaymentMethodDataParams](/api/setup_intents/create?api-version=2025-03-31.basil#create_setup_intent-payment_method_data) |

| Values | Change | Enums |
| --- | --- | --- |
| `billie` | Added | `ConfirmationTokenPaymentMethodPreview.Type`, `PaymentMethod.Type` |
| `billie` | Added | `PaymentLink.PaymentMethodTypes` |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BilliePayments` | Added | [AccountCapabilitiesOptions](/api/accounts/create?api-version=2025-03-31.basil#create_account-capabilities), [AccountCapabilities](/api/accounts/object?api-version=2025-03-31.basil#account_object-capabilities) |
| `Billie` | Added | [ChargePaymentMethodDetails](/api/charges/object?api-version=2025-03-31.basil#charge_object-payment_method_details), [ConfirmationTokenPaymentMethodDataOptions](/api/confirmation_tokens/test_create?api-version=2025-03-31.basil#test_create-payment_method_data), [ConfirmationTokenPaymentMethodPreview](/api/confirmation_tokens/object?api-version=2025-03-31.basil#confirmation_token_object-payment_method_preview), `CustomerPaymentMethod`, [PaymentIntentPaymentMethodDataOptions](/api/payment_intents/create?api-version=2025-03-31.basil#create_payment_intent-payment_method_data), [PaymentMethodConfigurationCreateOptions](/api/payment_method_configurations/create?api-version=2025-03-31.basil), [PaymentMethodConfigurationUpdateOptions](/api/payment_method_configurations/update?api-version=2025-03-31.basil), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-03-31.basil), [PaymentMethodCreateOptions](/api/payment_methods/create?api-version=2025-03-31.basil), [PaymentMethod](/api/payment_methods/object?api-version=2025-03-31.basil), [SetupIntentPaymentMethodDataOptions](/api/setup_intents/create?api-version=2025-03-31.basil#create_setup_intent-payment_method_data) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-03-31.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.0.0](https://github.com/stripe/stripe-python/releases/tag/v12.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.0.0](https://github.com/stripe/stripe-php/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.0.0](https://github.com/stripe/stripe-java/releases/tag/v29.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.0.0](https://github.com/stripe/stripe-node/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.0.0](https://github.com/stripe/stripe-go/releases/tag/v82.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Updates the Vault and Forward API to return a 402 status code for upstream request timeouts](https://docs.stripe.com/changelog/basil/2025-03-31/vault-forward-api-returns-402.md)
- [Removes manual capture method for Interac cards](https://docs.stripe.com/changelog/basil/2025-03-31/deprecate-interac-present-manual-capture-method.md)
- [Payment Methods won’t allow modifying fields for Naver Pay after the object is first created](https://docs.stripe.com/changelog/basil/2025-03-31/naver-pay-payment-method.md)
- [Partially capturing or cancelling payments no longer creates a Refund](https://docs.stripe.com/changelog/basil/2025-03-31/remove-refund-from-partial-capture-and-payment-cancellation-flow.md)
- [Adds support for Klarna in the hosted invoice page](https://docs.stripe.com/changelog/basil/2025-03-31/klarna-send-invoice.md)
- [Adds ability to configure saved payment methods for one-time payments on the hosted invoice page](https://docs.stripe.com/changelog/basil/2025-03-31/hosted-payment-method-save.md)
- [Adds support for saving and reusing Naver Pay payment methods](https://docs.stripe.com/changelog/basil/2025-03-31/naver-pay-recurring.md)
- [Adds support for the Satispay local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/satispay-lpm.md)
- [Makes the client parameter optional for WeChat Pay until confirmation](https://docs.stripe.com/changelog/basil/2025-03-31/lient-param-optional-wechatpay-before-confirmation.md)
- [Adds support for the New Zealand BECS Direct Debit local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/nz-bank-account.md)
