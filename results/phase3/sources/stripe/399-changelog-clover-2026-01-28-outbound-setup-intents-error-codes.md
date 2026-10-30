# Updates error codes for the Outbound Setup Intents API

## What’s new

Updates the [error codes](https://docs.stripe.com/api/errors.md?api-version=2026-01-28.preview#errors-code) returned by the [Outbound Setup Intents](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents.md?api-version=2026-01-28.preview) API to use more generic error types instead of credential-type-specific codes. This change replaces several existing error codes with standardised error types:

- `blocked_payout_method_bank_account`, `blocked_payout_method_card` and `blocked_payout_method_crypto_wallet` errors now return `blocked_payout_method`.
- `unsupported_payout_method_bank_account` and `unsupported_payout_method_card` errors now return `unsupported_payout_method`.
- `invalid_payout_method_bank_account`, `invalid_payout_method_card` and `invalid_payout_method_crypto_wallet` errors now return `invalid_payout_method`.
- `limit_payout_method_bank_account`, `limit_payout_method_card` and `limit_payout_method_crypto_wallet` errors now return `limit_payout_method`.

This standardisation improves the consistency of error handling across different [Payout Method](https://docs.stripe.com/api/v2/money-management/payout-methods.md?api-version=2026-01-28.preview) types and supports future extensibility when adding new credential types to Payout Methods.

## Why is this a breaking change?

This is a breaking change because your integration can rely on the specific error code identifiers that this update replaces. If your code checks for type specific error codes like `blocked_payout_method_bank_account`, `unsupported_payout_method_bank_account`, `invalid_payout_method_bank_account_` or `limit_payout_method_bank_account`, those checks no longer work and you must update them to handle the generic error types.

## Impact

If your integration handles specific error codes from Outbound Setup Intents endpoints, you need to update your error handling logic to use the generic error types. The error messages and underlying reasons remain the same, but the error code identifiers have changed to be more consistent across different Payout Method types.

## Changes

#### REST API

| Codes | Change |  |
| --- | --- | --- |
| `blocked_payout_method`, `unsupported_payout_method` | Added | `blocked_by_stripe` |
| `invalid_payout_method_data` | Added | `invalid_payout_method` |
| `limit_payout_method` | Added | `quota_exceeded` |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Codes | Change |  |
| --- | --- | --- |
| `blocked_payout_method`, `unsupported_payout_method` | Added | `BlockedByStripeError` |
| `invalid_payout_method_data` | Added | `InvalidPayoutMethodError` |
| `limit_payout_method` | Added | `QuotaExceededError` |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Codes | Change |  |
| --- | --- | --- |
| `blocked_payout_method`, `unsupported_payout_method` | Added | `BlockedByStripeError` |
| `invalid_payout_method_data` | Added | `InvalidPayoutMethodError` |
| `limit_payout_method` | Added | `QuotaExceededError` |

#### Go

| Codes | Change |  |
| --- | --- | --- |
| `blocked_payout_method`, `unsupported_payout_method` | Added | `BlockedByStripeError` |
| `invalid_payout_method_data` | Added | `InvalidPayoutMethodError` |
| `limit_payout_method` | Added | `QuotaExceededError` |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-01-28.preview`
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

- [Adds alternative reference field to bank account and payout method resources](https://docs.stripe.com/changelog/clover/2026-01-28/alternative-reference-field.md)
- [Adds fingerprint property to card payout methods](https://docs.stripe.com/changelog/clover/2026-01-28/card-payout-methods-fingerprint-property.md)
- [Global Payouts adds support for 15 new countries for cross-border payouts](https://docs.stripe.com/changelog/clover/2026-01-28/cross-border-payouts-new-countries.md)
