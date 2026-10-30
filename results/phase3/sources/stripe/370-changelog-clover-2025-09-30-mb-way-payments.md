# Adds support for the MB WAY payment method

## What’s new

You can now use [MB WAY](https://docs.stripe.com/payments/mb-way.md), the most popular digital wallet payment method in Portugal.

Learn more about [adding MB WAY as a payment method](https://docs.stripe.com/payments/mb-way.md#get-started).

## Impact

Customers pay with MB WAY using a phone number linked to their MB WAY app. After providing their phone number, customers receive a push notification in their MB WAY app, authorise the payment, then return to your website.

You can use MB WAY with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) or integrate it using the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md?api-version=2025-09-30.clover).

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `mb_way_payments` | Added | [Account#create.capabilities](/api/accounts/create?api-version=2025-09-30.clover#create_account-capabilities), [Account#update.capabilities](/api/accounts/update?api-version=2025-09-30.clover#update_account-capabilities), [Account.capabilities](/api/accounts/object?api-version=2025-09-30.clover#account_object-capabilities) |
| `mb_way` | Added | [Charge.payment_method_details](/api/charges/object?api-version=2025-09-30.clover#charge_object-payment_method_details), [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-payment_method_preview), [ConfirmationToken.testHelpers#create.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data), [PaymentIntent#confirm.payment_method_data](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_data), [PaymentIntent#confirm.payment_method_options](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_options), [PaymentIntent#create.payment_method_data](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_data), [PaymentIntent#create.payment_method_options](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_options), [PaymentIntent#update.payment_method_data](/api/payment_intents/update?api-version=2025-09-30.clover#update_payment_intent-payment_method_data), [PaymentIntent#update.payment_method_options](/api/payment_intents/update?api-version=2025-09-30.clover#update_payment_intent-payment_method_options), [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-payment_method_options), [PaymentMethod](/api/payment_methods/object?api-version=2025-09-30.clover), [PaymentMethod#create](/api/payment_methods/create?api-version=2025-09-30.clover), [SetupIntent#confirm.payment_method_data](/api/setup_intents/confirm?api-version=2025-09-30.clover#confirm_setup_intent-payment_method_data), [SetupIntent#create.payment_method_data](/api/setup_intents/create?api-version=2025-09-30.clover#create_setup_intent-payment_method_data), [SetupIntent#update.payment_method_data](/api/setup_intents/update?api-version=2025-09-30.clover#update_setup_intent-payment_method_data) |

| Values | Change | Enums |
| --- | --- | --- |
| `mb_way` | Added | [ConfirmationToken.testHelpers#create.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [PaymentIntent#create.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [PaymentIntent#update.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [PaymentIntent#confirm.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [SetupIntent#create.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [SetupIntent#update.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [SetupIntent#confirm.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type) |
| `mb_way` | Added | [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-payment_method_preview-type), [PaymentMethod](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-type) |
| `mb_way` | Added | [Customer#list_payment_methods](/api/payment_methods/customer_list?api-version=2025-09-30.clover#list_payment_methods-type), [PaymentMethod#list](/api/payment_methods/customer_list?api-version=2025-09-30.clover#list_payment_methods-type), [PaymentMethod#create](/api/payment_methods/customer_list?api-version=2025-09-30.clover#list_payment_methods-type) |
| `mb_way` | Added | [PaymentIntent#create](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excluded_payment_method_types), [PaymentIntent#update](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excluded_payment_method_types), [PaymentIntent#confirm](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excluded_payment_method_types), [PaymentIntent](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excluded_payment_method_types) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mb_way_payments` | Added | [Account::Capability](/api/accounts/object?api-version=2025-09-30.clover#account_object-capabilities), [Account::CreateParams::Capability](/api/accounts/create?api-version=2025-09-30.clover#create_account-capabilities), [Account::UpdateParams::Capability](/api/accounts/update?api-version=2025-09-30.clover#update_account-capabilities) |
| `mb_way` | Added | [Charge::PaymentMethodDetail](/api/charges/object?api-version=2025-09-30.clover#charge_object-payment_method_details), [ConfirmationToken::CreateParams::PaymentMethodDatum](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data), [ConfirmationToken::PaymentMethodPreview](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-payment_method_preview), [PaymentIntent::ConfirmParams::PaymentMethodDatum](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_data), [PaymentIntent::ConfirmParams::PaymentMethodOption](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_options), [PaymentIntent::CreateParams::PaymentMethodDatum](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_data), [PaymentIntent::CreateParams::PaymentMethodOption](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_options), [PaymentIntent::PaymentMethodOption](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-payment_method_options), [PaymentIntent::UpdateParams::PaymentMethodDatum](/api/payment_intents/update?api-version=2025-09-30.clover#update_payment_intent-payment_method_data), [PaymentIntent::UpdateParams::PaymentMethodOption](/api/payment_intents/update?api-version=2025-09-30.clover#update_payment_intent-payment_method_options), [PaymentMethod](/api/payment_methods/object?api-version=2025-09-30.clover), [PaymentMethod::CreateParams](/api/payment_methods/create?api-version=2025-09-30.clover), [SetupIntent::ConfirmParams::PaymentMethodDatum](/api/setup_intents/confirm?api-version=2025-09-30.clover#confirm_setup_intent-payment_method_data), [SetupIntent::CreateParams::PaymentMethodDatum](/api/setup_intents/create?api-version=2025-09-30.clover#create_setup_intent-payment_method_data), [SetupIntent::UpdateParams::PaymentMethodDatum](/api/setup_intents/update?api-version=2025-09-30.clover#update_setup_intent-payment_method_data) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mb_way_payments` | Added | [Account.Capability](/api/accounts/object?api-version=2025-09-30.clover#account_object-capabilities), [Account.CreateParamsCapability](/api/accounts/create?api-version=2025-09-30.clover#create_account-capabilities), [Account.ModifyParamsCapability](/api/accounts/update?api-version=2025-09-30.clover#update_account-capabilities) |
| `mb_way` | Added | [Charge.PaymentMethodDetail](/api/charges/object?api-version=2025-09-30.clover#charge_object-payment_method_details), [ConfirmationToken.CreateParamsPaymentMethodDatum](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data), [ConfirmationToken.PaymentMethodPreview](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-payment_method_preview), [PaymentIntent.ConfirmParamsPaymentMethodDatum](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_data), [PaymentIntent.ConfirmParamsPaymentMethodOption](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_options), [PaymentIntent.CreateParamsPaymentMethodDatum](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_data), [PaymentIntent.CreateParamsPaymentMethodOption](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_options), [PaymentIntent.ModifyParamsPaymentMethodDatum](/api/payment_intents/update?api-version=2025-09-30.clover#update_payment_intent-payment_method_data), [PaymentIntent.ModifyParamsPaymentMethodOption](/api/payment_intents/update?api-version=2025-09-30.clover#update_payment_intent-payment_method_options), [PaymentIntent.PaymentMethodOption](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-payment_method_options), [PaymentMethod](/api/payment_methods/object?api-version=2025-09-30.clover), [PaymentMethod.CreateParams](/api/payment_methods/create?api-version=2025-09-30.clover), [SetupIntent.ConfirmParamsPaymentMethodDatum](/api/setup_intents/confirm?api-version=2025-09-30.clover#confirm_setup_intent-payment_method_data), [SetupIntent.CreateParamsPaymentMethodDatum](/api/setup_intents/create?api-version=2025-09-30.clover#create_setup_intent-payment_method_data), [SetupIntent.ModifyParamsPaymentMethodDatum](/api/setup_intents/update?api-version=2025-09-30.clover#update_setup_intent-payment_method_data) |

| Values | Change | Enums |
| --- | --- | --- |
| `mb_way` | Added | [ConfirmationToken.CreateParamsPaymentMethodDatum](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [PaymentIntent.CreateParamsPaymentMethodDatum](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [PaymentIntent.ModifyParamsPaymentMethodDatum](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [PaymentIntent.ConfirmParamsPaymentMethodDatum](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [SetupIntent.CreateParamsPaymentMethodDatum](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [SetupIntent.ModifyParamsPaymentMethodDatum](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [SetupIntent.ConfirmParamsPaymentMethodDatum](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type) |
| `mb_way` | Added | [ConfirmationToken.PaymentMethodPreview](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-payment_method_preview-type), [PaymentMethod](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-type) |
| `mb_way` | Added | [Customer.ListPaymentMethodsParams](/api/payment_methods/customer_list?api-version=2025-09-30.clover#list_payment_methods-type), [PaymentMethod.ListParams](/api/payment_methods/customer_list?api-version=2025-09-30.clover#list_payment_methods-type), [PaymentMethod.CreateParams](/api/payment_methods/customer_list?api-version=2025-09-30.clover#list_payment_methods-type) |
| `mb_way` | Added | [PaymentIntent.CreateParams](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excluded_payment_method_types), [PaymentIntent.ModifyParams](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excluded_payment_method_types), [PaymentIntent.ConfirmParams](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excluded_payment_method_types), [PaymentIntent](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excluded_payment_method_types) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mb_way_payments` | Added | [Account.capabilities](/api/accounts/object?api-version=2025-09-30.clover#account_object-capabilities), [Account.create().$params.capability](/api/accounts/create?api-version=2025-09-30.clover#create_account-capabilities), [Account.update().$params.capability](/api/accounts/update?api-version=2025-09-30.clover#update_account-capabilities) |
| `mb_way` | Added | [Charge.payment_method_details](/api/charges/object?api-version=2025-09-30.clover#charge_object-payment_method_details), [ConfirmationToken.create().$params.payment_method_datum](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data), [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-payment_method_preview), [PaymentIntent.confirm().$params.payment_method_datum](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_data), [PaymentIntent.confirm().$params.payment_method_option](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_options), [PaymentIntent.create().$params.payment_method_datum](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_data), [PaymentIntent.create().$params.payment_method_option](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_options), [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-payment_method_options), [PaymentIntent.update().$params.payment_method_datum](/api/payment_intents/update?api-version=2025-09-30.clover#update_payment_intent-payment_method_data), [PaymentIntent.update().$params.payment_method_option](/api/payment_intents/update?api-version=2025-09-30.clover#update_payment_intent-payment_method_options), [PaymentMethod](/api/payment_methods/object?api-version=2025-09-30.clover), [PaymentMethod.create().$params](/api/payment_methods/create?api-version=2025-09-30.clover), [SetupIntent.confirm().$params.payment_method_datum](/api/setup_intents/confirm?api-version=2025-09-30.clover#confirm_setup_intent-payment_method_data), [SetupIntent.create().$params.payment_method_datum](/api/setup_intents/create?api-version=2025-09-30.clover#create_setup_intent-payment_method_data), [SetupIntent.update().$params.payment_method_datum](/api/setup_intents/update?api-version=2025-09-30.clover#update_setup_intent-payment_method_data) |

| Values | Change | Enums |
| --- | --- | --- |
| `mb_way` | Added | [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-payment_method_preview-type), [PaymentMethod](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-type) |
| `mb_way` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-excluded_payment_method_types) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mbWayPayments` | Added | [Account.capabilities](/api/accounts/object?api-version=2025-09-30.clover#account_object-capabilities), [AccountCreateParams.capabilities](/api/accounts/create?api-version=2025-09-30.clover#create_account-capabilities), [AccountUpdateParams.capabilities](/api/accounts/update?api-version=2025-09-30.clover#update_account-capabilities) |
| `mbWay` | Added | [Charge.payment_method_details](/api/charges/object?api-version=2025-09-30.clover#charge_object-payment_method_details), [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-payment_method_preview), [ConfirmationTokenCreateParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data), [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-payment_method_options), [PaymentIntentConfirmParams.payment_method_data](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_data), [PaymentIntentConfirmParams.payment_method_options](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_options), [PaymentIntentCreateParams.payment_method_data](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_data), [PaymentIntentCreateParams.payment_method_options](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_options), [PaymentIntentUpdateParams.payment_method_data](/api/payment_intents/update?api-version=2025-09-30.clover#update_payment_intent-payment_method_data), [PaymentIntentUpdateParams.payment_method_options](/api/payment_intents/update?api-version=2025-09-30.clover#update_payment_intent-payment_method_options), [PaymentMethod](/api/payment_methods/object?api-version=2025-09-30.clover), [PaymentMethodCreateParams](/api/payment_methods/create?api-version=2025-09-30.clover), [SetupIntentConfirmParams.payment_method_data](/api/setup_intents/confirm?api-version=2025-09-30.clover#confirm_setup_intent-payment_method_data), [SetupIntentCreateParams.payment_method_data](/api/setup_intents/create?api-version=2025-09-30.clover#create_setup_intent-payment_method_data), [SetupIntentUpdateParams.payment_method_data](/api/setup_intents/update?api-version=2025-09-30.clover#update_setup_intent-payment_method_data) |

| Values | Change | Enums |
| --- | --- | --- |
| `mb_way` | Added | [ConfirmationTokenCreateParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [PaymentIntentCreateParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [PaymentIntentUpdateParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [PaymentIntentConfirmParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [SetupIntentCreateParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [SetupIntentUpdateParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [SetupIntentConfirmParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type) |
| `mb_way` | Added | [CustomerListPaymentMethodsParams](/api/payment_methods/customer_list?api-version=2025-09-30.clover#list_payment_methods-type), [PaymentMethodListParams](/api/payment_methods/customer_list?api-version=2025-09-30.clover#list_payment_methods-type), [PaymentMethodCreateParams](/api/payment_methods/customer_list?api-version=2025-09-30.clover#list_payment_methods-type) |
| `mb_way` | Added | [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excludedPaymentMethodTypes), [PaymentIntentUpdateParams](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excludedPaymentMethodTypes), [PaymentIntentConfirmParams](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excludedPaymentMethodTypes) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mb_way_payments` | Added | [Account.capabilities](/api/accounts/object?api-version=2025-09-30.clover#account_object-capabilities), [AccountCreateParams.capabilities](/api/accounts/create?api-version=2025-09-30.clover#create_account-capabilities), [AccountUpdateParams.capabilities](/api/accounts/update?api-version=2025-09-30.clover#update_account-capabilities) |
| `mb_way` | Added | [Charge.payment_method_details](/api/charges/object?api-version=2025-09-30.clover#charge_object-payment_method_details), [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-payment_method_preview), [ConfirmationTokenCreateParams.testHelpers.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data), [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-payment_method_options), [PaymentIntentConfirmParams.payment_method_data](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_data), [PaymentIntentConfirmParams.payment_method_options](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_options), [PaymentIntentCreateParams.payment_method_data](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_data), [PaymentIntentCreateParams.payment_method_options](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_options), [PaymentIntentUpdateParams.payment_method_data](/api/payment_intents/update?api-version=2025-09-30.clover#update_payment_intent-payment_method_data), [PaymentIntentUpdateParams.payment_method_options](/api/payment_intents/update?api-version=2025-09-30.clover#update_payment_intent-payment_method_options), [PaymentMethod](/api/payment_methods/object?api-version=2025-09-30.clover), [PaymentMethodCreateParams](/api/payment_methods/create?api-version=2025-09-30.clover), [SetupIntentConfirmParams.payment_method_data](/api/setup_intents/confirm?api-version=2025-09-30.clover#confirm_setup_intent-payment_method_data), [SetupIntentCreateParams.payment_method_data](/api/setup_intents/create?api-version=2025-09-30.clover#create_setup_intent-payment_method_data), [SetupIntentUpdateParams.payment_method_data](/api/setup_intents/update?api-version=2025-09-30.clover#update_setup_intent-payment_method_data) |

| Values | Change | Enums |
| --- | --- | --- |
| `mb_way` | Added | [ConfirmationTokenCreateParams.testHelpers.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [PaymentIntentCreateParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [PaymentIntentUpdateParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [PaymentIntentConfirmParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [SetupIntentCreateParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [SetupIntentUpdateParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type), [SetupIntentConfirmParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data-type) |
| `mb_way` | Added | [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-payment_method_preview-type), [PaymentMethod](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-type) |
| `mb_way` | Added | [CustomerListPaymentMethodsParams](/api/payment_methods/customer_list?api-version=2025-09-30.clover#list_payment_methods-type), [PaymentMethodListParams](/api/payment_methods/customer_list?api-version=2025-09-30.clover#list_payment_methods-type), [PaymentMethodCreateParams](/api/payment_methods/customer_list?api-version=2025-09-30.clover#list_payment_methods-type) |
| `mb_way` | Added | [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excluded_payment_method_types), [PaymentIntentUpdateParams](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excluded_payment_method_types), [PaymentIntentConfirmParams](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excluded_payment_method_types), [PaymentIntent](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-excluded_payment_method_types) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `MbWayPayments` | Added | [AccountCapabilities](/api/accounts/object?api-version=2025-09-30.clover#account_object-capabilities), [AccountCapabilitiesParams](/api/accounts/update?api-version=2025-09-30.clover#update_account-capabilities) |
| `MbWay` | Added | [ChargePaymentMethodDetails](/api/charges/object?api-version=2025-09-30.clover#charge_object-payment_method_details), [ConfirmationTokenPaymentMethodDataParams](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data), [ConfirmationTokenPaymentMethodPreview](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-payment_method_preview), [PaymentIntentConfirmPaymentMethodDataParams](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_data), [PaymentIntentConfirmPaymentMethodOptionsParams](/api/payment_intents/confirm?api-version=2025-09-30.clover#confirm_payment_intent-payment_method_options), [PaymentIntentPaymentMethodDataParams](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_data), [PaymentIntentPaymentMethodOptions](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-payment_method_options), [PaymentIntentPaymentMethodOptionsParams](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_options), [PaymentMethod](/api/payment_methods/object?api-version=2025-09-30.clover), [PaymentMethodParams](/api/payment_methods/create?api-version=2025-09-30.clover), [SetupIntentConfirmPaymentMethodDataParams](/api/setup_intents/confirm?api-version=2025-09-30.clover#confirm_setup_intent-payment_method_data), [SetupIntentPaymentMethodDataParams](/api/setup_intents/create?api-version=2025-09-30.clover#create_setup_intent-payment_method_data) |

| Values | Change | Enums |
| --- | --- | --- |
| `mb_way` | Added | [ConfirmationTokenPaymentMethodPreview](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-payment_method_preview-Type), [PaymentMethod](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-Type) |
| `mb_way` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-ExcludedPaymentMethodTypes) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `MbWayPayments` | Added | [Account.Capabilities](/api/accounts/object?api-version=2025-09-30.clover#account_object-capabilities), [AccountCapabilitiesOptions](/api/accounts/update?api-version=2025-09-30.clover#update_account-capabilities) |
| `MbWay` | Added | [Charge.PaymentMethodDetails](/api/charges/object?api-version=2025-09-30.clover#charge_object-payment_method_details), [ConfirmationToken.PaymentMethodPreview](/api/confirmation_tokens/object?api-version=2025-09-30.clover#confirmation_token_object-payment_method_preview), [ConfirmationTokenPaymentMethodDataOptions](/api/confirmation_tokens/test_create?api-version=2025-09-30.clover#create_confirmation_token-payment_method_data), [PaymentIntent.PaymentMethodOptions](/api/payment_intents/object?api-version=2025-09-30.clover#payment_intent_object-payment_method_options), [PaymentIntentPaymentMethodDataOptions](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_data), [PaymentIntentPaymentMethodOptionsOptions](/api/payment_intents/create?api-version=2025-09-30.clover#create_payment_intent-payment_method_options), [PaymentMethod](/api/payment_methods/object?api-version=2025-09-30.clover), [PaymentMethodCreateOptions](/api/payment_methods/create?api-version=2025-09-30.clover), [SetupIntentPaymentMethodDataOptions](/api/setup_intents/create?api-version=2025-09-30.clover#create_setup_intent-payment_method_data) |

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

## Related changes

- [Changes the set of decline codes used for Alma, Amazon Pay, Billie, Satispay and South Korean payment methods](https://docs.stripe.com/changelog/clover/2025-09-30/lpm-descriptive-decline-codes.md)
- [Adds a processing status to submitted stablecoin payments](https://docs.stripe.com/changelog/clover/2025-09-30/stablecoin-payments-processing-status.md)
- [Adds a documented reason for Klarna chargeback losses to Disputes API](https://docs.stripe.com/changelog/clover/2025-09-30/chargeback-loss-reason.md)
