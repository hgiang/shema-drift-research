# Moves platform-specific identity fields to a default profile for Accounts

## What’s new

We’ve moved the following fields from the `identity` hash of the Accounts v2 object because they’re specific to the platform and not canonical to the identity of the business being represented:

- `identity.business_details.doing_business_as`
- `identity.business_details.url`
- `identity.business_details.product_description`

The properties now exist in the new [defaults.profile](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2025-09-30.preview#v2_account_object-defaults-profile) hash.

## Why is this a breaking change?

In the new API version, requests passing`doing_business_as`,`url` and`product_description` on`identity.business_details` will fail.

## Impact

If you participate in the Accounts v2 API public preview and want to use API version 2025-09-30.clover or later, you must update your integration to specify these properties in the`defaults.profile` hash instead of`identity.business_details`.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `profile` | Added | [V2.Core.Account#create.defaults](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-defaults), [V2.Core.Account#update.defaults](/api/v2/core/accounts/update?api-version=2025-09-30.preview#v2_update_accounts-defaults), [V2.Core.Account.defaults](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-defaults) |
| `doing_business_as`, `product_description`, `url` | Removed | [V2.Core.Account#create.identity.business_details](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-identity-business_details), [V2.Core.Account#update.identity.business_details](/api/v2/core/accounts/update?api-version=2025-09-30.preview#v2_update_accounts-identity-business_details), [V2.Core.Account.identity.business_details](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-identity-business_details) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `profile` | Added | [V2::Core::Account::CreateParams::Default](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-defaults), [V2::Core::Account::Default](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-defaults), [V2::Core::Account::UpdateParams::Default](/api/v2/core/accounts/update?api-version=2025-09-30.preview#v2_update_accounts-defaults) |
| `doing_business_as`, `product_description`, `url` | Removed | [V2::Core::Account::CreateParams::Identity::BusinessDetail](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-identity-business_details), [V2::Core::Account::Identity::BusinessDetail](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-identity-business_details), [V2::Core::Account::UpdateParams::Identity::BusinessDetail](/api/v2/core/accounts/update?api-version=2025-09-30.preview#v2_update_accounts-identity-business_details) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `profile` | Added | [V2.Core.Account.Default](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-defaults), [v2.core.Account.CreateParamsDefault](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-defaults), [v2.core.Account.ModifyParamsDefault](/api/v2/core/accounts/update?api-version=2025-09-30.preview#v2_update_accounts-defaults) |
| `doing_business_as`, `product_description`, `url` | Removed | [V2.Core.Account.Identity.BusinessDetail](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-identity-business_details), [v2.core.Account.CreateParamsIdentityBusinessDetail](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-identity-business_details), [v2.core.Account.ModifyParamsIdentityBusinessDetail](/api/v2/core/accounts/update?api-version=2025-09-30.preview#v2_update_accounts-identity-business_details) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `profile` | Added | [V2.Core.Account.defaults](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-defaults), [V2\Core\Account.create().$params.default](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-defaults), [V2\Core\Account.update().$params.default](/api/v2/core/accounts/update?api-version=2025-09-30.preview#v2_update_accounts-defaults) |
| `doing_business_as`, `product_description`, `url` | Removed | [V2.Core.Account.identity.business_details](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-identity-business_details), [V2\Core\Account.create().$params.identity.business_detail](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-identity-business_details), [V2\Core\Account.update().$params.identity.business_detail](/api/v2/core/accounts/update?api-version=2025-09-30.preview#v2_update_accounts-identity-business_details) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `profile` | Added | [v2.core.Account.defaults](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-defaults), [v2.core.AccountCreateParams.defaults](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-defaults), [v2.core.AccountUpdateParams.defaults](/api/v2/core/accounts/update?api-version=2025-09-30.preview#v2_update_accounts-defaults) |
| `doingBusinessAs`, `productDescription`, `url` | Removed | [v2.core.Account.identity.business_details](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-identity-business_details), [v2.core.AccountCreateParams.identity.business_details](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-identity-business_details), [v2.core.AccountUpdateParams.identity.business_details](/api/v2/core/accounts/update?api-version=2025-09-30.preview#v2_update_accounts-identity-business_details) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `profile` | Added | [V2.Core.Account.defaults](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-defaults), [V2.Core.AccountCreateParams.defaults](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-defaults), [V2.Core.AccountUpdateParams.defaults](/api/v2/core/accounts/update?api-version=2025-09-30.preview#v2_update_accounts-defaults) |
| `doing_business_as`, `product_description`, `url` | Removed | [V2.Core.Account.identity.business_details](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-identity-business_details), [V2.Core.AccountCreateParams.identity.business_details](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-identity-business_details), [V2.Core.AccountUpdateParams.identity.business_details](/api/v2/core/accounts/update?api-version=2025-09-30.preview#v2_update_accounts-identity-business_details) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Profile` | Added | [V2CoreAccountDefaults](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-defaults), [V2CoreAccountDefaultsParams](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-defaults) |
| `DoingBusinessAs`, `ProductDescription`, `URL` | Removed | [V2CoreAccountIdentityBusinessDetails](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-identity-business_details), [V2CoreAccountIdentityBusinessDetailsParams](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-identity-business_details) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Profile` | Added | [V2.Core.Account.Defaults](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-defaults), [V2CoreAccountDefaultsOptions](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-defaults) |
| `DoingBusinessAs`, `ProductDescription`, `Url` | Removed | [V2.Core.Account.Identity.BusinessDetails](/api/v2/core/accounts/object?api-version=2025-09-30.preview#v2_account_object-identity-business_details), [V2CoreAccountIdentityBusinessDetailsOptions](/api/v2/core/accounts/create?api-version=2025-09-30.preview#v2_create_accounts-identity-business_details) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-09-30.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v16.1.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v16.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.1.2b1](https://github.com/stripe/stripe-python/releases/tag/v13.1.2b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.1.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v18.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.1.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v30.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.2.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v19.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.1.0-beta.1](https://github.com/stripe/stripe-go/releases/tag/v83.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.1.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v49.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds per-currency minimum balances for automatic payouts on the Balance Settings API](https://docs.stripe.com/changelog/clover/2025-09-30/minimum-balance-by-currency-on-balance-settings.md)
- [Updating Balance Settings no longer requires specifying payment settings](https://docs.stripe.com/changelog/clover/2025-09-30/payments-field-optional-for-update-balance-settings.md)
