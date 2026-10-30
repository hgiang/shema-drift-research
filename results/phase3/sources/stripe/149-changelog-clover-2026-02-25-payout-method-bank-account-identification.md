# Expands bank account identification details in payout method responses

## What’s new

Adds the [swift_code](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=2026-02-25.preview#v2_payout_method_object-bank_account-swift_code) and [branch_number](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=2026-02-25.preview#v2_payout_method_object-bank_account-branch_number) properties to the `bank_account` hash on the [Payout Method](https://docs.stripe.com/api/v2/money-management/payout-methods.md?api-version=2026-02-25.preview) object. Both properties return null when the information isn’t available or doesn’t apply to the bank account.

## Impact

You can now access additional bank account identification details when retrieving Payout Methods. The `swift_code` property contains the bank’s SWIFT or BIC code, and the `branch_number` property contains the branch identifier.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `branch_number`, `swift_code` | Added | [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-02-25.preview#v2_payout_method_object-bank_account) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `branch_number`, `swift_code` | Added | [V2::MoneyManagement::PayoutMethod::BankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-02-25.preview#v2_payout_method_object-bank_account) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `branch_number`, `swift_code` | Added | [V2.MoneyManagement.PayoutMethod.BankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-02-25.preview#v2_payout_method_object-bank_account) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `branch_number`, `swift_code` | Added | [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-02-25.preview#v2_payout_method_object-bank_account) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `branchNumber`, `swiftCode` | Added | [v2.moneymanagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-02-25.preview#v2_payout_method_object-bank_account) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `branch_number`, `swift_code` | Added | [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-02-25.preview#v2_payout_method_object-bank_account) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BranchNumber`, `SwiftCode` | Added | [V2MoneyManagementPayoutMethodBankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-02-25.preview#v2_payout_method_object-bank_account) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BranchNumber`, `SwiftCode` | Added | [V2.MoneyManagement.PayoutMethod.BankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-02-25.preview#v2_payout_method_object-bank_account) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-02-25.preview`
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

- [Expands cross-border payout destinations to 12 additional countries](https://docs.stripe.com/changelog/clover/2026-02-25/cross-border-payouts-new-countries.md)
- [Adds the ability to specify the purpose of Outbound Payments](https://docs.stripe.com/changelog/clover/2026-02-25/outbound-payments-purpose.md)
