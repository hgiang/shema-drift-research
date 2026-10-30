# Standardises SEPA Direct Debit payment settings in the Accounts API

## What’s new

The [sepa_debit_payments.creditor_id](https://docs.stripe.com/api/accounts/create.md?api-version=2026-09-30.endive#create_account-settings-sepa_debit_payments-creditor_id) property on [Accounts](https://docs.stripe.com/api/accounts/object.md?api-version=2026-09-30.endive#account_object-settings) now returns Stripe’s country-specific shared [SEPA Creditor Identifier](https://support.stripe.com/questions/sepa-creditor-identifier-\(creditor-id\)) when an account doesn’t have a custom one. Previously, this property was omitted for accounts using the shared identifier.

You can now set a custom SEPA Creditor Identifier to be used for SEPA Direct Debit payments when you [create a v1 Account](https://docs.stripe.com/api/accounts/create.md?api-version=2026-09-30.endive). In [Accounts v2](https://docs.stripe.com/api/v2/core/accounts.md?api-version=2026-09-30.endive), you can set a custom SEPA Creditor Identifier when you [create](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=2026-09-30.endive) or [update](https://docs.stripe.com/api/v2/core/accounts/update.md?api-version=2026-09-30.endive) a v2 Account using the [configuration.merchant.sepa_debit_payments.creditor_id](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant) parameter.

## Why is this a breaking change?

The `sepa_debit_payments.creditor_id` property on the Account object was previously omitted for accounts using Stripe’s shared SEPA Creditor Identifier. It now returns the shared identifier value. If your code relies on an omitted value to infer that an account uses the shared identifier, you must update your integration to handle the new response.

## Impact

If your integration checks whether `sepa_debit_payments.creditor_id` is null or undefined to determine whether an account uses a shared SEPA Creditor Identifier, update that logic. This property now returns the shared identifier value.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `sepa_debit_payments` | Added | [Account#create.settings](/api/accounts/create?api-version=2026-09-30.endive#create_account-settings), [V2.Core.Account#create.configuration.merchant](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant), [V2.Core.Account#update.configuration.merchant](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sepa_debit_payments` | Added | [AccountCreateParams::Setting](/api/accounts/create?api-version=2026-09-30.endive#create_account-settings), [V2::Core::AccountCreateParams::Configuration::Merchant](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant), [V2::Core::AccountUpdateParams::Configuration::Merchant](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sepa_debit_payments` | Added | [AccountCreateParamsSetting](/api/accounts/create?api-version=2026-09-30.endive#create_account-settings), [v2.core.AccountCreateParamsConfigurationMerchant](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant), [v2.core.AccountModifyParamsConfigurationMerchant](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sepa_debit_payments` | Added | [Account.create().$params.setting](/api/accounts/create?api-version=2026-09-30.endive#create_account-settings), [V2\Core\Account.create().$params.configuration.merchant](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant), [V2\Core\Account.update().$params.configuration.merchant](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sepaDebitPayments` | Added | [AccountCreateParams.settings](/api/accounts/create?api-version=2026-09-30.endive#create_account-settings), [v2.core.AccountCreateParams.configuration.merchant](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant), [v2.core.AccountUpdateParams.configuration.merchant](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sepa_debit_payments` | Added | [AccountCreateParams.settings](/api/accounts/create?api-version=2026-09-30.endive#create_account-settings), [V2.Core.AccountCreateParams.configuration.merchant](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant), [V2.Core.AccountUpdateParams.configuration.merchant](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SEPADebitPayments` | Added | [AccountSettingsParams](/api/accounts/create?api-version=2026-09-30.endive#create_account-settings), [V2CoreAccountConfigurationMerchantParams](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SepaDebitPayments` | Added | [AccountSettingsOptions](/api/accounts/create?api-version=2026-09-30.endive#create_account-settings), [V2CoreAccountConfigurationMerchantOptions](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.endive`
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

- [Adds address validation errors for CMRAs and registered agents to Accounts v1 and Accounts v2](https://docs.stripe.com/changelog/endive/2026-09-30/address-validation-cmra-registered-agents-accounts-v2.md)
- [Adds rejected status for Accounts v2 capabilities](https://docs.stripe.com/changelog/endive/2026-09-30/rejected-accounts-v2-capabilities.md)
- [Replaces the generic fraud rejection reason with specific fraud reasons](https://docs.stripe.com/changelog/endive/2026-09-30/updated-reject-reason-codes.md)
- [Removes the configurations parameter from the Account Links v2 API](https://docs.stripe.com/changelog/endive/2026-09-30/removes-configurations-parameter-from-v2-core-account-links-api.md)
- [Shows errors for eventually due requirements](https://docs.stripe.com/changelog/endive/2026-09-30/shows-errors-for-eventually-due-requirements.md)
- [Distinguishes platform-initiated account rejections from Stripe rejections](https://docs.stripe.com/changelog/endive/2026-09-30/platform-rejection-reasons.md)
- [Adds additional shared fields to customer sharing](https://docs.stripe.com/changelog/endive/2026-09-30/additional-shared-fields-customer-sharing.md)
