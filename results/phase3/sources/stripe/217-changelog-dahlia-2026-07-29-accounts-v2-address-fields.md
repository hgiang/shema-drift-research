# Adds new address fields to Accounts v2 for Singapore compliance

## What’s new

Adds the [additional_addresses](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-07-29.dahlia#v2_account_object-identity-business_details-additional_addresses) property to the [identity.business_details](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-07-29.dahlia#v2_account_object-identity-business_details) hash of the [v2 Account](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-07-29.dahlia) object. This property contains the business’s principal place of business and administrative address. Set each address’s [purpose](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-07-29.dahlia#v2_account_object-identity-business_details-additional_addresses-purpose) to `principal_place_of_business` or `administrative`.

You can optionally provide the `additional_addresses` parameter when you create or update a v2 Account, or create an [Account Token](https://docs.stripe.com/api/v2/core/account-tokens.md?api-version=2026-07-29.dahlia).

## Impact

If you use API-based onboarding for Singapore connected accounts, update your integration to pass `additional_addresses` with the applicable `purpose` values when required. For implementation guidance, see [Upcoming requirement updates for Singapore](https://docs.stripe.com/connect/upcoming-requirements-updates.md?program=sg-2026).

Unless it’s required for you, `additional_addresses` is optional and doesn’t affect existing requests.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `additional_addresses` | Added | [V2.Core.Account#create.identity.business_details](/api/v2/core/accounts/create?api-version=2026-07-29.dahlia#v2_create_accounts-identity-business_details), [V2.Core.Account#update.identity.business_details](/api/v2/core/accounts/update?api-version=2026-07-29.dahlia#v2_update_accounts-identity-business_details), [V2.Core.Account.identity.business_details](/api/v2/core/accounts/object?api-version=2026-07-29.dahlia#v2_account_object-identity-business_details), [V2.Core.AccountToken#create.identity.business_details](/api/v2/core/account-tokens/create?api-version=2026-07-29.dahlia#v2_create_account_tokens-identity-business_details) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `additional_addresses` | Added | [V2::Core::Account::Identity::BusinessDetail](/api/v2/core/accounts/object?api-version=2026-07-29.dahlia#v2_account_object-identity-business_details), [V2::Core::AccountCreateParams::Identity::BusinessDetail](/api/v2/core/accounts/create?api-version=2026-07-29.dahlia#v2_create_accounts-identity-business_details), [V2::Core::AccountTokenCreateParams::Identity::BusinessDetail](/api/v2/core/account-tokens/create?api-version=2026-07-29.dahlia#v2_create_account_tokens-identity-business_details), [V2::Core::AccountUpdateParams::Identity::BusinessDetail](/api/v2/core/accounts/update?api-version=2026-07-29.dahlia#v2_update_accounts-identity-business_details) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `additional_addresses` | Added | [V2.Core.Account.Identity.BusinessDetail](/api/v2/core/accounts/object?api-version=2026-07-29.dahlia#v2_account_object-identity-business_details), [v2.core.AccountCreateParamsIdentityBusinessDetail](/api/v2/core/accounts/create?api-version=2026-07-29.dahlia#v2_create_accounts-identity-business_details), [v2.core.AccountModifyParamsIdentityBusinessDetail](/api/v2/core/accounts/update?api-version=2026-07-29.dahlia#v2_update_accounts-identity-business_details), [v2.core.AccountTokenCreateParamsIdentityBusinessDetail](/api/v2/core/account-tokens/create?api-version=2026-07-29.dahlia#v2_create_account_tokens-identity-business_details) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `additional_addresses` | Added | [V2.Core.Account.identity.business_details](/api/v2/core/accounts/object?api-version=2026-07-29.dahlia#v2_account_object-identity-business_details), [V2\Core\Account.create().$params.identity.business_detail](/api/v2/core/accounts/create?api-version=2026-07-29.dahlia#v2_create_accounts-identity-business_details), [V2\Core\Account.update().$params.identity.business_detail](/api/v2/core/accounts/update?api-version=2026-07-29.dahlia#v2_update_accounts-identity-business_details), [V2\Core\AccountToken.create().$params.identity.business_detail](/api/v2/core/account-tokens/create?api-version=2026-07-29.dahlia#v2_create_account_tokens-identity-business_details) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `additionalAddresses` | Added | [v2.core.Account.identity.business_details](/api/v2/core/accounts/object?api-version=2026-07-29.dahlia#v2_account_object-identity-business_details), [v2.core.AccountCreateParams.identity.business_details](/api/v2/core/accounts/create?api-version=2026-07-29.dahlia#v2_create_accounts-identity-business_details), [v2.core.AccountTokenCreateParams.identity.business_details](/api/v2/core/account-tokens/create?api-version=2026-07-29.dahlia#v2_create_account_tokens-identity-business_details), [v2.core.AccountUpdateParams.identity.business_details](/api/v2/core/accounts/update?api-version=2026-07-29.dahlia#v2_update_accounts-identity-business_details) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `additional_addresses` | Added | [V2.Core.Account.identity.business_details](/api/v2/core/accounts/object?api-version=2026-07-29.dahlia#v2_account_object-identity-business_details), [V2.Core.AccountCreateParams.identity.business_details](/api/v2/core/accounts/create?api-version=2026-07-29.dahlia#v2_create_accounts-identity-business_details), [V2.Core.AccountTokenCreateParams.identity.business_details](/api/v2/core/account-tokens/create?api-version=2026-07-29.dahlia#v2_create_account_tokens-identity-business_details), [V2.Core.AccountUpdateParams.identity.business_details](/api/v2/core/accounts/update?api-version=2026-07-29.dahlia#v2_update_accounts-identity-business_details) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AdditionalAddresses` | Added | [V2CoreAccountIdentityBusinessDetails](/api/v2/core/accounts/object?api-version=2026-07-29.dahlia#v2_account_object-identity-business_details), [V2CoreAccountIdentityBusinessDetailsParams](/api/v2/core/accounts/create?api-version=2026-07-29.dahlia#v2_create_accounts-identity-business_details), [V2CoreAccountTokenIdentityBusinessDetailsParams](/api/v2/core/account-tokens/create?api-version=2026-07-29.dahlia#v2_create_account_tokens-identity-business_details) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AdditionalAddresses` | Added | [V2.Core.Account.Identity.BusinessDetails](/api/v2/core/accounts/object?api-version=2026-07-29.dahlia#v2_account_object-identity-business_details), [V2CoreAccountIdentityBusinessDetailsOptions](/api/v2/core/accounts/create?api-version=2026-07-29.dahlia#v2_create_accounts-identity-business_details), [V2CoreAccountTokenIdentityBusinessDetailsOptions](/api/v2/core/account-tokens/create?api-version=2026-07-29.dahlia#v2_create_account_tokens-identity-business_details) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-07-29.dahlia`
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

- [Adds the ability to show who initiated a top-up](https://docs.stripe.com/changelog/dahlia/2026-07-29/top-up-initiated-by-property.md)
- [Adds Payment Method support to Top-ups](https://docs.stripe.com/changelog/dahlia/2026-07-29/adds-payment-method-support-to-top-ups.md)
- [Adds new address fields to Accounts v1 for Singapore compliance](https://docs.stripe.com/changelog/dahlia/2026-07-29/accounts-v1-address-fields.md)
- [Adds a new Smart Disputes management feature to Account Session embedded components](https://docs.stripe.com/changelog/dahlia/2026-07-29/account-session-embedded-components-smart-disputes-management.md)
- [Enables rejecting connected accounts with non-zero balances and controlling whether to pause payouts](https://docs.stripe.com/changelog/dahlia/2026-07-29/reject-connected-accounts-with-non-zero-balances.md)
- [Adds the ability to reverse platform rejections on connected accounts](https://docs.stripe.com/changelog/dahlia/2026-07-29/unreject-connected-account-endpoint.md)
