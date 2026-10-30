# Adds Alipay support for invoices and subscriptions that send invoices for collection

## What’s new

Adds support for using `alipay` as a value for the `payment_settings.payment_method_types` parameter on [Invoices](https://docs.stripe.com/api/invoices/object.md?api-version=2026-07-29.dahlia#invoice_object-payment_settings-payment_method_types) and [Subscriptions](https://docs.stripe.com/api/subscriptions/object.md?api-version=2026-07-29.dahlia#subscription_object-payment_settings-payment_method_types). For both Invoice and Subscription objects, this payment method type is only supported when `collection_method` is `send_invoice`.

## Impact

You can now accept [Alipay](https://docs.stripe.com/payments/alipay.md) as a payment method type for invoices and subscriptions. If you have existing invoices or subscriptions that should accept Alipay, update `payment_settings.payment_method_types` for the [Invoice](https://docs.stripe.com/api/invoices/update.md?api-version=2026-07-29.dahlia) or [Subscription](https://docs.stripe.com/api/subscriptions/update.md?api-version=2026-07-29.dahlia) object.

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `alipay` | Added | [Invoice#update.payment_settings.payment_method_types](/api/invoices/update?api-version=2026-07-29.dahlia#update_invoice-payment_settings-payment_method_types), [Invoice#create.payment_settings.payment_method_types](/api/invoices/create?api-version=2026-07-29.dahlia#create-payment_settings-payment_method_types), [Subscription#update.payment_settings.payment_method_types](/api/subscriptions/update?api-version=2026-07-29.dahlia#update_subscription-payment_settings-payment_method_types), [Subscription#create.payment_settings.payment_method_types](/api/subscriptions/create?api-version=2026-07-29.dahlia#create_subscription-payment_settings-payment_method_types), [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2026-07-29.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2026-07-29.dahlia#subscription_object-payment_settings-payment_method_types) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enums |
| --- | --- | --- |
| `alipay` | Added | [InvoiceModifyParamsPaymentSetting.payment_method_types](/api/invoices/update?api-version=2026-07-29.dahlia#update_invoice-payment_settings-payment_method_types), [InvoiceCreateParamsPaymentSetting.payment_method_types](/api/invoices/create?api-version=2026-07-29.dahlia#create-payment_settings-payment_method_types), [SubscriptionModifyParamsPaymentSetting.payment_method_types](/api/subscriptions/update?api-version=2026-07-29.dahlia#update_subscription-payment_settings-payment_method_types), [SubscriptionCreateParamsPaymentSetting.payment_method_types](/api/subscriptions/create?api-version=2026-07-29.dahlia#create_subscription-payment_settings-payment_method_types), [Invoice.PaymentSetting.payment_method_types](/api/invoices/object?api-version=2026-07-29.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription.PaymentSetting.payment_method_types](/api/subscriptions/object?api-version=2026-07-29.dahlia#subscription_object-payment_settings-payment_method_types) |

#### PHP

| Value | Change | Enums |
| --- | --- | --- |
| `alipay` | Added | [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2026-07-29.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2026-07-29.dahlia#subscription_object-payment_settings-payment_method_types) |

#### Java

| Value | Change | Enums |
| --- | --- | --- |
| `alipay` | Added | [InvoiceUpdateParams.payment_settings.paymentMethodTypes](/api/invoices/update?api-version=2026-07-29.dahlia#update_invoice-payment_settings-paymentMethodTypes), [InvoiceCreateParams.payment_settings.paymentMethodTypes](/api/invoices/create?api-version=2026-07-29.dahlia#create-payment_settings-paymentMethodTypes), [SubscriptionUpdateParams.payment_settings.paymentMethodTypes](/api/subscriptions/update?api-version=2026-07-29.dahlia#update_subscription-payment_settings-paymentMethodTypes), [SubscriptionCreateParams.payment_settings.paymentMethodTypes](/api/subscriptions/create?api-version=2026-07-29.dahlia#create_subscription-payment_settings-paymentMethodTypes) |

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `alipay` | Added | [InvoiceUpdateParams.payment_settings.payment_method_types](/api/invoices/update?api-version=2026-07-29.dahlia#update_invoice-payment_settings-payment_method_types), [InvoiceCreateParams.payment_settings.payment_method_types](/api/invoices/create?api-version=2026-07-29.dahlia#create-payment_settings-payment_method_types), [SubscriptionUpdateParams.payment_settings.payment_method_types](/api/subscriptions/update?api-version=2026-07-29.dahlia#update_subscription-payment_settings-payment_method_types), [SubscriptionCreateParams.payment_settings.payment_method_types](/api/subscriptions/create?api-version=2026-07-29.dahlia#create_subscription-payment_settings-payment_method_types), [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2026-07-29.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2026-07-29.dahlia#subscription_object-payment_settings-payment_method_types) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `alipay` | Added | [InvoicePaymentSettings.PaymentMethodTypes](/api/invoices/object?api-version=2026-07-29.dahlia#invoice_object-payment_settings-PaymentMethodTypes), [SubscriptionPaymentSettings.PaymentMethodTypes](/api/subscriptions/object?api-version=2026-07-29.dahlia#subscription_object-payment_settings-PaymentMethodTypes) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-07-29.dahlia`
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
