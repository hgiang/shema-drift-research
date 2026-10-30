# Adds support for Accounts v2 to accept the terms of service for storing stablecoins

## What’s new

You can now attest to terms of service acceptance for [Financial Accounts](https://docs.stripe.com/api/v2/money-management/financial-accounts.md?api-version=2025-11-17.preview) that store [stablecoins](https://docs.stripe.com/treasury/store-funds.md). Use the [crypto_storer](https://docs.stripe.com/api/v2/core/accounts/update.md?api-version=2025-11-17.preview#v2_update_accounts-identity-attestations-terms_of_service-crypto_storer) parameter in the [identity.attestations.terms_of_service](https://docs.stripe.com/api/v2/core/accounts/update.md?api-version=2025-11-17.preview#v2_update_accounts-identity-attestations-terms_of_service) hash of [Accounts v2](https://docs.stripe.com/api/v2/core/accounts/.md?api-version=2025-11-17.preview).

## Impact

You can programmatically record terms of service acceptance for Financial Accounts that store stablecoins. You must record acceptance when creating accounts that store cryptocurrency.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `crypto_storer` | Added | [V2.Core.Account#update.identity.attestations.terms_of_service](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-identity-attestations-terms_of_service) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `crypto_storer` | Added | [V2::Core::AccountUpdateParams::Identity::Attestation::TermsOfService](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-identity-attestations-terms_of_service) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `crypto_storer` | Added | [v2.core.AccountModifyParamsIdentityAttestationTermsOfService](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-identity-attestations-terms_of_service) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `crypto_storer` | Added | [V2\Core\Account.update().$params.identity.attestation.terms_of_service](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-identity-attestations-terms_of_service) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `cryptoStorer` | Added | [v2.core.AccountUpdateParams.identity.attestations.terms_of_service](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-identity-attestations-terms_of_service) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `crypto_storer` | Added | [V2.Core.AccountUpdateParams.identity.attestations.terms_of_service](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-identity-attestations-terms_of_service) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CryptoStorer` | Added | [V2CoreAccountIdentityAttestationsTermsOfServiceParams](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-identity-attestations-terms_of_service) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CryptoStorer` | Added | [V2CoreAccountIdentityAttestationsTermsOfServiceOptions](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-identity-attestations-terms_of_service) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-11-17.preview`
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
