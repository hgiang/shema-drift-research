# Adds support for Pix recurring payments

## What’s new

Adds support for [Pix](https://docs.stripe.com/payments/pix.md) recurring payments. You can now use Pix to collect recurring payments from customers by creating subscriptions with [mandate options](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix-mandate_options) that specify the terms for future payments.

When you create a [Payment Intent](https://docs.stripe.com/api/payment_intents.md?api-version=2026-04-22.dahlia), [Setup Intent](https://docs.stripe.com/api/setup_intents.md?api-version=2026-04-22.dahlia), or [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md?api-version=2026-04-22.dahlia) with Pix, you can configure mandate options including:

- [amount](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix-mandate_options-amount): The amount to charge for future payments
- [amount_type](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix-mandate_options-amount_type): Whether the amount is fixed or represents a maximum
- [currency](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix-mandate_options-currency): Three-letter ISO currency code
- [payment_schedule](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix-mandate_options-payment_schedule): Schedule for recurring payments (monthly, quarterly, etc.)
- [reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix-mandate_options-reference): Subscription name displayed to customers
- [start_date](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix-mandate_options-start_date) and [end_date](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix-mandate_options-end_date): Mandate validity period

You can also set [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-04-22.dahlia#create_payment_intent-setup_future_usage) to `off_session` when creating Payment Intents with Pix to enable recurring payments. Setup Intents with Pix support QR code display for customer authentication.

## Impact

You can now create subscriptions that use Pix as the payment method for recurring billing for customers in Brazil. If you’re already using Pix for one-time payments, update your integration to [support recurring payments](https://docs.stripe.com/payments/pix/pix-automatico.md) by adding mandate options when creating Payment Intents, Setup Intents, or Checkout Sessions with Pix.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `mandate` | Added | [Charge.payment_method_details.pix](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-pix), [PaymentAttemptRecord.payment_method_details.pix](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-pix), [PaymentRecord.payment_method_details.pix](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-pix) |
| `mandate_options` | Added | [Checkout.Session#create.payment_method_options.pix](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session-payment_method_options-pix), [Checkout.Session.payment_method_options.pix](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object-payment_method_options-pix), [PaymentIntent#confirm.payment_method_options.pix](/api/payment_intents/confirm?api-version=2026-04-22.dahlia#confirm_payment_intent-payment_method_options-pix), [PaymentIntent#create.payment_method_options.pix](/api/payment_intents/create?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix), [PaymentIntent#update.payment_method_options.pix](/api/payment_intents/update?api-version=2026-04-22.dahlia#update_payment_intent-payment_method_options-pix), [PaymentIntent.payment_method_options.pix](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-payment_method_options-pix) |
| `pix` | Added | [Invoice#create.payment_settings.payment_method_options](/api/invoices/create?api-version=2026-04-22.dahlia#create-payment_settings-payment_method_options), [Invoice#update.payment_settings.payment_method_options](/api/invoices/update?api-version=2026-04-22.dahlia#update_invoice-payment_settings-payment_method_options), [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2026-04-22.dahlia#invoice_object-payment_settings-payment_method_options), [Mandate.payment_method_details](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details), [SetupIntent#confirm.payment_method_options](/api/setup_intents/confirm?api-version=2026-04-22.dahlia#confirm_setup_intent-payment_method_options), [SetupIntent#create.payment_method_options](/api/setup_intents/create?api-version=2026-04-22.dahlia#create_setup_intent-payment_method_options), [SetupIntent#update.payment_method_options](/api/setup_intents/update?api-version=2026-04-22.dahlia#update_setup_intent-payment_method_options), [SetupIntent.payment_method_options](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-payment_method_options), [Subscription#create.payment_settings.payment_method_options](/api/subscriptions/create?api-version=2026-04-22.dahlia#create_subscription-payment_settings-payment_method_options), [Subscription#update.payment_settings.payment_method_options](/api/subscriptions/update?api-version=2026-04-22.dahlia#update_subscription-payment_settings-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object-payment_settings-payment_method_options) |
| `amount`, `currency` | Added | [Mandate.multi_use](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-multi_use) |
| `pix_display_qr_code` | Added | [SetupIntent.next_action](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-next_action) |

| Value | Change | Enums |
| --- | --- | --- |
| `pix` | Added | [Invoice#update.payment_settings](/api/invoices/update?api-version=2026-04-22.dahlia#update_invoice-payment_settings-payment_method_types), [Invoice#create.payment_settings](/api/invoices/create?api-version=2026-04-22.dahlia#create-payment_settings-payment_method_types), [Invoice.payment_settings](/api/invoices/object?api-version=2026-04-22.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription#update.payment_settings](/api/subscriptions/update?api-version=2026-04-22.dahlia#update_subscription-payment_settings-payment_method_types), [Subscription#create.payment_settings](/api/subscriptions/create?api-version=2026-04-22.dahlia#create_subscription-payment_settings-payment_method_types), [Subscription.payment_settings](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object-payment_settings-payment_method_types) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Checkout.Session#create.payment_method_options.pix.setup_future_usage`, `Checkout.Session.payment_method_options.pix.setup_future_usage`, `PaymentIntent#confirm.payment_method_options.pix.setup_future_usage`, `PaymentIntent#create.payment_method_options.pix.setup_future_usage`, `PaymentIntent#update.payment_method_options.pix.setup_future_usage`, `PaymentIntent.payment_method_options.pix.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mandate` | Added | [Charge::PaymentMethodDetail::Pix](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-pix), [PaymentAttemptRecord::PaymentMethodDetail::Pix](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-pix), [PaymentRecord::PaymentMethodDetail::Pix](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-pix) |
| `mandate_options` | Added | [Checkout::Session::PaymentMethodOption::Pix](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object-payment_method_options-pix), [Checkout::SessionCreateParams::PaymentMethodOption::Pix](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session-payment_method_options-pix), [PaymentIntent::PaymentMethodOption::Pix](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-payment_method_options-pix), [PaymentIntentConfirmParams::PaymentMethodOption::Pix](/api/payment_intents/confirm?api-version=2026-04-22.dahlia#confirm_payment_intent-payment_method_options-pix), [PaymentIntentCreateParams::PaymentMethodOption::Pix](/api/payment_intents/create?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix), [PaymentIntentUpdateParams::PaymentMethodOption::Pix](/api/payment_intents/update?api-version=2026-04-22.dahlia#update_payment_intent-payment_method_options-pix) |
| `pix` | Added | [Invoice::PaymentSetting::PaymentMethodOption](/api/invoices/object?api-version=2026-04-22.dahlia#invoice_object-payment_settings-payment_method_options), [InvoiceCreateParams::PaymentSetting::PaymentMethodOption](/api/invoices/create?api-version=2026-04-22.dahlia#create-payment_settings-payment_method_options), [InvoiceUpdateParams::PaymentSetting::PaymentMethodOption](/api/invoices/update?api-version=2026-04-22.dahlia#update_invoice-payment_settings-payment_method_options), [Mandate::PaymentMethodDetail](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-payment_method_details), [SetupAttempt::PaymentMethodDetail](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details), [SetupIntent::PaymentMethodOption](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-payment_method_options), [SetupIntentConfirmParams::PaymentMethodOption](/api/setup_intents/confirm?api-version=2026-04-22.dahlia#confirm_setup_intent-payment_method_options), [SetupIntentCreateParams::PaymentMethodOption](/api/setup_intents/create?api-version=2026-04-22.dahlia#create_setup_intent-payment_method_options), [SetupIntentUpdateParams::PaymentMethodOption](/api/setup_intents/update?api-version=2026-04-22.dahlia#update_setup_intent-payment_method_options), [Subscription::PaymentSetting::PaymentMethodOption](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object-payment_settings-payment_method_options), [SubscriptionCreateParams::PaymentSetting::PaymentMethodOption](/api/subscriptions/create?api-version=2026-04-22.dahlia#create_subscription-payment_settings-payment_method_options), [SubscriptionUpdateParams::PaymentSetting::PaymentMethodOption](/api/subscriptions/update?api-version=2026-04-22.dahlia#update_subscription-payment_settings-payment_method_options) |
| `amount`, `currency` | Added | [Mandate::MultiUse](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-multi_use) |
| `pix_display_qr_code` | Added | [SetupIntent::NextAction](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-next_action) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Checkout::Session::PaymentMethodOption::Pix.setup_future_usage`, `Checkout::SessionCreateParams::PaymentMethodOption::Pix.setup_future_usage`, `PaymentIntent::PaymentMethodOption::Pix.setup_future_usage`, `PaymentIntentConfirmParams::PaymentMethodOption::Pix.setup_future_usage`, `PaymentIntentCreateParams::PaymentMethodOption::Pix.setup_future_usage`, `PaymentIntentUpdateParams::PaymentMethodOption::Pix.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mandate` | Added | [Charge.PaymentMethodDetail.Pix](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-pix), [PaymentAttemptRecord.PaymentMethodDetail.Pix](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-pix), [PaymentRecord.PaymentMethodDetail.Pix](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-pix) |
| `mandate_options` | Added | [Checkout.Session.PaymentMethodOption.Pix](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object-payment_method_options-pix), [PaymentIntent.PaymentMethodOption.Pix](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-payment_method_options-pix), [PaymentIntentConfirmParamsPaymentMethodOptionPix](/api/payment_intents/confirm?api-version=2026-04-22.dahlia#confirm_payment_intent-payment_method_options-pix), [PaymentIntentCreateParamsPaymentMethodOptionPix](/api/payment_intents/create?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix), [PaymentIntentModifyParamsPaymentMethodOptionPix](/api/payment_intents/update?api-version=2026-04-22.dahlia#update_payment_intent-payment_method_options-pix), [checkout.SessionCreateParamsPaymentMethodOptionPix](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session-payment_method_options-pix) |
| `pix` | Added | [Invoice.PaymentSetting.PaymentMethodOption](/api/invoices/object?api-version=2026-04-22.dahlia#invoice_object-payment_settings-payment_method_options), [InvoiceCreateParamsPaymentSettingPaymentMethodOption](/api/invoices/create?api-version=2026-04-22.dahlia#create-payment_settings-payment_method_options), [InvoiceModifyParamsPaymentSettingPaymentMethodOption](/api/invoices/update?api-version=2026-04-22.dahlia#update_invoice-payment_settings-payment_method_options), [Mandate.PaymentMethodDetail](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-payment_method_details), [SetupAttempt.PaymentMethodDetail](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details), [SetupIntent.PaymentMethodOption](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-payment_method_options), [SetupIntentConfirmParamsPaymentMethodOption](/api/setup_intents/confirm?api-version=2026-04-22.dahlia#confirm_setup_intent-payment_method_options), [SetupIntentCreateParamsPaymentMethodOption](/api/setup_intents/create?api-version=2026-04-22.dahlia#create_setup_intent-payment_method_options), [SetupIntentModifyParamsPaymentMethodOption](/api/setup_intents/update?api-version=2026-04-22.dahlia#update_setup_intent-payment_method_options), [Subscription.PaymentSetting.PaymentMethodOption](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object-payment_settings-payment_method_options), [SubscriptionCreateParamsPaymentSettingPaymentMethodOption](/api/subscriptions/create?api-version=2026-04-22.dahlia#create_subscription-payment_settings-payment_method_options), [SubscriptionModifyParamsPaymentSettingPaymentMethodOption](/api/subscriptions/update?api-version=2026-04-22.dahlia#update_subscription-payment_settings-payment_method_options) |
| `amount`, `currency` | Added | [Mandate.MultiUse](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-multi_use) |
| `pix_display_qr_code` | Added | [SetupIntent.NextAction](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-next_action) |

| Value | Change | Enums |
| --- | --- | --- |
| `pix` | Added | [InvoiceModifyParamsPaymentSetting](/api/invoices/update?api-version=2026-04-22.dahlia#update_invoice-payment_settings-payment_method_types), [InvoiceCreateParamsPaymentSetting](/api/invoices/create?api-version=2026-04-22.dahlia#create-payment_settings-payment_method_types), [Invoice.PaymentSetting](/api/invoices/object?api-version=2026-04-22.dahlia#invoice_object-payment_settings-payment_method_types), [SubscriptionModifyParamsPaymentSetting](/api/subscriptions/update?api-version=2026-04-22.dahlia#update_subscription-payment_settings-payment_method_types), [SubscriptionCreateParamsPaymentSetting](/api/subscriptions/create?api-version=2026-04-22.dahlia#create_subscription-payment_settings-payment_method_types), [Subscription.PaymentSetting](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object-payment_settings-payment_method_types) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Checkout.Session.PaymentMethodOption.Pix.setup_future_usage`, `PaymentIntent.PaymentMethodOption.Pix.setup_future_usage`, `PaymentIntentConfirmParamsPaymentMethodOptionPix.setup_future_usage`, `PaymentIntentCreateParamsPaymentMethodOptionPix.setup_future_usage`, `PaymentIntentModifyParamsPaymentMethodOptionPix.setup_future_usage`, `checkout.SessionCreateParamsPaymentMethodOptionPix.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mandate` | Added | [Charge.payment_method_details.pix](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-pix), [PaymentAttemptRecord.payment_method_details.pix](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-pix), [PaymentRecord.payment_method_details.pix](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-pix) |
| `mandate_options` | Added | [Checkout.Session.payment_method_options.pix](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object-payment_method_options-pix), [Checkout\Session.create().$params.payment_method_option.pix](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session-payment_method_options-pix), [PaymentIntent.confirm().$params.payment_method_option.pix](/api/payment_intents/confirm?api-version=2026-04-22.dahlia#confirm_payment_intent-payment_method_options-pix), [PaymentIntent.create().$params.payment_method_option.pix](/api/payment_intents/create?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix), [PaymentIntent.payment_method_options.pix](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-payment_method_options-pix), [PaymentIntent.update().$params.payment_method_option.pix](/api/payment_intents/update?api-version=2026-04-22.dahlia#update_payment_intent-payment_method_options-pix) |
| `pix` | Added | [Invoice.create().$params.payment_setting.payment_method_option](/api/invoices/create?api-version=2026-04-22.dahlia#create-payment_settings-payment_method_options), [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2026-04-22.dahlia#invoice_object-payment_settings-payment_method_options), [Invoice.update().$params.payment_setting.payment_method_option](/api/invoices/update?api-version=2026-04-22.dahlia#update_invoice-payment_settings-payment_method_options), [Mandate.payment_method_details](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details), [SetupIntent.confirm().$params.payment_method_option](/api/setup_intents/confirm?api-version=2026-04-22.dahlia#confirm_setup_intent-payment_method_options), [SetupIntent.create().$params.payment_method_option](/api/setup_intents/create?api-version=2026-04-22.dahlia#create_setup_intent-payment_method_options), [SetupIntent.payment_method_options](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-payment_method_options), [SetupIntent.update().$params.payment_method_option](/api/setup_intents/update?api-version=2026-04-22.dahlia#update_setup_intent-payment_method_options), [Subscription.create().$params.payment_setting.payment_method_option](/api/subscriptions/create?api-version=2026-04-22.dahlia#create_subscription-payment_settings-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object-payment_settings-payment_method_options), [Subscription.update().$params.payment_setting.payment_method_option](/api/subscriptions/update?api-version=2026-04-22.dahlia#update_subscription-payment_settings-payment_method_options) |
| `amount`, `currency` | Added | [Mandate.multi_use](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-multi_use) |
| `pix_display_qr_code` | Added | [SetupIntent.next_action](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-next_action) |

| Value | Change | Enums |
| --- | --- | --- |
| `pix` | Added | [Invoice.payment_settings](/api/invoices/object?api-version=2026-04-22.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription.payment_settings](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object-payment_settings-payment_method_types) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Checkout.Session.payment_method_options.pix.setup_future_usage`, `Checkout\Session.create().$params.payment_method_option.pix.setup_future_usage`, `PaymentIntent.confirm().$params.payment_method_option.pix.setup_future_usage`, `PaymentIntent.create().$params.payment_method_option.pix.setup_future_usage`, `PaymentIntent.payment_method_options.pix.setup_future_usage`, `PaymentIntent.update().$params.payment_method_option.pix.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mandate` | Added | [Charge.payment_method_details.pix](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-pix), [PaymentAttemptRecord.payment_method_details.pix](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-pix), [PaymentRecord.payment_method_details.pix](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-pix) |
| `mandateOptions` | Added | [PaymentIntent.payment_method_options.pix](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-payment_method_options-pix), [PaymentIntentConfirmParams.payment_method_options.pix](/api/payment_intents/confirm?api-version=2026-04-22.dahlia#confirm_payment_intent-payment_method_options-pix), [PaymentIntentCreateParams.payment_method_options.pix](/api/payment_intents/create?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix), [PaymentIntentUpdateParams.payment_method_options.pix](/api/payment_intents/update?api-version=2026-04-22.dahlia#update_payment_intent-payment_method_options-pix), [checkout.Session.payment_method_options.pix](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object-payment_method_options-pix), [checkout.SessionCreateParams.payment_method_options.pix](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session-payment_method_options-pix) |
| `pix` | Added | [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2026-04-22.dahlia#invoice_object-payment_settings-payment_method_options), [InvoiceCreateParams.payment_settings.payment_method_options](/api/invoices/create?api-version=2026-04-22.dahlia#create-payment_settings-payment_method_options), [InvoiceUpdateParams.payment_settings.payment_method_options](/api/invoices/update?api-version=2026-04-22.dahlia#update_invoice-payment_settings-payment_method_options), [Mandate.payment_method_details](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details), [SetupIntent.payment_method_options](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-payment_method_options), [SetupIntentConfirmParams.payment_method_options](/api/setup_intents/confirm?api-version=2026-04-22.dahlia#confirm_setup_intent-payment_method_options), [SetupIntentCreateParams.payment_method_options](/api/setup_intents/create?api-version=2026-04-22.dahlia#create_setup_intent-payment_method_options), [SetupIntentUpdateParams.payment_method_options](/api/setup_intents/update?api-version=2026-04-22.dahlia#update_setup_intent-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object-payment_settings-payment_method_options), [SubscriptionCreateParams.payment_settings.payment_method_options](/api/subscriptions/create?api-version=2026-04-22.dahlia#create_subscription-payment_settings-payment_method_options), [SubscriptionUpdateParams.payment_settings.payment_method_options](/api/subscriptions/update?api-version=2026-04-22.dahlia#update_subscription-payment_settings-payment_method_options) |
| `amount`, `currency` | Added | [Mandate.multi_use](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-multi_use) |
| `pixDisplayQrCode` | Added | [SetupIntent.next_action](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-next_action) |

| Value | Change | Enums |
| --- | --- | --- |
| `pix` | Added | [InvoiceUpdateParams.payment_settings](/api/invoices/update?api-version=2026-04-22.dahlia#update_invoice-payment_settings-paymentMethodTypes), [InvoiceCreateParams.payment_settings](/api/invoices/create?api-version=2026-04-22.dahlia#create-payment_settings-paymentMethodTypes), [SubscriptionUpdateParams.payment_settings](/api/subscriptions/update?api-version=2026-04-22.dahlia#update_subscription-payment_settings-paymentMethodTypes), [SubscriptionCreateParams.payment_settings](/api/subscriptions/create?api-version=2026-04-22.dahlia#create_subscription-payment_settings-paymentMethodTypes) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentIntent.payment_method_options.pix.setupFutureUsage`, `PaymentIntentConfirmParams.payment_method_options.pix.setupFutureUsage`, `PaymentIntentCreateParams.payment_method_options.pix.setupFutureUsage`, `PaymentIntentUpdateParams.payment_method_options.pix.setupFutureUsage`, `checkout.Session.payment_method_options.pix.setupFutureUsage`, `checkout.SessionCreateParams.payment_method_options.pix.setupFutureUsage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mandate` | Added | [Charge.payment_method_details.pix](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-pix), [PaymentAttemptRecord.payment_method_details.pix](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-pix), [PaymentRecord.payment_method_details.pix](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-pix) |
| `mandate_options` | Added | [Checkout.Session.payment_method_options.pix](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object-payment_method_options-pix), [Checkout.SessionCreateParams.payment_method_options.pix](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session-payment_method_options-pix), [PaymentIntent.payment_method_options.pix](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-payment_method_options-pix), [PaymentIntentConfirmParams.payment_method_options.pix](/api/payment_intents/confirm?api-version=2026-04-22.dahlia#confirm_payment_intent-payment_method_options-pix), [PaymentIntentCreateParams.payment_method_options.pix](/api/payment_intents/create?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix), [PaymentIntentUpdateParams.payment_method_options.pix](/api/payment_intents/update?api-version=2026-04-22.dahlia#update_payment_intent-payment_method_options-pix) |
| `pix` | Added | [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2026-04-22.dahlia#invoice_object-payment_settings-payment_method_options), [InvoiceCreateParams.payment_settings.payment_method_options](/api/invoices/create?api-version=2026-04-22.dahlia#create-payment_settings-payment_method_options), [InvoiceUpdateParams.payment_settings.payment_method_options](/api/invoices/update?api-version=2026-04-22.dahlia#update_invoice-payment_settings-payment_method_options), [Mandate.payment_method_details](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details), [SetupIntent.payment_method_options](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-payment_method_options), [SetupIntentConfirmParams.payment_method_options](/api/setup_intents/confirm?api-version=2026-04-22.dahlia#confirm_setup_intent-payment_method_options), [SetupIntentCreateParams.payment_method_options](/api/setup_intents/create?api-version=2026-04-22.dahlia#create_setup_intent-payment_method_options), [SetupIntentUpdateParams.payment_method_options](/api/setup_intents/update?api-version=2026-04-22.dahlia#update_setup_intent-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object-payment_settings-payment_method_options), [SubscriptionCreateParams.payment_settings.payment_method_options](/api/subscriptions/create?api-version=2026-04-22.dahlia#create_subscription-payment_settings-payment_method_options), [SubscriptionUpdateParams.payment_settings.payment_method_options](/api/subscriptions/update?api-version=2026-04-22.dahlia#update_subscription-payment_settings-payment_method_options) |
| `amount`, `currency` | Added | [Mandate.multi_use](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-multi_use) |
| `pix_display_qr_code` | Added | [SetupIntent.next_action](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-next_action) |

| Value | Change | Enums |
| --- | --- | --- |
| `pix` | Added | [InvoiceUpdateParams.payment_settings](/api/invoices/update?api-version=2026-04-22.dahlia#update_invoice-payment_settings-payment_method_types), [InvoiceCreateParams.payment_settings](/api/invoices/create?api-version=2026-04-22.dahlia#create-payment_settings-payment_method_types), [Invoice.payment_settings](/api/invoices/object?api-version=2026-04-22.dahlia#invoice_object-payment_settings-payment_method_types), [SubscriptionUpdateParams.payment_settings](/api/subscriptions/update?api-version=2026-04-22.dahlia#update_subscription-payment_settings-payment_method_types), [SubscriptionCreateParams.payment_settings](/api/subscriptions/create?api-version=2026-04-22.dahlia#create_subscription-payment_settings-payment_method_types), [Subscription.payment_settings](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object-payment_settings-payment_method_types) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Checkout.Session.payment_method_options.pix.setup_future_usage`, `Checkout.SessionCreateParams.payment_method_options.pix.setup_future_usage`, `PaymentIntent.payment_method_options.pix.setup_future_usage`, `PaymentIntentConfirmParams.payment_method_options.pix.setup_future_usage`, `PaymentIntentCreateParams.payment_method_options.pix.setup_future_usage`, `PaymentIntentUpdateParams.payment_method_options.pix.setup_future_usage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Mandate` | Added | [ChargePaymentMethodDetailsPix](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-pix), [PaymentAttemptRecordPaymentMethodDetailsPix](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-pix), [PaymentRecordPaymentMethodDetailsPix](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-pix) |
| `MandateOptions` | Added | [CheckoutSessionPaymentMethodOptionsPix](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object-payment_method_options-pix), [CheckoutSessionPaymentMethodOptionsPixParams](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session-payment_method_options-pix), [PaymentIntentConfirmPaymentMethodOptionsPixParams](/api/payment_intents/confirm?api-version=2026-04-22.dahlia#confirm_payment_intent-payment_method_options-pix), [PaymentIntentPaymentMethodOptionsPix](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-payment_method_options-pix), [PaymentIntentPaymentMethodOptionsPixParams](/api/payment_intents/create?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix) |
| `Pix` | Added | [InvoicePaymentSettingsPaymentMethodOptions](/api/invoices/object?api-version=2026-04-22.dahlia#invoice_object-payment_settings-payment_method_options), [InvoicePaymentSettingsPaymentMethodOptionsParams](/api/invoices/update?api-version=2026-04-22.dahlia#update_invoice-payment_settings-payment_method_options), [MandatePaymentMethodDetails](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-payment_method_details), [SetupAttemptPaymentMethodDetails](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details), [SetupIntentConfirmPaymentMethodOptionsParams](/api/setup_intents/confirm?api-version=2026-04-22.dahlia#confirm_setup_intent-payment_method_options), [SetupIntentPaymentMethodOptions](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-payment_method_options), [SetupIntentPaymentMethodOptionsParams](/api/setup_intents/create?api-version=2026-04-22.dahlia#create_setup_intent-payment_method_options), [SubscriptionPaymentSettingsPaymentMethodOptions](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object-payment_settings-payment_method_options), [SubscriptionPaymentSettingsPaymentMethodOptionsParams](/api/subscriptions/update?api-version=2026-04-22.dahlia#update_subscription-payment_settings-payment_method_options) |
| `Amount`, `Currency` | Added | [MandateMultiUse](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-multi_use) |
| `PixDisplayQRCode` | Added | [SetupIntentNextAction](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-next_action) |

| Value | Change | Enums |
| --- | --- | --- |
| `pix` | Added | [InvoicePaymentSettings](/api/invoices/object?api-version=2026-04-22.dahlia#invoice_object-payment_settings-PaymentMethodTypes), [SubscriptionPaymentSettings](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object-payment_settings-PaymentMethodTypes) |

| Fields | Change | From → to |
| --- | --- | --- |
| `CheckoutSessionPaymentMethodOptionsPix.SetupFutureUsage`, `CheckoutSessionPaymentMethodOptionsPixParams.SetupFutureUsage`, `PaymentIntentConfirmPaymentMethodOptionsPixParams.SetupFutureUsage`, `PaymentIntentPaymentMethodOptionsPix.SetupFutureUsage`, `PaymentIntentPaymentMethodOptionsPixParams.SetupFutureUsage` | Changed | `literal('none') → enum('none'|'off_session')` |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Mandate` | Added | [Charge.PaymentMethodDetails.Pix](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-pix), [PaymentAttemptRecord.PaymentMethodDetails.Pix](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-pix), [PaymentRecord.PaymentMethodDetails.Pix](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-pix) |
| `MandateOptions` | Added | [Checkout.Session.PaymentMethodOptions.Pix](/api/checkout/sessions/object?api-version=2026-04-22.dahlia#checkout_session_object-payment_method_options-pix), [CheckoutSessionPaymentMethodOptionsPixOptions](/api/checkout/sessions/create?api-version=2026-04-22.dahlia#create_checkout_session-payment_method_options-pix), [PaymentIntent.PaymentMethodOptions.Pix](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-payment_method_options-pix), [PaymentIntentPaymentMethodOptionsPixOptions](/api/payment_intents/create?api-version=2026-04-22.dahlia#create_payment_intent-payment_method_options-pix) |
| `Pix` | Added | [Invoice.PaymentSettings.PaymentMethodOptions](/api/invoices/object?api-version=2026-04-22.dahlia#invoice_object-payment_settings-payment_method_options), [InvoicePaymentSettingsPaymentMethodOptionsOptions](/api/invoices/update?api-version=2026-04-22.dahlia#update_invoice-payment_settings-payment_method_options), [Mandate.PaymentMethodDetails](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-payment_method_details), [SetupAttempt.PaymentMethodDetails](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details), [SetupIntent.PaymentMethodOptions](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-payment_method_options), [SetupIntentPaymentMethodOptionsOptions](/api/setup_intents/create?api-version=2026-04-22.dahlia#create_setup_intent-payment_method_options), [Subscription.PaymentSettings.PaymentMethodOptions](/api/subscriptions/object?api-version=2026-04-22.dahlia#subscription_object-payment_settings-payment_method_options), [SubscriptionPaymentSettingsPaymentMethodOptionsOptions](/api/subscriptions/update?api-version=2026-04-22.dahlia#update_subscription-payment_settings-payment_method_options) |
| `Amount`, `Currency` | Added | [Mandate.MultiUse](/api/mandates/object?api-version=2026-04-22.dahlia#mandate_object-multi_use) |
| `PixDisplayQrCode` | Added | [SetupIntent.NextAction](/api/setup_intents/object?api-version=2026-04-22.dahlia#setup_intent_object-next_action) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Checkout.Session.PaymentMethodOptions.Pix.SetupFutureUsage`, `CheckoutSessionPaymentMethodOptionsPixOptions.SetupFutureUsage`, `PaymentIntent.PaymentMethodOptions.Pix.SetupFutureUsage`, `PaymentIntentPaymentMethodOptionsPixOptions.SetupFutureUsage` | Changed | `literal('none') → enum('none'|'off_session')` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-04-22.dahlia`
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

- [Adds support for Sunbit, a Buy Now, Pay Later payment method](https://docs.stripe.com/changelog/dahlia/2026-04-22/sunbit-buy-now-pay-later-support.md)
- [Adds the moto property to Setup Attempt payment method details for cards](https://docs.stripe.com/changelog/dahlia/2026-04-22/setup-attempt-payment-method-details-for-cards-moto.md)
- [Adds QR code support for Klarna payments with Terminal readers](https://docs.stripe.com/changelog/dahlia/2026-04-22/klarna-payments-with-terminal-readers-qr-code-support.md)
- [Adds support for Managed Payments, Stripe’s merchant of record solution](https://docs.stripe.com/changelog/dahlia/2026-04-22/managed-payments.md)
