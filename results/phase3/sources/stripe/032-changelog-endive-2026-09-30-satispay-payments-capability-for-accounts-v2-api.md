# Adds Satispay payments capability to Accounts v2

## What’s new

Adds [satispay_payments](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-09-30.endive#account-configuration) as a new capability under [configuration.merchant.capabilities](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-09-30.endive#account-configuration) on [Accounts v2](https://docs.stripe.com/api/v2/core/accounts.md?api-version=2026-09-30.endive). You can request this capability when you [create](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=2026-09-30.endive) or [update](https://docs.stripe.com/api/v2/core/accounts/update.md?api-version=2026-09-30.endive) a v2 Account by setting `satispay_payments.requested` to `true`. The capability includes a [status](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-09-30.endive#account-configuration) property that reports whether [Satispay](https://docs.stripe.com/payments/satispay.md) payments are active, pending, restricted or unsupported for the account, along with a [status_details](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-09-30.endive#account-configuration) array that provides additional context.

## Impact

If your integration uses [Accounts v2](https://docs.stripe.com/api/v2/core/accounts.md?api-version=2026-09-30.endive) and you want to accept Satispay payments, you can now request the `satispay_payments` capability directly on the v2 Account instead of configuring it separately.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `satispay_payments` | Added | [V2.Core.Account#create.configuration.merchant.capabilities](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities), [V2.Core.Account#update.configuration.merchant.capabilities](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant-capabilities), [V2.Core.Account.configuration.merchant.capabilities](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities) |

| Value | Change | Enums |
| --- | --- | --- |
| `satispay_payments` | Added | [V2.Core.Account.future_requirements.entries[].impact.restricts_capabilities[].capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-future_requirements-entries-impact-restricts_capabilities-capability), [V2.Core.Account.requirements.entries[].impact.restricts_capabilities[].capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-requirements-entries-impact-restricts_capabilities-capability), [EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability](/api/v2/core/accounts/event-types?api-version=2026-09-30.endive#v2_accounts_event_types-v2.core.account[configuration.merchant].capability_status_updated) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `satispay_payments` | Added | [V2::Core::Account::Configuration::Merchant::Capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [V2::Core::AccountCreateParams::Configuration::Merchant::Capability](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities), [V2::Core::AccountUpdateParams::Configuration::Merchant::Capability](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant-capabilities) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `satispay_payments` | Added | [V2.Core.Account.Configuration.Merchant.Capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [v2.core.AccountCreateParamsConfigurationMerchantCapability](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities), [v2.core.AccountModifyParamsConfigurationMerchantCapability](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant-capabilities) |

| Value | Change | Enums |
| --- | --- | --- |
| `satispay_payments` | Added | [V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-future_requirements-entries-impact-restricts_capabilities-capability), [V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-requirements-entries-impact-restricts_capabilities-capability), [EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability](/api/v2/core/accounts/event-types?api-version=2026-09-30.endive#v2_accounts_event_types-v2.core.account[configuration.merchant].capability_status_updated) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `satispay_payments` | Added | [V2.Core.Account.configuration.merchant.capabilities](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [V2\Core\Account.create().$params.configuration.merchant.capability](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities), [V2\Core\Account.update().$params.configuration.merchant.capability](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant-capabilities) |

| Value | Change | Enums |
| --- | --- | --- |
| `satispay_payments` | Added | [V2.Core.Account.future_requirements.entries[].impact.restricts_capabilities[].capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-future_requirements-entries-impact-restricts_capabilities-capability), [V2.Core.Account.requirements.entries[].impact.restricts_capabilities[].capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-requirements-entries-impact-restricts_capabilities-capability), [EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability](/api/v2/core/accounts/event-types?api-version=2026-09-30.endive#v2_accounts_event_types-v2.core.account[configuration.merchant].capability_status_updated) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `satispayPayments` | Added | [v2.core.Account.configuration.merchant.capabilities](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [v2.core.AccountCreateParams.configuration.merchant.capabilities](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities), [v2.core.AccountUpdateParams.configuration.merchant.capabilities](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant-capabilities) |

| Value | Change | Enum |
| --- | --- | --- |
| `satispay_payments` | Added | [EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updatedCapability](/api/v2/core/accounts/event-types?api-version=2026-09-30.endive#v2_accounts_event_types-v2.core.account[configuration.merchant].capability_status_updated) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `satispay_payments` | Added | [V2.Core.Account.configuration.merchant.capabilities](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [V2.Core.AccountCreateParams.configuration.merchant.capabilities](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities), [V2.Core.AccountUpdateParams.configuration.merchant.capabilities](/api/v2/core/accounts/update?api-version=2026-09-30.endive#v2_update_accounts-configuration-merchant-capabilities) |

| Value | Change | Enums |
| --- | --- | --- |
| `satispay_payments` | Added | [V2.Core.Account.future_requirements.entries[].impact.restricts_capabilities[].capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-future_requirements-entries-impact-restricts_capabilities-capability), [V2.Core.Account.requirements.entries[].impact.restricts_capabilities[].capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-requirements-entries-impact-restricts_capabilities-capability), [EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability](/api/v2/core/accounts/event-types?api-version=2026-09-30.endive#v2_accounts_event_types-v2.core.account[configuration.merchant].capability_status_updated) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SatispayPayments` | Added | [V2CoreAccountConfigurationMerchantCapabilities](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [V2CoreAccountConfigurationMerchantCapabilitiesParams](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities) |

| Value | Change | Enums |
| --- | --- | --- |
| `satispay_payments` | Added | [V2CoreAccountFutureRequirementsEntryImpactRestrictsCapability.Capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-future_requirements-entries-impact-restricts_capabilities-Capability), [V2CoreAccountRequirementsEntryImpactRestrictsCapability.Capability](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-requirements-entries-impact-restricts_capabilities-Capability), [EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.UpdatedCapability](/api/v2/core/accounts/event-types?api-version=2026-09-30.endive#v2_accounts_event_types-v2.core.account[configuration.merchant].capability_status_updated) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SatispayPayments` | Added | [V2.Core.Account.Configuration.Merchant.Capabilities](/api/v2/core/accounts/object?api-version=2026-09-30.endive#v2_account_object-configuration-merchant-capabilities), [V2CoreAccountConfigurationMerchantCapabilitiesOptions](/api/v2/core/accounts/create?api-version=2026-09-30.endive#v2_create_accounts-configuration-merchant-capabilities) |

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
