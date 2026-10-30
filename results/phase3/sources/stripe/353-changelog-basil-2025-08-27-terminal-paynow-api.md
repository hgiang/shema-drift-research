# Adds support for PayNow on Terminal

## What’s new

Adds support for PayNow Charges by integrating additional fields for Terminal in the `payment_method_details` parameter.

## Impact

Lets you collect PayNow payments in-person on Terminal smart readers. Learn more about the [payment methods](https://docs.stripe.com/terminal/payments/additional-payment-methods.md) available on Terminal.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `location`, `reader` | Added | [Charge.payment_method_details.paynow](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-paynow) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `location`, `reader` | Added | [Charge::PaymentMethodDetail::Paynow](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-paynow) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `location`, `reader` | Added | [Charge.PaymentMethodDetail.Paynow](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-paynow) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `location`, `reader` | Added | [Charge.payment_method_details.paynow](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-paynow) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `location`, `reader` | Added | [Charge.payment_method_details.paynow](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-paynow) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Location`, `Reader` | Added | [ChargePaymentMethodDetailsPaynow](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-paynow) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Location`, `Reader` | Added | [Charge.PaymentMethodDetails.Paynow](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-paynow) |

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

- [Adds support for simulating card payments on Terminal readers](https://docs.stripe.com/changelog/basil/2025-08-27/card-present-payment-method.md)
- [Adds support for MXN currency in Terminal tipping configuration](https://docs.stripe.com/changelog/basil/2025-08-27/terminal-tipping-configuration-mxn.md)
- [Makes CVC optional when presenting a payment method on a simulated reader](https://docs.stripe.com/changelog/basil/2025-08-27/make-cvc-optional.md)
