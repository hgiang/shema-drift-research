# Adds a failure reason for received debits when the debit capability is inactive

## What’s new

Adds `capability_inactive` as a new enum value for the [status_details.failed.reason](https://docs.stripe.com/api/v2/money-management/received-debits/object.md?api-version=2026-06-24.preview#v2_received_debit_object-status_details-failed-reason) of the [ReceivedDebit](https://docs.stripe.com/api/v2/money-management/received-debits/object.md?api-version=2026-06-24.preview) object. When a received debit fails because the associated capability is inactive, `status_details.failed.reason` now returns `capability_inactive` explicitly, instead of a generic failure reason.

## Why is this a breaking change?

Previously, if a received debit failed because the associated capability was inactive, no explicit `capability_inactive` enum value existed on `status_details.failed.reason`. If your integration switches on or otherwise evaluates `status_details.failed.reason` for a ReceivedDebit, update your code to handle `capability_inactive`.

## Impact

You can now identify received debit failures caused by an inactive capability through the new `capability_inactive` value in `status_details.failed.reason`.

## Changes

#### REST API

| Value | Change | Enum |
| --- | --- | --- |
| `capability_inactive` | Added | [V2.MoneyManagement.ReceivedDebit.status_details.failed.reason](/api/v2/money-management/received-debits/object?api-version=2026-06-24.preview#v2_received_debit_object-status_details-failed-reason) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enum |
| --- | --- | --- |
| `capability_inactive` | Added | [V2.MoneyManagement.ReceivedDebit.StatusDetail.Failed.reason](/api/v2/money-management/received-debits/object?api-version=2026-06-24.preview#v2_received_debit_object-status_details-failed-reason) |

#### PHP

| Value | Change | Enum |
| --- | --- | --- |
| `capability_inactive` | Added | [V2.MoneyManagement.ReceivedDebit.status_details.failed.reason](/api/v2/money-management/received-debits/object?api-version=2026-06-24.preview#v2_received_debit_object-status_details-failed-reason) |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Value | Change | Enum |
| --- | --- | --- |
| `capability_inactive` | Added | [V2.MoneyManagement.ReceivedDebit.status_details.failed.reason](/api/v2/money-management/received-debits/object?api-version=2026-06-24.preview#v2_received_debit_object-status_details-failed-reason) |

#### Go

| Value | Change | Enum |
| --- | --- | --- |
| `capability_inactive` | Added | [V2MoneyManagementReceivedDebitStatusDetailsFailed.Reason](/api/v2/money-management/received-debits/object?api-version=2026-06-24.preview#v2_received_debit_object-status_details-failed-Reason) |

#### .NET

This change doesn’t affect the .NET SDK.

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
- [Replaces the status filter with statuses on the List Financial Accounts endpoint](https://docs.stripe.com/changelog/dahlia/2026-06-24/v2-financial-accounts-statuses-filter.md)
- [Adds the originating account holder name to Received Credit bank transfers](https://docs.stripe.com/changelog/dahlia/2026-06-24/received-credit-bank-transfers-account-holder-name.md)
