# Adds account and person tokens to Accounts v2 to securely transmit sensitive data

## What’s new

Adds [v2.core.account_token](https://docs.stripe.com/api/v2/core/account-tokens/object.md?api-version=2025-11-17.preview#v2_account_token_object) and [v2.core.account_person_token](https://docs.stripe.com/api/v2/core/person-tokens/object.md?api-version=2025-11-17.preview#v2_person_token_object) resources to the [Accounts v2](https://docs.stripe.com/api/v2/core/accounts.md?api-version=2025-11-17.preview) API. Account and person tokens can be created directly from a browser with a publishable key and then later be included in a request with the new [account_token](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=2025-11-17.preview#v2_create_accounts-account_token) and [person_token](https://docs.stripe.com/api/v2/core/persons/create.md?api-version=2025-11-17.preview#v2_create_persons-person_token) parameters.

## Impact

Instead of receiving and transmitting PII for Accounts v2 and their associated persons yourself, you can now send it directly to Stripe from your customer’s browser to make sure their sensitive information is securely and correctly handled.

## Changes

#### REST API

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Core.AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [V2.Core.AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [V2.Core.AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [V2.Core.AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [V2.Core.Account#create](/api/v2/core/accounts/create?api-version=2025-11-17.preview), [V2.Core.Account#update](/api/v2/core/accounts/update?api-version=2025-11-17.preview), [V2.Core.AccountPerson#create](/api/v2/core/accounts/create-person?api-version=2025-11-17.preview#v2_create_persons), [V2.Core.AccountPerson#update](/api/v2/core/accounts/update-person?api-version=2025-11-17.preview#v2_update_persons) |

#### Ruby

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2::Core::AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [V2::Core::AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [V2::Core::AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [V2::Core::AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [V2::Core::AccountCreateParams](/api/v2/core/accounts/create?api-version=2025-11-17.preview), [V2::Core::AccountUpdateParams](/api/v2/core/accounts/update?api-version=2025-11-17.preview), [V2::Core::AccountPersonCreateParams](/api/v2/core/accounts/create-person?api-version=2025-11-17.preview#v2_create_persons), [V2::Core::AccountPersonUpdateParams](/api/v2/core/accounts/update-person?api-version=2025-11-17.preview#v2_update_persons) |

#### Python

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [v2.core.AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [v2.core.AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [v2.core.AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [v2.core.AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [v2.core.AccountCreateParams](/api/v2/core/accounts/create?api-version=2025-11-17.preview), [v2.core.AccountModifyParams](/api/v2/core/accounts/update?api-version=2025-11-17.preview), [v2.core.AccountPersonCreateParams](/api/v2/core/accounts/create-person?api-version=2025-11-17.preview#v2_create_persons), [v2.core.AccountPersonModifyParams](/api/v2/core/accounts/update-person?api-version=2025-11-17.preview#v2_update_persons) |

#### PHP

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Core.AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [V2.Core.AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [V2.Core.AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [V2.Core.AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [V2\Core\Account.create().$params](/api/v2/core/accounts/create?api-version=2025-11-17.preview), [V2\Core\Account.update().$params](/api/v2/core/accounts/update?api-version=2025-11-17.preview), [V2\Core\AccountPerson.create().$params](/api/v2/core/accounts/create-person?api-version=2025-11-17.preview#v2_create_persons), [V2\Core\AccountPerson.update().$params](/api/v2/core/accounts/update-person?api-version=2025-11-17.preview#v2_update_persons) |

#### Java

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [v2.core.AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [v2.core.AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [v2.core.AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [v2.core.AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [v2.core.AccountCreateParams](/api/v2/core/accounts/create?api-version=2025-11-17.preview), [v2.core.AccountUpdateParams](/api/v2/core/accounts/update?api-version=2025-11-17.preview), [v2.core.AccountPersonCreateParams](/api/v2/core/accounts/create-person?api-version=2025-11-17.preview#v2_create_persons), [v2.core.AccountPersonUpdateParams](/api/v2/core/accounts/update-person?api-version=2025-11-17.preview#v2_update_persons) |

#### Node.js

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Core.AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [V2.Core.AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [V2.Core.AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [V2.Core.AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [V2.Core.AccountCreateParams](/api/v2/core/accounts/create?api-version=2025-11-17.preview), [V2.Core.AccountUpdateParams](/api/v2/core/accounts/update?api-version=2025-11-17.preview), [V2.Core.AccountPersonCreateParams](/api/v2/core/accounts/create-person?api-version=2025-11-17.preview#v2_create_persons), [V2.Core.AccountPersonUpdateParams](/api/v2/core/accounts/update-person?api-version=2025-11-17.preview#v2_update_persons) |

#### Go

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2CoreAccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [V2CoreAccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [V2CoreAccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [V2CoreAccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [V2CoreAccountParams](/api/v2/core/accounts/create?api-version=2025-11-17.preview), [V2CoreAccountPersonParams](/api/v2/core/accounts/create-person?api-version=2025-11-17.preview#v2_create_persons) |

#### .NET

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Core.AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [V2.Core.AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [V2.Core.AccountPersonToken](/api/v2/person-tokens/object?api-version=2025-11-17.preview#v2_person_token_object), [V2.Core.AccountToken](/api/v2/account-tokens/object?api-version=2025-11-17.preview#v2_account_token_object), [V2.Core.AccountCreateOptions](/api/v2/core/accounts/create?api-version=2025-11-17.preview), [V2.Core.AccountUpdateOptions](/api/v2/core/accounts/update?api-version=2025-11-17.preview), [V2.Core.AccountPersonCreateOptions](/api/v2/core/accounts/create-person?api-version=2025-11-17.preview#v2_create_persons), [V2.Core.AccountPersonUpdateOptions](/api/v2/core/accounts/update-person?api-version=2025-11-17.preview#v2_update_persons) |

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

## Related changes

- [Updates requirements collection parameters for Accounts v2](https://docs.stripe.com/changelog/clover/2025-11-17/accounts-v2-requirements-collection.md)
- [Adds future requirements field to Accounts v2](https://docs.stripe.com/changelog/clover/2025-11-17/accounts-v2-future-requirements.md)
- [PaymentMethods can now list payment methods for a customer account using Accounts v2](https://docs.stripe.com/changelog/clover/2025-11-17/v2-accounts-payment-methods.md)
- [Adds support for PayPay to Accounts](https://docs.stripe.com/changelog/clover/2025-11-17/paypay-connect.md)
- [Adds support for Konbini payments and Japanese statement descriptors in Accounts v2](https://docs.stripe.com/changelog/clover/2025-11-17/accounts-v2-konbini-payments.md)
- [Adds the capability to hold EUR funds to Accounts v2](https://docs.stripe.com/changelog/clover/2025-11-17/account-v2-storer-config-eur.md)
