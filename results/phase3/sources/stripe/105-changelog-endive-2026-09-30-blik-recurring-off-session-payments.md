# Adds support for BLIK recurring off-session payments

## What’s new

Adds support for [BLIK](https://docs.stripe.com/payments/blik.md) recurring off-session payments in Poland. You can accept recurring off-session BLIK charges by creating [Mandates](https://docs.stripe.com/api/mandates.md?api-version=2026-09-30.endive) with your customers.

This release adds the following BLIK functionality:

- [Accounts v1](https://docs.stripe.com/api/accounts/object.md?api-version=2026-09-30.endive) support for the [blik_recurring_payments](https://docs.stripe.com/api/accounts/create.md?api-version=2026-09-30.endive#create_account-capabilities-blik_recurring_payments) capability.
- [Accounts v2](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-09-30.endive) support for [blik_recurring_payments](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities-blik_recurring_payments) in:
  - The [merchant capabilities configuration](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities)
  - [requirements](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-09-30.endive#v2_account_object-requirements-entries-impact-restricts_capabilities-capability) and [future requirements](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-09-30.endive#v2_account_object-future_requirements-entries-impact-restricts_capabilities-capability) entries that restrict capabilities
  - Merchant capability [status updates](https://docs.stripe.com/api/v2/core/accounts/event-types.md?api-version=2026-09-30.endive#v2_accounts_event_types-v2.core.account%5Bconfiguration.merchant%5D.capability_status_updated).
- [PaymentIntents](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.endive), [SetupIntents](https://docs.stripe.com/api/setup_intents/create.md?api-version=2026-09-30.endive), and [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-09-30.endive) now include a [mandate_options](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-blik-mandate_options) parameter in BLIK payment method options.
- PaymentIntents now include [off_session](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-blik-setup_future_usage) as a value for [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-blik-setup_future_usage) in BLIK payment method options.
- SetupIntents now include a [blik](https://docs.stripe.com/api/setup_intents/create.md?api-version=2026-09-30.endive#create_setup_intent-payment_method_options-blik) payment method options parameter.
- [Mandates](https://docs.stripe.com/api/mandates.md?api-version=2026-09-30.endive) now include BLIK [payment_method_details](https://docs.stripe.com/api/mandates/object.md?api-version=2026-09-30.endive#mandate_object-payment_method_details) including the [expires_at](https://docs.stripe.com/api/mandates/object.md?api-version=2026-09-30.endive#mandate_object-payment_method_details-blik-expires_at) and [type](https://docs.stripe.com/api/mandates/object.md?api-version=2026-09-30.endive#mandate_object-payment_method_details-blik-type) properties.
- Checkout Sessions now include BLIK payment method options on [setup_intent_data](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-09-30.endive#create_checkout_session-setup_intent_data) and [subscription_data](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-09-30.endive#create_checkout_session-subscription_data)
- BLIK descriptions for [Subscriptions](https://docs.stripe.com/api/subscriptions.md?api-version=2026-09-30.endive), [Invoices](https://docs.stripe.com/api/invoices.md?api-version=2026-09-30.endive), [Customers](https://docs.stripe.com/api/customers.md?api-version=2026-09-30.endive), and [Quotes](https://docs.stripe.com/api/quotes.md?api-version=2026-09-30.endive) now reflect support for automatic charge collection.

## Impact

To collect recurring off-session BLIK payments in Poland:

- Follow the [BLIK recurring payments](https://docs.stripe.com/payments/blik/recurring-payments.md) guide
- Create mandates through PaymentIntents or SetupIntents
- Ensure that both the [blik_payments](https://docs.stripe.com/api/accounts/create.md?api-version=2026-09-30.endive#create_account-capabilities-blik_payments) and [blik_recurring_payments](https://docs.stripe.com/api/accounts/create.md?api-version=2026-09-30.endive#create_account-capabilities-blik_recurring_payments) capabilities are active on your account.

For Accounts v2, request `blik_recurring_payments` through [configuration.merchant.capabilities](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities). Monitor account requirements and merchant capability status updates to determine when the capability is active.

If your integration already accepts one-time BLIK payments, provide [mandate_data.customer_acceptance](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.endive#create_payment_intent-mandate_data-customer_acceptance) to create a mandate. You can also pass `mandate_options` and set `setup_future_usage` to `off_session` in your BLIK payment method options.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `blik_recurring_payments` | Added | [Account#create.capabilities](/api/accounts/create?api-version=2026-09-30.endive#create_account-capabilities), [Account#update.capabilities](/api/accounts/update?api-version=2026-09-30.endive#update_account-capabilities), [Account.capabilities](/api/accounts/object?api-version=2026-09-30.endive#account_object-capabilities), [V2.Core.Account#create.configuration.merchant.capabilities](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities), [V2.Core.Account#update.configuration.merchant.capabilities](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant-capabilities), [V2.Core.Account.configuration.merchant.capabilities](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities) |
| `blik` | Added | [Checkout.Session#create.payment_method_options](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-payment_method_options), [Invoice#create.payment_settings.payment_method_options](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_options), [Invoice#update.payment_settings.payment_method_options](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options), [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options), [Mandate.payment_method_details](/api/mandates/object?api-version=2026-09-30.endive#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-09-30.endive#setup_attempt_object-payment_method_details), [SetupIntent#confirm.payment_method_options](/api/setup_intents/confirm?api-version=2026-09-30.endive#confirm_setup_intent-payment_method_options), [SetupIntent#create.payment_method_options](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent-payment_method_options), [SetupIntent#update.payment_method_options](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent-payment_method_options), [SetupIntent.payment_method_options](/api/setup_intents/object?api-version=2026-09-30.endive#setup_intent_object-payment_method_options), [Subscription#create.payment_settings.payment_method_options](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_options), [Subscription#update.payment_settings.payment_method_options](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options) |
| `mandate_options` | Added | [PaymentIntent#confirm.payment_method_options.blik](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-blik), [PaymentIntent#create.payment_method_options.blik](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-blik), [PaymentIntent#update.payment_method_options.blik](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-payment_method_options-blik), [PaymentIntent.payment_method_options.blik](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-blik) |

| Values | Change | Enums |
| --- | --- | --- |
| `blik_recurring_payments` | Added | [V2.Core.Account.future_requirements.entries[].impact.restricts_capabilities[].capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-future_requirements-entries-impact-restricts_capabilities-capability), [V2.Core.Account.requirements.entries[].impact.restricts_capabilities[].capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-requirements-entries-impact-restricts_capabilities-capability), [EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability](/api/v2/core/accounts/event-types?api-version=2026-09-30.endive#v2_accounts_event_types-v2.core.account[configuration.merchant].capability_status_updated) |
| `blik` | Added | [Invoice#update.payment_settings.payment_method_types](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_types), [Invoice#create.payment_settings.payment_method_types](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_types), [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_types), [Subscription#update.payment_settings.payment_method_types](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_types), [Subscription#create.payment_settings.payment_method_types](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_types) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentIntent#confirm.payment_method_options.blik.setup_future_usage`, `PaymentIntent#create.payment_method_options.blik.setup_future_usage`, `PaymentIntent#update.payment_method_options.blik.setup_future_usage`, `PaymentIntent.payment_method_options.blik.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `blik_recurring_payments` | Added | [Account::Capability](/api/accounts/object?api-version=2026-09-30.endive#account_object-capabilities), [AccountCreateParams::Capability](/api/accounts/create?api-version=2026-09-30.endive#create_account-capabilities), [AccountUpdateParams::Capability](/api/accounts/update?api-version=2026-09-30.endive#update_account-capabilities), [V2::Core::Account::Configuration::Merchant::Capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [V2::Core::AccountCreateParams::Configuration::Merchant::Capability](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities), [V2::Core::AccountUpdateParams::Configuration::Merchant::Capability](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant-capabilities) |
| `blik` | Added | [Checkout::SessionCreateParams::PaymentMethodOption](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-payment_method_options), [Invoice::PaymentSetting::PaymentMethodOption](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options), [InvoiceCreateParams::PaymentSetting::PaymentMethodOption](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_options), [InvoiceUpdateParams::PaymentSetting::PaymentMethodOption](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options), [Mandate::PaymentMethodDetail](/api/mandates/object?api-version=2026-09-30.endive#mandate_object-payment_method_details), [SetupAttempt::PaymentMethodDetail](/api/setup_attempts/object?api-version=2026-09-30.endive#setup_attempt_object-payment_method_details), [SetupIntent::PaymentMethodOption](/api/setup_intents/object?api-version=2026-09-30.endive#setup_intent_object-payment_method_options), [SetupIntentConfirmParams::PaymentMethodOption](/api/setup_intents/confirm?api-version=2026-09-30.endive#confirm_setup_intent-payment_method_options), [SetupIntentCreateParams::PaymentMethodOption](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent-payment_method_options), [SetupIntentUpdateParams::PaymentMethodOption](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent-payment_method_options), [Subscription::PaymentSetting::PaymentMethodOption](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options), [SubscriptionCreateParams::PaymentSetting::PaymentMethodOption](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_options), [SubscriptionUpdateParams::PaymentSetting::PaymentMethodOption](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options) |
| `mandate_options` | Added | [PaymentIntent::PaymentMethodOption::Blik](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-blik), [PaymentIntentConfirmParams::PaymentMethodOption::Blik](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-blik), [PaymentIntentCreateParams::PaymentMethodOption::Blik](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-blik), [PaymentIntentUpdateParams::PaymentMethodOption::Blik](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-payment_method_options-blik) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentIntent::PaymentMethodOption::Blik.setup_future_usage`, `PaymentIntentConfirmParams::PaymentMethodOption::Blik.setup_future_usage`, `PaymentIntentCreateParams::PaymentMethodOption::Blik.setup_future_usage`, `PaymentIntentUpdateParams::PaymentMethodOption::Blik.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `blik_recurring_payments` | Added | [Account.Capability](/api/accounts/object?api-version=2026-09-30.endive#account_object-capabilities), [AccountCreateParamsCapability](/api/accounts/create?api-version=2026-09-30.endive#create_account-capabilities), [AccountModifyParamsCapability](/api/accounts/update?api-version=2026-09-30.endive#update_account-capabilities), [V2.Core.Account.Configuration.Merchant.Capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [v2.core.AccountCreateParamsConfigurationMerchantCapability](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities), [v2.core.AccountModifyParamsConfigurationMerchantCapability](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant-capabilities) |
| `blik` | Added | [checkout.SessionCreateParamsPaymentMethodOption](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-payment_method_options), [Invoice.PaymentSetting.PaymentMethodOption](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options), [InvoiceCreateParamsPaymentSettingPaymentMethodOption](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_options), [InvoiceModifyParamsPaymentSettingPaymentMethodOption](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options), [Mandate.PaymentMethodDetail](/api/mandates/object?api-version=2026-09-30.endive#mandate_object-payment_method_details), [SetupAttempt.PaymentMethodDetail](/api/setup_attempts/object?api-version=2026-09-30.endive#setup_attempt_object-payment_method_details), [SetupIntent.PaymentMethodOption](/api/setup_intents/object?api-version=2026-09-30.endive#setup_intent_object-payment_method_options), [SetupIntentConfirmParamsPaymentMethodOption](/api/setup_intents/confirm?api-version=2026-09-30.endive#confirm_setup_intent-payment_method_options), [SetupIntentCreateParamsPaymentMethodOption](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent-payment_method_options), [SetupIntentModifyParamsPaymentMethodOption](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent-payment_method_options), [Subscription.PaymentSetting.PaymentMethodOption](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options), [SubscriptionCreateParamsPaymentSettingPaymentMethodOption](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_options), [SubscriptionModifyParamsPaymentSettingPaymentMethodOption](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options) |
| `mandate_options` | Added | [PaymentIntent.PaymentMethodOption.Blik](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-blik), [PaymentIntentConfirmParamsPaymentMethodOptionBlik](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-blik), [PaymentIntentCreateParamsPaymentMethodOptionBlik](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-blik), [PaymentIntentModifyParamsPaymentMethodOptionBlik](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-payment_method_options-blik) |

| Values | Change | Enums |
| --- | --- | --- |
| `blik_recurring_payments` | Added | [V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-future_requirements-entries-impact-restricts_capabilities-capability), [V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-requirements-entries-impact-restricts_capabilities-capability), [EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability](/api/v2/core/accounts/event-types?api-version=2026-09-30.endive#v2_accounts_event_types-v2.core.account[configuration.merchant].capability_status_updated) |
| `blik` | Added | [InvoiceModifyParamsPaymentSetting.payment_method_types](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_types), [InvoiceCreateParamsPaymentSetting.payment_method_types](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_types), [Invoice.PaymentSetting.payment_method_types](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_types), [SubscriptionModifyParamsPaymentSetting.payment_method_types](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_types), [SubscriptionCreateParamsPaymentSetting.payment_method_types](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_types), [Subscription.PaymentSetting.payment_method_types](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_types) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentIntent.PaymentMethodOption.Blik.setup_future_usage`, `PaymentIntentConfirmParamsPaymentMethodOptionBlik.setup_future_usage`, `PaymentIntentCreateParamsPaymentMethodOptionBlik.setup_future_usage`, `PaymentIntentModifyParamsPaymentMethodOptionBlik.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `blik_recurring_payments` | Added | [Account.capabilities](/api/accounts/object?api-version=2026-09-30.endive#account_object-capabilities), [Account.create().$params.capability](/api/accounts/create?api-version=2026-09-30.endive#create_account-capabilities), [Account.update().$params.capability](/api/accounts/update?api-version=2026-09-30.endive#update_account-capabilities), [V2.Core.Account.configuration.merchant.capabilities](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [V2\Core\Account.create().$params.configuration.merchant.capability](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities), [V2\Core\Account.update().$params.configuration.merchant.capability](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant-capabilities) |
| `blik` | Added | [Checkout\Session.create().$params.payment_method_option](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-payment_method_options), [Invoice.create().$params.payment_setting.payment_method_option](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_options), [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options), [Invoice.update().$params.payment_setting.payment_method_option](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options), [Mandate.payment_method_details](/api/mandates/object?api-version=2026-09-30.endive#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-09-30.endive#setup_attempt_object-payment_method_details), [SetupIntent.confirm().$params.payment_method_option](/api/setup_intents/confirm?api-version=2026-09-30.endive#confirm_setup_intent-payment_method_options), [SetupIntent.create().$params.payment_method_option](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent-payment_method_options), [SetupIntent.payment_method_options](/api/setup_intents/object?api-version=2026-09-30.endive#setup_intent_object-payment_method_options), [SetupIntent.update().$params.payment_method_option](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent-payment_method_options), [Subscription.create().$params.payment_setting.payment_method_option](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options), [Subscription.update().$params.payment_setting.payment_method_option](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options) |
| `mandate_options` | Added | [PaymentIntent.confirm().$params.payment_method_option.blik](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-blik), [PaymentIntent.create().$params.payment_method_option.blik](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-blik), [PaymentIntent.payment_method_options.blik](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-blik), [PaymentIntent.update().$params.payment_method_option.blik](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-payment_method_options-blik) |

| Values | Change | Enums |
| --- | --- | --- |
| `blik_recurring_payments` | Added | [V2.Core.Account.future_requirements.entries[].impact.restricts_capabilities[].capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-future_requirements-entries-impact-restricts_capabilities-capability), [V2.Core.Account.requirements.entries[].impact.restricts_capabilities[].capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-requirements-entries-impact-restricts_capabilities-capability), [EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability](/api/v2/core/accounts/event-types?api-version=2026-09-30.endive#v2_accounts_event_types-v2.core.account[configuration.merchant].capability_status_updated) |
| `blik` | Added | [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_types) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentIntent.confirm().$params.payment_method_option.blik.setup_future_usage`, `PaymentIntent.create().$params.payment_method_option.blik.setup_future_usage`, `PaymentIntent.payment_method_options.blik.setup_future_usage`, `PaymentIntent.update().$params.payment_method_option.blik.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `blikRecurringPayments` | Added | [Account.capabilities](/api/accounts/object?api-version=2026-09-30.endive#account_object-capabilities), [AccountCreateParams.capabilities](/api/accounts/create?api-version=2026-09-30.endive#create_account-capabilities), [AccountUpdateParams.capabilities](/api/accounts/update?api-version=2026-09-30.endive#update_account-capabilities), [v2.core.Account.configuration.merchant.capabilities](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [v2.core.AccountCreateParams.configuration.merchant.capabilities](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities), [v2.core.AccountUpdateParams.configuration.merchant.capabilities](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant-capabilities) |
| `blik` | Added | [checkout.SessionCreateParams.payment_method_options](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-payment_method_options), [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options), [InvoiceCreateParams.payment_settings.payment_method_options](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_options), [InvoiceUpdateParams.payment_settings.payment_method_options](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options), [Mandate.payment_method_details](/api/mandates/object?api-version=2026-09-30.endive#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-09-30.endive#setup_attempt_object-payment_method_details), [SetupIntent.payment_method_options](/api/setup_intents/object?api-version=2026-09-30.endive#setup_intent_object-payment_method_options), [SetupIntentConfirmParams.payment_method_options](/api/setup_intents/confirm?api-version=2026-09-30.endive#confirm_setup_intent-payment_method_options), [SetupIntentCreateParams.payment_method_options](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent-payment_method_options), [SetupIntentUpdateParams.payment_method_options](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options), [SubscriptionCreateParams.payment_settings.payment_method_options](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_options), [SubscriptionUpdateParams.payment_settings.payment_method_options](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options) |
| `mandateOptions` | Added | [PaymentIntent.payment_method_options.blik](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-blik), [PaymentIntentConfirmParams.payment_method_options.blik](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-blik), [PaymentIntentCreateParams.payment_method_options.blik](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-blik), [PaymentIntentUpdateParams.payment_method_options.blik](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-payment_method_options-blik) |

| Values | Change | Enums |
| --- | --- | --- |
| `blik_recurring_payments` | Added | [EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updatedCapability](/api/v2/core/accounts/event-types?api-version=2026-09-30.endive#v2_accounts_event_types-v2.core.account[configuration.merchant].capability_status_updated) |
| `blik` | Added | [InvoiceUpdateParams.payment_settings.paymentMethodTypes](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-paymentMethodTypes), [InvoiceCreateParams.payment_settings.paymentMethodTypes](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-paymentMethodTypes), [SubscriptionUpdateParams.payment_settings.paymentMethodTypes](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-paymentMethodTypes), [SubscriptionCreateParams.payment_settings.paymentMethodTypes](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-paymentMethodTypes) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentIntent.payment_method_options.blik.setupFutureUsage`, `PaymentIntentConfirmParams.payment_method_options.blik.setupFutureUsage`, `PaymentIntentCreateParams.payment_method_options.blik.setupFutureUsage`, `PaymentIntentUpdateParams.payment_method_options.blik.setupFutureUsage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `blik_recurring_payments` | Added | [Account.capabilities](/api/accounts/object?api-version=2026-09-30.endive#account_object-capabilities), [AccountCreateParams.capabilities](/api/accounts/create?api-version=2026-09-30.endive#create_account-capabilities), [AccountUpdateParams.capabilities](/api/accounts/update?api-version=2026-09-30.endive#update_account-capabilities), [V2.Core.Account.configuration.merchant.capabilities](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [V2.Core.AccountCreateParams.configuration.merchant.capabilities](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities), [V2.Core.AccountUpdateParams.configuration.merchant.capabilities](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant-capabilities) |
| `blik` | Added | [Checkout.SessionCreateParams.payment_method_options](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-payment_method_options), [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options), [InvoiceCreateParams.payment_settings.payment_method_options](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_options), [InvoiceUpdateParams.payment_settings.payment_method_options](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options), [Mandate.payment_method_details](/api/mandates/object?api-version=2026-09-30.endive#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-09-30.endive#setup_attempt_object-payment_method_details), [SetupIntent.payment_method_options](/api/setup_intents/object?api-version=2026-09-30.endive#setup_intent_object-payment_method_options), [SetupIntentConfirmParams.payment_method_options](/api/setup_intents/confirm?api-version=2026-09-30.endive#confirm_setup_intent-payment_method_options), [SetupIntentCreateParams.payment_method_options](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent-payment_method_options), [SetupIntentUpdateParams.payment_method_options](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options), [SubscriptionCreateParams.payment_settings.payment_method_options](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_options), [SubscriptionUpdateParams.payment_settings.payment_method_options](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options) |
| `mandate_options` | Added | [PaymentIntent.payment_method_options.blik](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-blik), [PaymentIntentConfirmParams.payment_method_options.blik](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-blik), [PaymentIntentCreateParams.payment_method_options.blik](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-blik), [PaymentIntentUpdateParams.payment_method_options.blik](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-payment_method_options-blik) |

| Values | Change | Enums |
| --- | --- | --- |
| `blik_recurring_payments` | Added | [V2.Core.Account.future_requirements.entries[].impact.restricts_capabilities[].capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-future_requirements-entries-impact-restricts_capabilities-capability), [V2.Core.Account.requirements.entries[].impact.restricts_capabilities[].capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-requirements-entries-impact-restricts_capabilities-capability), [EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability](/api/v2/core/accounts/event-types?api-version=2026-09-30.endive#v2_accounts_event_types-v2.core.account[configuration.merchant].capability_status_updated) |
| `blik` | Added | [InvoiceUpdateParams.payment_settings.payment_method_types](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_types), [InvoiceCreateParams.payment_settings.payment_method_types](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_types), [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_types), [SubscriptionUpdateParams.payment_settings.payment_method_types](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_types), [SubscriptionCreateParams.payment_settings.payment_method_types](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_types) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentIntent.payment_method_options.blik.setup_future_usage`, `PaymentIntentConfirmParams.payment_method_options.blik.setup_future_usage`, `PaymentIntentCreateParams.payment_method_options.blik.setup_future_usage`, `PaymentIntentUpdateParams.payment_method_options.blik.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BLIKRecurringPayments` | Added | [AccountCapabilities](/api/accounts/object?api-version=2026-09-30.endive#account_object-capabilities), [AccountCapabilitiesParams](/api/accounts/update?api-version=2026-09-30.endive#update_account-capabilities), [V2CoreAccountConfigurationMerchantCapabilities](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [V2CoreAccountConfigurationMerchantCapabilitiesParams](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities) |
| `BLIK` | Added | [CheckoutSessionPaymentMethodOptionsParams](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-payment_method_options), [InvoicePaymentSettingsPaymentMethodOptions](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options), [InvoicePaymentSettingsPaymentMethodOptionsParams](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options), [MandatePaymentMethodDetails](/api/mandates/object?api-version=2026-09-30.endive#mandate_object-payment_method_details), [SetupAttemptPaymentMethodDetails](/api/setup_attempts/object?api-version=2026-09-30.endive#setup_attempt_object-payment_method_details), [SetupIntentConfirmPaymentMethodOptionsParams](/api/setup_intents/confirm?api-version=2026-09-30.endive#confirm_setup_intent-payment_method_options), [SetupIntentPaymentMethodOptions](/api/setup_intents/object?api-version=2026-09-30.endive#setup_intent_object-payment_method_options), [SetupIntentPaymentMethodOptionsParams](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent-payment_method_options), [SubscriptionPaymentSettingsPaymentMethodOptions](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options), [SubscriptionPaymentSettingsPaymentMethodOptionsParams](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options) |
| `MandateOptions` | Added | [PaymentIntentConfirmPaymentMethodOptionsBlikParams](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-blik), [PaymentIntentPaymentMethodOptionsBlik](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-blik), [PaymentIntentPaymentMethodOptionsBlikParams](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-blik) |

| Values | Change | Enums |
| --- | --- | --- |
| `blik_recurring_payments` | Added | [V2CoreAccountFutureRequirementsEntryImpactRestrictsCapability.Capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-future_requirements-entries-impact-restricts_capabilities-Capability), [V2CoreAccountRequirementsEntryImpactRestrictsCapability.Capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-requirements-entries-impact-restricts_capabilities-Capability), [EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.UpdatedCapability](/api/v2/core/accounts/event-types?api-version=2026-09-30.endive#v2_accounts_event_types-v2.core.account[configuration.merchant].capability_status_updated) |
| `blik` | Added | [InvoicePaymentSettings.PaymentMethodTypes](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-PaymentMethodTypes), [SubscriptionPaymentSettings.PaymentMethodTypes](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-PaymentMethodTypes) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentIntentConfirmPaymentMethodOptionsBlikParams.SetupFutureUsage`, `PaymentIntentPaymentMethodOptionsBlik.SetupFutureUsage`, `PaymentIntentPaymentMethodOptionsBlikParams.SetupFutureUsage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BlikRecurringPayments` | Added | [Account.Capabilities](/api/accounts/object?api-version=2026-09-30.endive#account_object-capabilities), [AccountCapabilitiesOptions](/api/accounts/update?api-version=2026-09-30.endive#update_account-capabilities), [V2.Core.Account.Configuration.Merchant.Capabilities](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [V2CoreAccountConfigurationMerchantCapabilitiesOptions](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities) |
| `Blik` | Added | [CheckoutSessionPaymentMethodOptionsOptions](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-payment_method_options), [Invoice.PaymentSettings.PaymentMethodOptions](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options), [InvoicePaymentSettingsPaymentMethodOptionsOptions](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options), [Mandate.PaymentMethodDetails](/api/mandates/object?api-version=2026-09-30.endive#mandate_object-payment_method_details), [SetupAttempt.PaymentMethodDetails](/api/setup_attempts/object?api-version=2026-09-30.endive#setup_attempt_object-payment_method_details), [SetupIntent.PaymentMethodOptions](/api/setup_intents/object?api-version=2026-09-30.endive#setup_intent_object-payment_method_options), [SetupIntentPaymentMethodOptionsOptions](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent-payment_method_options), [Subscription.PaymentSettings.PaymentMethodOptions](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options), [SubscriptionPaymentSettingsPaymentMethodOptionsOptions](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options) |
| `MandateOptions` | Added | [PaymentIntent.PaymentMethodOptions.Blik](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-blik), [PaymentIntentPaymentMethodOptionsBlikOptions](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-blik) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentIntent.PaymentMethodOptions.Blik.SetupFutureUsage`, `PaymentIntentPaymentMethodOptionsBlikOptions.SetupFutureUsage` | Changed | `literal('none') → enum('none'|'off_session')` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.endive`
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

- [Removes the payment method types parameter from Checkout Sessions](https://docs.stripe.com/changelog/endive/2026-09-30/remove-payment-method-types-checkout-sessions.md)
- [Adds support for Data Share Only for 3D Secure authentication](https://docs.stripe.com/changelog/endive/2026-09-30/data-share-only.md)
- [Makes Payment Evaluation signal scores nullable](https://docs.stripe.com/changelog/endive/2026-09-30/payment-evaluations-nullable-score.md)
- [Removes PayTo-specific fields from Payment Methods](https://docs.stripe.com/changelog/endive/2026-09-30/removed-payto-fields.md)
- [Removes the payment method types parameter from Payment Intents and Setup Intents](https://docs.stripe.com/changelog/endive/2026-09-30/removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents.md)
- [Returns specific decline codes for BLIK payment failures](https://docs.stripe.com/changelog/endive/2026-09-30/blik-granular-decline-codes.md)
- [Deprecates the payment request button](https://docs.stripe.com/changelog/endive/2026-09-30/deprecate-payment-request-button.md)
- [Shows pending-authorization UI for MB WAY, Bizum, and BLIK with stripe.handleNextAction](https://docs.stripe.com/changelog/endive/2026-09-30/handle-next-action-mb-way-bizum-ui.md)
- [Removes support for the payment method types option in Elements](https://docs.stripe.com/changelog/endive/2026-09-30/remove-elements-deferred-intent-payment-method-types.md)
- [Saves Bancontact payment details for future off-session payments in Checkout](https://docs.stripe.com/changelog/endive/2026-09-30/bancontact-off-session-payments-checkout.md)
- [Adds the Standalone 3D Secure API](https://docs.stripe.com/changelog/endive/2026-09-30/standalone-3ds.md)
- [Adds support for SeQura payments](https://docs.stripe.com/changelog/endive/2026-09-30/sequra-payments.md)
- [Adds card-present payment methods to allowed payment method types](https://docs.stripe.com/changelog/endive/2026-09-30/card-present-and-interac-present-enum-values-for-allowed-payment-method-types.md)
- [Adds Link funding source group details on Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/link-funding-source-group-payment-records.md)
- [Adds early fraud warnings and fraudulent dispute signals for Payment Evaluations](https://docs.stripe.com/changelog/endive/2026-09-30/new-radar-signals-for-payment-evaluations.md)
- [Adds the ability to report cancelled payments](https://docs.stripe.com/changelog/endive/2026-09-30/reporting-canceled-payments.md)
- [Adds support for expanding the mandate on card payment method details](https://docs.stripe.com/changelog/endive/2026-09-30/expand-mandate-on-card-payments-details.md)
- [Adds the Payment Record property to the Payment Intent object](https://docs.stripe.com/changelog/endive/2026-09-30/payment-records-on-payment-intents.md)
- [Adds Link wallet details to Payment Records for card payments](https://docs.stripe.com/changelog/endive/2026-09-30/adds-link-wallet-details-to-payment-records-for-card-payments.md)
- [Adds 3D Secure versions 2.3.0 and 2.3.1 to Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/3d-secure-payment-records.md)
- [Adds PayPay support for one-time online payments in Japan](https://docs.stripe.com/changelog/endive/2026-09-30/paypay-payments-japan.md)
- [Exposes the network response electronic commerce indicator on card charges](https://docs.stripe.com/changelog/endive/2026-09-30/view-network-response-eci-on-card-charges.md)
- [Adds payment method type information for failed payments](https://docs.stripe.com/changelog/endive/2026-09-30/payment-method-type-payment-failures.md)
- [Adds MoMo payment method details to Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/adds-momo-payment-method-details-to-payment-records.md)
