# Replaces the generic fraud rejection reason with specific fraud reasons

## What’s new

Replaces the generic `fraud` value for the [reason](https://docs.stripe.com/api/account/reject.md?api-version=2026-09-30.endive#reject_account-reason) parameter when [rejecting an account](https://docs.stripe.com/api/account/reject.md?api-version=2026-09-30.endive) with more specific fraud reasons:

- `fraud_payment_method_casher`
- `fraud_payment_method_tester`
- `fraud_no_intent_to_fulfill`
- `fraud_other`

The parameter now also supports `credit` as a new value. The existing values `terms_of_service` and `other` remain supported.

Also updates the `reason` parameter from a string to an enum in affected SDKs.

## Why is this a breaking change?

The `reason` parameter changes from a string to an enum that doesn’t include `fraud` as a value. Requests that pass `fraud` return an HTTP `400` error.

## Impact

If your integration [rejects connected accounts](https://docs.stripe.com/api/account/reject.md?api-version=2026-09-30.endive) for suspected fraud, update it to use one of the new fraud reasons that best describes the suspected activity. Use `fraud_other` when none of the more specific reasons apply.

Update your integration to use the new `reason` enum, including calls that continue to use `terms_of_service` or `other`.

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `fraud` | Removed | [Account#reject.reason](/api/account/reject?api-version=2026-09-30.endive#reject_account-reason) |
| `fraud_payment_method_casher`, `fraud_payment_method_tester`, `fraud_no_intent_to_fulfill`, `fraud_other`, `credit` | Added | [Account#reject.reason](/api/account/reject?api-version=2026-09-30.endive#reject_account-reason) |

| Field | Change | From → to |
| --- | --- | --- |
| `Account#reject.reason` | Changed | `string → enum` |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `fraud` | Removed | [AccountRejectParams.reason](/api/account/reject?api-version=2026-09-30.endive#reject_account-reason) |
| `fraud_payment_method_casher`, `fraud_payment_method_tester`, `fraud_no_intent_to_fulfill`, `fraud_other`, `credit` | Added | [AccountRejectParams.reason](/api/account/reject?api-version=2026-09-30.endive#reject_account-reason) |

| Field | Change | From → to |
| --- | --- | --- |
| `AccountRejectParams.reason` | Changed | `string → enum` |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Values | Change | Enums |
| --- | --- | --- |
| `fraud` | Removed | [AccountRejectParams.reason](/api/account/reject?api-version=2026-09-30.endive#reject_account-reason) |
| `fraud_payment_method_casher`, `fraud_payment_method_tester`, `fraud_no_intent_to_fulfill`, `fraud_other`, `credit` | Added | [AccountRejectParams.reason](/api/account/reject?api-version=2026-09-30.endive#reject_account-reason) |

| Field | Change | From → to |
| --- | --- | --- |
| `AccountRejectParams.reason` | Changed | `string → enum` |

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `fraud` | Removed | [AccountRejectParams.reason](/api/account/reject?api-version=2026-09-30.endive#reject_account-reason) |
| `fraud_payment_method_casher`, `fraud_payment_method_tester`, `fraud_no_intent_to_fulfill`, `fraud_other`, `credit` | Added | [AccountRejectParams.reason](/api/account/reject?api-version=2026-09-30.endive#reject_account-reason) |

| Field | Change | From → to |
| --- | --- | --- |
| `AccountRejectParams.reason` | Changed | `string → enum` |

#### Go

This change doesn’t affect the Go SDK.

#### .NET

This change doesn’t affect the .NET SDK.

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

- [Adds address validation errors for CMRAs and registered agents to Accounts v1 and Accounts v2](https://docs.stripe.com/changelog/endive/2026-09-30/address-validation-cmra-registered-agents-accounts-v2.md)
- [Adds rejected status for Accounts v2 capabilities](https://docs.stripe.com/changelog/endive/2026-09-30/rejected-accounts-v2-capabilities.md)
- [Removes the configurations parameter from the Account Links v2 API](https://docs.stripe.com/changelog/endive/2026-09-30/removes-configurations-parameter-from-v2-core-account-links-api.md)
- [Standardises SEPA Direct Debit payment settings in the Accounts API](https://docs.stripe.com/changelog/endive/2026-09-30/sepa-debit-settings-accounts.md)
- [Shows errors for eventually due requirements](https://docs.stripe.com/changelog/endive/2026-09-30/shows-errors-for-eventually-due-requirements.md)
- [Distinguishes platform-initiated account rejections from Stripe rejections](https://docs.stripe.com/changelog/endive/2026-09-30/platform-rejection-reasons.md)
- [Adds additional shared fields to customer sharing](https://docs.stripe.com/changelog/endive/2026-09-30/additional-shared-fields-customer-sharing.md)
