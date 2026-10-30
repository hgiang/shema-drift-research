# Accounts v2 now always returns the responsibilities field when the defaults field is included

## What’s new

The [defaults.responsibilities](https://docs.stripe.com/api/v2/core/accounts/retrieve.md?api-version=2025-12-15.preview#v2_retrieve_accounts-response-defaults-responsibilities) field is now always returned in the [Accounts v2](https://docs.stripe.com/api/v2/accounts.md?api-version=2025-12-15.preview) object if you specify [defaults](https://docs.stripe.com/api/v2/core/accounts/retrieve.md?api-version=2025-12-15.preview#v2_retrieve_accounts-response-defaults) in the [include](https://docs.stripe.com/api-includable-response-values.md?api-version=2025-12-15.preview) field. This is a breaking change for users on the existing public preview for Accounts v2, which became available in our GA channel as of [2025-12-15.clover](https://docs.stripe.com/changelog.md#2025-12-15.clover).

## Why is this a breaking change?

The `defaults.responsibilities` field is returned even when [responsibilities.fees_collector](https://docs.stripe.com/api/v2/core/accounts/retrieve.md?api-version=2025-12-15.preview#v2_retrieve_accounts-response-defaults-responsibilities-fees_collector) and [responsibilities.losses_collector](https://docs.stripe.com/api/v2/core/accounts/retrieve.md?api-version=2025-12-15.preview#v2_retrieve_accounts-response-defaults-responsibilities-losses_collector) are `null`. If your existing integration doesn’t expect this field in API responses, you must use the new object structure to prevent validation errors.

## Impact

Previously, the [responsibilities.requirements_collector](https://docs.stripe.com/api/v2/core/accounts/retrieve.md?api-version=2025-12-15.preview#v2_retrieve_accounts-response-defaults-responsibilities-requirements_collector) field wasn’t returned unless `fees_collector` and `losses_collector` were present in the response.

You must update your integration to expect the `defaults.responsibilities` field, even if you didn’t set `fees_collector` and `losses_collector` when [creating](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=2025-12-15.preview) or [updating](https://docs.stripe.com/api/v2/core/accounts/update.md?api-version=2025-12-15.preview) the account. Make sure your integration correctly handles `fees_collector` and `losses_collector` when their values are `null`.

## Changes

#### REST API

| Field | Change | From → to |
| --- | --- | --- |
| `V2.Core.Account.defaults.responsibilities` | Changed | `optional → required`, `required → optional`, `required → optional` |

#### Ruby

| Field | Change | From → to |
| --- | --- | --- |
| `V2::Core::Account::Default.responsibilities` | Changed | `optional → required`, `required → optional`, `required → optional` |

#### Python

| Field | Change | From → to |
| --- | --- | --- |
| `V2.Core.Account.Default.responsibilities` | Changed | `optional → required`, `required → optional`, `required → optional` |

#### PHP

| Field | Change | From → to |
| --- | --- | --- |
| `V2.Core.Account.defaults.responsibilities` | Changed | `optional → required`, `required → optional`, `required → optional` |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Field | Change | From → to |
| --- | --- | --- |
| `V2.Core.Account.defaults.responsibilities` | Changed | `optional → required`, `required → optional`, `required → optional` |

#### Go

This change doesn’t affect the Go SDK.

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-12-15.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v18.2.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v18.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v14.2.0b1](https://github.com/stripe/stripe-python/releases/tag/v14.2.0b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v19.2.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v19.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v31.2.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v31.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v20.2.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v20.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v84.2.0-beta.1](https://github.com/stripe/stripe-go/releases/tag/v84.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v50.2.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v50.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Removes requested field from Accounts v2 capabilities hashes](https://docs.stripe.com/changelog/clover/2025-12-15/accounts-v2-capabilities-remove-requested.md)
