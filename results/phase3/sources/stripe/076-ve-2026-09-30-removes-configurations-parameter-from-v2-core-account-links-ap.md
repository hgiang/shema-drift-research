# Removes the configurations parameter from the Account Links v2 API

## What’s new

Removes the [configurations](https://docs.stripe.com/api/v2/core/account-links/create.md?api-version=2026-08-26.dahlia#v2_create_account_links-use_case-account_onboarding-configurations) parameter from the [use_case.account_onboarding](https://docs.stripe.com/api/v2/core/account-links/object.md?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_onboarding) and [use_case.account_update](https://docs.stripe.com/api/v2/core/account-links/object.md?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_update) hashes when you [create a v2 Account Link](https://docs.stripe.com/api/v2/core/account-links/create.md?api-version=2026-09-30.endive). Previously, `configurations` accepted an array of configuration names (such as customer, merchant or recipient) to specify which configurations should be onboarded or updated. Stripe now automatically determines which configurations require onboarding, making this parameter unnecessary.

## Why is this a breaking change?

This change removes the `configurations` parameter from the `account_onboarding` and `account_update` use cases in the Account Links v2 API. If your existing integration includes `configurations` when creating a v2 Account Link, those requests fail on API version `2026-09-30.endive` or later. To avoid errors, remove the `configurations` parameter from your [create Account Link](https://docs.stripe.com/api/v2/core/account-links/create.md?api-version=2026-09-30.endive) requests before upgrading.

## Impact

If your integration passes `configurations` in any `use_case` when creating a v2 Account Link, you must remove that parameter before upgrading to the `2026-09-30.endive` API version. Requests that include `configurations`  now return an error.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `configurations` | Removed | [V2.Core.AccountLink#create.use_case.account_onboarding](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_onboarding), [V2.Core.AccountLink#create.use_case.account_update](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_update), [V2.Core.AccountLink.use_case.account_onboarding](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_onboarding), [V2.Core.AccountLink.use_case.account_update](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_update) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `configurations` | Removed | [V2::Core::AccountLink::UseCase::AccountOnboarding](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_onboarding), [V2::Core::AccountLink::UseCase::AccountUpdate](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_update), [V2::Core::AccountLinkCreateParams::UseCase::AccountOnboarding](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_onboarding), [V2::Core::AccountLinkCreateParams::UseCase::AccountUpdate](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_update) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `configurations` | Removed | [V2.Core.AccountLink.UseCase.AccountOnboarding](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_onboarding), [V2.Core.AccountLink.UseCase.AccountUpdate](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_update), [v2.core.AccountLinkCreateParamsUseCaseAccountOnboarding](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_onboarding), [v2.core.AccountLinkCreateParamsUseCaseAccountUpdate](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_update) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `configurations` | Removed | [V2.Core.AccountLink.use_case.account_onboarding](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_onboarding), [V2.Core.AccountLink.use_case.account_update](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_update), [V2\Core\AccountLink.create().$params.use_case.account_onboarding](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_onboarding), [V2\Core\AccountLink.create().$params.use_case.account_update](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_update) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `configurations` | Removed | [v2.core.AccountLink.use_case.account_onboarding](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_onboarding), [v2.core.AccountLink.use_case.account_update](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_update), [v2.core.AccountLinkCreateParams.use_case.account_onboarding](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_onboarding), [v2.core.AccountLinkCreateParams.use_case.account_update](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_update) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `configurations` | Removed | [V2.Core.AccountLink.use_case.account_onboarding](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_onboarding), [V2.Core.AccountLink.use_case.account_update](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_update), [V2.Core.AccountLinkCreateParams.use_case.account_onboarding](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_onboarding), [V2.Core.AccountLinkCreateParams.use_case.account_update](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_update) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Configurations` | Removed | [V2CoreAccountLinkUseCaseAccountOnboarding](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_onboarding), [V2CoreAccountLinkUseCaseAccountOnboardingParams](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_onboarding), [V2CoreAccountLinkUseCaseAccountUpdate](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_update), [V2CoreAccountLinkUseCaseAccountUpdateParams](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_update) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Configurations` | Removed | [V2.Core.AccountLink.UseCase.AccountOnboarding](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_onboarding), [V2.Core.AccountLink.UseCase.AccountUpdate](/api/v2/core/account-links/object?api-version=2026-09-30.endive#v2_account_link_object-use_case-account_update), [V2CoreAccountLinkUseCaseAccountOnboardingOptions](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_onboarding), [V2CoreAccountLinkUseCaseAccountUpdateOptions](/api/v2/core/account-links/create?api-version=2026-09-30.endive#v2_create_account_links-use_case-account_update) |

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
- [Standardises SEPA Direct Debit payment settings in the Accounts API](https://docs.stripe.com/changelog/endive/2026-09-30/sepa-debit-settings-accounts.md)
- [Shows errors for eventually due requirements](https://docs.stripe.com/changelog/endive/2026-09-30/shows-errors-for-eventually-due-requirements.md)
- [Distinguishes platform-initiated account rejections from Stripe rejections](https://docs.stripe.com/changelog/endive/2026-09-30/platform-rejection-reasons.md)
- [Adds additional shared fields to customer sharing](https://docs.stripe.com/changelog/endive/2026-09-30/additional-shared-fields-customer-sharing.md)
