# Adds support for paying out to Financial Accounts v2

## What’s new

You can now create payouts to [Financial Accounts v2](https://docs.stripe.com/api/v2/money-management/financial-accounts.md?api-version=2025-07-30.preview) by passing the [payout_method](https://docs.stripe.com/api/payouts/object.md?api-version=2025-07-30.preview&#payout_object-payout_method) parameter. The value you pass in must be the ID of the financial account.

## Impact

You can use the new [payout_method](https://docs.stripe.com/api/payouts/object.md?api-version=2025-07-30.preview&#payout_object-payout_method) parameter to pay out to [Financial Accounts v2](https://docs.stripe.com/api/v2/money-management/financial-accounts.md?api-version=2025-07-30.preview).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `payout_method` | Added | [Payout](/api/payouts/object?api-version=2025-08-27.basil), [Payout#create](/api/payouts/create?api-version=2025-08-27.basil) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payout_method` | Added | [Payout](/api/payouts/object?api-version=2025-08-27.basil), [Payout::CreateParams](/api/payouts/create?api-version=2025-08-27.basil) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payout_method` | Added | [Payout](/api/payouts/object?api-version=2025-08-27.basil), [Payout.CreateParams](/api/payouts/create?api-version=2025-08-27.basil) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payout_method` | Added | [Payout](/api/payouts/object?api-version=2025-08-27.basil) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payoutMethod` | Added | [Payout](/api/payouts/object?api-version=2025-08-27.basil), [PayoutCreateParams](/api/payouts/create?api-version=2025-08-27.basil) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payout_method` | Added | [Payout](/api/payouts/object?api-version=2025-08-27.basil), [PayoutCreateParams](/api/payouts/create?api-version=2025-08-27.basil) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PayoutMethod` | Added | [Payout](/api/payouts/object?api-version=2025-08-27.basil), [PayoutParams](/api/payouts/create?api-version=2025-08-27.basil) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PayoutMethod` | Added | [Payout](/api/payouts/object?api-version=2025-08-27.basil), [PayoutCreateOptions](/api/payouts/create?api-version=2025-08-27.basil) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-08-27.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.5.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.5.0](https://github.com/stripe/stripe-python/releases/tag/v12.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.6.0](https://github.com/stripe/stripe-php/releases/tag/v17.6.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.5.0](https://github.com/stripe/stripe-java/releases/tag/v29.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.5.0](https://github.com/stripe/stripe-node/releases/tag/v18.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.5.0](https://github.com/stripe/stripe-go/releases/tag/v82.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.5.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds Payout Details embedded component to the Account Session API](https://docs.stripe.com/changelog/basil/2025-08-27/embedded-payout-details.md)
- [Public preview for Payout Details embedded component](https://docs.stripe.com/changelog/basil/2025-08-27/embedded-payout-details-public-preview.md)
