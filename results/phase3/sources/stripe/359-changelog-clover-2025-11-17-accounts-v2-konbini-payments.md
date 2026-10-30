# Adds support for Konbini payments and Japanese statement descriptors in Accounts v2

## What’s new

Adds the ability to request the [konbini_payments](https://docs.stripe.com/api/accounts/update.md?api-version=2025-11-17.clover#update_account-capabilities-konbini_payments) capability and fulfil its requirements using [Accounts v2](https://docs.stripe.com/api/v2/core/accounts.md?api-version=2025-11-17.preview). To support the `konbini_payments` capability, we added new fields to the [merchant configuration](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2025-11-17.preview#v2_account_object-configuration-merchant):

- [konbini_payments](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2025-11-17.preview#v2_account_object-configuration-merchant-konbini_payments): Contains support fields specific to the Konbini payments capability, including email, phone and support availability hours.
- [script_statement_descriptor](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2025-11-17.preview#v2_account_object-configuration-merchant-script_statement_descriptor): Allows you to set statement descriptors in kana and kanji characters for Japanese payment statements.

For more information about Konbini payments, see the [Konbini payments documentation](https://docs.stripe.com/payments/konbini.md).

## Impact

You can now enable Konbini payments for connected accounts in Japan by requesting the `konbini_payments` capability for Accounts v2 and providing the new required fields. This enables connected accounts to offer Konbini as a payment method to their customers.

Additionally, you can provide localised statement descriptors in kana and kanji characters, which display correctly on Japanese customer payment statements and improve clarity on payment statements in Japan.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `konbini_payments`, `script_statement_descriptor` | Added | [V2.Core.Account#create.configuration.merchant](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-merchant), [V2.Core.Account#update.configuration.merchant](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-configuration-merchant), [V2.Core.Account.configuration.merchant](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-merchant) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `konbini_payments`, `script_statement_descriptor` | Added | [V2::Core::Account::Configuration::Merchant](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-merchant), [V2::Core::AccountCreateParams::Configuration::Merchant](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-merchant), [V2::Core::AccountUpdateParams::Configuration::Merchant](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-configuration-merchant) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `konbini_payments`, `script_statement_descriptor` | Added | [V2.Core.Account.Configuration.Merchant](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-merchant), [v2.core.AccountCreateParamsConfigurationMerchant](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-merchant), [v2.core.AccountModifyParamsConfigurationMerchant](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-configuration-merchant) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `konbini_payments`, `script_statement_descriptor` | Added | [V2.Core.Account.configuration.merchant](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-merchant), [V2\Core\Account.create().$params.configuration.merchant](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-merchant), [V2\Core\Account.update().$params.configuration.merchant](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-configuration-merchant) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `konbiniPayments`, `scriptStatementDescriptor` | Added | [v2.core.Account.configuration.merchant](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-merchant), [v2.core.AccountCreateParams.configuration.merchant](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-merchant), [v2.core.AccountUpdateParams.configuration.merchant](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-configuration-merchant) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `konbini_payments`, `script_statement_descriptor` | Added | [V2.Core.Account.configuration.merchant](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-merchant), [V2.Core.AccountCreateParams.configuration.merchant](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-merchant), [V2.Core.AccountUpdateParams.configuration.merchant](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-configuration-merchant) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `KonbiniPayments`, `ScriptStatementDescriptor` | Added | [V2CoreAccountConfigurationMerchant](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-merchant), [V2CoreAccountConfigurationMerchantParams](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-merchant) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `KonbiniPayments`, `ScriptStatementDescriptor` | Added | [V2.Core.Account.Configuration.Merchant](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-merchant), [V2CoreAccountConfigurationMerchantOptions](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-merchant) |

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
- [Adds the capability to hold EUR funds to Accounts v2](https://docs.stripe.com/changelog/clover/2025-11-17/account-v2-storer-config-eur.md)
- [Adds account and person tokens to Accounts v2 to securely transmit sensitive data](https://docs.stripe.com/changelog/clover/2025-11-17/accounts-v2-tokens.md)
