# Adds destination property and new enum values to Reserve Plans, Holds and Releases

## What’s new

Adds a [destination](https://docs.stripe.com/api/reserve/plan/object.md?api-version=2026-09-30.endive#reserve_plan_object-destination) property to all three Reserve objects. You can now identify which balance holds reserved funds and where those funds go when they’re released:

- [Reserve Plans](https://docs.stripe.com/api/reserve/plan/object.md?api-version=2026-09-30.endive#reserve_plan_object-destination) and [Reserve Holds](https://docs.stripe.com/api/reserve/hold/object.md?api-version=2026-09-30.endive#reserve_hold_object-destination) now include `destination` to indicate where reserved funds are sent. Possible values are `risk_reserved`, `settlement_reserved` and `other`. Previously, the destination was implicitly `risk_reserved`.
- [Reserve Releases](https://docs.stripe.com/api/reserve/release/object.md?api-version=2026-09-30.endive#reserve_release_object-destination) now include `destination` to indicate where released funds are sent. Possible values are `payments` and `other`. Previously, the destination was implicitly `payments`.

Reserve Plans can now represent funds that remain reserved until you disable the plan. These plans have a [type](https://docs.stripe.com/api/reserve/plan/object.md?api-version=2026-09-30.endive#reserve_plan_object-type) of `manual_release`. When this value is present, the response includes a [manual_release](https://docs.stripe.com/api/reserve/plan/object.md?api-version=2026-09-30.endive#reserve_plan_object-manual_release) property indicating that funds are released when the plan is disabled instead of on a schedule. In addition:

- The [type](https://docs.stripe.com/api/reserve/plan/object.md?api-version=2026-09-30.endive#reserve_plan_object-type) property adds `manual_release` and `other` to its existing `fixed_release` and `rolling_release` values.
- The [status](https://docs.stripe.com/api/reserve/plan/object.md?api-version=2026-09-30.endive#reserve_plan_object-status) property adds `other` to its existing `active`, `disabled` and `expired` values.

## Why is this a breaking change?

Previously, every Reserve Plan and Reserve Hold used the `risk_reserved` balance, and every Reserve Release sent funds to the `payments` balance. Those assumptions are no longer valid.

If your integration uses them for reporting, reconciliation or other reserve-specific logic, it might classify funds incorrectly unless it reads `destination` from each object.

Update your integration to check [Reserve Plan](https://docs.stripe.com/api/reserve/plan/object.md?api-version=2026-09-30.endive#reserve_plan_object-destination), [Reserve Hold](https://docs.stripe.com/api/reserve/hold/object.md?api-version=2026-09-30.endive#reserve_hold_object-destination) and [Reserve Release](https://docs.stripe.com/api/reserve/release/object.md?api-version=2026-09-30.endive#reserve_release_object-destination) for destination-specific logic.

Reserve Plans can also return new [type](https://docs.stripe.com/api/reserve/plan/object.md?api-version=2026-09-30.endive#reserve_plan_object-type) and [status](https://docs.stripe.com/api/reserve/plan/object.md?api-version=2026-09-30.endive#reserve_plan_object-status) values. Update your integration if it rejects unrecognised enum values.

## Impact

You can now represent risk and settlement reserves accurately, track where released funds are sent and recognise plans that release funds only when disabled.

Before upgrading:

- Check the `destination` property on [Reserve Plan](https://docs.stripe.com/api/reserve/plan/object.md?api-version=2026-09-30.endive#reserve_plan_object-destination), [Reserve Hold](https://docs.stripe.com/api/reserve/hold/object.md?api-version=2026-09-30.endive#reserve_hold_object-destination) and [Reserve Release](https://docs.stripe.com/api/reserve/release/object.md?api-version=2026-09-30.endive#reserve_release_object-destination) objects rather than assuming a destination.
- Support `manual_release` plans and use [manual_release](https://docs.stripe.com/api/reserve/plan/object.md?api-version=2026-09-30.endive#reserve_plan_object-manual_release) to identify their release behaviour.
- Handle the new Reserve Plan [type](https://docs.stripe.com/api/reserve/plan/object.md?api-version=2026-09-30.endive#reserve_plan_object-type) and [status](https://docs.stripe.com/api/reserve/plan/object.md?api-version=2026-09-30.endive#reserve_plan_object-status) values.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `destination` | Added | [Reserve.Hold](/api/reserve/hold/object?api-version=2026-09-30.endive#reserve_hold_object), [Reserve.Release](/api/reserve/release/object?api-version=2026-09-30.endive#reserve_release_object) |
| `destination`, `manual_release` | Added | [Reserve.Plan](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object) |

| Values | Change | Enums |
| --- | --- | --- |
| `manual_release`, `other` | Added | [Reserve.Plan.type](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object-type) |
| `other` | Added | [Reserve.Plan.status](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object-status) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `destination` | Added | [Reserve::Hold](/api/reserve/hold/object?api-version=2026-09-30.endive#reserve_hold_object), [Reserve::Release](/api/reserve/release/object?api-version=2026-09-30.endive#reserve_release_object) |
| `destination`, `manual_release` | Added | [Reserve::Plan](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `destination` | Added | [Reserve.Hold](/api/reserve/hold/object?api-version=2026-09-30.endive#reserve_hold_object), [Reserve.Release](/api/reserve/release/object?api-version=2026-09-30.endive#reserve_release_object) |
| `destination`, `manual_release` | Added | [Reserve.Plan](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object) |

| Values | Change | Enums |
| --- | --- | --- |
| `manual_release`, `other` | Added | [Reserve.Plan.type](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object-type) |
| `other` | Added | [Reserve.Plan.status](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object-status) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `destination` | Added | [Reserve.Hold](/api/reserve/hold/object?api-version=2026-09-30.endive#reserve_hold_object), [Reserve.Release](/api/reserve/release/object?api-version=2026-09-30.endive#reserve_release_object) |
| `destination`, `manual_release` | Added | [Reserve.Plan](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object) |

| Values | Change | Enums |
| --- | --- | --- |
| `manual_release`, `other` | Added | [Reserve.Plan.type](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object-type) |
| `other` | Added | [Reserve.Plan.status](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object-status) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `destination` | Added | [reserve.Hold](/api/reserve/hold/object?api-version=2026-09-30.endive#reserve_hold_object), [reserve.Release](/api/reserve/release/object?api-version=2026-09-30.endive#reserve_release_object) |
| `destination`, `manualRelease` | Added | [reserve.Plan](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `destination` | Added | [Reserve.Hold](/api/reserve/hold/object?api-version=2026-09-30.endive#reserve_hold_object), [Reserve.Release](/api/reserve/release/object?api-version=2026-09-30.endive#reserve_release_object) |
| `destination`, `manual_release` | Added | [Reserve.Plan](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object) |

| Values | Change | Enums |
| --- | --- | --- |
| `manual_release`, `other` | Added | [Reserve.Plan.type](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object-type) |
| `other` | Added | [Reserve.Plan.status](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object-status) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Destination` | Added | [ReserveHold](/api/reserve/hold/object?api-version=2026-09-30.endive#reserve_hold_object), [ReserveRelease](/api/reserve/release/object?api-version=2026-09-30.endive#reserve_release_object) |
| `Destination`, `ManualRelease` | Added | [ReservePlan](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object) |

| Values | Change | Enums |
| --- | --- | --- |
| `manual_release`, `other` | Added | [ReservePlan.Type](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object-type) |
| `other` | Added | [ReservePlan.Status](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object-status) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Destination` | Added | [Reserve.Hold](/api/reserve/hold/object?api-version=2026-09-30.endive#reserve_hold_object), [Reserve.Release](/api/reserve/release/object?api-version=2026-09-30.endive#reserve_release_object) |
| `Destination`, `ManualRelease` | Added | [Reserve.Plan](/api/reserve/plan/object?api-version=2026-09-30.endive#reserve_plan_object) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.endive`
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

- [Renames the Reserve Release reason enum value](https://docs.stripe.com/changelog/endive/2026-09-30/reserve-release-reason.md)
- [Adds support for received credits sent via the Real-Time Payments network](https://docs.stripe.com/changelog/endive/2026-09-30/rtp-network-received-credits.md)
- [Exposes ACH return codes on OutboundPayments, OutboundTransfers and InboundTransfers in v1 Treasury](https://docs.stripe.com/changelog/endive/2026-09-30/v1-treasury-ach-return-codes.md)
