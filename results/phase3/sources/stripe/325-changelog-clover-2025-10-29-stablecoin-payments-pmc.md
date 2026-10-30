# Adds support for managing stablecoin payments with Payment Method Configurations

## What’s new

You can now create, update and manage [stablecoin payments](https://docs.stripe.com/payments/stablecoin-payments.md) alongside other payment methods using the [crypto](https://docs.stripe.com/api/payment_method_configurations/object.md?api-version=2025-10-29.clover#payment_method_configuration_object-crypto) parameter of the [Payment Method Configurations](https://docs.stripe.com/api/payment_method_configurations.md?api-version=2025-10-29.clover).

## Impact

You can now programmatically enable and disable stablecoin payments using Payment Method Configurations. If you’re already using a Payment Method Configuration, you can now configure stablecoin usage in your existing integration without using additional API endpoints or authentication requirements.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `crypto` | Added | [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-10-29.clover), [PaymentMethodConfiguration#create](/api/payment_method_configurations/create?api-version=2025-10-29.clover#create_payment_method_configuration), [PaymentMethodConfiguration#update](/api/payment_method_configurations/update?api-version=2025-10-29.clover#update_payment_method_configuration) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `crypto` | Added | [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-10-29.clover), [PaymentMethodConfiguration::CreateParams](/api/payment_method_configurations/create?api-version=2025-10-29.clover#create_payment_method_configuration), [PaymentMethodConfiguration::UpdateParams](/api/payment_method_configurations/update?api-version=2025-10-29.clover#update_payment_method_configuration) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `crypto` | Added | [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-10-29.clover), [PaymentMethodConfiguration.CreateParams](/api/payment_method_configurations/create?api-version=2025-10-29.clover#create_payment_method_configuration), [PaymentMethodConfiguration.ModifyParams](/api/payment_method_configurations/update?api-version=2025-10-29.clover#update_payment_method_configuration) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `crypto` | Added | [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-10-29.clover), [PaymentMethodConfiguration.create().$params](/api/payment_method_configurations/create?api-version=2025-10-29.clover#create_payment_method_configuration), [PaymentMethodConfiguration.update().$params](/api/payment_method_configurations/update?api-version=2025-10-29.clover#update_payment_method_configuration) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `crypto` | Added | [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-10-29.clover), [PaymentMethodConfigurationCreateParams](/api/payment_method_configurations/create?api-version=2025-10-29.clover#create_payment_method_configuration), [PaymentMethodConfigurationUpdateParams](/api/payment_method_configurations/update?api-version=2025-10-29.clover#update_payment_method_configuration) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `crypto` | Added | [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-10-29.clover), [PaymentMethodConfigurationCreateParams](/api/payment_method_configurations/create?api-version=2025-10-29.clover#create_payment_method_configuration), [PaymentMethodConfigurationUpdateParams](/api/payment_method_configurations/update?api-version=2025-10-29.clover#update_payment_method_configuration) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Crypto` | Added | [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-10-29.clover), [PaymentMethodConfigurationParams](/api/payment_method_configurations/create?api-version=2025-10-29.clover#create_payment_method_configuration) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Crypto` | Added | [PaymentMethodConfiguration](/api/payment_method_configurations/object?api-version=2025-10-29.clover), [PaymentMethodConfigurationCreateOptions](/api/payment_method_configurations/create?api-version=2025-10-29.clover#create_payment_method_configuration), [PaymentMethodConfigurationUpdateOptions](/api/payment_method_configurations/update?api-version=2025-10-29.clover#update_payment_method_configuration) |

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

- [Adds crypto network support for Solana](https://docs.stripe.com/changelog/clover/2025-10-29/crypto-network-solana.md)
- [Adds blockchain transaction hash to stablecoin refunds](https://docs.stripe.com/changelog/clover/2025-10-29/stablecoin-refunds-reference-details.md)
