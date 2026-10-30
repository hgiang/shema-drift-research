# Adds Blik as a supported payment method for recurring payments in Stripe Billing

## What’s new

> BLIK recurring payments for Stripe Billing requires account-level enablement. Contact [Stripe support](https://support.stripe.com/contact) to request access for your account.

Adds support for [BLIK](https://docs.stripe.com/payments/blik.md) as a payment method for recurring payments in [Stripe Billing](https://docs.stripe.com/billing.md). You can use BLIK with [Subscriptions](https://docs.stripe.com/api/subscriptions.md?api-version=2026-04-22.preview), [Invoices](https://docs.stripe.com/api/invoices.md?api-version=2026-04-22.preview) and [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md?api-version=2026-04-22.preview) for off-session recurring payments in Poland.

This implementation uses flexible mandates ([Model O](https://www.blik.com/lp/reccuring-payments/Model-O.141951072.html)) that allow variable payment amounts up to 2000 PLN per transaction. When you create a subscription or invoice with BLIK, customers can authorise recurring payments through the [mandate_options](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-04-22.preview#create_checkout_session-payment_method_options-blik-mandate_options) parameter.

This payment method is available in Poland with PLN currency only.

## Impact

You can offer Polish customers the ability to pay for subscriptions and recurring invoices using BLIK, a popular mobile payment method in Poland. This increases payment options for businesses operating in the Polish market and can help decrease payment friction for local customers.

To use BLIK for recurring payments, add `blik` to the [payment_method_types](https://docs.stripe.com/api/subscriptions/create.md?api-version=2026-04-22.preview#create_subscription-payment_settings-payment_method_types) parameter when creating subscriptions or include it in your [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-04-22.preview#create_checkout_session-payment_method_types) configuration. Configure the [expires_after](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-04-22.preview#create_checkout_session-payment_method_options-blik-mandate_options-expires_after) parameter to set how long the recurring payment authorisation remains valid, if not perpetual.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `blik` | Added | [Invoice#update.payment_settings.payment_method_options](/api/invoices/update?api-version=2026-04-22.preview#update_invoice-payment_settings-payment_method_options), [Subscription#update.payment_settings.payment_method_options](/api/subscriptions/update?api-version=2026-04-22.preview#update_subscription-payment_settings-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2026-04-22.preview#subscription_object-payment_settings-payment_method_options), [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2026-04-22.preview#invoice_object-payment_settings-payment_method_options), [Subscription#create.payment_settings.payment_method_options](/api/subscriptions/create?api-version=2026-04-22.preview#create_subscription-payment_settings-payment_method_options), [Checkout.Session#create.payment_method_options](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session-payment_method_options), [Invoice#create.payment_settings.payment_method_options](/api/invoices/create?api-version=2026-04-22.preview#create-payment_settings-payment_method_options) |

| Value | Change | Enums |
| --- | --- | --- |
| `blik` | Added | [Invoice#update.payment_settings](/api/invoices/update?api-version=2026-04-22.preview#update_invoice-payment_settings-payment_method_types), [Invoice#create.payment_settings](/api/invoices/create?api-version=2026-04-22.preview#create-payment_settings-payment_method_types), [Invoice.payment_settings](/api/invoices/object?api-version=2026-04-22.preview#invoice_object-payment_settings-payment_method_types), [Subscription#create.payment_settings](/api/subscriptions/create?api-version=2026-04-22.preview#create_subscription-payment_settings-payment_method_types), [Subscription#update.payment_settings](/api/subscriptions/update?api-version=2026-04-22.preview#update_subscription-payment_settings-payment_method_types), [Subscription.payment_settings](/api/subscriptions/object?api-version=2026-04-22.preview#subscription_object-payment_settings-payment_method_types) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `blik` | Added | [Checkout::SessionCreateParams::PaymentMethodOption](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session-payment_method_options), [InvoiceCreateParams::PaymentSetting::PaymentMethodOption](/api/invoices/create?api-version=2026-04-22.preview#create-payment_settings-payment_method_options), [Invoice::PaymentSetting::PaymentMethodOption](/api/invoices/object?api-version=2026-04-22.preview#invoice_object-payment_settings-payment_method_options), [SubscriptionUpdateParams::PaymentSetting::PaymentMethodOption](/api/subscriptions/update?api-version=2026-04-22.preview#update_subscription-payment_settings-payment_method_options), [SubscriptionCreateParams::PaymentSetting::PaymentMethodOption](/api/subscriptions/create?api-version=2026-04-22.preview#create_subscription-payment_settings-payment_method_options), [Subscription::PaymentSetting::PaymentMethodOption](/api/subscriptions/object?api-version=2026-04-22.preview#subscription_object-payment_settings-payment_method_options), [InvoiceUpdateParams::PaymentSetting::PaymentMethodOption](/api/invoices/update?api-version=2026-04-22.preview#update_invoice-payment_settings-payment_method_options) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `blik` | Added | [Invoice.PaymentSetting.PaymentMethodOption](/api/invoices/object?api-version=2026-04-22.preview#invoice_object-payment_settings-payment_method_options), [InvoiceCreateParamsPaymentSettingPaymentMethodOption](/api/invoices/create?api-version=2026-04-22.preview#create-payment_settings-payment_method_options), [checkout.SessionCreateParamsPaymentMethodOption](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session-payment_method_options), [Subscription.PaymentSetting.PaymentMethodOption](/api/subscriptions/object?api-version=2026-04-22.preview#subscription_object-payment_settings-payment_method_options), [SubscriptionModifyParamsPaymentSettingPaymentMethodOption](/api/subscriptions/update?api-version=2026-04-22.preview#update_subscription-payment_settings-payment_method_options), [InvoiceModifyParamsPaymentSettingPaymentMethodOption](/api/invoices/update?api-version=2026-04-22.preview#update_invoice-payment_settings-payment_method_options), [SubscriptionCreateParamsPaymentSettingPaymentMethodOption](/api/subscriptions/create?api-version=2026-04-22.preview#create_subscription-payment_settings-payment_method_options) |

| Value | Change | Enums |
| --- | --- | --- |
| `blik` | Added | [SubscriptionCreateParamsPaymentSetting](/api/subscriptions/create?api-version=2026-04-22.preview#create_subscription-payment_settings-payment_method_types), [InvoiceModifyParamsPaymentSetting](/api/invoices/update?api-version=2026-04-22.preview#update_invoice-payment_settings-payment_method_types), [Subscription.PaymentSetting](/api/subscriptions/object?api-version=2026-04-22.preview#subscription_object-payment_settings-payment_method_types), [InvoiceCreateParamsPaymentSetting](/api/invoices/create?api-version=2026-04-22.preview#create-payment_settings-payment_method_types), [Invoice.PaymentSetting](/api/invoices/object?api-version=2026-04-22.preview#invoice_object-payment_settings-payment_method_types), [SubscriptionModifyParamsPaymentSetting](/api/subscriptions/update?api-version=2026-04-22.preview#update_subscription-payment_settings-payment_method_types) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `blik` | Added | [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2026-04-22.preview#invoice_object-payment_settings-payment_method_options), [Checkout\Session.create().$params.payment_method_option](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session-payment_method_options), [Invoice.update().$params.payment_setting.payment_method_option](/api/invoices/update?api-version=2026-04-22.preview#update_invoice-payment_settings-payment_method_options), [Subscription.create().$params.payment_setting.payment_method_option](/api/subscriptions/create?api-version=2026-04-22.preview#create_subscription-payment_settings-payment_method_options), [Subscription.update().$params.payment_setting.payment_method_option](/api/subscriptions/update?api-version=2026-04-22.preview#update_subscription-payment_settings-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2026-04-22.preview#subscription_object-payment_settings-payment_method_options), [Invoice.create().$params.payment_setting.payment_method_option](/api/invoices/create?api-version=2026-04-22.preview#create-payment_settings-payment_method_options) |

| Value | Change | Enums |
| --- | --- | --- |
| `blik` | Added | [Subscription.payment_settings](/api/subscriptions/object?api-version=2026-04-22.preview#subscription_object-payment_settings-payment_method_types), [Invoice.payment_settings](/api/invoices/object?api-version=2026-04-22.preview#invoice_object-payment_settings-payment_method_types) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `blik` | Added | [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2026-04-22.preview#invoice_object-payment_settings-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2026-04-22.preview#subscription_object-payment_settings-payment_method_options), [SubscriptionUpdateParams.payment_settings.payment_method_options](/api/subscriptions/update?api-version=2026-04-22.preview#update_subscription-payment_settings-payment_method_options), [InvoiceCreateParams.payment_settings.payment_method_options](/api/invoices/create?api-version=2026-04-22.preview#create-payment_settings-payment_method_options), [InvoiceUpdateParams.payment_settings.payment_method_options](/api/invoices/update?api-version=2026-04-22.preview#update_invoice-payment_settings-payment_method_options), [checkout.SessionCreateParams.payment_method_options](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session-payment_method_options), [SubscriptionCreateParams.payment_settings.payment_method_options](/api/subscriptions/create?api-version=2026-04-22.preview#create_subscription-payment_settings-payment_method_options) |

| Value | Change | Enums |
| --- | --- | --- |
| `blik` | Added | [SubscriptionUpdateParams.payment_settings](/api/subscriptions/update?api-version=2026-04-22.preview#update_subscription-payment_settings-paymentMethodTypes), [SubscriptionCreateParams.payment_settings](/api/subscriptions/create?api-version=2026-04-22.preview#create_subscription-payment_settings-paymentMethodTypes), [InvoiceUpdateParams.payment_settings](/api/invoices/update?api-version=2026-04-22.preview#update_invoice-payment_settings-paymentMethodTypes), [InvoiceCreateParams.payment_settings](/api/invoices/create?api-version=2026-04-22.preview#create-payment_settings-paymentMethodTypes) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `blik` | Added | [InvoiceCreateParams.payment_settings.payment_method_options](/api/invoices/create?api-version=2026-04-22.preview#create-payment_settings-payment_method_options), [SubscriptionCreateParams.payment_settings.payment_method_options](/api/subscriptions/create?api-version=2026-04-22.preview#create_subscription-payment_settings-payment_method_options), [SubscriptionUpdateParams.payment_settings.payment_method_options](/api/subscriptions/update?api-version=2026-04-22.preview#update_subscription-payment_settings-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2026-04-22.preview#subscription_object-payment_settings-payment_method_options), [Checkout.SessionCreateParams.payment_method_options](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session-payment_method_options), [InvoiceUpdateParams.payment_settings.payment_method_options](/api/invoices/update?api-version=2026-04-22.preview#update_invoice-payment_settings-payment_method_options), [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2026-04-22.preview#invoice_object-payment_settings-payment_method_options) |

| Value | Change | Enums |
| --- | --- | --- |
| `blik` | Added | [InvoiceUpdateParams.payment_settings](/api/invoices/update?api-version=2026-04-22.preview#update_invoice-payment_settings-payment_method_types), [SubscriptionCreateParams.payment_settings](/api/subscriptions/create?api-version=2026-04-22.preview#create_subscription-payment_settings-payment_method_types), [Subscription.payment_settings](/api/subscriptions/object?api-version=2026-04-22.preview#subscription_object-payment_settings-payment_method_types), [InvoiceCreateParams.payment_settings](/api/invoices/create?api-version=2026-04-22.preview#create-payment_settings-payment_method_types), [Invoice.payment_settings](/api/invoices/object?api-version=2026-04-22.preview#invoice_object-payment_settings-payment_method_types), [SubscriptionUpdateParams.payment_settings](/api/subscriptions/update?api-version=2026-04-22.preview#update_subscription-payment_settings-payment_method_types) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `BLIK` | Added | [InvoicePaymentSettingsPaymentMethodOptionsParams](/api/invoices/update?api-version=2026-04-22.preview#update_invoice-payment_settings-payment_method_options), [SubscriptionPaymentSettingsPaymentMethodOptions](/api/subscriptions/object?api-version=2026-04-22.preview#subscription_object-payment_settings-payment_method_options), [CheckoutSessionPaymentMethodOptionsParams](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session-payment_method_options), [SubscriptionPaymentSettingsPaymentMethodOptionsParams](/api/subscriptions/update?api-version=2026-04-22.preview#update_subscription-payment_settings-payment_method_options), [InvoicePaymentSettingsPaymentMethodOptions](/api/invoices/object?api-version=2026-04-22.preview#invoice_object-payment_settings-payment_method_options) |

| Value | Change | Enums |
| --- | --- | --- |
| `blik` | Added | [InvoicePaymentSettings](/api/invoices/object?api-version=2026-04-22.preview#invoice_object-payment_settings-PaymentMethodTypes), [SubscriptionPaymentSettings](/api/subscriptions/object?api-version=2026-04-22.preview#subscription_object-payment_settings-PaymentMethodTypes) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Blik` | Added | [InvoicePaymentSettingsPaymentMethodOptionsOptions](/api/invoices/update?api-version=2026-04-22.preview#update_invoice-payment_settings-payment_method_options), [Subscription.PaymentSettings.PaymentMethodOptions](/api/subscriptions/object?api-version=2026-04-22.preview#subscription_object-payment_settings-payment_method_options), [SubscriptionPaymentSettingsPaymentMethodOptionsOptions](/api/subscriptions/update?api-version=2026-04-22.preview#update_subscription-payment_settings-payment_method_options), [CheckoutSessionPaymentMethodOptionsOptions](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session-payment_method_options), [Invoice.PaymentSettings.PaymentMethodOptions](/api/invoices/object?api-version=2026-04-22.preview#invoice_object-payment_settings-payment_method_options) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-04-22.preview`
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

- [Adds validation for billing meter event values with more than 15 digits](https://docs.stripe.com/changelog/dahlia/2026-04-22/billing-meter-event-values-validation.md)
