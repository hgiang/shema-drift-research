# Adds the restricted property to the Payout Method object

## What’s new

Adds the [restricted](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=2026-03-25.preview#v2_payout_method_object-restricted) boolean property to the [v2 Payout Method](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=2026-03-25.preview) object. If the `restricted` value is true, the payout method has restrictions that prevent it from being used for payouts.

## Impact

You can now check the `restricted` status of payout methods in your integration. A payout method can be restricted from use even if it’s correctly set up. For example, it might be on a denylist.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `restricted` | Added | [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `restricted` | Added | [V2::MoneyManagement::PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `restricted` | Added | [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `restricted` | Added | [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `restricted` | Added | [v2.moneymanagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `restricted` | Added | [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Restricted` | Added | [V2MoneyManagementPayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Restricted` | Added | [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview) |

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

## Related changes

- [Adds multicurrency support for v2 payout methods](https://docs.stripe.com/changelog/dahlia/2026-03-25/multicurrency-v2-payout-methods.md)
- [Restricts Accounts v2 identity properties for some Global Payouts use cases](https://docs.stripe.com/changelog/dahlia/2026-03-25/accounts-identity-fields-global-payouts.md)
- [Expands Global Payouts cross-border payout destinations to three additional countries](https://docs.stripe.com/changelog/dahlia/2026-03-25/cross-border-payouts-new-countries.md)
