# Adds support for Azure Event Grid as an event destination

## What’s new

Stripe now supports [Azure Event Grid](https://docs.microsoft.com/en-us/azure/event-grid/) as an [event destination](https://docs.stripe.com/events/how-events-work.md?api-version=2026-03-25.preview) type.

This release adds the `azure_event_grid` value to the [type](https://docs.stripe.com/api/v2/core/event-destinations/object.md?api-version=2026-03-25.preview#v2_event_destination_object-type) enum for event destinations. When creating an event destination with this type, you can specify Azure Event Grid configuration details using the [azure_event_grid](https://docs.stripe.com/api/v2/core/event-destinations/object.md?api-version=2026-03-25.preview#v2_event_destination_object-azure_event_grid) parameter.

## Impact

You can now send Stripe events directly to Azure using [Azure Event Grid](https://docs.stripe.com/event-destinations/eventgrid.md?api-version=2026-03-25.preview) as a new type of destination.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `azure_event_grid` | Added | [V2.Core.EventDestination](/api/v2/core/event-destinations/object?api-version=2026-03-25.preview), [V2.Core.EventDestination#create](/api/v2/core/event-destinations/create?api-version=2026-03-25.preview) |

| Values | Change | Enums |
| --- | --- | --- |
| `no_azure_partner_topic_exists` | Added | [V2.Core.EventDestination.status_details.disabled](/api/v2/core/event-destinations/object-status_details-disabled-reason?api-version=2026-03-25.preview) |
| `azure_event_grid` | Added | [V2.Core.EventDestination](/api/v2/core/event-destinations/object-type?api-version=2026-03-25.preview), [V2.Core.EventDestination#create](/api/v2/core/event-destinations/object-type?api-version=2026-03-25.preview) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `azure_event_grid` | Added | [V2::Core::EventDestination](/api/v2/core/event-destinations/object?api-version=2026-03-25.preview), [V2::Core::EventDestinationCreateParams](/api/v2/core/event-destinations/create?api-version=2026-03-25.preview) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `azure_event_grid` | Added | [V2.Core.EventDestination](/api/v2/core/event-destinations/object?api-version=2026-03-25.preview), [v2.core.EventDestinationCreateParams](/api/v2/core/event-destinations/create?api-version=2026-03-25.preview) |

| Values | Change | Enums |
| --- | --- | --- |
| `no_azure_partner_topic_exists` | Added | [V2.Core.EventDestination.StatusDetail.Disabled](/api/v2/core/event-destinations/object-status_details-disabled-reason?api-version=2026-03-25.preview) |
| `azure_event_grid` | Added | [V2.Core.EventDestination](/api/v2/core/event-destinations/object-type?api-version=2026-03-25.preview), [v2.core.EventDestinationCreateParams](/api/v2/core/event-destinations/object-type?api-version=2026-03-25.preview) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `azure_event_grid` | Added | [V2.Core.EventDestination](/api/v2/core/event-destinations/object?api-version=2026-03-25.preview), [V2\Core\EventDestination.create().$params](/api/v2/core/event-destinations/create?api-version=2026-03-25.preview) |

| Values | Change | Enums |
| --- | --- | --- |
| `no_azure_partner_topic_exists` | Added | [V2.Core.EventDestination.status_details.disabled](/api/v2/core/event-destinations/object-status_details-disabled-reason?api-version=2026-03-25.preview) |
| `azure_event_grid` | Added | [V2.Core.EventDestination](/api/v2/core/event-destinations/object-type?api-version=2026-03-25.preview) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `azureEventGrid` | Added | [v2.core.EventDestination](/api/v2/core/event-destinations/object?api-version=2026-03-25.preview), [v2.core.EventDestinationCreateParams](/api/v2/core/event-destinations/create?api-version=2026-03-25.preview) |

| Value | Change | Enum |
| --- | --- | --- |
| `azure_event_grid` | Added | [v2.core.EventDestinationCreateParams](/api/v2/core/event-destinations/create-type?api-version=2026-03-25.preview) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `azure_event_grid` | Added | [V2.Core.EventDestination](/api/v2/core/event-destinations/object?api-version=2026-03-25.preview), [V2.Core.EventDestinationCreateParams](/api/v2/core/event-destinations/create?api-version=2026-03-25.preview) |

| Values | Change | Enums |
| --- | --- | --- |
| `no_azure_partner_topic_exists` | Added | [V2.Core.EventDestination.status_details.disabled](/api/v2/core/event-destinations/object-status_details-disabled-reason?api-version=2026-03-25.preview) |
| `azure_event_grid` | Added | [V2.Core.EventDestination](/api/v2/core/event-destinations/object-type?api-version=2026-03-25.preview), [V2.Core.EventDestinationCreateParams](/api/v2/core/event-destinations/object-type?api-version=2026-03-25.preview) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AzureEventGrid` | Added | [V2CoreEventDestination](/api/v2/core/event-destinations/object?api-version=2026-03-25.preview), [V2CoreEventDestinationParams](/api/v2/core/event-destinations/create?api-version=2026-03-25.preview) |

| Values | Change | Enums |
| --- | --- | --- |
| `no_azure_partner_topic_exists` | Added | [V2CoreEventDestinationStatusDetailsDisabled](/api/v2/core/event-destinations/object-status_details-disabled-Reason?api-version=2026-03-25.preview) |
| `azure_event_grid` | Added | [V2CoreEventDestination](/api/v2/core/event-destinations/object-Type?api-version=2026-03-25.preview) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AzureEventGrid` | Added | [V2.Core.EventDestination](/api/v2/core/event-destinations/object?api-version=2026-03-25.preview), [V2.Core.EventDestinationCreateOptions](/api/v2/core/event-destinations/create?api-version=2026-03-25.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-03-25.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
