# Renames the countries filter to country on Financial Connections Sessions

## What’s new

Renames the [filters.countries](https://docs.stripe.com/api/financial_connections/sessions/create.md?api-version=2026-09-30.endive#create_financial_connections_session-filters) parameter to [filters.country](https://docs.stripe.com/api/financial_connections/sessions/create.md?api-version=2026-09-30.endive#create_financial_connections_session-filters-country) and changes its type from an array of strings to a single string when you [create a Financial Connections Session](https://docs.stripe.com/api/financial_connections/sessions/create.md?api-version=2026-09-30.endive). Previously, `filters.countries` accepted an array but used only the first element. The parameter now accepts a single country code, making this behaviour explicit.

## Why is this a breaking change?

The `filters.countries` parameter no longer exists. If your code passes an array of country codes to `filters.countries`, you must replace it with `filters.country` and provide a single country code string. Passing the old parameter name or an array value results in an error.

## Impact

If your integration passes `filters.countries` as an array when creating a [Financial Connections](https://docs.stripe.com/financial-connections.md) Session, update it to use `filters.country` with a single string value.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `country` | Added | [FinancialConnections.Session#create.filters](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |
| `countries` | Removed | [FinancialConnections.Session#create.filters](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters), [FinancialConnections.Session.filters](/api/financial_connections/sessions/object?api-version=2026-09-30.endive#financial_connections_session_object-filters) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `country` | Added | [FinancialConnections::SessionCreateParams::Filter](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |
| `countries` | Removed | [FinancialConnections::Session::Filter](/api/financial_connections/sessions/object?api-version=2026-09-30.endive#financial_connections_session_object-filters), [FinancialConnections::SessionCreateParams::Filter](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `country` | Added | [financial_connections.SessionCreateParamsFilter](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |
| `countries` | Removed | [FinancialConnections.Session.Filter](/api/financial_connections/sessions/object?api-version=2026-09-30.endive#financial_connections_session_object-filters), [financial_connections.SessionCreateParamsFilter](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `country` | Added | [FinancialConnections\Session.create().$params.filters](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |
| `countries` | Removed | [FinancialConnections.Session.filters](/api/financial_connections/sessions/object?api-version=2026-09-30.endive#financial_connections_session_object-filters), [FinancialConnections\Session.create().$params.filters](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `country` | Added | [financialconnections.SessionCreateParams.filters](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |
| `countries` | Removed | [financialconnections.Session.filters](/api/financial_connections/sessions/object?api-version=2026-09-30.endive#financial_connections_session_object-filters), [financialconnections.SessionCreateParams.filters](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `country` | Added | [FinancialConnections.SessionCreateParams.filters](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |
| `countries` | Removed | [FinancialConnections.Session.filters](/api/financial_connections/sessions/object?api-version=2026-09-30.endive#financial_connections_session_object-filters), [FinancialConnections.SessionCreateParams.filters](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Country` | Added | [FinancialConnectionsSessionFiltersParams](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |
| `Countries` | Removed | [FinancialConnectionsSessionFilters](/api/financial_connections/sessions/object?api-version=2026-09-30.endive#financial_connections_session_object-filters), [FinancialConnectionsSessionFiltersParams](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Country` | Added | [FinancialConnectionsSessionFiltersOptions](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |
| `Countries` | Removed | [FinancialConnections.Session.Filters](/api/financial_connections/sessions/object?api-version=2026-09-30.endive#financial_connections_session_object-filters), [FinancialConnectionsSessionFiltersOptions](/api/financial_connections/sessions/create?api-version=2026-09-30.endive#financial_connections_create_session-filters) |

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

- [Updates Financial Connections Session defaults](https://docs.stripe.com/changelog/endive/2026-09-30/financial-connections-session-defaults.md)
- [Adds pending and expired statuses to Financial Connections account numbers](https://docs.stripe.com/changelog/endive/2026-09-30/pending-and-expired-status-added-to-financial-connections-account-numbers.md)
