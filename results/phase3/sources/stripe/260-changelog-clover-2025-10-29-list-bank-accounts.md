# Adds support for listing US and GB bank accounts

## What’s new

Adds new API endpoints for listing [US Bank Accounts](https://docs.stripe.com/api/v2/core/vault/us-bank-accounts.md?api-version=2025-10-29.preview) and [GB Bank Accounts](https://docs.stripe.com/api/v2/core/vault/gb-bank-accounts.md?api-version=2025-10-29.preview).

## Impact

You can now list your bank accounts in the US and GB using the API. US Bank Accounts can be listed with a filter on [verification.status](https://docs.stripe.com/api/v2/core/vault/us-bank-accounts/archive.md?api-version=2025-10-29.preview#v2_archive_us_bank_accounts-response-verification-status) which can be `unverified`, `verified`, `awaiting_verification` or `verification_failed`.

## Changes

#### REST API

| Endpoint | Change | Resources |
| --- | --- | --- |
| `list` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2025-10-29.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2025-10-29.preview) |

#### Ruby

| Method | Change | Resources |
| --- | --- | --- |
| `list` | Added | [V2::Core::Vault::GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2025-10-29.preview), [V2::Core::Vault::UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2025-10-29.preview) |

#### Python

| Method | Change | Resources |
| --- | --- | --- |
| `list` | Added | [v2.core.vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2025-10-29.preview), [v2.core.vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2025-10-29.preview) |

#### PHP

| Method | Change | Resources |
| --- | --- | --- |
| `all` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2025-10-29.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2025-10-29.preview) |

#### Java

| Method | Change | Resources |
| --- | --- | --- |
| `list` | Added | [v2.core.vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2025-10-29.preview), [v2.core.vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2025-10-29.preview) |

#### Node.js

| Method | Change | Resources |
| --- | --- | --- |
| `list` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2025-10-29.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2025-10-29.preview) |

#### Go

| Method | Change | Resources |
| --- | --- | --- |
| `List` | Added | [V2CoreVaultGBBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2025-10-29.preview), [V2CoreVaultUSBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2025-10-29.preview) |

#### .NET

| Method | Change | Resources |
| --- | --- | --- |
| `List` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2025-10-29.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2025-10-29.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-10-29.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v17.2.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v17.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.2.0b1](https://github.com/stripe/stripe-python/releases/tag/v13.2.0b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.2.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v18.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.2.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v30.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.3.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v19.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.1.0-beta.3](https://github.com/stripe/stripe-go/releases/tag/v83.1.0-beta.3)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.2.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v49.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds support for microdeposits to US Bank Accounts](https://docs.stripe.com/changelog/clover/2025-10-29/microdeposits-us-bank-accounts.md)
