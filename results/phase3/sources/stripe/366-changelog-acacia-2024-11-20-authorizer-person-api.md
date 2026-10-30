# Adds support for authorisers to Person API

## What’s new

Adds the authoriser role as a parameter in the `relationship` field of the Person API.

The Stripe account [representative](https://docs.stripe.com/api/persons/object.md?api-version=2024-11-20.acacia#person_object-relationship) is defined as the person that’s authorised to act as the primary representative of the account. This person provides information about themselves and is designated by the business to provide general information about the account.

To fulfil [Know Your Customer](https://support.stripe.com/questions/know-your-customer-obligations) (KYC) requirements, Stripe might be required to verify the [authority of the representative](https://support.stripe.com/questions/representative-authority-verification). If the representative on the Stripe account doesn’t match a registered representative for the business, you can add an authoriser to the account to grant them authority to represent the business.

An authoriser is usually a person that qualifies as a registered representative for the business, but isn’t listed as a representative on the business Stripe account. Stripe might request additional information, such as a [company authorization document](https://docs.stripe.com/api/persons/create.md?api-version=2024-11-20.acacia#create_person-documents-company_authorization), that allows the authoriser to transfer authority (to authorise) the representative.

There can only be one authoriser on a Stripe account. The authoriser can’t be the account representative. This role is only available in countries where the authoriser can transfer authority to the representative.

```curl
curl https://api.stripe.com/v1/accounts/acct_xxxxx/persons \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d first_name=John \
  -d last_name=Doe \
  -d "relationship[authorizer]=true"
```

## Impact

You can use the new authoriser `relationship` field to create an authoriser for your connected accounts. Use this authoriser to satisfy authority verification requirements on your connected account.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `authorizer` | Added | [Account#persons.relationship](/api/persons/list?api-version=2024-11-20.acacia#list_person-relationship), [Token#create.person.relationship](/api/tokens/create_person?api-version=2024-11-20.acacia#create_person_token-person-relationship) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `authorizer` | Added | [stripe.Account.CreatePersonParamsRelationship](/api/persons/create?api-version=2024-11-20.acacia#create_person-relationship), [stripe.Account.ListPersonsParamsRelationship](/api/persons/list?api-version=2024-11-20.acacia#list_person-relationship), [stripe.Account.ModifyPersonParamsRelationship](/api/persons/update?api-version=2024-11-20.acacia#update_person-relationship), [stripe.Account.PersonsParamsRelationship](/api/persons/object?api-version=2024-11-20.acacia#person_object-relationship), [stripe.Token.CreateParamsPersonRelationship](/api/tokens/create_person?api-version=2024-11-20.acacia#create_person_token-person-relationship), [stripe.Person.Relationship](/api/persons/object?api-version=2024-11-20.acacia#person_object-relationship) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `authorizer` | Added | [AccountPersonsParams.relationship](/api/persons/object?api-version=2024-11-20.acacia#person_object-relationship), [TokenCreateParams.person.relationship](/api/tokens/create_person?api-version=2024-11-20.acacia#create_person_token-person-relationship) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `authorizer` | Added | [AccountPersonsParams.relationship](/api/persons/object?api-version=2024-11-20.acacia#person_object-relationship), [TokenCreateParams.person.relationship](/api/tokens/create_person?api-version=2024-11-20.acacia#create_person_token-person-relationship) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Authorizer` | Added | [AccountPersonsRelationshipParams](/api/persons/object?api-version=2024-11-20.acacia#person_object-relationship), [TokenPersonRelationshipParams](/api/tokens/create_person?api-version=2024-11-20.acacia#create_person_token-person-relationship) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Authorizer` | Added | [AccountRelationshipOptions](/api/persons/object?api-version=2024-11-20.acacia#person_object-relationship), [TokenPersonRelationshipOptions](/api/tokens/create_person?api-version=2024-11-20.acacia#create_person_token-person-relationship) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-11-20.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.3.0](https://github.com/stripe/stripe-python/releases/tag/v11.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.3.0](https://github.com/stripe/stripe-php/releases/tag/v16.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.1.0](https://github.com/stripe/stripe-java/releases/tag/v28.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.4.0](https://github.com/stripe/stripe-node/releases/tag/v17.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.1.0](https://github.com/stripe/stripe-go/releases/tag/v81.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
