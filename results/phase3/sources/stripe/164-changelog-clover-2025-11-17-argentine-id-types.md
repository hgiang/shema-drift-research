# Adds support for Argentine ID types

## What’s new

Adds support for two Argentine ID number types: `ar_dni` (Documento Nacional de Identidad) and `ar_cuit` (Código Único de Identificación Tributaria). Use these types when you create or update [Accounts](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2025-11-17.preview) and [Persons](https://docs.stripe.com/api/v2/core/persons.md?api-version=2025-11-17.preview) for individuals and businesses in Argentina.

## Impact

If you work with users or businesses in Argentina, you can now collect and store DNI or CUIT numbers in the [id_numbers](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2025-11-17.preview#v2_account_object-identity-business_details-id_numbers) field. This improves identity verification and compliance for accounts in Argentina.

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `ar_cuit` | Added | [V2.Core.Account.identity.business_details.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-business_details-id_numbers-type), [V2.Core.Account#create.identity.business_details.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-business_details-id_numbers-type), [V2.Core.Account#update.identity.business_details.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-business_details-id_numbers-type), [V2.Core.Account.identity.individual.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-individual-id_numbers-type), [V2.Core.AccountPerson.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-id_numbers-type), [V2.Core.Account#create.identity.individual.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-individual-id_numbers-type), [V2.Core.Account#update.identity.individual.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-individual-id_numbers-type), [V2.Core.AccountPerson#create.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-id_numbers-type), [V2.Core.AccountPerson#update.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-id_numbers-type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enums |
| --- | --- | --- |
| `ar_cuit` | Added | [V2.Core.Account.Identity.BusinessDetail.IdNumber](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-business_details-id_numbers-type), [v2.core.AccountCreateParamsIdentityBusinessDetailIdNumber](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-business_details-id_numbers-type), [v2.core.AccountModifyParamsIdentityBusinessDetailIdNumber](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-business_details-id_numbers-type), [V2.Core.Account.Identity.Individual.IdNumber](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-individual-id_numbers-type), [V2.Core.AccountPerson.IdNumber](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-id_numbers-type), [v2.core.AccountCreateParamsIdentityIndividualIdNumber](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-individual-id_numbers-type), [v2.core.AccountModifyParamsIdentityIndividualIdNumber](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-individual-id_numbers-type), [v2.core.AccountPersonCreateParamsIdNumber](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-id_numbers-type), [v2.core.AccountPersonModifyParamsIdNumber](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-id_numbers-type) |

#### PHP

| Value | Change | Enums |
| --- | --- | --- |
| `ar_cuit` | Added | [V2.Core.Account.identity.business_details.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-business_details-id_numbers-type), [V2.Core.Account.identity.individual.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-individual-id_numbers-type), [V2.Core.AccountPerson.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-id_numbers-type) |

#### Java

| Value | Change | Enums |
| --- | --- | --- |
| `ar_cuit` | Added | [v2.core.AccountCreateParams.identity.business_details.id_numbers[]](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-identity-business_details-id_numbers-type), [v2.core.AccountUpdateParams.identity.business_details.id_numbers[]](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-identity-business_details-id_numbers-type), [v2.core.AccountCreateParams.identity.individual.id_numbers[]](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-identity-individual-id_numbers-type), [v2.core.AccountUpdateParams.identity.individual.id_numbers[]](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-identity-individual-id_numbers-type), [v2.core.AccountPersonCreateParams.id_numbers[]](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-id_numbers-type), [v2.core.AccountPersonUpdateParams.id_numbers[]](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-id_numbers-type) |

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `ar_cuit` | Added | [V2.Core.Account.identity.business_details.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-business_details-id_numbers-type), [V2.Core.AccountCreateParams.identity.business_details.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-business_details-id_numbers-type), [V2.Core.AccountUpdateParams.identity.business_details.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-business_details-id_numbers-type), [V2.Core.Account.identity.individual.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-individual-id_numbers-type), [V2.Core.AccountPerson.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-id_numbers-type), [V2.Core.AccountCreateParams.identity.individual.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-individual-id_numbers-type), [V2.Core.AccountUpdateParams.identity.individual.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-individual-id_numbers-type), [V2.Core.AccountPersonCreateParams.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-id_numbers-type), [V2.Core.AccountPersonUpdateParams.id_numbers[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-id_numbers-type) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `ar_cuit` | Added | [V2CoreAccountIdentityBusinessDetailsIdNumber](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-business_details-id_numbers-Type), [V2CoreAccountIdentityIndividualIdNumber](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-identity-individual-id_numbers-Type), [V2CoreAccountPersonIdNumber](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-id_numbers-Type) |

#### .NET

This change doesn’t affect the .NET SDK.

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
