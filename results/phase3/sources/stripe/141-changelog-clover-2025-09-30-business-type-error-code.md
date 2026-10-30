# Adds a new error code for business type validations

## What’s new

Adds an `unsupported_business_type` error code to the [requirements.errors](https://docs.stripe.com/api/accounts/object.md?api-version=2025-09-30.clover#account_object-requirements-errors) array in the [Accounts API](https://docs.stripe.com/api/accounts/object.md?api-version=2025-09-30.clover#account_object-requirements-errors-code), [Capabilities API](https://docs.stripe.com/api/capabilities/object.md?api-version=2025-09-30.clover#capability_object-requirements-errors-code), [Persons API](https://docs.stripe.com/api/persons/object.md?api-version=2025-09-30.clover#person_object-requirements-errors-code) and [Bank Accounts API](https://docs.stripe.com/api/external_account_bank_accounts/object.md?api-version=2025-09-30.clover#account_bank_account_object-requirements-errors-code).

We return the `unsupported_business_type` error if the business type isn’t supported in the merchant’s country.

```json
// GET /v1/accounts/{{CONNECTED_ACCOUNT_ID}}
{
  ...
  "requirements": {
    "currently_due": ["business_type"],
    "errors": [
      {
        "code": "unsupported_business_type",
        "requirement": "business_type",
        "reason": "Business type isn't supported in merchant country. 'individual' isn't a supported business type in country NL."
      }
    ],
    ...
  },
  ...
}
```

## Why is this a breaking change?

Some Connect integrations might require an update to handle the new error codes.

## Impact

If you provide a business type that isn’t supported for the merchant’s country, we return the `unsupported_business_type` error code. You need to update the business type to a valid value.

### Create new accounts with the correct business type and company structure

When creating new accounts, make sure to provide a valid business type and company structure for the country. Doing so can prevent you from receiving any errors.

```bash
# Correct approach for new accounts
curl -X POST https://api.stripe.com/v1/accounts \
  -u sk_test_123: \
  -d "country=NL" \
  -d "type=custom" \
  -d "business_type=company" \
  -d "company[structure]=sole_proprietorship"
```

If you encounter the error on existing accounts, update the accounts to resolve the error.

```bash
# Update existing accounts
curl -X POST https://api.stripe.com/v1/accounts/acct_123 \
  -u sk_test_123: \
  -d "business_type=company" \
  -d "company[structure]=sole_proprietorship"
```

```json
// Successful response
{
  "id": "acct_123",
  "business_type": "company",
  "company": {
    "structure": "sole_proprietorship",
    ...
  },
  "requirements": {
    "currently_due": [],  // business_type requirement resolved
    "errors": []
  }
  ...
}
```

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `unsupported_business_type` | Added | [BankAccount.future_requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-future_requirements-errors-code), [BankAccount.requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-requirements-errors-code), [Account.future_requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-future_requirements-errors-code), [Account.requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-requirements-errors-code), [Capability.future_requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-future_requirements-errors-code), [Capability.requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-requirements-errors-code), [Person.future_requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-future_requirements-errors-code), [Person.requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-requirements-errors-code) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enums |
| --- | --- | --- |
| `unsupported_business_type` | Added | [BankAccount.FutureRequirement.Error](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-future_requirements-errors-code), [BankAccount.Requirement.Error](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-requirements-errors-code), [Account.FutureRequirement.Error](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-future_requirements-errors-code), [Account.Requirement.Error](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-requirements-errors-code), [Capability.FutureRequirement.Error](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-future_requirements-errors-code), [Capability.Requirement.Error](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-requirements-errors-code), [Person.FutureRequirement.Error](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-future_requirements-errors-code), [Person.Requirement.Error](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-requirements-errors-code) |

#### PHP

| Value | Change | Enums |
| --- | --- | --- |
| `unsupported_business_type` | Added | [BankAccount.future_requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-future_requirements-errors-code), [BankAccount.requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-requirements-errors-code), [Account.future_requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-future_requirements-errors-code), [Account.requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-requirements-errors-code), [Capability.future_requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-future_requirements-errors-code), [Capability.requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-requirements-errors-code), [Person.future_requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-future_requirements-errors-code), [Person.requirements.errors[]](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-requirements-errors-code) |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `unsupported_business_type` | Added | [Account.future_requirements.errors[]](/api/accounts/object?api-version=2025-09-30.clover#account_object-future_requirements-errors-code), [Account.requirements.errors[]](/api/accounts/object?api-version=2025-09-30.clover#account_object-requirements-errors-code), [BankAccount.future_requirements.errors[]](/api/accounts/object?api-version=2025-09-30.clover#account_object-future_requirements-errors-code), [BankAccount.requirements.errors[]](/api/accounts/object?api-version=2025-09-30.clover#account_object-requirements-errors-code), [Capability.future_requirements.errors[]](/api/accounts/object?api-version=2025-09-30.clover#account_object-future_requirements-errors-code), [Capability.requirements.errors[]](/api/accounts/object?api-version=2025-09-30.clover#account_object-requirements-errors-code), [Person.future_requirements.errors[]](/api/accounts/object?api-version=2025-09-30.clover#account_object-future_requirements-errors-code), [Person.requirements.errors[]](/api/accounts/object?api-version=2025-09-30.clover#account_object-requirements-errors-code) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `unsupported_business_type` | Added | [BankAccountFutureRequirementsErrors](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-future_requirements-errors-Code), [BankAccountRequirementsErrors](/api/customer_bank_accounts/object?api-version=2025-09-30.clover#bank_account_object-requirements-errors-Code) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-09-30.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v16.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.0.1](https://github.com/stripe/stripe-python/releases/tag/v13.0.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.0.0](https://github.com/stripe/stripe-php/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.0.0](https://github.com/stripe/stripe-java/releases/tag/v30.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.1.0](https://github.com/stripe/stripe-node/releases/tag/v19.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.0.0](https://github.com/stripe/stripe-go/releases/tag/v83.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds specific descriptions for risk requirements during legal, PEP and sanctions review](https://docs.stripe.com/changelog/clover/2025-09-30/expanded-risk-requirement-descriptions.md)
- [Adds account balance and payout settings with the Balance Settings API](https://docs.stripe.com/changelog/clover/2025-09-30/balance-settings-ga.md)
