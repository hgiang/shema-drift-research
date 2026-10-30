# Subscriptions updated from the Customer Portal can now also modify their billing cycle anchor

## What’s new

When customers update their subscription from the [customer portal](https://docs.stripe.com/customer-management.md), you can now configure the [billing_cycle_anchor](https://docs.stripe.com/api/customer_portal/configurations/create.md?api-version=2025-12-15.clover#create_portal_configuration-features-subscription_update-billing_cycle_anchor) that applies to the updated subscription by specifying a [Customer Portal Configuration](https://docs.stripe.com/api/customer_portal/configurations.md?api-version=2025-12-15.clover). The billing cycle anchor is the reference point that aligns future billing period dates, defined as a UNIX timestamp in seconds from the current epoch, or `now` (the current UTC timestamp).

## Impact

You can now control the billing cycle anchor that applies when customers update their subscription from the customer portal. This change gives you more flexibility when you reset the billing date during subscription updates. Previously, updates made from the customer portal would always retain the existing billing cycle anchor.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `billing_cycle_anchor` | Added | [BillingPortal.Configuration#create.features.subscription_update](/api/customer_portal/configurations/create?api-version=2025-12-15.clover#create_billing_portal_configuration-features-subscription_update), [BillingPortal.Configuration#update.features.subscription_update](/api/customer_portal/configurations/update?api-version=2025-12-15.clover#update_billing_portal_configuration-features-subscription_update), [BillingPortal.Configuration.features.subscription_update](/api/customer_portal/configurations/object?api-version=2025-12-15.clover#billing_portal_configuration_object-features-subscription_update) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billing_cycle_anchor` | Added | [BillingPortal::Configuration::Feature::SubscriptionUpdate](/api/customer_portal/configurations/object?api-version=2025-12-15.clover#billing_portal_configuration_object-features-subscription_update), [BillingPortal::ConfigurationCreateParams::Feature::SubscriptionUpdate](/api/customer_portal/configurations/create?api-version=2025-12-15.clover#create_billing_portal_configuration-features-subscription_update), [BillingPortal::ConfigurationUpdateParams::Feature::SubscriptionUpdate](/api/customer_portal/configurations/update?api-version=2025-12-15.clover#update_billing_portal_configuration-features-subscription_update) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billing_cycle_anchor` | Added | [BillingPortal.Configuration.Feature.SubscriptionUpdate](/api/customer_portal/configurations/object?api-version=2025-12-15.clover#billing_portal_configuration_object-features-subscription_update), [billing_portal.ConfigurationCreateParamsFeatureSubscriptionUpdate](/api/customer_portal/configurations/create?api-version=2025-12-15.clover#create_billing_portal_configuration-features-subscription_update), [billing_portal.ConfigurationModifyParamsFeatureSubscriptionUpdate](/api/customer_portal/configurations/update?api-version=2025-12-15.clover#update_billing_portal_configuration-features-subscription_update) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billing_cycle_anchor` | Added | [BillingPortal.Configuration.features.subscription_update](/api/customer_portal/configurations/object?api-version=2025-12-15.clover#billing_portal_configuration_object-features-subscription_update), [BillingPortal\Configuration.create().$params.feature.subscription_update](/api/customer_portal/configurations/create?api-version=2025-12-15.clover#create_billing_portal_configuration-features-subscription_update), [BillingPortal\Configuration.update().$params.feature.subscription_update](/api/customer_portal/configurations/update?api-version=2025-12-15.clover#update_billing_portal_configuration-features-subscription_update) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billingCycleAnchor` | Added | [billingportal.Configuration.features.subscription_update](/api/customer_portal/configurations/object?api-version=2025-12-15.clover#billing_portal_configuration_object-features-subscription_update), [billingportal.ConfigurationCreateParams.features.subscription_update](/api/customer_portal/configurations/create?api-version=2025-12-15.clover#create_billing_portal_configuration-features-subscription_update), [billingportal.ConfigurationUpdateParams.features.subscription_update](/api/customer_portal/configurations/update?api-version=2025-12-15.clover#update_billing_portal_configuration-features-subscription_update) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billing_cycle_anchor` | Added | [BillingPortal.Configuration.features.subscription_update](/api/customer_portal/configurations/object?api-version=2025-12-15.clover#billing_portal_configuration_object-features-subscription_update), [BillingPortal.ConfigurationCreateParams.features.subscription_update](/api/customer_portal/configurations/create?api-version=2025-12-15.clover#create_billing_portal_configuration-features-subscription_update), [BillingPortal.ConfigurationUpdateParams.features.subscription_update](/api/customer_portal/configurations/update?api-version=2025-12-15.clover#update_billing_portal_configuration-features-subscription_update) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `BillingCycleAnchor` | Added | [BillingPortalConfigurationFeaturesSubscriptionUpdate](/api/customer_portal/configurations/object?api-version=2025-12-15.clover#billing_portal_configuration_object-features-subscription_update), [BillingPortalConfigurationFeaturesSubscriptionUpdateParams](/api/customer_portal/configurations/create?api-version=2025-12-15.clover#create_billing_portal_configuration-features-subscription_update) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `BillingCycleAnchor` | Added | [BillingPortal.Configuration.Features.SubscriptionUpdate](/api/customer_portal/configurations/object?api-version=2025-12-15.clover#billing_portal_configuration_object-features-subscription_update), [BillingPortalConfigurationFeaturesSubscriptionUpdateOptions](/api/customer_portal/configurations/create?api-version=2025-12-15.clover#create_billing_portal_configuration-features-subscription_update) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-12-15.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v18.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v18.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v14.2.0](https://github.com/stripe/stripe-python/releases/tag/v14.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v19.2.0](https://github.com/stripe/stripe-php/releases/tag/v19.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v31.2.0](https://github.com/stripe/stripe-java/releases/tag/v31.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v20.2.0](https://github.com/stripe/stripe-node/releases/tag/v20.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v84.2.0](https://github.com/stripe/stripe-go/releases/tag/v84.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v50.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v50.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds the ability to filter customer balance transactions by invoice](https://docs.stripe.com/changelog/clover/2025-12-15/customer-balance-transations-list-invoice.md)
- [Enables expansion for invoice pricing details](https://docs.stripe.com/changelog/clover/2025-12-15/expandable-price-details-price.md)
- [Adds subtotal property to Invoice Line Items](https://docs.stripe.com/changelog/clover/2025-12-15/invoice-line-item-subtotal.md)
