# Expands Reserve Plan listing access and adds filters

## What’s new

Direct accounts and connected accounts with API access can now [List Reserve Plans](https://docs.stripe.com/api/reserve/plan/list.md?api-version=2026-09-30.preview).

You can now optionally use the [destination](https://docs.stripe.com/api/reserve/plan/list.md?api-version=2026-09-30.preview#list_reserve_plans-destination) and [status](https://docs.stripe.com/api/reserve/plan/list.md?api-version=2026-09-30.preview#list_reserve_plans-status) filter parameters when you [List Reserve Plans](https://docs.stripe.com/api/reserve/plan/list.md?api-version=2026-09-30.preview).

For changes to destination properties and Reserve Plan enum values, see the [2026-09-30.endive GA changelog](https://docs.stripe.com/changelog/endive/2026-09-30/settlement-reserve-api.md).

## Why is this a breaking change?

Previously, [Listing Reserve Plans](https://docs.stripe.com/api/reserve/plan/list.md?api-version=2026-09-30.preview) only returned risk reserve plans. It now returns plans across all destinations when the [destination](https://docs.stripe.com/api/reserve/plan/list.md?api-version=2026-09-30.preview#list_reserve_plans-destination) parameter isn’t set. Integrations that assume all returned plans are risk reserves must account for the broader results or filter by destination.

## Impact

When upgrading, set the [destination](https://docs.stripe.com/api/reserve/plan/list.md?api-version=2026-09-30.preview#list_reserve_plans-destination) parameter to `risk_reserved` if your integration expects only risk reserve plans when [Listing Reserve Plans](https://docs.stripe.com/api/reserve/plan/list.md?api-version=2026-09-30.preview).

## Changes

#### REST API

| Endpoint | Change | Resource |
| --- | --- | --- |
| `list` | Added | [Reserve.Plan](/api/reserve/plan/object?api-version=2026-09-30.preview#reserve_plan_object) |

#### Ruby

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [Reserve::Plan](/api/reserve/plan/object?api-version=2026-09-30.preview#reserve_plan_object) |

#### Python

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [reserve.Plan](/api/reserve/plan/object?api-version=2026-09-30.preview#reserve_plan_object) |

#### PHP

| Method | Change | Resource |
| --- | --- | --- |
| `all` | Added | [Reserve.Plan](/api/reserve/plan/object?api-version=2026-09-30.preview#reserve_plan_object) |

#### Java

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [reserve.Plan](/api/reserve/plan/object?api-version=2026-09-30.preview#reserve_plan_object) |

#### Node.js

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [Reserve.Plan](/api/reserve/plan/object?api-version=2026-09-30.preview#reserve_plan_object) |

#### Go

| Method | Change | Resource |
| --- | --- | --- |
| `List` | Added | [ReservePlan](/api/reserve/plan/object?api-version=2026-09-30.preview#reserve_plan_object) |

#### .NET

| Method | Change | Resource |
| --- | --- | --- |
| `List` | Added | [Reserve.Plan](/api/reserve/plan/object?api-version=2026-09-30.preview#reserve_plan_object) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.preview`
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

- [Updates the shapes of v2 Financial Address and v2 Received Credit objects](https://docs.stripe.com/changelog/endive/2026-09-30/financial-address-and-received-credit-shape-updates.md)
- [Removes level property from inbound transfer history and changes date filtering syntax for list endpoints](https://docs.stripe.com/changelog/endive/2026-09-30/removes-level-property-from-inbound-transfer-history-and-changes-date-filtering-syntax-for-list-endpoints.md)
- [Moves Financial Address test helper endpoints to the money management namespace](https://docs.stripe.com/changelog/endive/2026-09-30/moves-financial-address-test-helper-endpoints-to-the-money-management-namespace.md)
- [Opens the adjusted flow type enum and changes the list filters for v2 Adjustments and v2 Transactions](https://docs.stripe.com/changelog/endive/2026-09-30/opens-adjusted-flow-type-enum-and-changes-date-filtering-syntax.md)
- [Updates Financial Address request and response structure](https://docs.stripe.com/changelog/endive/2026-09-30/updating-financial-address-request-and-response-structure.md)
- [Adds a Treasury Transaction property to the Money Management Transaction update events](https://docs.stripe.com/changelog/endive/2026-09-30/treasury-transaction-property-for-money-management-transaction-update-events.md)
- [Adds deposit insurance eligibility details to Financial Accounts](https://docs.stripe.com/changelog/endive/2026-09-30/includable-insurance-eligibility-field-for-v2-financial-accounts.md)
- [Adds network fee details to estimated fees on Outbound Payment Quotes](https://docs.stripe.com/changelog/endive/2026-09-30/adds-network-fee-details-to-estimated-fees.md)
