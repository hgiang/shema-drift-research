# Adds Smart Disputes settings to v2 Accounts

## What’s new

Adds the [smart_disputes](https://docs.stripe.com/api/v2/core/accounts.md?api-version=2026-02-25.preview#v2_account_object-configuration-merchant-smart_disputes) hash to the [configuration.merchant](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-02-25.preview#v2_account_object-configuration-merchant) field on the [v2 Account](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-02-25.preview) object. The `smart_disputes` hash contains an [auto_respond](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-02-25.preview#v2_account_object-configuration-merchant-smart_disputes-auto_respond) configuration that lets platforms control whether connected accounts automatically respond to disputes using [Smart Disputes](https://docs.stripe.com/disputes/smart-disputes.md).

The `auto_respond` configuration includes two fields:

- [preference](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-02-25.preview#v2_account_object-configuration-merchant-smart_disputes-auto_respond-preference): A writable parameter that accepts `on`, `off`, or `inherit` values to control the Smart Disputes setting. When you set `preference` to `inherit`, the connected account uses your platform’s default Smart Disputes configuration.
- [value](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-02-25.preview#v2_account_object-configuration-merchant-smart_disputes-auto_respond-value): A read-only property that shows the effective setting value as either `on` or `off`.

You can update these settings when you [create](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=2026-02-25.preview) or [update](https://docs.stripe.com/api/v2/core/accounts/update.md?api-version=2026-02-25.preview) an account.

## Impact

You can now configure Smart Disputes behaviour for your connected accounts programmatically. Previously, connected accounts could only manage Smart Disputes settings through their Dashboard access.

This change gives you programmatic control over how disputes are handled for individual connected accounts while maintaining the flexibility to let accounts inherit your platform’s default configuration.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `smart_disputes` | Added | [V2.Core.Account#create.configuration.merchant](/api/v2/core/accounts/create?api-version=2026-02-25.preview#v2_create_accounts-configuration-merchant), [V2.Core.Account#update.configuration.merchant](/api/v2/core/accounts/update?api-version=2026-02-25.preview#v2_update_accounts-configuration-merchant), [V2.Core.Account.configuration.merchant](/api/v2/core/accounts/object?api-version=2026-02-25.preview#v2_account_object-configuration-merchant) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `smart_disputes` | Added | [V2::Core::Account::Configuration::Merchant](/api/v2/core/accounts/object?api-version=2026-02-25.preview#v2_account_object-configuration-merchant), [V2::Core::AccountCreateParams::Configuration::Merchant](/api/v2/core/accounts/create?api-version=2026-02-25.preview#v2_create_accounts-configuration-merchant), [V2::Core::AccountUpdateParams::Configuration::Merchant](/api/v2/core/accounts/update?api-version=2026-02-25.preview#v2_update_accounts-configuration-merchant) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `smart_disputes` | Added | [V2.Core.Account.Configuration.Merchant](/api/v2/core/accounts/object?api-version=2026-02-25.preview#v2_account_object-configuration-merchant), [v2.core.AccountCreateParamsConfigurationMerchant](/api/v2/core/accounts/create?api-version=2026-02-25.preview#v2_create_accounts-configuration-merchant), [v2.core.AccountModifyParamsConfigurationMerchant](/api/v2/core/accounts/update?api-version=2026-02-25.preview#v2_update_accounts-configuration-merchant) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `smart_disputes` | Added | [V2.Core.Account.configuration.merchant](/api/v2/core/accounts/object?api-version=2026-02-25.preview#v2_account_object-configuration-merchant), [V2\Core\Account.create().$params.configuration.merchant](/api/v2/core/accounts/create?api-version=2026-02-25.preview#v2_create_accounts-configuration-merchant), [V2\Core\Account.update().$params.configuration.merchant](/api/v2/core/accounts/update?api-version=2026-02-25.preview#v2_update_accounts-configuration-merchant) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `smartDisputes` | Added | [v2.core.Account.configuration.merchant](/api/v2/core/accounts/object?api-version=2026-02-25.preview#v2_account_object-configuration-merchant), [v2.core.AccountCreateParams.configuration.merchant](/api/v2/core/accounts/create?api-version=2026-02-25.preview#v2_create_accounts-configuration-merchant), [v2.core.AccountUpdateParams.configuration.merchant](/api/v2/core/accounts/update?api-version=2026-02-25.preview#v2_update_accounts-configuration-merchant) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `smart_disputes` | Added | [V2.Core.Account.configuration.merchant](/api/v2/core/accounts/object?api-version=2026-02-25.preview#v2_account_object-configuration-merchant), [V2.Core.AccountCreateParams.configuration.merchant](/api/v2/core/accounts/create?api-version=2026-02-25.preview#v2_create_accounts-configuration-merchant), [V2.Core.AccountUpdateParams.configuration.merchant](/api/v2/core/accounts/update?api-version=2026-02-25.preview#v2_update_accounts-configuration-merchant) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SmartDisputes` | Added | [V2CoreAccountConfigurationMerchant](/api/v2/core/accounts/object?api-version=2026-02-25.preview#v2_account_object-configuration-merchant), [V2CoreAccountConfigurationMerchantParams](/api/v2/core/accounts/create?api-version=2026-02-25.preview#v2_create_accounts-configuration-merchant) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SmartDisputes` | Added | [V2.Core.Account.Configuration.Merchant](/api/v2/core/accounts/object?api-version=2026-02-25.preview#v2_account_object-configuration-merchant), [V2CoreAccountConfigurationMerchantOptions](/api/v2/core/accounts/create?api-version=2026-02-25.preview#v2_create_accounts-configuration-merchant) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-02-25.preview`
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
