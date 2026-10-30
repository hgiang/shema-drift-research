# Adds events for reserve holds, releases and plans

## What’s new

Adds support for receiving real-time notifications about changes to [Reserve Holds](https://docs.stripe.com/api/reserve/hold.md?api-version=2026-02-25.clover), [Reserve Releases](https://docs.stripe.com/api/reserve/release.md?api-version=2026-02-25.clover) and [Reserve Plans](https://docs.stripe.com/api/reserve/plan.md?api-version=2026-02-25.clover) associated with reserved funds on accounts.

- [reserve.hold.created](https://docs.stripe.com/api/events/types.md?api-version=2026-02-25.clover#event_types-reserve.hold.created): occurs when a `ReserveHold` is created.
- [reserve.hold.updated](https://docs.stripe.com/api/events/types.md?api-version=2026-02-25.clover#event_types-reserve.hold.updated): occurs when a `ReserveHold` is updated.
- [reserve.release.created](https://docs.stripe.com/api/events/types.md?api-version=2026-02-25.clover#event_types-reserve.release.created): occurs when a `ReserveRelease` is created.
- [reserve.plan.created](https://docs.stripe.com/api/events/types.md?api-version=2026-02-25.clover#event_types-reserve.plan.created): occurs when a `ReservePlan` is created.
- [reserve.plan.updated](https://docs.stripe.com/api/events/types.md?api-version=2026-02-25.clover#event_types-reserve.plan.updated): occurs when a `ReservePlan` is updated.
- [reserve.plan.expired](https://docs.stripe.com/api/events/types.md?api-version=2026-02-25.clover#event_types-reserve.plan.expired): occurs when a `ReservePlan` expires.
- [reserve.plan.disabled](https://docs.stripe.com/api/events/types.md?api-version=2026-02-25.clover#event_types-reserve.plan.disabled): occurs when a `ReservePlan` is disabled.

## Impact

You can use these new events to programmatically monitor holds, releases and plan configurations associated with reserved funds on accounts.

## Changes

#### REST API

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [Reserve.Hold](/api/reserve/hold/object?api-version=2026-02-25.clover), [Reserve.Plan](/api/reserve/plan/object?api-version=2026-02-25.clover), [Reserve.Release](/api/reserve/release/object?api-version=2026-02-25.clover) |

| Values | Change | Enums |
| --- | --- | --- |
| `reserve.hold.created`, `reserve.hold.updated`, `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, `reserve.plan.updated`, `reserve.release.created` | Added | [Event](/api/events/object?api-version=2026-02-25.clover#event_object-type), [WebhookEndpoint#update](/api/webhook_endpoints/update?api-version=2026-02-25.clover#update_webhook_endpoint-enabled_events), [WebhookEndpoint#create](/api/webhook_endpoints/update?api-version=2026-02-25.clover#update_webhook_endpoint-enabled_events) |

|  | Change | Event types |
| --- | --- | --- |
| `reserve.hold.created`, `reserve.hold.updated` | Added | `Reserve.Hold` |
| `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, `reserve.plan.updated` | Added | `Reserve.Plan` |
| `reserve.release.created` | Added | `Reserve.Release` |

#### Ruby

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [Reserve::Hold](/api/reserve/hold/object?api-version=2026-02-25.clover), [Reserve::Plan](/api/reserve/plan/object?api-version=2026-02-25.clover), [Reserve::Release](/api/reserve/release/object?api-version=2026-02-25.clover) |

#### Python

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [reserve.Hold](/api/reserve/hold/object?api-version=2026-02-25.clover), [reserve.Plan](/api/reserve/plan/object?api-version=2026-02-25.clover), [reserve.Release](/api/reserve/release/object?api-version=2026-02-25.clover) |

| Values | Change | Enums |
| --- | --- | --- |
| `reserve.hold.created`, `reserve.hold.updated`, `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, `reserve.plan.updated`, `reserve.release.created` | Added | [Event](/api/events/object?api-version=2026-02-25.clover#event_object-type), [WebhookEndpointModifyParams](/api/webhook_endpoints/update?api-version=2026-02-25.clover#update_webhook_endpoint-enabled_events), [WebhookEndpointCreateParams](/api/webhook_endpoints/update?api-version=2026-02-25.clover#update_webhook_endpoint-enabled_events) |

|  | Change | Event types |
| --- | --- | --- |
| `reserve.hold.created`, `reserve.hold.updated` | Added | `reserve.Hold` |
| `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, `reserve.plan.updated` | Added | `reserve.Plan` |
| `reserve.release.created` | Added | `reserve.Release` |

#### PHP

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [Reserve.Hold](/api/reserve/hold/object?api-version=2026-02-25.clover), [Reserve.Plan](/api/reserve/plan/object?api-version=2026-02-25.clover), [Reserve.Release](/api/reserve/release/object?api-version=2026-02-25.clover) |

| Values | Change | Enum |
| --- | --- | --- |
| `reserve.hold.created`, `reserve.hold.updated`, `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, `reserve.plan.updated`, `reserve.release.created` | Added | [Event](/api/events/object?api-version=2026-02-25.clover#event_object-type) |

|  | Change | Event types |
| --- | --- | --- |
| `RESERVE_HOLD_CREATED`, `RESERVE_HOLD_UPDATED` | Added | `Reserve.Hold` |
| `RESERVE_PLAN_CREATED`, `RESERVE_PLAN_DISABLED`, `RESERVE_PLAN_EXPIRED`, `RESERVE_PLAN_UPDATED` | Added | `Reserve.Plan` |
| `RESERVE_RELEASE_CREATED` | Added | `Reserve.Release` |

#### Java

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [reserve.Hold](/api/reserve/hold/object?api-version=2026-02-25.clover), [reserve.Plan](/api/reserve/plan/object?api-version=2026-02-25.clover), [reserve.Release](/api/reserve/release/object?api-version=2026-02-25.clover) |

| Values | Change | Enums |
| --- | --- | --- |
| `reserve.hold.created`, `reserve.hold.updated`, `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, `reserve.plan.updated`, `reserve.release.created` | Added | [WebhookEndpointUpdateParams](/api/webhook_endpoints/update?api-version=2026-02-25.clover#update_webhook_endpoint-enabledEvents), [WebhookEndpointCreateParams](/api/webhook_endpoints/update?api-version=2026-02-25.clover#update_webhook_endpoint-enabledEvents) |

|  | Change | Event types |
| --- | --- | --- |
| `reserve.hold.created`, `reserve.hold.updated` | Added | `reserve.Hold` |
| `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, `reserve.plan.updated` | Added | `reserve.Plan` |
| `reserve.release.created` | Added | `reserve.Release` |

#### Node.js

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [Reserve.Hold](/api/reserve/hold/object?api-version=2026-02-25.clover), [Reserve.Plan](/api/reserve/plan/object?api-version=2026-02-25.clover), [Reserve.Release](/api/reserve/release/object?api-version=2026-02-25.clover) |

| Values | Change | Enums |
| --- | --- | --- |
| `reserve.hold.created`, `reserve.hold.updated`, `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, `reserve.plan.updated`, `reserve.release.created` | Added | [Event](/api/events/object?api-version=2026-02-25.clover#event_object-type), [WebhookEndpointUpdateParams](/api/webhook_endpoints/update?api-version=2026-02-25.clover#update_webhook_endpoint-enabled_events), [WebhookEndpointCreateParams](/api/webhook_endpoints/update?api-version=2026-02-25.clover#update_webhook_endpoint-enabled_events) |

|  | Change | Event types |
| --- | --- | --- |
| `ReserveHoldCreatedEvent`, `ReserveHoldUpdatedEvent` | Added | `Reserve.Hold` |
| `ReservePlanCreatedEvent`, `ReservePlanDisabledEvent`, `ReservePlanExpiredEvent`, `ReservePlanUpdatedEvent` | Added | `Reserve.Plan` |
| `ReserveReleaseCreatedEvent` | Added | `Reserve.Release` |

#### Go

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [ReserveHold](/api/reserve/hold/object?api-version=2026-02-25.clover), [ReservePlan](/api/reserve/plan/object?api-version=2026-02-25.clover), [ReserveRelease](/api/reserve/release/object?api-version=2026-02-25.clover) |

| Values | Change | Enum |
| --- | --- | --- |
| `reserve.hold.created`, `reserve.hold.updated`, `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, `reserve.plan.updated`, `reserve.release.created` | Added | [Event](/api/events/object?api-version=2026-02-25.clover#event_object-Type) |

|  | Change | Event types |
| --- | --- | --- |
| `EventTypeReserveHoldCreated`, `EventTypeReserveHoldUpdated` | Added | `ReserveHold` |
| `EventTypeReservePlanCreated`, `EventTypeReservePlanDisabled`, `EventTypeReservePlanExpired`, `EventTypeReservePlanUpdated` | Added | `ReservePlan` |
| `EventTypeReserveReleaseCreated` | Added | `ReserveRelease` |

#### .NET

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [Reserve.Hold](/api/reserve/hold/object?api-version=2026-02-25.clover), [Reserve.Plan](/api/reserve/plan/object?api-version=2026-02-25.clover), [Reserve.Release](/api/reserve/release/object?api-version=2026-02-25.clover) |

|  | Change | Event types |
| --- | --- | --- |
| `ReserveHoldCreated`, `ReserveHoldUpdated` | Added | `Reserve.Hold` |
| `ReservePlanCreated`, `ReservePlanDisabled`, `ReservePlanExpired`, `ReservePlanUpdated` | Added | `Reserve.Plan` |
| `ReserveReleaseCreated` | Added | `Reserve.Release` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-02-25.clover`
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

## Related changes

- [Adds display name and service user number to Bacs Direct Debit mandates](https://docs.stripe.com/changelog/clover/2026-02-25/display-name-and-service-user-number.md)
- [Adds transaction purpose to PaymentIntents for US bank account payments](https://docs.stripe.com/changelog/clover/2026-02-25/us-bank-account-payments-transaction-purpose.md)
- [Makes Boleto tax ID nullable in payment method details for Payment Records](https://docs.stripe.com/changelog/clover/2026-02-25/makes-tax-id-field-nullable-in-boleto-payment-method-details.md)
