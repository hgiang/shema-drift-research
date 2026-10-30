# Adds the number of instalments for Alma payments to Charge objects

## What’s new

Adds the [count](https://docs.stripe.com/api/charges/object.md?api-version=2025-08-30.basil#charge_object-payment_method_details-alma-installments-count) of [instalments](https://docs.stripe.com/api/charges/object.md?api-version=2025-08-30.basil#charge_object-payment_method_details-alma-installments) for [Alma payments](https://docs.stripe.com/payments/alma.md) to the [Charge](https://docs.stripe.com/api/charge/object.md?api-version=2025-08-27.basil) object.

## Impact

You can now track Alma payments by product type by using the new [count](https://docs.stripe.com/api/charges/object.md?api-version=2025-08-30.basil#charge_object-payment_method_details-alma-installments-count) property, which contains the number of instalments selected by the customer for an Alma payment.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `installments` | Added | [Charge.payment_method_details.alma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `installments` | Added | [Charge::PaymentMethodDetail::Alma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `installments` | Added | [Charge.PaymentMethodDetail.Alma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `installments` | Added | [Charge.payment_method_details.alma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `installments` | Added | [Charge.payment_method_details.alma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Installments` | Added | [ChargePaymentMethodDetailsAlma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Installments` | Added | [Charge.PaymentMethodDetails.Alma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-08-27.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.5.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.5.0](https://github.com/stripe/stripe-python/releases/tag/v12.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.6.0](https://github.com/stripe/stripe-php/releases/tag/v17.6.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.5.0](https://github.com/stripe/stripe-java/releases/tag/v29.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.5.0](https://github.com/stripe/stripe-node/releases/tag/v18.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.5.0](https://github.com/stripe/stripe-go/releases/tag/v82.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.5.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds PayPay settings to the Account object](https://docs.stripe.com/changelog/basil/2025-08-27/add_paypay_payments_settings.md)
- [Adds a Charge transaction ID for several payment methods](https://docs.stripe.com/changelog/basil/2025-08-27/transaction-id.md)
- [Adds support to include the IOF tax in the amount for Pix payments](https://docs.stripe.com/changelog/basil/2025-08-27/pix-payments-iof-tax.md)
- [Adds excluded payment method types to the Payment Intents API](https://docs.stripe.com/changelog/basil/2025-08-27/cs_add_excluded_payment_method_types_pi.md)
