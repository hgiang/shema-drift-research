# Replaces SWIFT code with BIC in Financial Addresses

## What’s new

Replaces [swift_code](https://docs.stripe.com/api/v2/money-management/financial-addresses/object.md?api-version=2026-05-27.preview#v2_financial_address_object-credentials-us_bank_account-swift_code) with [bic](https://docs.stripe.com/api/v2/money-management/financial-addresses/object.md?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account-bic) on the [credentials.us_bank_account](https://docs.stripe.com/api/v2/money-management/financial-addresses/object.md?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) hash of the [Financial Address](https://docs.stripe.com/api/v2/money-management/financial-addresses/object.md?api-version=2026-06-24.preview) object. BIC (Bank Identifier Code) is the standard term for what was previously labelled as a SWIFT code.

## Why is this a breaking change?

Previously, `swift_code` returned the BIC on `credentials.us_bank_account`. If your code reads `swift_code` from Financial Address responses, it will no longer receive this property. You must update it to read `bic` instead. If your code passes `swift_code` in requests, those requests will fail.

## Impact

If your code currently reads or sets `swift_code` on Financial Address objects, you must update it to use `bic` instead.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `bic` | Added | [V2.MoneyManagement.FinancialAddress.credentials.us_bank_account](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |
| `swift_code` | Removed | [V2.MoneyManagement.FinancialAddress.credentials.us_bank_account](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `bic` | Added | [V2::MoneyManagement::FinancialAddress::Credential::UsBankAccount](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |
| `swift_code` | Removed | [V2::MoneyManagement::FinancialAddress::Credential::UsBankAccount](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `bic` | Added | [V2.MoneyManagement.FinancialAddress.Credential.UsBankAccount](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |
| `swift_code` | Removed | [V2.MoneyManagement.FinancialAddress.Credential.UsBankAccount](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `bic` | Added | [V2.MoneyManagement.FinancialAddress.credentials.us_bank_account](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |
| `swift_code` | Removed | [V2.MoneyManagement.FinancialAddress.credentials.us_bank_account](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `bic` | Added | [v2.moneymanagement.FinancialAddress.credentials.us_bank_account](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |
| `swiftCode` | Removed | [v2.moneymanagement.FinancialAddress.credentials.us_bank_account](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `bic` | Added | [V2.MoneyManagement.FinancialAddress.credentials.us_bank_account](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |
| `swift_code` | Removed | [V2.MoneyManagement.FinancialAddress.credentials.us_bank_account](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BIC` | Added | [V2MoneyManagementFinancialAddressCredentialsUsBankAccount](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |
| `SwiftCode` | Removed | [V2MoneyManagementFinancialAddressCredentialsUsBankAccount](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Bic` | Added | [V2.MoneyManagement.FinancialAddress.Credentials.UsBankAccount](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |
| `SwiftCode` | Removed | [V2.MoneyManagement.FinancialAddress.Credentials.UsBankAccount](/api/v2/money-management/financial-addresses/object?api-version=2026-06-24.preview#v2_financial_address_object-credentials-us_bank_account) |

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

- [Adds a failure reason for received debits when the debit capability is inactive](https://docs.stripe.com/changelog/dahlia/2026-06-24/received-debits-failure-reason-enum-capability-inactive.md)
- [Replaces the status filter with statuses on the List Financial Accounts endpoint](https://docs.stripe.com/changelog/dahlia/2026-06-24/v2-financial-accounts-statuses-filter.md)
- [Adds the originating account holder name to Received Credit bank transfers](https://docs.stripe.com/changelog/dahlia/2026-06-24/received-credit-bank-transfers-account-holder-name.md)
