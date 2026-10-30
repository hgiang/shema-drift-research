# Accounts now support digital attestation for proof of registration and beneficial ownership verification

## What’s new

Adds support for digital attestation to the [Accounts](https://docs.stripe.com/api/accounts.md?api-version=2025-12-15.clover) API when uploading documents for proof of registration and ultimate beneficial ownership verification. You can now specify the person who electronically signed the document using the following parameters:

- [documents.proof_of_registration.signer.person](https://docs.stripe.com/api/accounts/update.md?api-version=2025-12-15.clover#update_account-documents-proof_of_registration-signer-person): ID of the [Person](https://docs.stripe.com/api/persons/object.md?api-version=2025-12-15.clover) who electronically signed the proof of registration document
- [documents.proof_of_ultimate_beneficial_ownership.signer.person](https://docs.stripe.com/api/accounts/update.md?api-version=2025-12-15.clover#update_account-documents-proof_of_ultimate_beneficial_ownership-signer-person): ID of the [Person](https://docs.stripe.com/api/persons/object.md?api-version=2025-12-15.clover) who electronically signed the proof of ultimate beneficial ownership document

These parameters are available when you [create an Account](https://docs.stripe.com/api/accounts/create.md?api-version=2025-12-15.clover) or [update an existing Account](https://docs.stripe.com/api/accounts/update.md?api-version=2025-12-15.clover).

## Impact

You can now provide digital attestation for proof of registration and ultimate beneficial ownership verification. Digital attestation allows authorised signers to electronically sign attestation agreements as an alternative to uploading physical documents. This streamlines the onboarding process for European compliance requirements while maintaining the same level of verification.

If you use this feature, make sure the person specified in the `signer.person` parameter has the proper authorisation to sign on behalf of the business, and their [first_name](https://docs.stripe.com/api/persons/object.md?api-version=2025-12-15#person_object-first_name) and [last_name](https://docs.stripe.com/api/persons/object.md?api-version=2025-12-15#person_object-last_name) are set.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `signer` | Added | [Account#create.documents.proof_of_registration](/api/accounts/create?api-version=2025-12-15.clover#create_account-documents-proof_of_registration), [Account#create.documents.proof_of_ultimate_beneficial_ownership](/api/accounts/create?api-version=2025-12-15.clover#create_account-documents-proof_of_ultimate_beneficial_ownership), [Account#update.documents.proof_of_registration](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_registration), [Account#update.documents.proof_of_ultimate_beneficial_ownership](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_ultimate_beneficial_ownership) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `signer` | Added | [AccountCreateParams::Document::ProofOfRegistration](/api/accounts/create?api-version=2025-12-15.clover#create_account-documents-proof_of_registration), [AccountCreateParams::Document::ProofOfUltimateBeneficialOwnership](/api/accounts/create?api-version=2025-12-15.clover#create_account-documents-proof_of_ultimate_beneficial_ownership), [AccountUpdateParams::Document::ProofOfRegistration](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_registration), [AccountUpdateParams::Document::ProofOfUltimateBeneficialOwnership](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_ultimate_beneficial_ownership) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `signer` | Added | [AccountCreateParamsDocumentProofOfRegistration](/api/accounts/create?api-version=2025-12-15.clover#create_account-documents-proof_of_registration), [AccountCreateParamsDocumentProofOfUltimateBeneficialOwnership](/api/accounts/create?api-version=2025-12-15.clover#create_account-documents-proof_of_ultimate_beneficial_ownership), [AccountModifyParamsDocumentProofOfRegistration](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_registration), [AccountModifyParamsDocumentProofOfUltimateBeneficialOwnership](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_ultimate_beneficial_ownership) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `signer` | Added | [Account.create().$params.document.proof_of_registration](/api/accounts/create?api-version=2025-12-15.clover#create_account-documents-proof_of_registration), [Account.create().$params.document.proof_of_ultimate_beneficial_ownership](/api/accounts/create?api-version=2025-12-15.clover#create_account-documents-proof_of_ultimate_beneficial_ownership), [Account.update().$params.document.proof_of_registration](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_registration), [Account.update().$params.document.proof_of_ultimate_beneficial_ownership](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_ultimate_beneficial_ownership) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `signer` | Added | [AccountCreateParams.documents.proof_of_registration](/api/accounts/create?api-version=2025-12-15.clover#create_account-documents-proof_of_registration), [AccountCreateParams.documents.proof_of_ultimate_beneficial_ownership](/api/accounts/create?api-version=2025-12-15.clover#create_account-documents-proof_of_ultimate_beneficial_ownership), [AccountUpdateParams.documents.proof_of_registration](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_registration), [AccountUpdateParams.documents.proof_of_ultimate_beneficial_ownership](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_ultimate_beneficial_ownership) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `signer` | Added | [AccountCreateParams.documents.proof_of_registration](/api/accounts/create?api-version=2025-12-15.clover#create_account-documents-proof_of_registration), [AccountCreateParams.documents.proof_of_ultimate_beneficial_ownership](/api/accounts/create?api-version=2025-12-15.clover#create_account-documents-proof_of_ultimate_beneficial_ownership), [AccountUpdateParams.documents.proof_of_registration](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_registration), [AccountUpdateParams.documents.proof_of_ultimate_beneficial_ownership](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_ultimate_beneficial_ownership) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Signer` | Added | [AccountDocumentsProofOfRegistrationParams](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_registration), [AccountDocumentsProofOfUltimateBeneficialOwnershipParams](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_ultimate_beneficial_ownership) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Signer` | Added | [AccountDocumentsProofOfRegistrationOptions](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_registration), [AccountDocumentsProofOfUltimateBeneficialOwnershipOptions](/api/accounts/update?api-version=2025-12-15.clover#update_account-documents-proof_of_ultimate_beneficial_ownership) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-12-15.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v18.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v18.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v14.2.0](https://github.com/stripe/stripe-python/releases/tag/v14.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v19.2.0](https://github.com/stripe/stripe-php/releases/tag/v19.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v31.2.0](https://github.com/stripe/stripe-java/releases/tag/v31.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v20.2.0](https://github.com/stripe/stripe-node/releases/tag/v20.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v84.2.0](https://github.com/stripe/stripe-go/releases/tag/v84.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v50.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v50.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Connect platforms can now use Accounts v2 to manage connected accounts and customers](https://docs.stripe.com/changelog/clover/2025-12-15/accounts-v2.md)
- [Adds the customer account property to v1 APIs for Accounts v2 interoperability](https://docs.stripe.com/changelog/clover/2025-12-15/accounts-v2-v1-api-support.md)
