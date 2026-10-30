# Adds support for custom payment methods

## What’s new

You can now create custom [Payment Methods](https://docs.stripe.com/api/payment_methods.md?api-version=2025-10-29.clover) and extend your payment integration to use payment methods that are processed outside of Stripe. For a list of payment method types that Stripe directly supports, see the [payment method overview page](https://docs.stripe.com/payments/payment-methods/overview.md).

## Impact

You can now create custom Payment Methods in Stripe to represent payment methods processed by third-party payment processors. When you process custom payment method transactions outside of Stripe, you can record the transaction details to your Stripe account using a custom [Payment Method](https://docs.stripe.com/api/payment_methods.md?api-version=2025-10-29.clover) and [Payment Record](https://docs.stripe.com/api/payment-record.md?2025-10-29.clover=&api-version=2025-10-29.clover).

To create a custom payment method type:

1. Open the [Custom payment methods page](https://dashboard.stripe.com/settings/custom_payment_methods) in your Dashboard.
2. Click **Create**.
3. Select an existing type to copy, or click **Provide a custom name and icon**.
4. If you’re providing a custom name and icon, enter a display name and upload a logo icon.
5. Read and agree to the terms, then click **Create**. In the list of types, note the ID of your custom payment method type, which starts with `cpmt_`. To create a payment method of your custom type, set its `type` to `custom` and its `custom.type` to the ID of your custom type.

> Custom payment methods are not compatible with Payment Intents or Setup Intents.

For more information about creating custom payment methods, see the [Create Payment Methods API](https://docs.stripe.com/api/payment_methods/create.md?api-version=2025-10-29.clover).

To use third-party payment processors with custom payment methods, see [Integrate with third-party payment processors](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md).

To use [Payment Records](https://docs.stripe.com/api/payment-record.md?api-version=2025-10-29.clover) with custom payment methods, report payment attempts with [payment_method_details](https://docs.stripe.com/api/payment-record/report-payment-attempt/report.md?api-version=2025-10-29.clover#report_payment_records_report_payment_attempt-payment_method_details).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `custom` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-10-29.clover), [PaymentMethod#create](/api/payment_methods/create?api-version=2025-10-29.clover) |

| Values | Change | Enums |
| --- | --- | --- |
| `custom` | Added | [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-10-29.clover#confirmation_token_object-payment_method_preview-type), [PaymentMethod](/api/confirmation_tokens/object?api-version=2025-10-29.clover#confirmation_token_object-type) |
| `custom` | Added | [Customer#list_payment_methods](/api/payment_methods/customer_list?api-version=2025-10-29.clover#list_payment_methods-type), [PaymentMethod#list](/api/payment_methods/customer_list?api-version=2025-10-29.clover#list_payment_methods-type), [PaymentMethod#create](/api/payment_methods/customer_list?api-version=2025-10-29.clover#list_payment_methods-type) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `custom` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-10-29.clover), [PaymentMethodCreateParams](/api/payment_methods/create?api-version=2025-10-29.clover) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `custom` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-10-29.clover), [PaymentMethodCreateParams](/api/payment_methods/create?api-version=2025-10-29.clover) |

| Values | Change | Enums |
| --- | --- | --- |
| `custom` | Added | [ConfirmationToken.PaymentMethodPreview](/api/confirmation_tokens/object?api-version=2025-10-29.clover#confirmation_token_object-payment_method_preview-type), [PaymentMethod](/api/confirmation_tokens/object?api-version=2025-10-29.clover#confirmation_token_object-type) |
| `custom` | Added | [CustomerListPaymentMethodsParams](/api/payment_methods/customer_list?api-version=2025-10-29.clover#list_payment_methods-type), [PaymentMethodListParams](/api/payment_methods/customer_list?api-version=2025-10-29.clover#list_payment_methods-type), [PaymentMethodCreateParams](/api/payment_methods/customer_list?api-version=2025-10-29.clover#list_payment_methods-type) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `custom` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-10-29.clover), [PaymentMethod.create().$params](/api/payment_methods/create?api-version=2025-10-29.clover) |

| Value | Change | Enums |
| --- | --- | --- |
| `custom` | Added | [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-10-29.clover#confirmation_token_object-payment_method_preview-type), [PaymentMethod](/api/confirmation_tokens/object?api-version=2025-10-29.clover#confirmation_token_object-type) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `custom` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-10-29.clover), [PaymentMethodCreateParams](/api/payment_methods/create?api-version=2025-10-29.clover) |

| Value | Change | Enums |
| --- | --- | --- |
| `custom` | Added | [CustomerListPaymentMethodsParams](/api/payment_methods/customer_list?api-version=2025-10-29.clover#list_payment_methods-type), [PaymentMethodListParams](/api/payment_methods/customer_list?api-version=2025-10-29.clover#list_payment_methods-type), [PaymentMethodCreateParams](/api/payment_methods/customer_list?api-version=2025-10-29.clover#list_payment_methods-type) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `custom` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-10-29.clover), [PaymentMethodCreateParams](/api/payment_methods/create?api-version=2025-10-29.clover) |

| Values | Change | Enums |
| --- | --- | --- |
| `custom` | Added | [ConfirmationToken.payment_method_preview](/api/confirmation_tokens/object?api-version=2025-10-29.clover#confirmation_token_object-payment_method_preview-type), [PaymentMethod](/api/confirmation_tokens/object?api-version=2025-10-29.clover#confirmation_token_object-type) |
| `custom` | Added | [CustomerListPaymentMethodsParams](/api/payment_methods/customer_list?api-version=2025-10-29.clover#list_payment_methods-type), [PaymentMethodListParams](/api/payment_methods/customer_list?api-version=2025-10-29.clover#list_payment_methods-type), [PaymentMethodCreateParams](/api/payment_methods/customer_list?api-version=2025-10-29.clover#list_payment_methods-type) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Custom` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-10-29.clover), [PaymentMethodParams](/api/payment_methods/create?api-version=2025-10-29.clover) |

| Value | Change | Enums |
| --- | --- | --- |
| `custom` | Added | [ConfirmationTokenPaymentMethodPreview](/api/confirmation_tokens/object?api-version=2025-10-29.clover#confirmation_token_object-payment_method_preview-Type), [PaymentMethod](/api/confirmation_tokens/object?api-version=2025-10-29.clover#confirmation_token_object-Type) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Custom` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-10-29.clover), [PaymentMethodCreateOptions](/api/payment_methods/create?api-version=2025-10-29.clover) |

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
- [Adds Klarna reference parameters for line items in Payment Intents](https://docs.stripe.com/changelog/clover/2025-10-29/klarna-line-item-reference.md)
- [Adds a subscription reference to Klarna line items in Payment Intents](https://docs.stripe.com/changelog/clover/2025-10-29/klarna-items-payment-intents.md)
