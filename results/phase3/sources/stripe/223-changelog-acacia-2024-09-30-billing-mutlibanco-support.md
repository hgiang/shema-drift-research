# Adds support for using the Multibanco payment method with billing

## What’s new

Adds the Multibanco payment method as an available option in invoices and subscriptions.

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `multibanco` | Added | [Invoice#create.payment_settings.payment_method_types[]](/api/invoices/create?api-version=2024-09-30.acacia#create_invoice-payment_settings-payment_method_types), [Invoice#update.payment_settings.payment_method_types[]](/api/invoices/update?api-version=2024-09-30.acacia#update_invoice-payment_settings-payment_method_types), [Invoice.payment_settings.payment_method_types[]](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-payment_settings-payment_method_types), [Subscription#create.payment_settings.payment_method_types[]](/api/subscriptions/create?api-version=2024-09-30.acacia#create_subscription-payment_settings-payment_method_types), [Subscription#update.payment_settings.payment_method_types[]](/api/subscriptions/update?api-version=2024-09-30.acacia#update_subscription-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types[]](/api/subscriptions/object?api-version=2024-09-30.acacia#subscription_object-payment_settings-payment_method_types) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enums |
| --- | --- | --- |
| `multibanco` | Added | [stripe.Invoice.PaymentSettings.payment_method_types](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-payment_settings-payment_method_types), [stripe.Invoice.CreateParamsPaymentSettings.payment_method_types](/api/invoices/create?api-version=2024-09-30.acacia#create_invoice-payment_settings-payment_method_types), [stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types](/api/invoices/update?api-version=2024-09-30.acacia#update_invoice-payment_settings-payment_method_types), [stripe.Subscription.PaymentSettings.payment_method_types](/api/subscriptions/object?api-version=2024-09-30.acacia#subscription_object-payment_settings-payment_method_types), [stripe.Subscription.CreateParamsPaymentSettings.payment_method_types](/api/subscriptions/create?api-version=2024-09-30.acacia#create_subscription-payment_settings-payment_method_types), [stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types](/api/subscriptions/update?api-version=2024-09-30.acacia#update_subscription-payment_settings-payment_method_types) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Value | Change | Enums |
| --- | --- | --- |
| `multibanco` | Added | [InvoiceCreateParams.payment_settings.payment_method_types[]](/api/invoices/create?api-version=2024-09-30.acacia#create_invoice-payment_settings-payment_method_types), [InvoiceUpdateParams.payment_settings.payment_method_types[]](/api/invoices/update?api-version=2024-09-30.acacia#update_invoice-payment_settings-payment_method_types), [SubscriptionCreateParams.payment_settings.payment_method_types[]](/api/subscriptions/create?api-version=2024-09-30.acacia#create_subscription-payment_settings-payment_method_types), [SubscriptionUpdateParams.payment_settings.payment_method_types[]](/api/subscriptions/update?api-version=2024-09-30.acacia#update_subscription-payment_settings-payment_method_types) |

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `multibanco` | Added | [Invoice.payment_settings.payment_method_types[]](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-payment_settings-payment_method_types), [InvoiceCreateParams.payment_settings.payment_method_types[]](/api/invoices/create?api-version=2024-09-30.acacia#create_invoice-payment_settings-payment_method_types), [InvoiceUpdateParams.payment_settings.payment_method_types[]](/api/invoices/update?api-version=2024-09-30.acacia#update_invoice-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types[]](/api/subscriptions/object?api-version=2024-09-30.acacia#subscription_object-payment_settings-payment_method_types), [SubscriptionCreateParams.payment_settings.payment_method_types[]](/api/subscriptions/create?api-version=2024-09-30.acacia#create_subscription-payment_settings-payment_method_types), [SubscriptionUpdateParams.payment_settings.payment_method_types[]](/api/subscriptions/update?api-version=2024-09-30.acacia#update_subscription-payment_settings-payment_method_types) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `multibanco` | Added | [InvoicePaymentSettingsPaymentMethodTypes](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-payment_settings-payment_method_types), [SubscriptionPaymentSettingsPaymentMethodTypes](/api/subscriptions/object?api-version=2024-09-30.acacia#subscription_object-payment_settings-payment_method_types) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-09-30.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.0.0](https://github.com/stripe/stripe-python/releases/tag/v11.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.0.0](https://github.com/stripe/stripe-php/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v27.0.0](https://github.com/stripe/stripe-java/releases/tag/v27.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.0.0](https://github.com/stripe/stripe-node/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v80.0.0](https://github.com/stripe/stripe-go/releases/tag/v80.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v46.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v46.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds support for three new payment methods: Multibanco, Twint, and Zip](https://docs.stripe.com/changelog/acacia/2024-09-30/payment-links-new-payment-methods.md)
- [Adds Twint to the PaymentMethodConfiguration API](https://docs.stripe.com/changelog/acacia/2024-09-30/twint-support-payment-method-configuration.md)
- [Adds Girocard as a PaymentMethod brand and network](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-girocard-paymentmethod-brand-network.md)
