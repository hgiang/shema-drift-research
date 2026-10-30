# Adds scheduled subscription downgrades in the customer portal

## What’s new

You can now configure the customer portal so that subscription downgrades occur at the end of the billing cycle, rather than immediately.

You can [manage downgrades in the Dashboard](https://docs.stripe.com/customer-management/configure-portal.md#downgrades) or by using the [schedule_at_period_end](https://docs.stripe.com/api/customer_portal/configurations/create.md?api-version=2024-10-28.acacia#create_portal_configuration-features-subscription_update-schedule_at_period_end) when you [create a portal configuration](https://docs.stripe.com/api/customer_portal/configurations/create.md?api-version=2024-10-28.acacia) through the API.

## Impact

Previously, customers on higher cost plans that allocated credits that switched to a lower cost plans would be given access to the remaining credits on the higher cost plan. This change makes it possible for downgrades to occur at the end of a billing cycle, preventing the credit issue.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `schedule_at_period_end` | Added | [BillingPortal.Configuration#create.features.subscription_update](/api/customer_portal/configurations/create?api-version=2024-10-28.acacia#create_portal_configuration-features-subscription_update), [BillingPortal.Configuration#update.features.subscription_update](/api/customer_portal/configurations/update?api-version=2024-10-28.acacia#update_portal_configuration-features-subscription_update), [BillingPortal.Configuration.features.subscription_update](/api/customer_portal/configurations/object?api-version=2024-10-28.acacia#portal_configuration_object-features-subscription_update) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `schedule_at_period_end` | Added | [stripe.billing_portal.Configuration.CreateParamsFeaturesSubscriptionUpdate](/api/customer_portal/configurations/create?api-version=2024-10-28.acacia#create_portal_configuration-features-subscription_update), [stripe.billing_portal.Configuration.ModifyParamsFeaturesSubscriptionUpdate](/api/customer_portal/configurations/update?api-version=2024-10-28.acacia#update_portal_configuration-features-subscription_update), [stripe.billing_portal.Configuration.Features.SubscriptionUpdate](/api/customer_portal/configurations/object?api-version=2024-10-28.acacia#portal_configuration_object-features-subscription_update) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `schedule_at_period_end` | Added | [BillingPortal.Configuration.features.subscription_update](/api/customer_portal/configurations/object?api-version=2024-10-28.acacia#portal_configuration_object-features-subscription_update), [billingportal.ConfigurationCreateParams.features.subscription_update](/api/customer_portal/configurations/create?api-version=2024-10-28.acacia#create_portal_configuration-features-subscription_update), [billingportal.ConfigurationUpdateParams.features.subscription_update](/api/customer_portal/configurations/update?api-version=2024-10-28.acacia#update_portal_configuration-features-subscription_update) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `schedule_at_period_end` | Added | [BillingPortal.Configuration.features.subscription_update](/api/customer_portal/configurations/object?api-version=2024-10-28.acacia#portal_configuration_object-features-subscription_update), [BillingPortal.ConfigurationCreateParams.features.subscription_update](/api/customer_portal/configurations/create?api-version=2024-10-28.acacia#create_portal_configuration-features-subscription_update), [BillingPortal.ConfigurationUpdateParams.features.subscription_update](/api/customer_portal/configurations/update?api-version=2024-10-28.acacia#update_portal_configuration-features-subscription_update) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `ScheduleAtPeriodEnd` | Added | [BillingPortalConfigurationFeaturesSubscriptionUpdateParams](/api/customer_portal/configurations/create?api-version=2024-10-28.acacia#create_portal_configuration-features-subscription_update), [BillingPortalConfigurationFeaturesSubscriptionUpdate](/api/customer_portal/configurations/object?api-version=2024-10-28.acacia#portal_configuration_object-features-subscription_update) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `ScheduleAtPeriodEnd` | Added | [BillingPortalConfigurationFeaturesSubscriptionUpdateOptions](/api/customer_portal/configurations/create?api-version=2024-10-28.acacia#create_portal_configuration-features-subscription_update), [BillingPortalConfigurationFeaturesSubscriptionUpdate](/api/customer_portal/configurations/object?api-version=2024-10-28.acacia#portal_configuration_object-features-subscription_update) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-10-28.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.2.0](https://github.com/stripe/stripe-python/releases/tag/v11.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.2.0](https://github.com/stripe/stripe-php/releases/tag/v16.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.0.0](https://github.com/stripe/stripe-java/releases/tag/v28.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.3.0](https://github.com/stripe/stripe-node/releases/tag/v17.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.0.0](https://github.com/stripe/stripe-go/releases/tag/v81.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
