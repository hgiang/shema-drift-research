# Adds reference and company details parameters for Billie

## What’s new

Adds two optional parameters to the [Billie](https://docs.stripe.com/payments/billie.md) payment method:

- [reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-billie): A string that identifies the transaction. You can use this parameter with [Payment Intents](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-billie) and [Invoices](https://docs.stripe.com/api/invoices/create.md?api-version=2026-09-30.endive#create_invoice-payment_settings-payment_method_options-billie).
- [company_details](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-billie): An object that contains `registered_name`, `registration_type`, `registration_number`, `vat`, and `registered_address`. You can use this parameter with [Payment Intents](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-billie), [Invoices](https://docs.stripe.com/api/invoices/create.md?api-version=2026-09-30.endive#create_invoice-payment_settings-payment_method_options-billie), and [Subscriptions](https://docs.stripe.com/api/subscriptions/create.md?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_options-billie).

The corresponding properties appear on the response objects for each resource.

## Impact

You now have the option to include additional `company_details` and a `reference` identifier when you use the Billie payment method for Payment Intents, Invoices or Subscriptions (`reference` isn’t supported for Subscriptions). These parameters don’t affect existing integrations as they’re additive and optional.

Providing this information to Billie can improve authorisation rates.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `company_details`, `reference` | Added | [Invoice#create.payment_settings.payment_method_options.billie](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_options-billie), [Invoice#update.payment_settings.payment_method_options.billie](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options-billie), [Invoice.payment_settings.payment_method_options.billie](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options-billie), [PaymentIntent#confirm.payment_method_options.billie](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-billie), [PaymentIntent#create.payment_method_options.billie](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-billie), [PaymentIntent#update.payment_method_options.billie](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-payment_method_options-billie), [PaymentIntent.payment_method_options.billie](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-billie) |
| `company_details` | Added | [Subscription#create.payment_settings.payment_method_options.billie](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_options-billie), [Subscription#update.payment_settings.payment_method_options.billie](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options-billie), [Subscription.payment_settings.payment_method_options.billie](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options-billie) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `company_details`, `reference` | Added | [Invoice::PaymentSetting::PaymentMethodOption::Billie](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options-billie), [InvoiceCreateParams::PaymentSetting::PaymentMethodOption::Billie](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_options-billie), [InvoiceUpdateParams::PaymentSetting::PaymentMethodOption::Billie](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options-billie), [PaymentIntent::PaymentMethodOption::Billie](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-billie), [PaymentIntentConfirmParams::PaymentMethodOption::Billie](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-billie), [PaymentIntentCreateParams::PaymentMethodOption::Billie](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-billie), [PaymentIntentUpdateParams::PaymentMethodOption::Billie](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-payment_method_options-billie) |
| `company_details` | Added | [Subscription::PaymentSetting::PaymentMethodOption::Billie](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options-billie), [SubscriptionCreateParams::PaymentSetting::PaymentMethodOption::Billie](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_options-billie), [SubscriptionUpdateParams::PaymentSetting::PaymentMethodOption::Billie](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options-billie) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `company_details`, `reference` | Added | [Invoice.PaymentSetting.PaymentMethodOption.Billie](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options-billie), [InvoiceCreateParamsPaymentSettingPaymentMethodOptionBillie](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_options-billie), [InvoiceModifyParamsPaymentSettingPaymentMethodOptionBillie](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options-billie), [PaymentIntent.PaymentMethodOption.Billie](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-billie), [PaymentIntentConfirmParamsPaymentMethodOptionBillie](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-billie), [PaymentIntentCreateParamsPaymentMethodOptionBillie](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-billie), [PaymentIntentModifyParamsPaymentMethodOptionBillie](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-payment_method_options-billie) |
| `company_details` | Added | [Subscription.PaymentSetting.PaymentMethodOption.Billie](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options-billie), [SubscriptionCreateParamsPaymentSettingPaymentMethodOptionBillie](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_options-billie), [SubscriptionModifyParamsPaymentSettingPaymentMethodOptionBillie](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options-billie) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `company_details`, `reference` | Added | [Invoice.create().$params.payment_setting.payment_method_option.billie](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_options-billie), [Invoice.payment_settings.payment_method_options.billie](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options-billie), [Invoice.update().$params.payment_setting.payment_method_option.billie](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options-billie), [PaymentIntent.confirm().$params.payment_method_option.billie](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-billie), [PaymentIntent.create().$params.payment_method_option.billie](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-billie), [PaymentIntent.payment_method_options.billie](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-billie), [PaymentIntent.update().$params.payment_method_option.billie](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-payment_method_options-billie) |
| `company_details` | Added | [Subscription.create().$params.payment_setting.payment_method_option.billie](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_options-billie), [Subscription.payment_settings.payment_method_options.billie](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options-billie), [Subscription.update().$params.payment_setting.payment_method_option.billie](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options-billie) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `companyDetails`, `reference` | Added | [Invoice.payment_settings.payment_method_options.billie](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options-billie), [InvoiceCreateParams.payment_settings.payment_method_options.billie](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_options-billie), [InvoiceUpdateParams.payment_settings.payment_method_options.billie](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options-billie), [PaymentIntent.payment_method_options.billie](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-billie), [PaymentIntentConfirmParams.payment_method_options.billie](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-billie), [PaymentIntentCreateParams.payment_method_options.billie](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-billie), [PaymentIntentUpdateParams.payment_method_options.billie](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-payment_method_options-billie) |
| `companyDetails` | Added | [Subscription.payment_settings.payment_method_options.billie](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options-billie), [SubscriptionCreateParams.payment_settings.payment_method_options.billie](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_options-billie), [SubscriptionUpdateParams.payment_settings.payment_method_options.billie](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options-billie) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `company_details`, `reference` | Added | [Invoice.payment_settings.payment_method_options.billie](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options-billie), [InvoiceCreateParams.payment_settings.payment_method_options.billie](/api/invoices/create?api-version=2026-09-30.endive#create-payment_settings-payment_method_options-billie), [InvoiceUpdateParams.payment_settings.payment_method_options.billie](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options-billie), [PaymentIntent.payment_method_options.billie](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-billie), [PaymentIntentConfirmParams.payment_method_options.billie](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-billie), [PaymentIntentCreateParams.payment_method_options.billie](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-billie), [PaymentIntentUpdateParams.payment_method_options.billie](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-payment_method_options-billie) |
| `company_details` | Added | [Subscription.payment_settings.payment_method_options.billie](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options-billie), [SubscriptionCreateParams.payment_settings.payment_method_options.billie](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-payment_settings-payment_method_options-billie), [SubscriptionUpdateParams.payment_settings.payment_method_options.billie](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options-billie) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CompanyDetails`, `Reference` | Added | [InvoicePaymentSettingsPaymentMethodOptionsBillie](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options-billie), [InvoicePaymentSettingsPaymentMethodOptionsBillieParams](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options-billie), [PaymentIntentConfirmPaymentMethodOptionsBillieParams](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-payment_method_options-billie), [PaymentIntentPaymentMethodOptionsBillie](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-billie), [PaymentIntentPaymentMethodOptionsBillieParams](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-billie) |
| `CompanyDetails` | Added | [SubscriptionPaymentSettingsPaymentMethodOptionsBillie](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options-billie), [SubscriptionPaymentSettingsPaymentMethodOptionsBillieParams](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options-billie) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CompanyDetails`, `Reference` | Added | [Invoice.PaymentSettings.PaymentMethodOptions.Billie](/api/invoices/object?api-version=2026-09-30.endive#invoice_object-payment_settings-payment_method_options-billie), [InvoicePaymentSettingsPaymentMethodOptionsBillieOptions](/api/invoices/update?api-version=2026-09-30.endive#update_invoice-payment_settings-payment_method_options-billie), [PaymentIntent.PaymentMethodOptions.Billie](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-payment_method_options-billie), [PaymentIntentPaymentMethodOptionsBillieOptions](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-payment_method_options-billie) |
| `CompanyDetails` | Added | [Subscription.PaymentSettings.PaymentMethodOptions.Billie](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-payment_settings-payment_method_options-billie), [SubscriptionPaymentSettingsPaymentMethodOptionsBillieOptions](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-payment_settings-payment_method_options-billie) |

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

- [Unifies the billing cycle anchor format across Subscriptions and Invoices](https://docs.stripe.com/changelog/endive/2026-09-30/polymorphic-billing-cycle-anchor.md)
- [Adds invoicing rules to Invoice Items](https://docs.stripe.com/changelog/endive/2026-09-30/invoicing-rules-for-invoice-items.md)
- [Adds the ability to clear invoicing rules on Invoice Items](https://docs.stripe.com/changelog/endive/2026-09-30/clear-invoicing-rules-on-invoice-items.md)
- [Adds proration details for Invoice Items using classic billing mode](https://docs.stripe.com/changelog/endive/2026-09-30/invoice-items-proration-details.md)
- [Makes trial offers generally available](https://docs.stripe.com/changelog/endive/2026-09-30/trial-offer-ga.md)
- [Adds detailed status to explain why an invoice is uncollectible](https://docs.stripe.com/changelog/endive/2026-09-30/invoice-uncollectible-status-detail.md)
- [Adds support for scheduling Subscription cancellation as part of pending update](https://docs.stripe.com/changelog/endive/2026-09-30/scheduled-subscription-cancellation.md)
- [Adds the ability to pause and resume Subscriptions on demand](https://docs.stripe.com/changelog/endive/2026-09-30/pause-subscription.md)
- [Adds the Feedback Options API](https://docs.stripe.com/changelog/endive/2026-09-30/feedback-options-api.md)
