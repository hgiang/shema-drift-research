# Adds support for the Pay by Bank local payment method

## What’s new

Adds support for the [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank.md) local payment method (LPM) – a single-use payment method that lets customers pay directly from their bank account.

## Impact

Pay by Bank is a single-use payment method that lets customers pay directly from their bank account instead of using a card. It runs on banking infrastructure and open banking APIs. When a customer chooses Pay by Bank, they select their bank and approve the payment on their bank’s mobile app or web portal.

You can use Pay by Bank with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) or integrate it using [Payment Intents](https://docs.stripe.com/api/payment_intents.md?api-version=2025-01-27.acacia).

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `pay_by_bank` | Added | [Charge.payment_method_details](/api/charges/object?api-version=2025-01-27.acacia#charge_object-payment_method_details), [Checkout.Session#create.payment_method_options](/api/checkout/sessions/create?api-version=2025-01-27.acacia#create_checkout_session-payment_method_options), [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-01-27.acacia#confirmation_token_object-payment_method_preview), [ConfirmationToken.testHelpers#create.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-01-27.acacia#test_create-payment_method_data), [PaymentIntent#confirm.payment_method_data](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_data), [PaymentIntent#confirm.payment_method_options](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_options), [PaymentIntent#create.payment_method_data](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_data), [PaymentIntent#create.payment_method_options](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_options), [PaymentIntent#update.payment_method_data](/api/payment_intents/update?api-version=2025-01-27.acacia#update_payment_intent-payment_method_data), [PaymentIntent#update.payment_method_options](/api/payment_intents/update?api-version=2025-01-27.acacia#update_payment_intent-payment_method_options), [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2025-01-27.acacia#payment_intent_object-payment_method_options), [PaymentMethod#create](/api/payment_methods/create?api-version=2025-01-27.acacia), [PaymentMethod#update](/api/payment_methods/update?api-version=2025-01-27.acacia), [PaymentMethodConfiguration#create](/api/payment_method_configurations/create?api-version=2025-01-27.acacia), [PaymentMethodConfiguration#update](/api/payment_method_configurations/update?api-version=2025-01-27.acacia), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-01-27.acacia), [PaymentMethod](/api/payment_methods/object?api-version=2025-01-27.acacia), [SetupIntent#confirm.payment_method_data](/api/setup_intents/confirm?api-version=2025-01-27.acacia#confirm_setup_intent-payment_method_data), [SetupIntent#create.payment_method_data](/api/setup_intents/create?api-version=2025-01-27.acacia#create_setup_intent-payment_method_data), [SetupIntent#update.payment_method_data](/api/setup_intents/update?api-version=2025-01-27.acacia#update_setup_intent-payment_method_data) |
| `pay_by_bank_payments` | Added | [Account#create.capabilities](/api/accounts/create?api-version=2025-01-27.acacia#create_account-capabilities), [Account#update.capabilities](/api/accounts/update?api-version=2025-01-27.acacia#update_account-capabilities), [Account.capabilities](/api/accounts/object?api-version=2025-01-27.acacia#account_object-capabilities) |

| Values | Change | Enums |
| --- | --- | --- |
| `pay_by_bank` | Added | [Checkout.Session#create.payment_method_types[]](/api/checkout/sessions/create?api-version=2025-01-27.acacia#create_checkout_session-payment_method_types) |
| `pay_by_bank` | Added | [ConfirmationToken.testHelpers#create.payment_method_data.type](/api/confirmation_tokens/test_create?api-version=2025-01-27.acacia#test_create-payment_method_data-type), [PaymentIntent#confirm.payment_method_data.type](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_data-type), [PaymentIntent#create.payment_method_data.type](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_data-type), [PaymentIntent#update.payment_method_data.type](/api/payment_intents/update?api-version=2025-01-27.acacia#update_payment_intent-payment_method_data-type), [SetupIntent#confirm.payment_method_data.type](/api/setup_intents/confirm?api-version=2025-01-27.acacia#confirm_setup_intent-payment_method_data-type), [SetupIntent#create.payment_method_data.type](/api/setup_intents/create?api-version=2025-01-27.acacia#create_setup_intent-payment_method_data-type), [SetupIntent#update.payment_method_data.type](/api/setup_intents/update?api-version=2025-01-27.acacia#update_setup_intent-payment_method_data-type) |
| `pay_by_bank` | Added | [ConfirmationToken.payment_method_preview.type](/api/confirmation_tokens/object?api-version=2025-01-27.acacia#confirmation_token_object-payment_method_preview-type), [PaymentMethod.type](/api/payment_methods/object?api-version=2025-01-27.acacia#payment_method_object-type) |
| `pay_by_bank` | Added | [PaymentLink#create.payment_method_types[]](/api/payment-link/create?api-version=2025-01-27.acacia#create_payment_link-payment_method_types), [PaymentLink#update.payment_method_types[]](/api/payment-link/update?api-version=2025-01-27.acacia#update_payment_link-payment_method_types), [PaymentLink.payment_method_types[]](/api/payment-link/object?api-version=2025-01-27.acacia#payment_link_object-payment_method_types), [Customer#list_payment_methods.type](/api/payment_methods/customer_list?api-version=2025-01-27.acacia#list_customer_payment_methods-type), [PaymentMethod#create.type](/api/payment_methods/create?api-version=2025-01-27.acacia#create_payment_method-type), [PaymentMethod#list.type](/api/payment_methods/list?api-version=2025-01-27.acacia#list_payment_methods-type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `pay_by_bank` | Added | [stripe.Charge.PaymentMethodDetails](/api/charges/object?api-version=2025-01-27.acacia#charge_object-payment_method_details), [stripe.ConfirmationToken.PaymentMethodPreview](/api/confirmation_tokens/object?api-version=2025-01-27.acacia#confirmation_token_object-payment_method_preview), [stripe.PaymentIntent.PaymentMethodOptions](/api/payment_intents/object?api-version=2025-01-27.acacia#payment_intent_object-payment_method_options), [stripe.ConfirmationToken.CreateParamsPaymentMethodData](/api/confirmation_tokens/object?api-version=2025-01-27.acacia#confirmation_token_object-payment_method_preview), [stripe.PaymentIntent.ConfirmParamsPaymentMethodData](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_data), [stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_options), [stripe.PaymentIntent.CreateParamsPaymentMethodData](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_data), [stripe.PaymentIntent.CreateParamsPaymentMethodOptions](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_options), [stripe.PaymentIntent.ModifyParamsPaymentMethodData](/api/payment_intents/update?api-version=2025-01-27.acacia#update_payment_intent-payment_method_data), [stripe.PaymentIntent.ModifyParamsPaymentMethodOptions](/api/payment_intents/update?api-version=2025-01-27.acacia#update_payment_intent-payment_method_options), [stripe.PaymentMethod.CreateParams](/api/payment_methods/create?api-version=2025-01-27.acacia), [stripe.PaymentMethod.ModifyParams](/api/payment_methods/update?api-version=2025-01-27.acacia), [stripe.PaymentMethodConfiguration.CreateParams](/api/payment_method_configurations/create?api-version=2025-01-27.acacia), [stripe.PaymentMethodConfiguration.ModifyParams](/api/payment_method_configurations/update?api-version=2025-01-27.acacia), [stripe.SetupIntent.ConfirmParamsPaymentMethodData](/api/setup_intents/confirm?api-version=2025-01-27.acacia#confirm_setup_intent-payment_method_data), [stripe.SetupIntent.CreateParamsPaymentMethodData](/api/setup_intents/create?api-version=2025-01-27.acacia#create_setup_intent-payment_method_data), [stripe.SetupIntent.ModifyParamsPaymentMethodData](/api/setup_intents/update?api-version=2025-01-27.acacia#update_setup_intent-payment_method_data), [stripe.checkout.Session.CreateParamsPaymentMethodOptions](/api/checkout/sessions/create?api-version=2025-01-27.acacia#create_checkout_session-payment_method_options), [stripe.PaymentMethod](/api/payment_methods/object?api-version=2025-01-27.acacia), [stripe.PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-01-27.acacia) |
| `pay_by_bank_payments` | Added | [stripe.Account.Capabilities](/api/accounts/object?api-version=2025-01-27.acacia#account_object-capabilities), [stripe.Account.CreateParamsCapabilities](/api/accounts/create?api-version=2025-01-27.acacia#create_account-capabilities) |

| Value | Change | Enums |
| --- | --- | --- |
| `pay_by_bank` | Added | [stripe.checkout.Session.CreateParams.payment_method_types](/api/checkout/sessions/create?api-version=2025-01-27.acacia#create_checkout_session-payment_method_types), [stripe.ConfirmationToken.PaymentMethodPreview.type](/api/confirmation_tokens/object?api-version=2025-01-27.acacia#confirmation_token_object-payment_method_preview-type), [stripe.ConfirmationToken.CreateParamsPaymentMethodData.type](/api/confirmation_tokens/object?api-version=2025-01-27.acacia#confirmation_token_object-payment_method_preview-type), [stripe.Customer.ListPaymentMethodsParams.type](/api/payment_methods/customer_list?api-version=2025-01-27.acacia#list_customer_payment_methods-type), [stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_data-type), [stripe.PaymentIntent.CreateParamsPaymentMethodData.type](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_data-type), [stripe.PaymentIntent.ModifyParamsPaymentMethodData.type](/api/payment_intents/update?api-version=2025-01-27.acacia#update_payment_intent-payment_method_data-type), [stripe.PaymentLink.payment_method_types](/api/payment-link/object?api-version=2025-01-27.acacia#payment_link_object-payment_method_types), [stripe.PaymentLink.CreateParams.payment_method_types](/api/payment-link/create?api-version=2025-01-27.acacia#create_payment_link-payment_method_types), [stripe.PaymentLink.ModifyParams.payment_method_types](/api/payment-link/update?api-version=2025-01-27.acacia#update_payment_link-payment_method_types), [stripe.PaymentMethod.type](/api/payment_methods/object?api-version=2025-01-27.acacia#payment_method_object-type), [stripe.PaymentMethod.CreateParams.type](/api/payment_methods/create?api-version=2025-01-27.acacia#create_payment_method-type), [stripe.PaymentMethod.ListParams.type](/api/payment_methods/list?api-version=2025-01-27.acacia#list_payment_methods-type), [stripe.SetupIntent.ConfirmParamsPaymentMethodData.type](/api/setup_intents/confirm?api-version=2025-01-27.acacia#confirm_setup_intent-payment_method_data-type), [stripe.SetupIntent.CreateParamsPaymentMethodData.type](/api/setup_intents/create?api-version=2025-01-27.acacia#create_setup_intent-payment_method_data-type), [stripe.SetupIntent.ModifyParamsPaymentMethodData.type](/api/setup_intents/update?api-version=2025-01-27.acacia#update_setup_intent-payment_method_data-type) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pay_by_bank` | Added | [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-01-27.acacia), [PaymentMethod](/api/payment_methods/object?api-version=2025-01-27.acacia) |

| Values | Change | Enums |
| --- | --- | --- |
| `pay_by_bank` | Added | [PaymentLink.payment_method_types[]](/api/payment-link/object?api-version=2025-01-27.acacia#payment_link_object-payment_method_types) |
| `pay_by_bank` | Added | [PaymentMethod.type](/api/payment_methods/object?api-version=2025-01-27.acacia#payment_method_object-type) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `pay_by_bank` | Added | [Charge.payment_method_details](/api/charges/object?api-version=2025-01-27.acacia#charge_object-payment_method_details), [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-01-27.acacia#confirmation_token_object-payment_method_preview), [ConfirmationTokenCreateParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-01-27.acacia#test_create-payment_method_data), [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2025-01-27.acacia#payment_intent_object-payment_method_options), [PaymentIntentConfirmParams.payment_method_data](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_data), [PaymentIntentConfirmParams.payment_method_options](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_options), [PaymentIntentCreateParams.payment_method_data](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_data), [PaymentIntentCreateParams.payment_method_options](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_options), [PaymentIntentUpdateParams.payment_method_data](/api/payment_intents/update?api-version=2025-01-27.acacia#update_payment_intent-payment_method_data), [PaymentIntentUpdateParams.payment_method_options](/api/payment_intents/update?api-version=2025-01-27.acacia#update_payment_intent-payment_method_options), [PaymentMethodConfigurationCreateParams](/api/payment_method_configurations/create?api-version=2025-01-27.acacia), [PaymentMethodConfigurationUpdateParams](/api/payment_method_configurations/update?api-version=2025-01-27.acacia), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-01-27.acacia), [PaymentMethodCreateParams](/api/payment_methods/create?api-version=2025-01-27.acacia), [PaymentMethodUpdateParams](/api/payment_methods/update?api-version=2025-01-27.acacia), [PaymentMethod](/api/payment_methods/object?api-version=2025-01-27.acacia), [SetupIntentConfirmParams.payment_method_data](/api/setup_intents/confirm?api-version=2025-01-27.acacia#confirm_setup_intent-payment_method_data), [SetupIntentCreateParams.payment_method_data](/api/setup_intents/create?api-version=2025-01-27.acacia#create_setup_intent-payment_method_data), [SetupIntentUpdateParams.payment_method_data](/api/setup_intents/update?api-version=2025-01-27.acacia#update_setup_intent-payment_method_data), [checkout.SessionCreateParams.payment_method_options](/api/checkout/sessions/create?api-version=2025-01-27.acacia#create_checkout_session-payment_method_options) |
| `pay_by_bank_payments` | Added | [Account.capabilities](/api/accounts/object?api-version=2025-01-27.acacia#account_object-capabilities), [AccountCreateParams.capabilities](/api/accounts/create?api-version=2025-01-27.acacia#create_account-capabilities), [AccountUpdateParams.capabilities](/api/accounts/update?api-version=2025-01-27.acacia#update_account-capabilities) |

| Values | Change | Enums |
| --- | --- | --- |
| `pay_by_bank` | Added | [CustomerListPaymentMethodsParams.type](/api/payment_methods/customer_list?api-version=2025-01-27.acacia#list_customer_payment_methods-type), [PaymentMethodCreateParams.type](/api/payment_methods/create?api-version=2025-01-27.acacia#create_payment_method-type), [PaymentMethodListParams.type](/api/payment_methods/list?api-version=2025-01-27.acacia#list_payment_methods-type), [checkout.SessionCreateParams.payment_method_types[]](/api/checkout/sessions/create?api-version=2025-01-27.acacia#create_checkout_session-payment_method_types) |
| `pay_by_bank` | Added | [ConfirmationTokenCreateParams.payment_method_data.type](/api/confirmation_tokens/test_create?api-version=2025-01-27.acacia#test_create-payment_method_data-type), [PaymentIntentConfirmParams.payment_method_data.type](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_data-type), [PaymentIntentCreateParams.payment_method_data.type](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_data-type), [PaymentIntentUpdateParams.payment_method_data.type](/api/payment_intents/update?api-version=2025-01-27.acacia#update_payment_intent-payment_method_data-type), [SetupIntentConfirmParams.payment_method_data.type](/api/setup_intents/confirm?api-version=2025-01-27.acacia#confirm_setup_intent-payment_method_data-type), [SetupIntentCreateParams.payment_method_data.type](/api/setup_intents/create?api-version=2025-01-27.acacia#create_setup_intent-payment_method_data-type), [SetupIntentUpdateParams.payment_method_data.type](/api/setup_intents/update?api-version=2025-01-27.acacia#update_setup_intent-payment_method_data-type) |
| `pay_by_bank` | Added | [PaymentLinkCreateParams.payment_method_types[]](/api/payment-link/create?api-version=2025-01-27.acacia#create_payment_link-payment_method_types), [PaymentLinkUpdateParams.payment_method_types[]](/api/payment-link/update?api-version=2025-01-27.acacia#update_payment_link-payment_method_types) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `pay_by_bank` | Added | [Charge.payment_method_details](/api/charges/object?api-version=2025-01-27.acacia#charge_object-payment_method_details), `Checkout.SessionCreateParams.payment_method_options`, [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-01-27.acacia#confirmation_token_object-payment_method_preview), [ConfirmationTokenCreateParams.testHelpers.payment_method_data](/api/confirmation_tokens/test_create?api-version=2025-01-27.acacia#test_create-payment_method_data), [PaymentIntent.payment_method_options](/api/payment_intents/object?api-version=2025-01-27.acacia#payment_intent_object-payment_method_options), [PaymentIntentConfirmParams.payment_method_data](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_data), [PaymentIntentConfirmParams.payment_method_options](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_options), [PaymentIntentCreateParams.payment_method_data](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_data), [PaymentIntentCreateParams.payment_method_options](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_options), [PaymentIntentUpdateParams.payment_method_data](/api/payment_intents/update?api-version=2025-01-27.acacia#update_payment_intent-payment_method_data), [PaymentIntentUpdateParams.payment_method_options](/api/payment_intents/update?api-version=2025-01-27.acacia#update_payment_intent-payment_method_options), [PaymentMethodConfigurationCreateParams](/api/payment_method_configurations/create?api-version=2025-01-27.acacia), [PaymentMethodConfigurationUpdateParams](/api/payment_method_configurations/update?api-version=2025-01-27.acacia), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-01-27.acacia), [PaymentMethodCreateParams](/api/payment_methods/create?api-version=2025-01-27.acacia), [PaymentMethodUpdateParams](/api/payment_methods/update?api-version=2025-01-27.acacia), [PaymentMethod](/api/payment_methods/object?api-version=2025-01-27.acacia), [SetupIntentConfirmParams.payment_method_data](/api/setup_intents/confirm?api-version=2025-01-27.acacia#confirm_setup_intent-payment_method_data), [SetupIntentCreateParams.payment_method_data](/api/setup_intents/create?api-version=2025-01-27.acacia#create_setup_intent-payment_method_data), [SetupIntentUpdateParams.payment_method_data](/api/setup_intents/update?api-version=2025-01-27.acacia#update_setup_intent-payment_method_data) |
| `pay_by_bank_payments` | Added | [Account.capabilities](/api/accounts/object?api-version=2025-01-27.acacia#account_object-capabilities), [AccountCreateParams.capabilities](/api/accounts/create?api-version=2025-01-27.acacia#create_account-capabilities), [AccountUpdateParams.capabilities](/api/accounts/update?api-version=2025-01-27.acacia#update_account-capabilities) |

| Values | Change | Enums |
| --- | --- | --- |
| `pay_by_bank` | Added | [Checkout.SessionCreateParams.payment_method_types[]](/api/checkout/sessions/create?api-version=2025-01-27.acacia#create_checkout_session-payment_method_types), [CustomerListPaymentMethodsParams.type](/api/payment_methods/customer_list?api-version=2025-01-27.acacia#list_customer_payment_methods-type), [PaymentMethodCreateParams.type](/api/payment_methods/create?api-version=2025-01-27.acacia#create_payment_method-type), [PaymentMethodListParams.type](/api/payment_methods/list?api-version=2025-01-27.acacia#list_payment_methods-type) |
| `pay_by_bank` | Added | [ConfirmationTokenCreateParams.testHelpers.payment_method_data.type](/api/confirmation_tokens/test_create?api-version=2025-01-27.acacia#test_create-payment_method_data-type), [PaymentIntentConfirmParams.payment_method_data.type](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_data-type), [PaymentIntentCreateParams.payment_method_data.type](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_data-type), [PaymentIntentUpdateParams.payment_method_data.type](/api/payment_intents/update?api-version=2025-01-27.acacia#update_payment_intent-payment_method_data-type), [SetupIntentConfirmParams.payment_method_data.type](/api/setup_intents/confirm?api-version=2025-01-27.acacia#confirm_setup_intent-payment_method_data-type), [SetupIntentCreateParams.payment_method_data.type](/api/setup_intents/create?api-version=2025-01-27.acacia#create_setup_intent-payment_method_data-type), [SetupIntentUpdateParams.payment_method_data.type](/api/setup_intents/update?api-version=2025-01-27.acacia#update_setup_intent-payment_method_data-type) |
| `pay_by_bank` | Added | [ConfirmationToken.payment_method_preview.type](/api/confirmation_tokens/object?api-version=2025-01-27.acacia#confirmation_token_object-payment_method_preview-type), [PaymentMethod.type](/api/payment_methods/object?api-version=2025-01-27.acacia#payment_method_object-type) |
| `pay_by_bank` | Added | [PaymentLink.payment_method_types[]](/api/payment-link/object?api-version=2025-01-27.acacia#payment_link_object-payment_method_types), [PaymentLinkCreateParams.payment_method_types[]](/api/payment-link/create?api-version=2025-01-27.acacia#create_payment_link-payment_method_types), [PaymentLinkUpdateParams.payment_method_types[]](/api/payment-link/update?api-version=2025-01-27.acacia#update_payment_link-payment_method_types) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PayByBank` | Added | [ChargePaymentMethodDetails](/api/charges/object?api-version=2025-01-27.acacia#charge_object-payment_method_details), [CheckoutSessionPaymentMethodOptionsParams](/api/checkout/sessions/create?api-version=2025-01-27.acacia#create_checkout_session-payment_method_options), [ConfirmationTokenPaymentMethodDataParams](/api/confirmation_tokens/test_create?api-version=2025-01-27.acacia#test_create-payment_method_data), [ConfirmationTokenPaymentMethodPreview](/api/confirmation_tokens/object?api-version=2025-01-27.acacia#confirmation_token_object-payment_method_preview), [PaymentIntentConfirmPaymentMethodDataParams](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_data), [PaymentIntentConfirmPaymentMethodOptionsParams](/api/payment_intents/confirm?api-version=2025-01-27.acacia#confirm_payment_intent-payment_method_options), [PaymentIntentPaymentMethodDataParams](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_data), [PaymentIntentPaymentMethodOptionsParams](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_options), [PaymentIntentPaymentMethodOptions](/api/payment_intents/object?api-version=2025-01-27.acacia#payment_intent_object-payment_method_options), [PaymentMethodConfigurationParams](/api/payment_method_configurations/create?api-version=2025-01-27.acacia), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-01-27.acacia), [PaymentMethodParams](/api/payment_methods/create?api-version=2025-01-27.acacia), [PaymentMethod](/api/payment_methods/object?api-version=2025-01-27.acacia), [SetupIntentConfirmPaymentMethodDataParams](/api/setup_intents/confirm?api-version=2025-01-27.acacia#confirm_setup_intent-payment_method_data), [SetupIntentPaymentMethodDataParams](/api/setup_intents/create?api-version=2025-01-27.acacia#create_setup_intent-payment_method_data) |
| `PayByBankPayments` | Added | [AccountCapabilitiesParams](/api/accounts/create?api-version=2025-01-27.acacia#create_account-capabilities), [AccountCapabilities](/api/accounts/object?api-version=2025-01-27.acacia#account_object-capabilities) |

| Values | Change | Enums |
| --- | --- | --- |
| `pay_by_bank` | Added | [ConfirmationTokenPaymentMethodPreviewType](/api/confirmation_tokens/object?api-version=2025-01-27.acacia#confirmation_token_object-payment_method_preview-type), [PaymentMethodType](/api/payment_methods/object?api-version=2025-01-27.acacia#payment_method_object-type) |
| `pay_by_bank` | Added | [PaymentLinkPaymentMethodTypes](/api/payment-link/object?api-version=2025-01-27.acacia#payment_link_object-payment_method_types) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PayByBank` | Added | [ChargePaymentMethodDetails](/api/charges/object?api-version=2025-01-27.acacia#charge_object-payment_method_details), [CheckoutSessionPaymentMethodOptionsOptions](/api/checkout/sessions/create?api-version=2025-01-27.acacia#create_checkout_session-payment_method_options), [ConfirmationTokenPaymentMethodDataOptions](/api/confirmation_tokens/test_create?api-version=2025-01-27.acacia#test_create-payment_method_data), [ConfirmationTokenPaymentMethodPreview](/api/confirmation_tokens/object?api-version=2025-01-27.acacia#confirmation_token_object-payment_method_preview), [PaymentIntentPaymentMethodDataOptions](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_data), [PaymentIntentPaymentMethodOptionsOptions](/api/payment_intents/create?api-version=2025-01-27.acacia#create_payment_intent-payment_method_options), [PaymentIntentPaymentMethodOptions](/api/payment_intents/object?api-version=2025-01-27.acacia#payment_intent_object-payment_method_options), [PaymentMethodConfigurationCreateOptions](/api/payment_method_configurations/create?api-version=2025-01-27.acacia), [PaymentMethodConfigurationUpdateOptions](/api/payment_method_configurations/update?api-version=2025-01-27.acacia), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-01-27.acacia), [PaymentMethodCreateOptions](/api/payment_methods/create?api-version=2025-01-27.acacia), [PaymentMethodUpdateOptions](/api/payment_methods/update?api-version=2025-01-27.acacia), [PaymentMethod](/api/payment_methods/object?api-version=2025-01-27.acacia), [SetupIntentPaymentMethodDataOptions](/api/setup_intents/create?api-version=2025-01-27.acacia#create_setup_intent-payment_method_data) |
| `PayByBankPayments` | Added | [AccountCapabilitiesOptions](/api/accounts/create?api-version=2025-01-27.acacia#create_account-capabilities), [AccountCapabilities](/api/accounts/object?api-version=2025-01-27.acacia#account_object-capabilities) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-01-27.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.4.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.5.0](https://github.com/stripe/stripe-python/releases/tag/v11.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.5.0](https://github.com/stripe/stripe-php/releases/tag/v16.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.3.0](https://github.com/stripe/stripe-java/releases/tag/v28.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.6.0](https://github.com/stripe/stripe-node/releases/tag/v17.6.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.3.0](https://github.com/stripe/stripe-go/releases/tag/v81.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.3.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds PayPal country property to the PaymentMethods and Charge objects](https://docs.stripe.com/changelog/acacia/2025-01-27/paypal-country.md)
