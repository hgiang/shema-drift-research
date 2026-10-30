# Adds the ability to attest to an Account's authorised company representative

## What’s new

You can now record the attestation of an authorised company representative for a Stripe account by specifying these [company](https://docs.stripe.com/api/accounts/update.md?api-version=2025-10-29.clover#update_account-company) parameters for a given [Account](https://docs.stripe.com/api/accounts/object.md?api-version=2025-10-29.clover):

- [representative_declaration.ip](https://docs.stripe.com/api/accounts/update.md?api-version=2025-10-29.clover#update_account-company-representative_declaration-ip) for the originating IP address of the attestation
- [representative_declaration.date](https://docs.stripe.com/api/accounts/update.md?api-version=2025-10-29.clover#update_account-company-representative_declaration-date) for the date of the attestation
- [representative_declaration.user_agent](https://docs.stripe.com/api/accounts/update.md?api-version=2025-10-29.clover#update_account-company-representative_declaration-user_agent) for the user agent used for the attestation

## Impact

A representative is the singular person designated by a business to manage their Stripe account. They’re identified by setting the [relationship.representative](https://docs.stripe.com/api/persons/object.md?api-version=2025-10-29.clover#person_object-relationship-representative) field.

In certain countries, Stripe is required to collect and verify that the representative’s information matches government records. When an account is created, the representative should be set to whoever is responsible for managing the account.

Accounts that require the the attestation of a company’s representative will see `company.representative_declaration.ip` and `company.representative_declaration.date` in the [requirements](https://docs.stripe.com/api/accounts/object.md?api-version=2025-10-29.clover#account_object-requirements) field.

```curl
curl https://api.stripe.com/v1/accounts/{{CONNECTEDACCOUNT_ID}}/ \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "company[representative_declaration][ip]=67.180.161.149" \
  -d "company[representative_declaration][date]=1737936000" \
  --data-urlencode "company[representative_declaration][user_agent]=Mozilla/5.0 (platform; rv:gecko-version) Gecko/gecko-trail Firefox/firefox-version"
```

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `representative_declaration` | Added | [Account#create.company](/api/accounts/create?api-version=2025-10-29.clover#create_account-company), [Account#update.company](/api/accounts/update?api-version=2025-10-29.clover#update_account-company), [Account.company](/api/accounts/object?api-version=2025-10-29.clover#account_object-company), [Token#create.account.company](/api/tokens/create_account?api-version=2025-10-29.clover#create_account_token-account-company) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `representative_declaration` | Added | [Account::Company](/api/accounts/object?api-version=2025-10-29.clover#account_object-company), [Account::CreateParams::Company](/api/accounts/create?api-version=2025-10-29.clover#create_account-company), [Account::UpdateParams::Company](/api/accounts/update?api-version=2025-10-29.clover#update_account-company), `Token::CreateParams::Account::Company` |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `representative_declaration` | Added | [Account.Company](/api/accounts/object?api-version=2025-10-29.clover#account_object-company), [Account.CreateParamsCompany](/api/accounts/create?api-version=2025-10-29.clover#create_account-company), [Account.ModifyParamsCompany](/api/accounts/update?api-version=2025-10-29.clover#update_account-company), [Token.CreateParamsAccountCompany](/api/tokens/create_account?api-version=2025-10-29.clover#create_account_token-account-company) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `representative_declaration` | Added | [Account.company](/api/accounts/object?api-version=2025-10-29.clover#account_object-company), [Account.create().$params.company](/api/accounts/create?api-version=2025-10-29.clover#create_account-company), [Account.update().$params.company](/api/accounts/update?api-version=2025-10-29.clover#update_account-company), `Token.create().$params.account.company` |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `representativeDeclaration` | Added | [Account.company](/api/accounts/object?api-version=2025-10-29.clover#account_object-company), [AccountCreateParams.company](/api/accounts/create?api-version=2025-10-29.clover#create_account-company), [AccountUpdateParams.company](/api/accounts/update?api-version=2025-10-29.clover#update_account-company), [TokenCreateParams.account.company](/api/tokens/create_account?api-version=2025-10-29.clover#create_account_token-account-company) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `representative_declaration` | Added | [Account.company](/api/accounts/object?api-version=2025-10-29.clover#account_object-company), [AccountCreateParams.company](/api/accounts/create?api-version=2025-10-29.clover#create_account-company), [AccountUpdateParams.company](/api/accounts/update?api-version=2025-10-29.clover#update_account-company), [TokenCreateParams.account.company](/api/tokens/create_account?api-version=2025-10-29.clover#create_account_token-account-company) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `RepresentativeDeclaration` | Added | [AccountCompany](/api/accounts/object?api-version=2025-10-29.clover#account_object-company), [AccountCompanyParams](/api/accounts/update?api-version=2025-10-29.clover#update_account-company), [TokenAccountCompanyParams](/api/tokens/create_account?api-version=2025-10-29.clover#create_account_token-account-company) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `RepresentativeDeclaration` | Added | [Account.Company](/api/accounts/object?api-version=2025-10-29.clover#account_object-company), [AccountCompanyOptions](/api/accounts/update?api-version=2025-10-29.clover#update_account-company), [TokenAccountCompanyOptions](/api/tokens/create_account?api-version=2025-10-29.clover#create_account_token-account-company) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-10-29.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v17.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v17.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.1.0](https://github.com/stripe/stripe-python/releases/tag/v13.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.1.0](https://github.com/stripe/stripe-php/releases/tag/v18.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.1.0](https://github.com/stripe/stripe-java/releases/tag/v30.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.2.0](https://github.com/stripe/stripe-node/releases/tag/v19.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.1.0](https://github.com/stripe/stripe-go/releases/tag/v83.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds the ability to upload your platform’s terms of service agreement](https://docs.stripe.com/changelog/clover/2025-10-29/upload-file-terms-of-service.md)
- [Adds a webhook event type for updates to the balance settings for connected accounts](https://docs.stripe.com/changelog/clover/2025-10-29/balance-settings-updated-webhook.md)
