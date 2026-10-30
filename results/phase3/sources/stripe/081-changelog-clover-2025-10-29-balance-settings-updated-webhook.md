# Adds a webhook event type for updates to the balance settings for connected accounts

## What’s new

Adds a [balance_settings.updated](https://docs.stripe.com/api/events/types.md?api-version=2025-10-29.clover#event_types-balance_settings.updated) webhook event type. Stripe sends this event when the [Balance Settings](https://docs.stripe.com/api/balance-settings.md?api-version=2025-10-29.clover) for a connected account changes.

## Impact

You can now retrieve or listen to [balance_settings.updated](https://docs.stripe.com/api/events/types.md?api-version=2025-10-29.clover#event_types-balance_settings.updated) events. Balance Settings specify options for customising account balances and payouts of a connected account.

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `balance_settings.updated` | Added | [Event](/api/events/object?api-version=2025-10-29.clover#event_object-type) |
| `balance_settings.updated` | Added | [WebhookEndpoint#update](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabled_events), [WebhookEndpoint#create](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabled_events) |

|  | Change | Event type |
| --- | --- | --- |
| `balance_settings.updated` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-10-29.clover) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `balance_settings.updated` | Added | [Event](/api/events/object?api-version=2025-10-29.clover#event_object-type) |
| `balance_settings.updated` | Added | [WebhookEndpoint.ModifyParams](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabled_events), [WebhookEndpoint.CreateParams](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabled_events) |

|  | Change | Event type |
| --- | --- | --- |
| `balance_settings.updated` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-10-29.clover) |

#### PHP

| Value | Change | Enum |
| --- | --- | --- |
| `balance_settings.updated` | Added | [Event](/api/events/object?api-version=2025-10-29.clover#event_object-type) |

|  | Change | Event type |
| --- | --- | --- |
| `BALANCE_SETTINGS_UPDATED` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-10-29.clover) |

#### Java

| Value | Change | Enums |
| --- | --- | --- |
| `balance_settings.updated` | Added | [WebhookEndpointUpdateParams](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabledEvents), [WebhookEndpointCreateParams](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabledEvents) |

|  | Change | Event type |
| --- | --- | --- |
| `balance_settings.updated` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-10-29.clover) |

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `balance_settings.updated` | Added | [Event](/api/events/object?api-version=2025-10-29.clover#event_object-type) |
| `balance_settings.updated` | Added | [WebhookEndpointUpdateParams](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabled_events), [WebhookEndpointCreateParams](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabled_events) |

|  | Change | Event type |
| --- | --- | --- |
| `BalanceSettingsUpdatedEvent` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-10-29.clover) |

#### Go

| Value | Change | Enum |
| --- | --- | --- |
| `balance_settings.updated` | Added | [Event](/api/events/object?api-version=2025-10-29.clover#event_object-Type) |

|  | Change | Event type |
| --- | --- | --- |
| `EventTypeBalanceSettingsUpdated` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-10-29.clover) |

#### .NET

|  | Change | Event type |
| --- | --- | --- |
| `BalanceSettingsUpdated` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-10-29.clover) |

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

- [Adds the ability to upload your platform’s terms of service agreement](https://docs.stripe.com/changelog/clover/2025-10-29/upload-file-terms-of-service.md)
- [Adds the ability to attest to an Account’s authorised company representative](https://docs.stripe.com/changelog/clover/2025-10-29/representative-declaration.md)
