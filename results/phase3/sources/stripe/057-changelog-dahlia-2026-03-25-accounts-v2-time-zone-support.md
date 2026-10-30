# Adds time zone support to the Accounts v2 API

## What’s new

Adds the ability to specify a v2 Account’s time zone by adding the optional [timezone](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview#v2_account_object-defaults-timezone) property to the `defaults` hash. The `timezone` parameter accepts standard IANA time zone identifiers (such as `America/New_York` or `Europe/London`).

## Impact

You can now configure the preferred time zones for your connected accounts, which is especially useful for platforms that serve businesses across multiple time zones and need to refer to an account’s precise local time for subscriptions or invoices.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `timezone` | Added | [V2.Core.Account#create.defaults](/api/v2/core/accounts/create?api-version=2026-03-25.preview#v2_create_accounts-defaults), [V2.Core.Account#update.defaults](/api/v2/core/accounts/update?api-version=2026-03-25.preview#v2_update_accounts-defaults), [V2.Core.Account.defaults](/api/v2/core/accounts/object?api-version=2026-03-25.preview#v2_account_object-defaults) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `timezone` | Added | [V2::Core::Account::Default](/api/v2/core/accounts/object?api-version=2026-03-25.preview#v2_account_object-defaults), [V2::Core::AccountCreateParams::Default](/api/v2/core/accounts/create?api-version=2026-03-25.preview#v2_create_accounts-defaults), [V2::Core::AccountUpdateParams::Default](/api/v2/core/accounts/update?api-version=2026-03-25.preview#v2_update_accounts-defaults) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `timezone` | Added | [V2.Core.Account.Default](/api/v2/core/accounts/object?api-version=2026-03-25.preview#v2_account_object-defaults), [v2.core.AccountCreateParamsDefault](/api/v2/core/accounts/create?api-version=2026-03-25.preview#v2_create_accounts-defaults), [v2.core.AccountModifyParamsDefault](/api/v2/core/accounts/update?api-version=2026-03-25.preview#v2_update_accounts-defaults) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `timezone` | Added | [V2.Core.Account.defaults](/api/v2/core/accounts/object?api-version=2026-03-25.preview#v2_account_object-defaults), [V2\Core\Account.create().$params.default](/api/v2/core/accounts/create?api-version=2026-03-25.preview#v2_create_accounts-defaults), [V2\Core\Account.update().$params.default](/api/v2/core/accounts/update?api-version=2026-03-25.preview#v2_update_accounts-defaults) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `timezone` | Added | [v2.core.Account.defaults](/api/v2/core/accounts/object?api-version=2026-03-25.preview#v2_account_object-defaults), [v2.core.AccountCreateParams.defaults](/api/v2/core/accounts/create?api-version=2026-03-25.preview#v2_create_accounts-defaults), [v2.core.AccountUpdateParams.defaults](/api/v2/core/accounts/update?api-version=2026-03-25.preview#v2_update_accounts-defaults) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `timezone` | Added | [V2.Core.Account.defaults](/api/v2/core/accounts/object?api-version=2026-03-25.preview#v2_account_object-defaults), [V2.Core.AccountCreateParams.defaults](/api/v2/core/accounts/create?api-version=2026-03-25.preview#v2_create_accounts-defaults), [V2.Core.AccountUpdateParams.defaults](/api/v2/core/accounts/update?api-version=2026-03-25.preview#v2_update_accounts-defaults) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Timezone` | Added | [V2CoreAccountDefaults](/api/v2/core/accounts/object?api-version=2026-03-25.preview#v2_account_object-defaults), [V2CoreAccountDefaultsParams](/api/v2/core/accounts/create?api-version=2026-03-25.preview#v2_create_accounts-defaults) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Timezone` | Added | [V2.Core.Account.Defaults](/api/v2/core/accounts/object?api-version=2026-03-25.preview#v2_account_object-defaults), [V2CoreAccountDefaultsOptions](/api/v2/core/accounts/create?api-version=2026-03-25.preview#v2_create_accounts-defaults) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-03-25.preview`
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
