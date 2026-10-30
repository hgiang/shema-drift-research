# Adds Pix to payment method configurations

## What’s new

Pix is now supported in the [Payment Method Configurations API](https://docs.stripe.com/api/payment_method_configurations.md?api-version=2025-04-30.basil).

## Impact

[Payment method configurations](https://docs.stripe.com/payments/payment-method-configurations.md) allow dynamic payment method users to display different sets of payment methods to customers for specific checkout scenarios. You can now use Pix, a popular payment method in Brazil, in payment method configurations.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `pix` | Added | [PaymentMethodConfiguration#create](/api/payment_method_configurations/create?api-version=2025-04-30.basil), [PaymentMethodConfiguration#update](/api/payment_method_configurations/update?api-version=2025-04-30.basil), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.basil) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pix` | Added | `PaymentMethodConfiguration::CreateParams`, `PaymentMethodConfiguration::UpdateParams`, `PaymentMethodConfiguration` |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pix` | Added | `PaymentMethodConfiguration.CreateParams`, `PaymentMethodConfiguration.UpdateParams`, [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.basil) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pix` | Added | [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.basil) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pix` | Added | [PaymentMethodConfigurationCreateParams](/api/payment_method_configurations/create?api-version=2025-04-30.basil), [PaymentMethodConfigurationUpdateParams](/api/payment_method_configurations/update?api-version=2025-04-30.basil), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.basil) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pix` | Added | [PaymentMethodConfigurationCreateParams](/api/payment_method_configurations/create?api-version=2025-04-30.basil), [PaymentMethodConfigurationUpdateParams](/api/payment_method_configurations/update?api-version=2025-04-30.basil), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.basil) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Pix` | Added | [PaymentMethodConfigurationParams](/api/payment_method_configurations/create?api-version=2025-04-30.basil), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.basil) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Pix` | Added | [PaymentMethodConfigurationCreateOptions](/api/payment_method_configurations/create?api-version=2025-04-30.basil), [PaymentMethodConfigurationUpdateOptions](/api/payment_method_configurations/update?api-version=2025-04-30.basil), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.basil) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-04-30.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.1.0](https://github.com/stripe/stripe-python/releases/tag/v12.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.2.0](https://github.com/stripe/stripe-php/releases/tag/v17.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.1.0](https://github.com/stripe/stripe-java/releases/tag/v29.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.1.0](https://github.com/stripe/stripe-node/releases/tag/v18.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.1.0](https://github.com/stripe/stripe-go/releases/tag/v82.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds Affirm as a supported payment method for one-off invoices and subscriptions](https://docs.stripe.com/changelog/basil/2025-04-30/affirm-send-invoice.md)
- [Adds tax ID to Payment Method billing details](https://docs.stripe.com/changelog/basil/2025-04-30/add-tax-id-to-billing-details.md)
- [Adds capture method option to Billie payments](https://docs.stripe.com/changelog/basil/2025-04-30/billie-capture-method-option.md)
