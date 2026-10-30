# Adds the capability to hold EUR funds to Accounts v2

## What’s new

[Accounts v2](https://docs.stripe.com/api/v2/core/accounts.md?api-version=2025-11-17.preview) can now add a [Storer Configuration](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=2025-11-17.preview#v2_create_accounts-configuration-storer) to hold EUR funds in a [Financial Account](https://docs.stripe.com/api/v2/money-management/financial-accounts.md?api-version=2025-11-17.preview). This capability is  specified in the field [storer.capabilities.holds_currencies.eur](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=2025-11-17.preview#v2_create_accounts-configuration-storer-capabilities-holds_currencies-eur).

## Impact

You can [request this capability](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=2025-11-17.preview#v2_create_accounts-configuration-storer-capabilities-holds_currencies-eur-requested) in supported regions. This expands the multi-currency capabilities available in Financial Accounts.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `eur` | Added | [V2.Core.Account#create.configuration.storer.capabilities.holds_currencies](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-storer-capabilities-holds_currencies), [V2.Core.Account#update.configuration.storer.capabilities.holds_currencies](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-configuration-storer-capabilities-holds_currencies), [V2.Core.Account.configuration.storer.capabilities.holds_currencies](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-storer-capabilities-holds_currencies) |

| Value | Change | Enum |
| --- | --- | --- |
| `holds_currencies.eur` | Added | [V2.Core.Account.requirements.entries[].impact.restricts_capabilities[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-requirements-entries-impact-restricts_capabilities-capability) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `eur` | Added | [V2::Core::Account::Configuration::Storer::Capability::HoldsCurrency](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-storer-capabilities-holds_currencies), [V2::Core::AccountCreateParams::Configuration::Storer::Capability::HoldsCurrency](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-storer-capabilities-holds_currencies), [V2::Core::AccountUpdateParams::Configuration::Storer::Capability::HoldsCurrency](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-configuration-storer-capabilities-holds_currencies) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `eur` | Added | [V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-storer-capabilities-holds_currencies), [v2.core.AccountCreateParamsConfigurationStorerCapabilityHoldsCurrency](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-storer-capabilities-holds_currencies), [v2.core.AccountModifyParamsConfigurationStorerCapabilityHoldsCurrency](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-configuration-storer-capabilities-holds_currencies) |

| Value | Change | Enum |
| --- | --- | --- |
| `holds_currencies.eur` | Added | [V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-requirements-entries-impact-restricts_capabilities-capability) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `eur` | Added | [V2.Core.Account.configuration.storer.capabilities.holds_currencies](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-storer-capabilities-holds_currencies), [V2\Core\Account.create().$params.configuration.storer.capability.holds_currency](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-storer-capabilities-holds_currencies), [V2\Core\Account.update().$params.configuration.storer.capability.holds_currency](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-configuration-storer-capabilities-holds_currencies) |

| Value | Change | Enum |
| --- | --- | --- |
| `holds_currencies.eur` | Added | [V2.Core.Account.requirements.entries[].impact.restricts_capabilities[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-requirements-entries-impact-restricts_capabilities-capability) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `eur` | Added | [v2.core.Account.configuration.storer.capabilities.holds_currencies](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-storer-capabilities-holds_currencies), [v2.core.AccountCreateParams.configuration.storer.capabilities.holds_currencies](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-storer-capabilities-holds_currencies), [v2.core.AccountUpdateParams.configuration.storer.capabilities.holds_currencies](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-configuration-storer-capabilities-holds_currencies) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `eur` | Added | [V2.Core.Account.configuration.storer.capabilities.holds_currencies](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-storer-capabilities-holds_currencies), [V2.Core.AccountCreateParams.configuration.storer.capabilities.holds_currencies](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-storer-capabilities-holds_currencies), [V2.Core.AccountUpdateParams.configuration.storer.capabilities.holds_currencies](/api/v2/core/accounts/update?api-version=2025-11-17.preview#v2_update_accounts-configuration-storer-capabilities-holds_currencies) |

| Value | Change | Enum |
| --- | --- | --- |
| `holds_currencies.eur` | Added | [V2.Core.Account.requirements.entries[].impact.restricts_capabilities[]](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-requirements-entries-impact-restricts_capabilities-capability) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `EUR` | Added | [V2CoreAccountConfigurationStorerCapabilitiesHoldsCurrencies](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-storer-capabilities-holds_currencies), [V2CoreAccountConfigurationStorerCapabilitiesHoldsCurrenciesParams](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-storer-capabilities-holds_currencies) |

| Value | Change | Enum |
| --- | --- | --- |
| `holds_currencies.eur` | Added | [V2CoreAccountRequirementsEntryImpactRestrictsCapability](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-requirements-entries-impact-restricts_capabilities-Capability) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Eur` | Added | [V2.Core.Account.Configuration.Storer.Capabilities.HoldsCurrencies](/api/v2/core/accounts/object?api-version=2025-11-17.preview#v2_account_object-configuration-storer-capabilities-holds_currencies), [V2CoreAccountConfigurationStorerCapabilitiesHoldsCurrenciesOptions](/api/v2/core/accounts/create?api-version=2025-11-17.preview#v2_create_accounts-configuration-storer-capabilities-holds_currencies) |

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
- [Adds account and person tokens to Accounts v2 to securely transmit sensitive data](https://docs.stripe.com/changelog/clover/2025-11-17/accounts-v2-tokens.md)
