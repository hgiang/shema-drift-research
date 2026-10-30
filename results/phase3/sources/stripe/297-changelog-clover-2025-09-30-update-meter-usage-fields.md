# Adds pagination and updates fields for aggregated Billing meter usage data

## What’s new

Adds pagination to aggregated Billing meter usage data and updates field names for consistency with other Stripe APIs.

## Why is this a breaking change?

We renamed some request parameters and response fields.

The request changes are as follows:

- `start_time` is now [starts_at](https://docs.stripe.com/api/billing/analytics/meter-usage/retrieves.md?api-version=2025-09-30.preview#retrieves_billing_analytics_meter_usage-starts_at)
- `end_time` is now [ends_at](https://docs.stripe.com/api/billing/analytics/meter-usage/retrieves.md?api-version=2025-09-30.preview#retrieves_billing_analytics_meter_usage-ends_at)
- `meters.meter_id` is now [meters.meter](https://docs.stripe.com/api/billing/analytics/meter-usage/retrieves.md?api-version=2025-09-30.preview#retrieves_billing_analytics_meter_usage-meters-meter)

The response changes are as follows:

- `data_refreshed_at` is now [refreshed_at](https://docs.stripe.com/api/billing/analytics/meter-usage/object.md?api-version=2025-09-30.preview#billing_analytics_meter_usage_object-refreshed_at)

The `data` object is now nested inside [rows](https://docs.stripe.com/api/billing/analytics/meter-usage/object.md?api-version=2025-09-30.preview#billing_analytics_meter_usage_object-rows), which includes pagination details. Within the `data` field, the response changes are as follows:

- `bucket_start_time` is now [starts_at](https://docs.stripe.com/api/billing/analytics/meter-usage/object.md?api-version=2025-09-30.preview#billing_analytics_meter_usage_object-rows-data-starts_at)
- `bucket_end_time` is now [ends_at](https://docs.stripe.com/api/billing/analytics/meter-usage/object.md?api-version=2025-09-30.preview#billing_analytics_meter_usage_object-rows-data-ends_at)
- `bucket_value` is now [value](https://docs.stripe.com/api/billing/analytics/meter-usage/object.md?api-version=2025-09-30.preview#billing_analytics_meter_usage_object-rows-data-value)
- `meter_id` is now [meter](https://docs.stripe.com/api/billing/analytics/meter-usage/object.md?api-version=2025-09-30.preview#billing_analytics_meter_usage_object-rows-data-meter)

## Impact

When you upgrade to this API version, you can use the pagination features to access more of your meter usage data.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `ends_at`, `starts_at` | Added | [Billing.Analytics.MeterUsage#retrieve](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview), `Billing.Analytics.MeterUsageRow` |
| `meter` | Added | [Billing.Analytics.MeterUsage#retrieve.meters[]](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview), `Billing.Analytics.MeterUsageRow` |
| `value` | Added | `Billing.Analytics.MeterUsageRow` |
| `bucket_end_time`, `bucket_start_time`, `bucket_value` | Removed | `Billing.Analytics.MeterUsageRow` |
| `meter_id` | Removed | [Billing.Analytics.MeterUsage#retrieve.meters[]](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview), `Billing.Analytics.MeterUsageRow` |
| `end_time`, `start_time` | Removed | [Billing.Analytics.MeterUsage#retrieve](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview) |
| `refreshed_at`, `rows` | Added | [Billing.Analytics.MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |
| `data`, `data_refreshed_at` | Removed | [Billing.Analytics.MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `ends_at`, `starts_at` | Added | [Billing::Analytics::MeterUsage::RetrieveParams](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview), `Billing::Analytics::MeterUsageRow` |
| `meter` | Added | [Billing::Analytics::MeterUsage::RetrieveParams::Meter](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview), `Billing::Analytics::MeterUsageRow` |
| `value` | Added | `Billing::Analytics::MeterUsageRow` |
| `bucket_end_time`, `bucket_start_time`, `bucket_value` | Removed | `Billing::Analytics::MeterUsageRow` |
| `meter_id` | Removed | [Billing::Analytics::MeterUsage::RetrieveParams::Meter](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview), `Billing::Analytics::MeterUsageRow` |
| `end_time`, `start_time` | Removed | [Billing::Analytics::MeterUsage::RetrieveParams](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview) |
| `refreshed_at`, `rows` | Added | [Billing::Analytics::MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |
| `data`, `data_refreshed_at` | Removed | [Billing::Analytics::MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `ends_at`, `starts_at` | Added | `Billing.Analytics.MeterUsageRow`, [billing.analytics.MeterUsage.RetrieveParams](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview) |
| `meter` | Added | `Billing.Analytics.MeterUsageRow`, [billing.analytics.MeterUsage.RetrieveParamsMeter](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview) |
| `value` | Added | `Billing.Analytics.MeterUsageRow` |
| `bucket_end_time`, `bucket_start_time`, `bucket_value` | Removed | `Billing.Analytics.MeterUsageRow` |
| `meter_id` | Removed | `Billing.Analytics.MeterUsageRow`, [billing.analytics.MeterUsage.RetrieveParamsMeter](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview) |
| `end_time`, `start_time` | Removed | [billing.analytics.MeterUsage.RetrieveParams](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview) |
| `refreshed_at`, `rows` | Added | [Billing.Analytics.MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |
| `data`, `data_refreshed_at` | Removed | [Billing.Analytics.MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `ends_at`, `starts_at` | Added | `Billing.Analytics.MeterUsageRow`, [Billing\Analytics\MeterUsage.retrieve().$params](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview) |
| `meter` | Added | `Billing.Analytics.MeterUsageRow`, [Billing\Analytics\MeterUsage.retrieve().$params.meter](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview) |
| `value` | Added | `Billing.Analytics.MeterUsageRow` |
| `bucket_end_time`, `bucket_start_time`, `bucket_value` | Removed | `Billing.Analytics.MeterUsageRow` |
| `meter_id` | Removed | `Billing.Analytics.MeterUsageRow`, [Billing\Analytics\MeterUsage.retrieve().$params.meter](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview) |
| `end_time`, `start_time` | Removed | [Billing\Analytics\MeterUsage.retrieve().$params](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview) |
| `refreshed_at`, `rows` | Added | [Billing.Analytics.MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |
| `data`, `data_refreshed_at` | Removed | [Billing.Analytics.MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `endsAt`, `startsAt` | Added | [billing.analytics.MeterUsageRetrieveParams](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview), `billing.analytics.MeterUsageRow` |
| `meter` | Added | [billing.analytics.MeterUsageRetrieveParams.meters[]](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview), `billing.analytics.MeterUsageRow` |
| `value` | Added | `billing.analytics.MeterUsageRow` |
| `bucketEndTime`, `bucketStartTime`, `bucketValue` | Removed | `billing.analytics.MeterUsageRow` |
| `meterId` | Removed | [billing.analytics.MeterUsageRetrieveParams.meters[]](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview), `billing.analytics.MeterUsageRow` |
| `endTime`, `startTime` | Removed | [billing.analytics.MeterUsageRetrieveParams](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview) |
| `refreshedAt`, `rows` | Added | [billing.analytics.MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |
| `data`, `dataRefreshedAt` | Removed | [billing.analytics.MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `ends_at`, `starts_at` | Added | [Billing.Analytics.MeterUsageRetrieveParams](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview), `Billing.Analytics.MeterUsageRow` |
| `meter` | Added | [Billing.Analytics.MeterUsageRetrieveParams.meters[]](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview), `Billing.Analytics.MeterUsageRow` |
| `value` | Added | `Billing.Analytics.MeterUsageRow` |
| `bucket_end_time`, `bucket_start_time`, `bucket_value` | Removed | `Billing.Analytics.MeterUsageRow` |
| `meter_id` | Removed | [Billing.Analytics.MeterUsageRetrieveParams.meters[]](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview), `Billing.Analytics.MeterUsageRow` |
| `end_time`, `start_time` | Removed | [Billing.Analytics.MeterUsageRetrieveParams](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview) |
| `refreshed_at`, `rows` | Added | [Billing.Analytics.MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |
| `data`, `data_refreshed_at` | Removed | [Billing.Analytics.MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `EndsAt`, `StartsAt` | Added | [BillingAnalyticsMeterUsageParams](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview), `BillingAnalyticsMeterUsageRow` |
| `Meter` | Added | [BillingAnalyticsMeterUsageMeterParams](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview), `BillingAnalyticsMeterUsageRow` |
| `Value` | Added | `BillingAnalyticsMeterUsageRow` |
| `BucketEndTime`, `BucketStartTime`, `BucketValue` | Removed | `BillingAnalyticsMeterUsageRow` |
| `MeterID` | Removed | [BillingAnalyticsMeterUsageMeterParams](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview), `BillingAnalyticsMeterUsageRow` |
| `EndTime`, `StartTime` | Removed | [BillingAnalyticsMeterUsageParams](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview) |
| `RefreshedAt`, `Rows` | Added | [BillingAnalyticsMeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |
| `Data`, `DataRefreshedAt` | Removed | [BillingAnalyticsMeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `EndsAt`, `StartsAt` | Added | [Billing.Analytics.MeterUsageGetOptions](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview), `Billing.Analytics.MeterUsageRow` |
| `Meter` | Added | `Billing.Analytics.MeterUsageRow`, [BillingAnalyticsMeterUsageMeterOptions](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview) |
| `Value` | Added | `Billing.Analytics.MeterUsageRow` |
| `BucketEndTime`, `BucketStartTime`, `BucketValue` | Removed | `Billing.Analytics.MeterUsageRow` |
| `MeterId` | Removed | `Billing.Analytics.MeterUsageRow`, [BillingAnalyticsMeterUsageMeterOptions](/api/billing/analytics/meter-usage/retrieves-meters?api-version=2025-09-30.preview) |
| `EndTime`, `StartTime` | Removed | [Billing.Analytics.MeterUsageGetOptions](/api/billing/analytics/meter-usage/retrieves?api-version=2025-09-30.preview) |
| `RefreshedAt`, `Rows` | Added | [Billing.Analytics.MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |
| `Data`, `DataRefreshedAt` | Removed | [Billing.Analytics.MeterUsage](/api/billing/analytics/meter-usage/object?api-version=2025-09-30.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-09-30.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v16.1.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v16.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.1.2b1](https://github.com/stripe/stripe-python/releases/tag/v13.1.2b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.1.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v18.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.1.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v30.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.2.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v19.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.1.0-beta.1](https://github.com/stripe/stripe-go/releases/tag/v83.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.1.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v49.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds the ability to update automatic tax, invoice creation and invoice settings for Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-sessions-tax-and-invoice-settings.md)
- [Enables prebilling for subscriptions](https://docs.stripe.com/changelog/clover/2025-09-30/subscriptions-prebilling.md)
- [Adds the unit label parameter to the product data hash](https://docs.stripe.com/changelog/clover/2025-09-30/add-product-data-unit-label-preview.md)
