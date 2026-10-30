# Adds support for three new payment methods: Multibanco, Twint, and Zip

## What’s new

Expands the suite of supported payment methods on Payment Links by adding support for [Multibanco](https://docs.stripe.com/payments/multibanco.md), [Twint](https://docs.stripe.com/payments/twint.md), and [Zip](https://docs.stripe.com/payments/zip.md).

## Impact

This allows you to use  [Multibanco](https://docs.stripe.com/payments/multibanco.md), [Twint](https://docs.stripe.com/payments/twint.md), and [Zip](https://docs.stripe.com/payments/zip.md) with Payment Links.

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `multibanco`, `twint`, `zip` | Added | [PaymentLink#create.payment_method_types[]](/api/payment-link/create?api-version=2024-09-30.acacia#create_payment_link-payment_method_types), [PaymentLink#update.payment_method_types[]](/api/payment-link/update?api-version=2024-09-30.acacia#update_payment_link-payment_method_types), [PaymentLink.payment_method_types[]](/api/payment-link/object?api-version=2024-09-30.acacia#payment_link_object-payment_method_types) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `multibanco`, `twint`, `zip` | Added | [stripe.PaymentLink.payment_method_types](/api/payment-link/object?api-version=2024-09-30.acacia#payment_link_object-payment_method_types), [stripe.PaymentLink.CreateParams.payment_method_types](/api/payment-link/create?api-version=2024-09-30.acacia#create_payment_link-payment_method_types), [stripe.PaymentLink.ModifyParams.payment_method_types](/api/payment-link/update?api-version=2024-09-30.acacia#update_payment_link-payment_method_types) |

#### PHP

| Values | Change | Enum |
| --- | --- | --- |
| `multibanco`, `twint`, `zip` | Added | [PaymentLink.payment_method_types[]](/api/payment-link/object?api-version=2024-09-30.acacia#payment_link_object-payment_method_types) |

#### Java

| Values | Change | Enums |
| --- | --- | --- |
| `multibanco`, `twint`, `zip` | Added | [PaymentLinkCreateParams.payment_method_types[]](/api/payment-link/create?api-version=2024-09-30.acacia#create_payment_link-payment_method_types), [PaymentLinkUpdateParams.payment_method_types[]](/api/payment-link/update?api-version=2024-09-30.acacia#update_payment_link-payment_method_types) |

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `multibanco`, `twint`, `zip` | Added | [PaymentLink.payment_method_types[]](/api/payment-link/object?api-version=2024-09-30.acacia#payment_link_object-payment_method_types), [PaymentLinkCreateParams.payment_method_types[]](/api/payment-link/create?api-version=2024-09-30.acacia#create_payment_link-payment_method_types), [PaymentLinkUpdateParams.payment_method_types[]](/api/payment-link/update?api-version=2024-09-30.acacia#update_payment_link-payment_method_types) |

#### Go

| Values | Change | Enum |
| --- | --- | --- |
| `multibanco`, `twint`, `zip` | Added | [PaymentLinkPaymentMethodTypes](/api/payment-link/object?api-version=2024-09-30.acacia#payment_link_object-payment_method_types) |

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

- [Adds support for using the Multibanco payment method with  billing](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-mutlibanco-support.md)
- [Adds Twint to the PaymentMethodConfiguration API](https://docs.stripe.com/changelog/acacia/2024-09-30/twint-support-payment-method-configuration.md)
- [Adds Girocard as a PaymentMethod brand and network](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-girocard-paymentmethod-brand-network.md)
