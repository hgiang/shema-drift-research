# Adds health alerts for when events fail to generate

## What’s new

Adds the [v2.core.health.event_generation_failure.resolved](https://docs.stripe.com/api/v2/core/events/event-types.md?api-version=2025-11-17.preview#v2_event_types-v2.core.health.event_generation_failure.resolved) webhook event type. This event occurs when Stripe fails to generate events for your webhook endpoints and then resolves the issue.

## Why is this a breaking change?

This public preview includes several breaking changes from the private preview:

- Replaces the `related_object_id` with the [related_object](https://docs.stripe.com/api/v2/core/events/event-types.md?api-version=2025-11-17.preview#v2_event_types-v2.core.health.event_generation_failure.resolved-related_object) hash, which contains `id`, `type`, and `url` properties. This makes it easier to retrieve related objects.
- Removes the `missing_delivery_attempts` property. If your integration depends on this value, remove that dependency.
- Since [livemode](https://docs.stripe.com/api/v2/core/events/event-types.md?api-version=2025-11-17.preview#v2_event_types-v2.core.health.event_generation_failure.resolved-livemode) already exists at the top level of the [Event](https://docs.stripe.com/api/v2/core/events/object.md?api-version=2025-11-17.preview) object, this release removes the `livemode` property from the [impact](https://docs.stripe.com/api/v2/core/events/event-types.md?api-version=2025-11-17.preview#v2_event_types-v2.core.health.event_generation_failure.resolved-data-impact) hash. Update how your integration reads the property.

- The [context](https://docs.stripe.com/api/v2/core/events/event-types.md?api-version=2025-11-17.preview#v2_event_types-v2.core.health.event_generation_failure.resolved-context) property replaces the `account` property. Update your integration to use `context` instead of `account`.

These changes ensure that the alert more consistently follows the standardised structure of other [thin events](https://docs.stripe.com/events/how-events-work.md#event-formats) and simplify reading the related object.

## Impact

You can now subscribe to the `v2.core.health.event_generation_failure.resolved` webhook event to receive notifications when Stripe resolves event generation issues for your webhook endpoints. You can use this to proactively monitor and [troubleshoot webhook delivery problems](https://docs.stripe.com/webhooks.md#debugging).

## Changes

#### REST API

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreHealthEventGenerationFailureResolvedEvent` | Added | `` |

#### Ruby

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreHealthEventGenerationFailureResolvedEvent` | Added | `` |

#### Python

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreHealthEventGenerationFailureResolvedEvent` | Added | `` |

#### PHP

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreHealthEventGenerationFailureResolvedEvent` | Added | `` |

#### Java

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreHealthEventGenerationFailureResolvedEvent` | Added | `` |

#### Node.js

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreHealthEventGenerationFailureResolvedEvent` | Added | `` |

#### Go

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreHealthEventGenerationFailureResolvedEvent` | Added | `` |

#### .NET

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreHealthEventGenerationFailureResolvedEvent` | Added | `` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-11-17.preview`
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
