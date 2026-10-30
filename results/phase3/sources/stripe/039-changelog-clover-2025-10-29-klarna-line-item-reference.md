# Adds Klarna reference parameters for line items in Payment Intents

## What’s new

Adds two fields for referencing transactions and subscriptions when using [Klarna](https://docs.stripe.com/payments/klarna.md) with [Payment Intents](https://docs.stripe.com/api/payment_intents.md?api-version=2025-10-29.clover) for individual line items:

- [reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-10-29.preview#create_payment_intent-amount_details-line_items-payment_method_options-klarna-reference): a reference number for this individual line item
- [subscription_reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-10-29.preview#create_payment_intent-amount_details-line_items-payment_method_options-klarna-subscription_reference): a reference number for subscriptions in this line item

These optional parameters accept strings to provide item-specific references that Klarna uses for transaction processing and customer communication. These reference numbers are used for order tracking and customer support inquiries.

## Impact

You can now provide transaction information to Klarna for individual line items. This improves the integration between your checkout flow and Klarna’s payment processing, and is used by Klarna to provide customer support and detailed transaction records.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `reference` | Added | [PaymentIntent#capture.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/capture?api-version=2025-10-29.clover#capture_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent#confirm.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/confirm?api-version=2025-10-29.clover#confirm_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent#create.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/create?api-version=2025-10-29.clover#create_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent#increment_authorization.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent#update.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/update?api-version=2025-10-29.clover#update_payment_intent-amount_details-line_items-payment_method_options-klarna), `PaymentIntentAmountDetailsLineItem.payment_method_options.klarna` |
| `subscription_reference` | Added | `PaymentIntentAmountDetailsLineItem.payment_method_options.klarna` |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `reference` | Added | [PaymentIntent::CaptureParams::AmountDetail::LineItem::PaymentMethodOption::Klarna](/api/payment_intents/capture?api-version=2025-10-29.clover#capture_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent::ConfirmParams::AmountDetail::LineItem::PaymentMethodOption::Klarna](/api/payment_intents/confirm?api-version=2025-10-29.clover#confirm_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent::CreateParams::AmountDetail::LineItem::PaymentMethodOption::Klarna](/api/payment_intents/create?api-version=2025-10-29.clover#create_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent::IncrementAuthorizationParams::AmountDetail::LineItem::PaymentMethodOption::Klarna](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent::UpdateParams::AmountDetail::LineItem::PaymentMethodOption::Klarna](/api/payment_intents/update?api-version=2025-10-29.clover#update_payment_intent-amount_details-line_items-payment_method_options-klarna), `PaymentIntentAmountDetailsLineItem::PaymentMethodOption::Klarna` |
| `subscription_reference` | Added | `PaymentIntentAmountDetailsLineItem::PaymentMethodOption::Klarna` |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `reference` | Added | [PaymentIntent.CaptureParamsAmountDetailLineItemPaymentMethodOptionKlarna](/api/payment_intents/capture?api-version=2025-10-29.clover#capture_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent.ConfirmParamsAmountDetailLineItemPaymentMethodOptionKlarna](/api/payment_intents/confirm?api-version=2025-10-29.clover#confirm_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent.CreateParamsAmountDetailLineItemPaymentMethodOptionKlarna](/api/payment_intents/create?api-version=2025-10-29.clover#create_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent.IncrementAuthorizationParamsAmountDetailLineItemPaymentMethodOptionKlarna](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent.ModifyParamsAmountDetailLineItemPaymentMethodOptionKlarna](/api/payment_intents/update?api-version=2025-10-29.clover#update_payment_intent-amount_details-line_items-payment_method_options-klarna), `PaymentIntentAmountDetailsLineItem.PaymentMethodOption.Klarna` |
| `subscription_reference` | Added | `PaymentIntentAmountDetailsLineItem.PaymentMethodOption.Klarna` |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `reference` | Added | [PaymentIntent.capture().$params.amount_detail.line_item.payment_method_option.klarna](/api/payment_intents/capture?api-version=2025-10-29.clover#capture_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent.confirm().$params.amount_detail.line_item.payment_method_option.klarna](/api/payment_intents/confirm?api-version=2025-10-29.clover#confirm_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent.create().$params.amount_detail.line_item.payment_method_option.klarna](/api/payment_intents/create?api-version=2025-10-29.clover#create_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent.increment_authorization().$params.amount_detail.line_item.payment_method_option.klarna](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntent.update().$params.amount_detail.line_item.payment_method_option.klarna](/api/payment_intents/update?api-version=2025-10-29.clover#update_payment_intent-amount_details-line_items-payment_method_options-klarna), `PaymentIntentAmountDetailsLineItem.payment_method_options.klarna` |
| `subscription_reference` | Added | `PaymentIntentAmountDetailsLineItem.payment_method_options.klarna` |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `reference` | Added | `PaymentIntentAmountDetailsLineItem.payment_method_options.klarna`, [PaymentIntentCaptureParams.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/capture?api-version=2025-10-29.clover#capture_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntentConfirmParams.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/confirm?api-version=2025-10-29.clover#confirm_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntentCreateParams.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/create?api-version=2025-10-29.clover#create_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntentIncrementAuthorizationParams.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntentUpdateParams.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/update?api-version=2025-10-29.clover#update_payment_intent-amount_details-line_items-payment_method_options-klarna) |
| `subscriptionReference` | Added | `PaymentIntentAmountDetailsLineItem.payment_method_options.klarna` |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `reference` | Added | `PaymentIntentAmountDetailsLineItem.payment_method_options.klarna`, [PaymentIntentCaptureParams.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/capture?api-version=2025-10-29.clover#capture_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntentConfirmParams.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/confirm?api-version=2025-10-29.clover#confirm_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntentCreateParams.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/create?api-version=2025-10-29.clover#create_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntentIncrementAuthorizationParams.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntentUpdateParams.amount_details.line_items[].payment_method_options.klarna](/api/payment_intents/update?api-version=2025-10-29.clover#update_payment_intent-amount_details-line_items-payment_method_options-klarna) |
| `subscription_reference` | Added | `PaymentIntentAmountDetailsLineItem.payment_method_options.klarna` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Reference` | Added | `PaymentIntentAmountDetailsLineItemPaymentMethodOptionsKlarna`, [PaymentIntentAmountDetailsLineItemsPaymentMethodOptionsKlarnaParams](/api/payment_intents/create?api-version=2025-10-29.clover#create_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntentCaptureAmountDetailsLineItemsPaymentMethodOptionsKlarnaParams](/api/payment_intents/capture?api-version=2025-10-29.clover#capture_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntentConfirmAmountDetailsLineItemsPaymentMethodOptionsKlarnaParams](/api/payment_intents/confirm?api-version=2025-10-29.clover#confirm_payment_intent-amount_details-line_items-payment_method_options-klarna), [PaymentIntentIncrementAuthorizationAmountDetailsLineItemsPaymentMethodOptionsKlarnaParams](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent-amount_details-line_items-payment_method_options-klarna) |
| `SubscriptionReference` | Added | `PaymentIntentAmountDetailsLineItemPaymentMethodOptionsKlarna` |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Reference` | Added | `PaymentIntentAmountDetailsLineItem.PaymentMethodOptions.Klarna`, [PaymentIntentAmountDetailsLineItemsPaymentMethodOptionsKlarnaOptions](/api/payment_intents/create?api-version=2025-10-29.clover#create_payment_intent-amount_details-line_items-payment_method_options-klarna) |
| `SubscriptionReference` | Added | `PaymentIntentAmountDetailsLineItem.PaymentMethodOptions.Klarna` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-10-29.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v17.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v17.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.1.0](https://github.com/stripe/stripe-python/releases/tag/v13.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.1.0](https://github.com/stripe/stripe-php/releases/tag/v18.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.1.0](https://github.com/stripe/stripe-java/releases/tag/v30.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.2.0](https://github.com/stripe/stripe-node/releases/tag/v19.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.1.0](https://github.com/stripe/stripe-go/releases/tag/v83.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds MB WAY to payment method configurations](https://docs.stripe.com/changelog/clover/2025-10-29/mb-way-payment-method-configuration.md)
- [Adds TWINT payment method options to Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-10-29/twint-checkout-sessions.md)
- [Adds support for specifying payment method configurations to the customer portal](https://docs.stripe.com/changelog/clover/2025-10-29/customer-portal-payment-method-configurations.md)
- [Adds MB WAY payment method to Payment Links and Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-10-29/mb-way-payment-link-checkout-sessions.md)
- [Adds the ability to exclude payment methods when using Setup Intents](https://docs.stripe.com/changelog/clover/2025-10-29/exclude-payment-methods-setup-intents.md)
- [Adds a subscription reference to Klarna line items in Payment Intents](https://docs.stripe.com/changelog/clover/2025-10-29/klarna-items-payment-intents.md)
- [Adds support for custom payment methods](https://docs.stripe.com/changelog/clover/2025-10-29/custom-payment-methods.md)
