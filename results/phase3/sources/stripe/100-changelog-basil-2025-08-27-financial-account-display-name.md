# Adds a display name to the FinancialAccount object

## What’s new

Adds a display name to the [FinancialAccount](https://docs.stripe.com/api/v2/money-management/financial-accounts/object.md?api-version=2025-08-27.preview) object. The Stripe Dashboard and embedded components use this name to label the financial account.

## Impact

You can now specify a name for your financial account.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `display_name` | Added | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-08-27.preview), [V2.MoneyManagement.FinancialAccount#create](/api/v2/money-management/financial-accounts/create?api-version=2025-08-27.preview) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `display_name` | Added | [V2::MoneyManagement::FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-08-27.preview), [V2::MoneyManagement::FinancialAccount::CreateParams](/api/v2/money-management/financial-accounts/create?api-version=2025-08-27.preview) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `display_name` | Added | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-08-27.preview), [v2.money_management.FinancialAccount.CreateParams](/api/v2/money-management/financial-accounts/create?api-version=2025-08-27.preview) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `display_name` | Added | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-08-27.preview) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `displayName` | Added | [v2.moneymanagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-08-27.preview), [v2.moneymanagement.FinancialAccountCreateParams](/api/v2/money-management/financial-accounts/create?api-version=2025-08-27.preview) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `display_name` | Added | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-08-27.preview), [V2.MoneyManagement.FinancialAccountCreateParams](/api/v2/money-management/financial-accounts/create?api-version=2025-08-27.preview) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `DisplayName` | Added | [V2MoneyManagementFinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-08-27.preview), [V2MoneyManagementFinancialAccountParams](/api/v2/money-management/financial-accounts/create?api-version=2025-08-27.preview) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `DisplayName` | Added | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-08-27.preview), [V2.MoneyManagement.FinancialAccountCreateOptions](/api/v2/money-management/financial-accounts/create?api-version=2025-08-27.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-08-27.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.6.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v15.6.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.6.0b1](https://github.com/stripe/stripe-python/releases/tag/v12.6.0b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.7.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v17.7.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.6.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v29.6.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.6.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v18.6.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.6.0-beta.1](https://github.com/stripe/stripe-go/releases/tag/v82.6.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.6.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v48.6.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
