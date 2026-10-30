# Adds a minority-owned business designation field to the business profile hash

## What’s new

Adds the `minority_owned_business_designation` field to the `business_profile` hash in the Accounts API, which accepts a list of enums for various ownership statuses.

This change complies with Section 1071 of the Dodd-Frank Act, which requires providers of small business financing in the US to collect demographic information about applicants. Stripe’s financial partners will report this information to the CFPB, which will analyse potential disparities in business financing. The information shared will be anonymised to protect the identity of applicants.

The field includes five possible enum values:

- `women_owned_business`: The account is a women-owned business.
- `lgbtqi_owned_business`: The account is an LGBTQI±owned business.
- `minority_owned_business`: The account is a minority-owned business. Minority means Hispanic or Latino, American Indian or Alaska Native, Asian, Black or African American, or Native Hawaiian or other Pacific Islander. A multi-racial or multi-ethnic individual is a minority for this purpose.
- `none_of_these_apply`: None of these apply.
- `prefer_not_to_answer`: Prefer not to answer.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/ \
  -u "sk_test_4eC39HqLyjWDarjtT1zdp7dc:" \
  -d business_profile[minority_owned_business_designation][]=women_owned_business \
  -d business_profile[minority_owned_business_designation][]=lgbtqi_owned_business
```

## Impact

This addition complies with Regulation 1071, requiring providers of small business financing to collect demographic information about applicants for financing.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `minority_owned_business_designation` | Added | [Account#create.business_profile](/api/accounts/create?api-version=2025-04-30.basil#create_account-business_profile), [Account#update.business_profile](/api/accounts/update?api-version=2025-04-30.basil#update_account-business_profile), [Account.business_profile](/api/accounts/object?api-version=2025-04-30.basil#account_object-business_profile) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `minority_owned_business_designation` | Added | [Account::BusinessProfile](/api/accounts/object?api-version=2025-04-30.basil#account_object-business_profile), [Account::CreateParams::BusinessProfile](/api/accounts/create?api-version=2025-04-30.basil#create_account-business_profile), [Account::UpdateParams::BusinessProfile](/api/accounts/update?api-version=2025-04-30.basil#update_account-business_profile) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `minority_owned_business_designation` | Added | [Account.BusinessProfile](/api/accounts/object?api-version=2025-04-30.basil#account_object-business_profile), [Account.CreateParamsBusinessProfile](/api/accounts/create?api-version=2025-04-30.basil#create_account-business_profile), [Account.UpdateParamsBusinessProfile](/api/accounts/update?api-version=2025-04-30.basil#update_account-business_profile) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `minorityOwnedBusinessDesignation` | Added | [Account.business_profile](/api/accounts/object?api-version=2025-04-30.basil#account_object-business_profile), [AccountCreateParams.business_profile](/api/accounts/create?api-version=2025-04-30.basil#create_account-business_profile), [AccountUpdateParams.business_profile](/api/accounts/update?api-version=2025-04-30.basil#update_account-business_profile) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `minority_owned_business_designation` | Added | [Account.business_profile](/api/accounts/object?api-version=2025-04-30.basil#account_object-business_profile), [AccountCreateParams.business_profile](/api/accounts/create?api-version=2025-04-30.basil#create_account-business_profile), [AccountUpdateParams.business_profile](/api/accounts/update?api-version=2025-04-30.basil#update_account-business_profile) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `MinorityOwnedBusinessDesignation` | Added | [AccountBusinessProfileParams](/api/accounts/create?api-version=2025-04-30.basil#create_account-business_profile), [AccountBusinessProfile](/api/accounts/object?api-version=2025-04-30.basil#account_object-business_profile) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `MinorityOwnedBusinessDesignation` | Added | [AccountBusinessProfileOptions](/api/accounts/create?api-version=2025-04-30.basil#create_account-business_profile), [AccountBusinessProfile](/api/accounts/object?api-version=2025-04-30.basil#account_object-business_profile) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-04-30.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.1.0](https://github.com/stripe/stripe-python/releases/tag/v12.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.2.0](https://github.com/stripe/stripe-php/releases/tag/v17.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.1.0](https://github.com/stripe/stripe-java/releases/tag/v29.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.1.0](https://github.com/stripe/stripe-node/releases/tag/v18.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.1.0](https://github.com/stripe/stripe-go/releases/tag/v82.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds a demographic information hash to the Persons API](https://docs.stripe.com/changelog/basil/2025-04-30/add-us-cfpb-data-to-person.md)
