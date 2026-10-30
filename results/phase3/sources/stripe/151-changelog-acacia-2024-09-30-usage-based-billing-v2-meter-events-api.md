# Adds Meter Event v2 API endpoints

## What’s new

Introduces the [Meter Event Stream](https://docs.stripe.com/api/v2/billing-meter-stream.md?api-version=2024-09-30.acacia) /v2 resource to support high-throughput usage reporting. You can send up to 10k events per second to a meter event stream. [Contact sales](https://stripe.com/contact/sales) for higher rate-limits.

First, you must create a [Meter Event Session](https://docs.stripe.com/api/v2/billing/meter-event-sessions/create.md?api-version=2024-09-30.acacia) to get a short-lived authentication token. You can then use the session authentication token to report usage to the [Meter Event Stream](https://docs.stripe.com/api/v2/billing/meter-event-stream/create.md?api-version=2024-09-30.acacia).

Learn more about [API v2](https://docs.stripe.com/api-v2-overview.md?api-version=2024-09-30.acacia).

## Impact

This meter event stream endpoint supports up to 100,000 events per second for a single business, an increase compared to the [current /v1 endpoint](https://docs.stripe.com/api/billing/meter-event.md?api-version=2024-09-30.acacia).

## Changes

#### REST API

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia), [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

| Endpoints | Change | Resources |
| --- | --- | --- |
| `create` | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

#### Ruby

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia), [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

| Methods | Change | Resources |
| --- | --- | --- |
| `create` | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

#### Python

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia), [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

| Methods | Change | Resources |
| --- | --- | --- |
| `create` | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

#### PHP

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia), [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

| Methods | Change | Resources |
| --- | --- | --- |
| `create` | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

#### Java

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia), [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

| Methods | Change | Resources |
| --- | --- | --- |
| `create` | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

#### Node.js

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia), [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

| Methods | Change | Resources |
| --- | --- | --- |
| `create` | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `create` | Added | [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

#### Go

This change doesn’t affect the Go SDK.

#### .NET

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia), [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia), [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

| Methods | Change | Resources |
| --- | --- | --- |
| `Create` | Added | [V2.Billing.MeterEvents](/api/v2/billing-meter?api-version=2024-09-30.acacia) |
| `Create` | Added | [V2.Billing.MeterEventSession](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `Create` | Added | [V2.Billing.MeterEventStream](/api/v2/billing-meter-stream?api-version=2024-09-30.acacia) |
| `Create` | Added | [V2.Billing.MeterEventAdjustments](/api/v2/billing-meter-adjustment?api-version=2024-09-30.acacia) |

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

- [Adds contextual filters to billing alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-contextualizing-filters.md)
- [Adds an Alerts API for usage-based billing](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-api.md)
- [Adds an event for triggered billing alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-trigger-event.md)
- [Adds support for listening to triggered billing alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-webhook-listener.md)
- [Adds billing alert resources and endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-billing-alert-resources-endpoints.md)
- [Adds support for subscriptions and subscription items to billing alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-subscription-items-subscriptions.md)
