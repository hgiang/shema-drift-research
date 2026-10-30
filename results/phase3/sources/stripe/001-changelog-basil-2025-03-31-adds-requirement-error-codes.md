# Adds new error codes for required verifications

## What’s new

Adds the following error codes to the `requirements.errors` array in the [Accounts API](https://docs.stripe.com/api/accounts/object.md?api-version=2025-03-31.basil#account_object-requirements-errors-code), [Capabilities API](https://docs.stripe.com/api/capabilities/object.md?api-version=2025-03-31.basil#capability_object-requirements-errors-code), [Persons API](https://docs.stripe.com/api/persons/object.md?api-version=2025-03-31.basil#person_object-requirements-errors-code) and [Bank Accounts API](https://docs.stripe.com/api/external_account_bank_accounts/object.md?api-version=2025-03-31.basil#account_bank_account_object-requirements-errors-code).

- `information_missing`
- `invalid_signator`
- `verification_failed_authorizer_authority`
- `verification_rejected_ownership_exemption_reason`

The `information_missing` error code is more generic than previous error codes. Use the associated `requirement` and `reason` fields to learn what information is missing. For example, some Singapore accounts might see:

```json
// GET /v1/accounts/{{CONNECTED_ACCOUNT_ID}}
{
  ...
  "requirements": {
    "currently_due": ["documents.proof_of_ultimate_beneficial_ownership.files"],
    "errors": [
      {
        "code": "information_missing",
        "requirement": "documents.proof_of_ultimate_beneficial_ownership.files",
        "reason": "We identified that your business is owned by holding companies that require additional information to be collected. Please provide documents that include information for each applicable holding company. For more information, see https://support.stripe.com/questions/beneficial-ownership-verification-for-holding-companies. The new holding companies we have identified are: ACME INC."
      }
    ],
    ...
  },
  ...
}
```

We return the `invalid_signator` error if you uploaded a [Letter of Attestation](https://support.stripe.com/questions/singapore-ultimate-beneficial-ownership-and-director-requirements) as your proof of Ultimate Beneficial Ownership document, and we couldn’t verify the professional body that notarised the document.

```json
{
  ...
  "requirements": {
    "currently_due": ["documents.proof_of_ultimate_beneficial_ownership.files"],
    "errors": [
      {
        "code": "invalid_signator",
        "requirement": "documents.proof_of_ultimate_beneficial_ownership.files",
        "reason": "We could not verify the professional certifying body of this document."
      }
    ],
    ...
  },
  ...
}
```

We return the `verification_failed_authorizer_authority` error if you designated a Person as the [authorizer](https://docs.stripe.com/api/persons/update.md?api-version=2025-03-31.basil#update_person-relationship-authorizer) on your account and we couldn’t verify their position of authority within your company. See [Representative Authority Verification](https://support.stripe.com/questions/representative-authority-verification) for more information.

```json
{
  ...
  "requirements": {
    "currently_due": ["{{AUTHORIZER_PERSON_TOKEN}}.relationship.authorizer"],
    "errors": [
      {
        "code": "verification_failed_authorizer_authority",
        "requirement": "{{AUTHORIZER_PERSON_TOKEN}}.relationship.authorizer",
        "reason": "The authority of the authorizer could not be verified. Authorizers must be one of Director, Chief Executive Officer listed on acra.gov.sg."
      }
    ],
    ...
  },
  ...
}
```

We return the `verification_rejected_ownership_exemption_reason` error if you submitted an exemption for providing your Ultimate Beneficial Owners, and we rejected the exemption request.

```json
{
  ...
  "requirements": {
    "currently_due": ["documents.proof_of_ultimate_beneficial_ownership.files"],
    "alternatives": [
      {
        "original_fields_due": ["documents.proof_of_ultimate_beneficial_ownership.files"],
        "alternative_fields_due": ["company.ownership_exemption_reason"],
      }
    ],
    "errors": [
      {
        "code": "verification_rejected_ownership_exemption_reason",
        "requirement": "company.ownership_exemption_reason",
        "reason": "The ownership exemption reason was rejected."
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

You’ll be able to handle new error codes for the [upcoming requirement updates](https://docs.stripe.com/connect/upcoming-requirements-updates.md?program=sg-2023) in Singapore.

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `information_missing`, `invalid_signator`, `verification_failed_authorizer_authority`, `verification_rejected_ownership_exemption_reason` | Added | [Account.future_requirements.errors[].code](/api/accounts/object?api-version=2025-03-31.basil#account_object-future_requirements-errors-code), [Account.requirements.errors[].code](/api/accounts/object?api-version=2025-03-31.basil#account_object-requirements-errors-code), [BankAccount.future_requirements.errors[].code](/api/external_account_bank_accounts/object?api-version=2025-03-31.basil#account_bank_account_object-future_requirements-errors-code), [BankAccount.requirements.errors[].code](/api/external_account_bank_accounts/object?api-version=2025-03-31.basil#account_bank_account_object-requirements), [Capability.future_requirements.errors[].code](/api/capabilities/object?api-version=2025-03-31.basil#capability_object-future_requirements-errors-code), [Capability.requirements.errors[].code](/api/capabilities/object?api-version=2025-03-31.basil#capability_object-requirements-errors-code), [Person.future_requirements.errors[].code](/api/persons/object?api-version=2025-03-31.basil#person_object-future_requirements-errors-code), [Person.requirements.errors[].code](/api/persons/object?api-version=2025-03-31.basil#person_object-requirements-errors-code) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `information_missing`, `invalid_signator`, `verification_failed_authorizer_authority`, `verification_rejected_ownership_exemption_reason` | Added | [Account.FutureRequirement.Error.code](/api/accounts/object?api-version=2025-03-31.basil#account_object-future_requirements-errors-code), [Account.Requirement.Error.code](/api/accounts/object?api-version=2025-03-31.basil#account_object-requirements-errors-code), [AccountCapability.FutureRequirement.Error.code](/api/capabilities/object?api-version=2025-03-31.basil#capability_object-future_requirements-errors-code), [AccountCapability.Requirement.Error.code](/api/capabilities/object?api-version=2025-03-31.basil#capability_object-requirements-errors-code), [AccountPerson.FutureRequirement.Error.code](/api/persons/object?api-version=2025-03-31.basil#person_object-future_requirements-errors-code), [AccountPerson.Requirement.Error.code](/api/persons/object?api-version=2025-03-31.basil#person_object-requirements-errors-code), [BankAccount.FutureRequirement.Error.code](/api/accounts/object?api-version=2025-03-31.basil#account_object-future_requirements-errors-code), [BankAccount.Requirement.Error.code](/api/accounts/object?api-version=2025-03-31.basil#account_object-requirements-errors-code) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `information_missing`, `invalid_signator`, `verification_failed_authorizer_authority`, `verification_rejected_ownership_exemption_reason` | Added | [Account.future_requirements.errors[].code](/api/accounts/object?api-version=2025-03-31.basil#account_object-future_requirements-errors-code), [Account.requirements.errors[].code](/api/accounts/object?api-version=2025-03-31.basil#account_object-requirements-errors-code), [AccountCapability.future_requirements.errors[].code](/api/capabilities/object?api-version=2025-03-31.basil#capability_object-future_requirements-errors-code), [AccountCapability.requirements.errors[].code](/api/capabilities/object?api-version=2025-03-31.basil#capability_object-requirements-errors-code), [AccountPerson.future_requirements.errors[].code](/api/persons/object?api-version=2025-03-31.basil#person_object-future_requirements-errors-code), [AccountPerson.requirements.errors[].code](/api/persons/object?api-version=2025-03-31.basil#person_object-requirements-errors-code), [BankAccount.future_requirements.errors[].code](/api/external_account_bank_accounts/object?api-version=2025-03-31.basil#account_bank_account_object-future_requirements-errors-code), [BankAccount.requirements.errors[].code](/api/external_account_bank_accounts/object?api-version=2025-03-31.basil#account_bank_account_object-requirements) |

#### Go

| Values | Change | Enums |
| --- | --- | --- |
| `information_missing`, `invalid_signator`, `verification_failed_authorizer_authority`, `verification_rejected_ownership_exemption_reason` | Added | [BankAccountFutureRequirementsErrors.Code](/api/external_account_bank_accounts/object?api-version=2025-03-31.basil#account_bank_account_object-future_requirements-errors-code), [BankAccountRequirementsErrors.Code](/api/external_account_bank_accounts/object?api-version=2025-03-31.basil#account_bank_account_object-requirements-errors-code) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-03-31.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.0.0](https://github.com/stripe/stripe-python/releases/tag/v12.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.0.0](https://github.com/stripe/stripe-php/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.0.0](https://github.com/stripe/stripe-java/releases/tag/v29.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.0.0](https://github.com/stripe/stripe-node/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.0.0](https://github.com/stripe/stripe-go/releases/tag/v82.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
