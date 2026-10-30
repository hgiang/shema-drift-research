# Adds support for US sellers to accept cross-border Pix payments

## What’s new

Adds support for US sellers to accept Pix payments from Brazilian buyers.

## Impact

Pix is the dominant payment method for e-commerce in Brazil. Based on our [study of global payment methods](https://stripe.com/blog/how-we-tested-the-conversion-impact-of-global-payment-methods), Stripe recommends that US-based sellers with potential customers in Brazil enable Pix. For more information, see [Pix payments](https://docs.stripe.com/payments/pix.md).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `pix` | Added | [PaymentMethodConfiguration#create](/api/payment_method_configurations/create?api-version=2025-04-30.preview), [PaymentMethodConfiguration#update](/api/payment_method_configurations/update?api-version=2025-04-30.preview), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.preview) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pix` | Added | [PaymentMethodConfiguration::CreateParams](/api/payment_method_configurations/create?api-version=2025-04-30.preview), [PaymentMethodConfiguration::UpdateParams](/api/payment_method_configurations/update?api-version=2025-04-30.preview), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.preview) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pix` | Added | [PaymentMethodConfiguration.CreateParams](/api/payment_method_configurations/create?api-version=2025-04-30.preview), [PaymentMethodConfiguration.UpdateParams](/api/payment_method_configurations/update?api-version=2025-04-30.preview), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.preview) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pix` | Added | [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.preview) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pix` | Added | [PaymentMethodConfigurationCreateParams](/api/payment_method_configurations/create?api-version=2025-04-30.preview), [PaymentMethodConfigurationUpdateParams](/api/payment_method_configurations/update?api-version=2025-04-30.preview), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.preview) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pix` | Added | [PaymentMethodConfigurationCreateParams](/api/payment_method_configurations/create?api-version=2025-04-30.preview), [PaymentMethodConfigurationUpdateParams](/api/payment_method_configurations/update?api-version=2025-04-30.preview), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.preview) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Pix` | Added | [PaymentMethodConfigurationParams](/api/payment_method_configurations/create?api-version=2025-04-30.preview), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.preview) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Pix` | Added | [PaymentMethodConfigurationCreateOptions](/api/payment_method_configurations/create?api-version=2025-04-30.preview), [PaymentMethodConfigurationUpdateOptions](/api/payment_method_configurations/update?api-version=2025-04-30.preview), [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-04-30.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-04-30.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.2.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v15.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.2.0b1](https://github.com/stripe/stripe-python/releases/tag/v12.2.0b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.3.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v17.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.2.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v29.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.2.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v18.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.2.0-beta.2](https://github.com/stripe/stripe-go/releases/tag/v82.2.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.2.0-beta.2](https://github.com/stripe/stripe-dotnet/releases/tag/v48.2.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
