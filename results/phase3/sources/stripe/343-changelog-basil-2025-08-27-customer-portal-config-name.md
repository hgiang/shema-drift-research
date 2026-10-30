# Adds a name field to the customer portal configuration object

## What’s new

Adds a `name` field to the [customer portal configuration object](https://docs.stripe.com/api/customer_portal/configurations/object.md?api-version=2025-08-27.basil) and related APIs.

## Impact

Use the `name` field to internally organise customer portal configurations. It’s not visible to your customers.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `name` | Added | [BillingPortal.Configuration](/api/customer_portal/configurations/object?api-version=2025-08-27.basil), [BillingPortal.Configuration#create](/api/customer_portal/configurations/create?api-version=2025-08-27.basil), [BillingPortal.Configuration#update](/api/customer_portal/configurations/update?api-version=2025-08-27.basil) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `name` | Added | [BillingPortal::Configuration](/api/customer_portal/configurations/object?api-version=2025-08-27.basil), [BillingPortal::Configuration::CreateParams](/api/customer_portal/configurations/create?api-version=2025-08-27.basil), [BillingPortal::Configuration::UpdateParams](/api/customer_portal/configurations/update?api-version=2025-08-27.basil) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `name` | Added | [BillingPortal.Configuration](/api/customer_portal/configurations/object?api-version=2025-08-27.basil), [billing_portal.Configuration.CreateParams](/api/customer_portal/configurations/create?api-version=2025-08-27.basil), [billing_portal.Configuration.ModifyParams](/api/customer_portal/configurations/update?api-version=2025-08-27.basil) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `name` | Added | [BillingPortal.Configuration](/api/customer_portal/configurations/object?api-version=2025-08-27.basil) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `name` | Added | [billingportal.Configuration](/api/customer_portal/configurations/object?api-version=2025-08-27.basil), [billingportal.ConfigurationCreateParams](/api/customer_portal/configurations/create?api-version=2025-08-27.basil), [billingportal.ConfigurationUpdateParams](/api/customer_portal/configurations/update?api-version=2025-08-27.basil) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `name` | Added | [BillingPortal.Configuration](/api/customer_portal/configurations/object?api-version=2025-08-27.basil), [BillingPortal.ConfigurationCreateParams](/api/customer_portal/configurations/create?api-version=2025-08-27.basil), [BillingPortal.ConfigurationUpdateParams](/api/customer_portal/configurations/update?api-version=2025-08-27.basil) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Name` | Added | [BillingPortalConfiguration](/api/customer_portal/configurations/object?api-version=2025-08-27.basil), [BillingPortalConfigurationParams](/api/customer_portal/configurations/create?api-version=2025-08-27.basil) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Name` | Added | [BillingPortal.Configuration](/api/customer_portal/configurations/object?api-version=2025-08-27.basil), [BillingPortal.ConfigurationUpdateOptions](/api/customer_portal/configurations/update?api-version=2025-08-27.basil) |

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

- [Adds support for invoice items metadata and period in subscriptions and schedules](https://docs.stripe.com/changelog/basil/2025-08-27/add_invoice_items_metadata_and_period.md)
- [Adds support for third-party tax on flexible billing mode subscriptions](https://docs.stripe.com/changelog/basil/2025-08-27/3p-tax.md)
