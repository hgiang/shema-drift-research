# Adds information about upcoming deactivations to the Financial Connections Account object

## What’s new

Adds information about upcoming deactivations in the new [status_details.active](https://docs.stripe.com/api/financial_connections/accounts/object.md?api-version=2026-06-24.dahlia#financial_connections_account_object-status_details-active) property of the [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts/object.md?api-version=2026-06-24.dahlia) object, with fields such as [expected_deactivation_date](https://docs.stripe.com/api/financial_connections/accounts/object.md?api-version=2026-06-24.dahlia#financial_connections_account_object-status_details-active-expected_deactivation_date), [cause](https://docs.stripe.com/api/financial_connections/accounts/object.md?api-version=2026-06-24.dahlia#financial_connections_account_object-status_details-active-cause), and [action](https://docs.stripe.com/api/financial_connections/accounts/object.md?api-version=2026-06-24.dahlia#financial_connections_account_object-status_details-active-action) describing when and why an account is expected to become `inactive`.

## Impact

You can now access information about upcoming deactivations on the Financial Connections Account object and in new webhooks. This lets you prepare for these events—for example, by asking users to reauthenticate their accounts to avoid interruptions in data access. Learn more about [managing inactive accounts](https://docs.stripe.com/financial-connections/inactive-accounts.md).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `status_details` | Added | [FinancialConnections.Account](/api/financial_connections/accounts/object?api-version=2026-06-24.dahlia#financial_connections_account_object) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `status_details` | Added | [FinancialConnections::Account](/api/financial_connections/accounts/object?api-version=2026-06-24.dahlia#financial_connections_account_object) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `status_details` | Added | [FinancialConnections.Account](/api/financial_connections/accounts/object?api-version=2026-06-24.dahlia#financial_connections_account_object) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `status_details` | Added | [FinancialConnections.Account](/api/financial_connections/accounts/object?api-version=2026-06-24.dahlia#financial_connections_account_object) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `statusDetails` | Added | [financialconnections.Account](/api/financial_connections/accounts/object?api-version=2026-06-24.dahlia#financial_connections_account_object) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `status_details` | Added | [FinancialConnections.Account](/api/financial_connections/accounts/object?api-version=2026-06-24.dahlia#financial_connections_account_object) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `StatusDetails` | Added | [FinancialConnectionsAccount](/api/financial_connections/accounts/object?api-version=2026-06-24.dahlia#financial_connections_account_object) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `StatusDetails` | Added | [FinancialConnections.Account](/api/financial_connections/accounts/object?api-version=2026-06-24.dahlia#financial_connections_account_object) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-06-24.dahlia`
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
