# Adds support for Klarna in the hosted invoice page

## What’s new

Introduces support for Klarna on the [hosted invoice page](https://docs.stripe.com/invoicing/hosted-invoice-page.md). For dynamic payment methods, enable Klarna in your Dashboard payment method settings. Otherwise, include `klarna` in `payment_settings.payment_method_types` when creating a [Subscription](https://docs.stripe.com/api/subscriptions.md?api-version=2025-03-31.basil) or an [Invoice](https://docs.stripe.com/api/invoices.md?api-version=2025-03-31.basil) with `collection_method=send_invoice`.

## Impact

For [Subscriptions](https://docs.stripe.com/api/subscriptions.md?api-version=2025-03-31.basil) and [Invoices](https://docs.stripe.com/api/invoices.md?api-version=2025-03-31.basil) with `collection_method=send_invoice`, you can pass `klarna` to `payment_settings.payment_method_types`.

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `klarna` | Added | [Invoice#create.payment_settings.payment_method_types](/api/invoices/create?api-version=2025-03-31.basil#create_invoice-payment_settings-payment_method_types), [Invoice#update.payment_settings.payment_method_types](/api/invoices/update?api-version=2025-03-31.basil#update_invoice-payment_settings-payment_method_types), [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2025-03-31.basil#invoice_object-payment_settings-payment_method_types), [Subscription#create.payment_settings.payment_method_types](/api/subscriptions/create?api-version=2025-03-31.basil#create_subscription-payment_settings-payment_method_types), [Subscription#update.payment_settings.payment_method_types](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2025-03-31.basil#subscription_object-payment_settings-payment_method_types) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enums |
| --- | --- | --- |
| `klarna` | Added | [Invoice.CreateParamsPaymentSetting.payment_method_types](/api/invoices/create?api-version=2025-03-31.basil#create_invoice-payment_settings-payment_method_types), [Invoice.PaymentSetting.payment_method_types](/api/invoices/object?api-version=2025-03-31.basil#invoice_object-payment_settings-payment_method_types), [Invoice.UpdateParamsPaymentSetting.payment_method_types](/api/invoices/update?api-version=2025-03-31.basil#update_invoice-payment_settings-payment_method_types), [Subscription.CreateParamsPaymentSetting.payment_method_types](/api/subscriptions/create?api-version=2025-03-31.basil#create_subscription-payment_settings-payment_method_types), [Subscription.PaymentSetting.payment_method_types](/api/subscriptions/object?api-version=2025-03-31.basil#subscription_object-payment_settings-payment_method_types), [Subscription.UpdateParamsPaymentSetting.payment_method_types](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-payment_settings-payment_method_types) |

#### PHP

| Value | Change | Enums |
| --- | --- | --- |
| `klarna` | Added | [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2025-03-31.basil#invoice_object-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2025-03-31.basil#subscription_object-payment_settings-payment_method_types) |

#### Java

| Value | Change | Enums |
| --- | --- | --- |
| `klarna` | Added | [InvoiceCreateParams.payment_settings.paymentMethodTypes](/api/invoices/create?api-version=2025-03-31.basil#create_invoice-payment_settings-payment_method_types), [InvoiceUpdateParams.payment_settings.paymentMethodTypes](/api/invoices/update?api-version=2025-03-31.basil#update_invoice-payment_settings-payment_method_types), [SubscriptionCreateParams.payment_settings.paymentMethodTypes](/api/subscriptions/create?api-version=2025-03-31.basil#create_subscription-payment_settings-payment_method_types), [SubscriptionUpdateParams.payment_settings.paymentMethodTypes](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-payment_settings-payment_method_types) |

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `klarna` | Added | [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2025-03-31.basil#invoice_object-payment_settings-payment_method_types), [InvoiceCreateParams.payment_settings.payment_method_types](/api/invoices/create?api-version=2025-03-31.basil#create_invoice-payment_settings-payment_method_types), [InvoiceUpdateParams.payment_settings.payment_method_types](/api/invoices/update?api-version=2025-03-31.basil#update_invoice-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2025-03-31.basil#subscription_object-payment_settings-payment_method_types), [SubscriptionCreateParams.payment_settings.payment_method_types](/api/subscriptions/create?api-version=2025-03-31.basil#create_subscription-payment_settings-payment_method_types), [SubscriptionUpdateParams.payment_settings.payment_method_types](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-payment_settings-payment_method_types) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `klarna` | Added | [InvoicePaymentSettings.PaymentMethodTypes](/api/invoices/object?api-version=2025-03-31.basil#invoice_object-payment_settings-payment_method_types), [SubscriptionPaymentSettings.PaymentMethodTypes](/api/subscriptions/object?api-version=2025-03-31.basil#subscription_object-payment_settings-payment_method_types) |

#### .NET

This change doesn’t affect the .NET SDK.

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
- [Adds ability to configure saved payment methods for one-time payments on the hosted invoice page](https://docs.stripe.com/changelog/basil/2025-03-31/hosted-payment-method-save.md)
- [Adds support for saving and reusing Naver Pay payment methods](https://docs.stripe.com/changelog/basil/2025-03-31/naver-pay-recurring.md)
- [Adds support for the Billie local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/add-billie.md)
- [Adds support for the Satispay local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/satispay-lpm.md)
- [Makes the client parameter optional for WeChat Pay until confirmation](https://docs.stripe.com/changelog/basil/2025-03-31/lient-param-optional-wechatpay-before-confirmation.md)
- [Adds support for the New Zealand BECS Direct Debit local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/nz-bank-account.md)
