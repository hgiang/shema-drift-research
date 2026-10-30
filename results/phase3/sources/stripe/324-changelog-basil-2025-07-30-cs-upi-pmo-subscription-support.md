# Adds UPI support to the Subscriptions API

## What’s new

You can now customize [UPI mandates](https://docs.stripe.com/payments/upi.md) by specifying the `upi` [payment_method_options](https://docs.stripe.com/api/subscriptions/object.md?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_options) for the [Subscriptions](https://docs.stripe.com/api/subscriptions.md?api-version=2025-07-30.preview) and [Invoices](https://docs.stripe.com/api/invoices.md?api-version=2025-07-30.preview) APIs.

## Impact

When you specify [mandate_options](https://docs.stripe.com/api/subscriptions/object.md?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_options-upi-mandate_options) to configure UPI eMandates for Stripe invoices, you can now customise how the mandates appear to your customers. This includes the description, expiration date, maximum amount, and more.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `upi` | Added | [Invoice#create.payment_settings.payment_method_options](/api/invoices/create?api-version=2025-07-30.preview#create_invoice-payment_settings-payment_method_options), [Invoice#update.payment_settings.payment_method_options](/api/invoices/update?api-version=2025-07-30.preview#update_invoice-payment_settings-payment_method_options), [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [QuotePreviewInvoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [Subscription#create.payment_settings.payment_method_options](/api/subscriptions/create?api-version=2025-07-30.preview#create_subscription-payment_settings-payment_method_options-upi), [Subscription#update.payment_settings.payment_method_options](/api/subscriptions/update?api-version=2025-07-30.preview#update_subscription-payment_settings-payment_method_options-upi), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_options-upi) |

| Value | Change | Enums |
| --- | --- | --- |
| `upi` | Added | [Invoice#create.payment_settings.payment_method_types](/api/invoices/create?api-version=2025-07-30.preview#create_invoice-payment_settings-payment_method_types), [Invoice#update.payment_settings.payment_method_types](/api/invoices/update?api-version=2025-07-30.preview#update_invoice-payment_settings-payment_method_types), [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_types), [QuotePreviewInvoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_types), [Subscription#create.payment_settings.payment_method_types](/api/subscriptions/create?api-version=2025-07-30.preview#create_subscription-payment_settings-payment_method_types), [Subscription#update.payment_settings.payment_method_types](/api/subscriptions/update?api-version=2025-07-30.preview#update_subscription-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_types) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `upi` | Added | [Invoice::CreateParams::PaymentSetting::PaymentMethodOption](/api/invoices/create?api-version=2025-07-30.preview#create_invoice-payment_settings-payment_method_options), [Invoice::PaymentSetting::PaymentMethodOption](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [Invoice::UpdateParams::PaymentSetting::PaymentMethodOption](/api/invoices/update?api-version=2025-07-30.preview#update_invoice-payment_settings-payment_method_options), [QuotePreviewInvoice::PaymentSetting::PaymentMethodOption](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [Subscription::CreateParams::PaymentSetting::PaymentMethodOption](/api/subscriptions/create?api-version=2025-07-30.preview#create_subscription-payment_settings-payment_method_options-upi), [Subscription::PaymentSetting::PaymentMethodOption](/api/subscriptions/object?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_options-upi), [Subscription::UpdateParams::PaymentSetting::PaymentMethodOption](/api/subscriptions/update?api-version=2025-07-30.preview#update_subscription-payment_settings-payment_method_options-upi) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `upi` | Added | [Invoice.CreateParamsPaymentSettingPaymentMethodOption](/api/invoices/create?api-version=2025-07-30.preview#create_invoice-payment_settings-payment_method_options), [Invoice.ModifyParamsPaymentSettingPaymentMethodOption](/api/invoices/update?api-version=2025-07-30.preview#update_invoice-payment_settings-payment_method_options), [Invoice.PaymentSetting.PaymentMethodOption](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [QuotePreviewInvoice.PaymentSetting.PaymentMethodOption](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [Subscription.CreateParamsPaymentSettingPaymentMethodOption](/api/subscriptions/create?api-version=2025-07-30.preview#create_subscription-payment_settings-payment_method_options-upi), [Subscription.ModifyParamsPaymentSettingPaymentMethodOption](/api/subscriptions/update?api-version=2025-07-30.preview#update_subscription-payment_settings-payment_method_options-upi), [Subscription.PaymentSetting.PaymentMethodOption](/api/subscriptions/object?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_options-upi) |

| Value | Change | Enums |
| --- | --- | --- |
| `upi` | Added | [Invoice.CreateParamsPaymentSetting.payment_method_types](/api/invoices/create?api-version=2025-07-30.preview#create_invoice-payment_settings-payment_method_types), [Invoice.ModifyParamsPaymentSetting.payment_method_types](/api/invoices/update?api-version=2025-07-30.preview#update_invoice-payment_settings-payment_method_types), [Invoice.PaymentSetting.payment_method_types](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_types), [QuotePreviewInvoice.PaymentSetting.payment_method_types](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_types), [Subscription.CreateParamsPaymentSetting.payment_method_types](/api/subscriptions/create?api-version=2025-07-30.preview#create_subscription-payment_settings-payment_method_types), [Subscription.ModifyParamsPaymentSetting.payment_method_types](/api/subscriptions/update?api-version=2025-07-30.preview#update_subscription-payment_settings-payment_method_types), [Subscription.PaymentSetting.payment_method_types](/api/subscriptions/object?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_types) |

#### PHP

| Value | Change | Enums |
| --- | --- | --- |
| `upi` | Added | [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_types), [QuotePreviewInvoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_types) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `upi` | Added | [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [InvoiceCreateParams.payment_settings.payment_method_options](/api/invoices/create?api-version=2025-07-30.preview#create_invoice-payment_settings-payment_method_options), [InvoiceUpdateParams.payment_settings.payment_method_options](/api/invoices/update?api-version=2025-07-30.preview#update_invoice-payment_settings-payment_method_options), [QuotePreviewInvoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_options-upi), [SubscriptionCreateParams.payment_settings.payment_method_options](/api/subscriptions/create?api-version=2025-07-30.preview#create_subscription-payment_settings-payment_method_options-upi), [SubscriptionUpdateParams.payment_settings.payment_method_options](/api/subscriptions/update?api-version=2025-07-30.preview#update_subscription-payment_settings-payment_method_options-upi) |

| Value | Change | Enums |
| --- | --- | --- |
| `upi` | Added | [InvoiceCreateParams.payment_settings.paymentMethodTypes](/api/invoices/create?api-version=2025-07-30.preview#create_invoice-payment_settings-payment_method_types), [InvoiceUpdateParams.payment_settings.paymentMethodTypes](/api/invoices/update?api-version=2025-07-30.preview#update_invoice-payment_settings-payment_method_types), [SubscriptionCreateParams.payment_settings.paymentMethodTypes](/api/subscriptions/create?api-version=2025-07-30.preview#create_subscription-payment_settings-payment_method_types), [SubscriptionUpdateParams.payment_settings.paymentMethodTypes](/api/subscriptions/update?api-version=2025-07-30.preview#update_subscription-payment_settings-payment_method_types) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `upi` | Added | [Invoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [InvoiceCreateParams.payment_settings.payment_method_options](/api/invoices/create?api-version=2025-07-30.preview#create_invoice-payment_settings-payment_method_options), [InvoiceUpdateParams.payment_settings.payment_method_options](/api/invoices/update?api-version=2025-07-30.preview#update_invoice-payment_settings-payment_method_options), [QuotePreviewInvoice.payment_settings.payment_method_options](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [Subscription.payment_settings.payment_method_options](/api/subscriptions/object?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_options-upi), [SubscriptionCreateParams.payment_settings.payment_method_options](/api/subscriptions/create?api-version=2025-07-30.preview#create_subscription-payment_settings-payment_method_options-upi), [SubscriptionUpdateParams.payment_settings.payment_method_options](/api/subscriptions/update?api-version=2025-07-30.preview#update_subscription-payment_settings-payment_method_options-upi) |

| Value | Change | Enums |
| --- | --- | --- |
| `upi` | Added | [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_types), [InvoiceCreateParams.payment_settings.payment_method_types](/api/invoices/create?api-version=2025-07-30.preview#create_invoice-payment_settings-payment_method_types), [InvoiceUpdateParams.payment_settings.payment_method_types](/api/invoices/update?api-version=2025-07-30.preview#update_invoice-payment_settings-payment_method_types), [QuotePreviewInvoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_types), [SubscriptionCreateParams.payment_settings.payment_method_types](/api/subscriptions/create?api-version=2025-07-30.preview#create_subscription-payment_settings-payment_method_types), [SubscriptionUpdateParams.payment_settings.payment_method_types](/api/subscriptions/update?api-version=2025-07-30.preview#update_subscription-payment_settings-payment_method_types) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Upi` | Added | [InvoicePaymentSettingsPaymentMethodOptions](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [InvoicePaymentSettingsPaymentMethodOptionsParams](/api/invoices/create?api-version=2025-07-30.preview#create_invoice-payment_settings-payment_method_options), [QuotePreviewInvoicePaymentSettingsPaymentMethodOptions](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [SubscriptionPaymentSettingsPaymentMethodOptions](/api/subscriptions/object?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_options-upi), [SubscriptionPaymentSettingsPaymentMethodOptionsParams](/api/subscriptions/create?api-version=2025-07-30.preview#create_subscription-payment_settings-payment_method_options-upi) |

| Value | Change | Enums |
| --- | --- | --- |
| `upi` | Added | [InvoicePaymentSettings.PaymentMethodTypes](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_types), [QuotePreviewInvoicePaymentSettings.PaymentMethodTypes](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_types), [SubscriptionPaymentSettings.PaymentMethodTypes](/api/subscriptions/object?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_types) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Upi` | Added | [Invoice.PaymentSettings.PaymentMethodOptions](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [InvoicePaymentSettingsPaymentMethodOptionsOptions](/api/invoices/create?api-version=2025-07-30.preview#create_invoice-payment_settings-payment_method_options), [QuotePreviewInvoice.PaymentSettings.PaymentMethodOptions](/api/invoices/object?api-version=2025-07-30.preview#invoice_object-payment_settings-payment_method_options), [Subscription.PaymentSettings.PaymentMethodOptions](/api/subscriptions/object?api-version=2025-07-30.preview#subscription_object-payment_settings-payment_method_options-upi), [SubscriptionPaymentSettingsPaymentMethodOptionsOptions](/api/subscriptions/create?api-version=2025-07-30.preview#create_subscription-payment_settings-payment_method_options-upi) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-07-30.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.5.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v15.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.5.0b1](https://github.com/stripe/stripe-python/releases/tag/v12.5.0b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.6.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v17.6.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.5.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v29.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.5.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v18.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.5.0-beta.1](https://github.com/stripe/stripe-go/releases/tag/v82.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.5.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v48.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
