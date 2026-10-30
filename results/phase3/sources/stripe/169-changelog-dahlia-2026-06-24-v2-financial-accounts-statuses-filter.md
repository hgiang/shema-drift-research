# Replaces the status filter with statuses on the List Financial Accounts endpoint

## What’s new

You can now filter [FinancialAccounts](https://docs.stripe.com/api/v2/money-management/financial-accounts.md?api-version=2026-06-24.preview) by multiple statuses in a single API call using the new [statuses](https://docs.stripe.com/api/v2/money-management/financial-accounts/list.md?api-version=2026-06-24.preview#v2_list_financial_accounts-statuses) parameter on the [List FinancialAccounts](https://docs.stripe.com/api/v2/money-management/financial-accounts/list.md?api-version=2026-06-24.preview) endpoint. For example, you can retrieve all `open` and `closed` financial accounts together without making separate requests. The statuses parameter replaces the [status](https://docs.stripe.com/api/v2/money-management/financial-accounts/list.md?api-version=2026-05-27.preview#v2_list_financial_accounts-status) parameter.

## Why is this a breaking change?

Previously, you could filter financial accounts using a singular `status` parameter. That parameter has been removed from the [List FinancialAccounts](https://docs.stripe.com/api/v2/money-management/financial-accounts/list.md?api-version=2026-06-24.preview) endpoint. Update your code to use the `statuses` array parameter instead. For example, replace `status=open` with `statuses[]=open`. This change affects all supported SDK languages (Node, Java, Go, PHP, Ruby, Python, and .NET).

## Impact

Update any existing calls to the [List FinancialAccounts](https://docs.stripe.com/api/v2/money-management/financial-accounts/list.md?api-version=2026-06-24.preview) endpoint that pass a `status` parameter to use `statuses` instead. The `statuses` parameter accepts an array, so you can filter by multiple statuses (such as `open` and `closed`) in a single request.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `statuses` | Added | [V2.MoneyManagement.FinancialAccount#list](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |
| `status` | Removed | [V2.MoneyManagement.FinancialAccount#list](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `statuses` | Added | [V2::MoneyManagement::FinancialAccountListParams](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |
| `status` | Removed | [V2::MoneyManagement::FinancialAccountListParams](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `statuses` | Added | [v2.money_management.FinancialAccountListParams](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |
| `status` | Removed | [v2.money_management.FinancialAccountListParams](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `statuses` | Added | [V2\MoneyManagement\FinancialAccount.all().$params](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |
| `status` | Removed | [V2\MoneyManagement\FinancialAccount.all().$params](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `statuses` | Added | [v2.moneymanagement.FinancialAccountListParams](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |
| `status` | Removed | [v2.moneymanagement.FinancialAccountListParams](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `statuses` | Added | [V2.MoneyManagement.FinancialAccountListParams](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |
| `status` | Removed | [V2.MoneyManagement.FinancialAccountListParams](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Statuses` | Added | [V2MoneyManagementFinancialAccountListParams](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |
| `Status` | Removed | [V2MoneyManagementFinancialAccountListParams](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Statuses` | Added | [V2.MoneyManagement.FinancialAccountListOptions](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |
| `Status` | Removed | [V2.MoneyManagement.FinancialAccountListOptions](/api/v2/money-management/financial-accounts/list?api-version=2026-06-24.preview#v2_list_financial_accounts) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-06-24.preview`
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

- [Replaces SWIFT code with BIC in Financial Addresses](https://docs.stripe.com/changelog/dahlia/2026-06-24/financial-addresses-replace-swift-with-bic.md)
- [Adds a failure reason for received debits when the debit capability is inactive](https://docs.stripe.com/changelog/dahlia/2026-06-24/received-debits-failure-reason-enum-capability-inactive.md)
- [Adds the originating account holder name to Received Credit bank transfers](https://docs.stripe.com/changelog/dahlia/2026-06-24/received-credit-bank-transfers-account-holder-name.md)
