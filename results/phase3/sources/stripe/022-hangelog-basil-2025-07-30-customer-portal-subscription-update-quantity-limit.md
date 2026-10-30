# Adds support for quantity adjustment to the Customer Portal Configuration API

## What’s new

Adds the [adjustable_quantity](https://docs.stripe.com/api/customer_portal/configurations/create.md?api-version=2025-07-30.basil#create_portal_configuration-features-subscription_update-products-adjustable_quantity) parameter to the [products](https://docs.stripe.com/api/customer_portal/configurations/object.md?api-version=2025-07-30.basil#portal_configuration_object-features-subscription_update-products) field of the [Customer Portal Configuration](https://docs.stripe.com/api/customer_portal/configurations/object.md?api-version=2025-07-30.basil) object.

## Impact

Before this change, you could only configure the quantity adjustment for the default Customer Portal Configuration object through the [Dashboard](https://dashboard.stripe.com/settings/billing/portal). Now, you can also use the `adjustable_quantity` parameter to programmatically control the quantity that customers can modify on a Customer Portal page for all Customer Portal Configuration objects.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `adjustable_quantity` | Added | [BillingPortal.Configuration#create.features.subscription_update.products[]](/api/customer_portal/configurations/create?api-version=2025-07-30.basil#create_portal_configuration-features-subscription_update-products), [BillingPortal.Configuration#update.features.subscription_update.products[]](/api/customer_portal/configurations/update?api-version=2025-07-30.basil#update_portal_configuration-features-subscription_update-products), [BillingPortal.Configuration.features.subscription_update.products[]](/api/customer_portal/configurations/object?api-version=2025-07-30.basil#portal_configuration_object-features-subscription_update-products) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `adjustable_quantity` | Added | [BillingPortal::Configuration::CreateParams::Feature::SubscriptionUpdate::Product](/api/customer_portal/configurations/create?api-version=2025-07-30.basil#create_portal_configuration-features-subscription_update-products), [BillingPortal::Configuration::Feature::SubscriptionUpdate::Product](/api/customer_portal/configurations/object?api-version=2025-07-30.basil#portal_configuration_object-features-subscription_update-products), [BillingPortal::Configuration::UpdateParams::Feature::SubscriptionUpdate::Product](/api/customer_portal/configurations/update?api-version=2025-07-30.basil#update_portal_configuration-features-subscription_update-products) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `adjustable_quantity` | Added | [BillingPortal.Configuration.Feature.SubscriptionUpdate.Product](/api/customer_portal/configurations/object?api-version=2025-07-30.basil#portal_configuration_object-features-subscription_update-products), [billing_portal.Configuration.CreateParamsFeatureSubscriptionUpdateProduct](/api/customer_portal/configurations/create?api-version=2025-07-30.basil#create_portal_configuration-features-subscription_update-products), [billing_portal.Configuration.ModifyParamsFeatureSubscriptionUpdateProduct](/api/customer_portal/configurations/update?api-version=2025-07-30.basil#update_portal_configuration-features-subscription_update-products) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `adjustableQuantity` | Added | [billingportal.Configuration.features.subscription_update.products[]](/api/customer_portal/configurations/object?api-version=2025-07-30.basil#portal_configuration_object-features-subscription_update-products), [billingportal.ConfigurationCreateParams.features.subscription_update.products[]](/api/customer_portal/configurations/create?api-version=2025-07-30.basil#create_portal_configuration-features-subscription_update-products), [billingportal.ConfigurationUpdateParams.features.subscription_update.products[]](/api/customer_portal/configurations/update?api-version=2025-07-30.basil#update_portal_configuration-features-subscription_update-products) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `adjustable_quantity` | Added | [BillingPortal.Configuration.features.subscription_update.products[]](/api/customer_portal/configurations/object?api-version=2025-07-30.basil#portal_configuration_object-features-subscription_update-products), [BillingPortal.ConfigurationCreateParams.features.subscription_update.products[]](/api/customer_portal/configurations/create?api-version=2025-07-30.basil#create_portal_configuration-features-subscription_update-products), [BillingPortal.ConfigurationUpdateParams.features.subscription_update.products[]](/api/customer_portal/configurations/update?api-version=2025-07-30.basil#update_portal_configuration-features-subscription_update-products) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AdjustableQuantity` | Added | [BillingPortalConfigurationFeaturesSubscriptionUpdateProducts](/api/customer_portal/configurations/object?api-version=2025-07-30.basil#portal_configuration_object-features-subscription_update-products), [BillingPortalConfigurationFeaturesSubscriptionUpdateProductsParams](/api/customer_portal/configurations/create?api-version=2025-07-30.basil#create_portal_configuration-features-subscription_update-products) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AdjustableQuantity` | Added | [BillingPortal.Configuration.Features.SubscriptionUpdate.Products](/api/customer_portal/configurations/object?api-version=2025-07-30.basil#portal_configuration_object-features-subscription_update-products), [BillingPortalConfigurationFeaturesSubscriptionUpdateProductsOptions](/api/customer_portal/configurations/create?api-version=2025-07-30.basil#create_portal_configuration-features-subscription_update-products) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-07-30.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.4.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.4.0](https://github.com/stripe/stripe-python/releases/tag/v12.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.5.0](https://github.com/stripe/stripe-php/releases/tag/v17.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.4.0](https://github.com/stripe/stripe-java/releases/tag/v29.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.4.0](https://github.com/stripe/stripe-node/releases/tag/v18.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.4.0](https://github.com/stripe/stripe-go/releases/tag/v82.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.4.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds a duration parameter for schedule phases](https://docs.stripe.com/changelog/basil/2025-07-30/add-schedule-phase-duration.md)
- [Adds helpers to cancel subscriptions for billing periods with mixed intervals](https://docs.stripe.com/changelog/basil/2025-07-30/cancel-at-enums.md)
- [Adds support for billing thresholds on flexible billing mode Subscriptions](https://docs.stripe.com/changelog/basil/2025-07-30/billing-thresholds.md)
- [Adds support for mixed intervals on the same subscription](https://docs.stripe.com/changelog/basil/2025-07-30/support-mixed-intervals.md)
