# Shows errors for eventually due requirements

## What’s new

In the [Accounts](https://docs.stripe.com/api/accounts.md?api-version=2026-09-30.endive), [Persons](https://docs.stripe.com/api/persons.md?api-version=2026-09-30.endive) and [Capabilities](https://docs.stripe.com/api/capabilities.md?api-version=2026-09-30.endive) APIs, validation and verification errors can now appear in the [requirements.errors](https://docs.stripe.com/api/accounts/object.md?api-version=2026-09-30.endive#account_object-requirements-errors) and [future_requirements.errors](https://docs.stripe.com/api/accounts/object.md?api-version=2026-09-30.endive#account_object-future_requirements-errors) arrays for [eventually_due](https://docs.stripe.com/api/accounts/object.md?api-version=2026-09-30.endive#account_object-future_requirements-eventually_due) requirements.

## Why is this a breaking change?

Previously, `requirements.errors` and `future_requirements.errors` only included errors for requirements that were currently due or overdue. If your integration assumes that `eventually_due` requirements don’t have corresponding errors, update your code to handle errors for those requirements.

## Impact

If your integration reads `requirements.errors` or `future_requirements.errors` from Accounts, Persons, Capabilities or related events, handle errors whose `requirement` value is also listed in `eventually_due`.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `requirements.errors`, `future_requirements.errors` | Changed | `Account.requirements.errors[]`, `Account.future_requirements.errors[]`, `Capability.requirements.errors[]`, `Capability.future_requirements.errors[]`, `Person.requirements.errors[]`, `Person.future_requirements.errors[]` |

|  | Change | Event type |
| --- | --- | --- |
| `account.updated`, `capability.updated`, `person.updated` | Changed | `Event` |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

This change doesn’t affect the Python SDK.

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

This change doesn’t affect the Node.js SDK.

#### Go

This change doesn’t affect the Go SDK.

#### .NET

This change doesn’t affect the .NET SDK.

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
- [Standardises SEPA Direct Debit payment settings in the Accounts API](https://docs.stripe.com/changelog/endive/2026-09-30/sepa-debit-settings-accounts.md)
- [Distinguishes platform-initiated account rejections from Stripe rejections](https://docs.stripe.com/changelog/endive/2026-09-30/platform-rejection-reasons.md)
- [Adds additional shared fields to customer sharing](https://docs.stripe.com/changelog/endive/2026-09-30/additional-shared-fields-customer-sharing.md)
