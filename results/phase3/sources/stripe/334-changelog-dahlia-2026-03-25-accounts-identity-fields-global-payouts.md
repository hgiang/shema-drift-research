# Restricts Accounts v2 identity properties for some Global Payouts use cases

## What’s new

Removes access for [Global Payouts](https://docs.stripe.com/global-payouts.md) users to certain [identity](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview#v2_account_object-identity) properties on [Accounts](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview) that have no configurations or where [defaults.responsibilities.requirements_collector](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview#v2_account_object-defaults-responsibilities-requirements_collector) is `stripe`.

## Why is this a breaking change?

Certain properties in an Account’s [identity](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview#v2_account_object-identity) hash are no longer accessible to Global Payouts users when those properties aren’t relevant. Attempting to read or write those properties will fail.

## Impact

Access to properties of the Account object’s [identity](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview#v2_account_object-identity) hash is now limited for Global Payouts users the same way as it is for other integrations. If your Global Payouts integration reads or writes any [identity](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview#v2_account_object-identity) properties, you might need to update your code to stop attempting to access properties that are no longer available. Review the following changes:

- You can no longer set [identity.attestations.terms_of_service](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview#v2_account_object-identity-attestations-terms_of_service) on an Account that only requests Global Payouts capabilities. Those Accounts don’t sign the Stripe Terms of Service, so that attestation property doesn’t apply.
- On an [Account](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview) with no requested capabilities, you can no longer access certain [identity](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview#v2_account_object-identity) properties.
- On an [Account](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview) where [defaults.responsibilities.requirements_collector](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview#v2_account_object-defaults-responsibilities-requirements_collector) is `stripe`, you can no longer access certain [identity](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview#v2_account_object-identity) properties.

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

## Related changes

- [Adds multicurrency support for v2 payout methods](https://docs.stripe.com/changelog/dahlia/2026-03-25/multicurrency-v2-payout-methods.md)
- [Adds the restricted property to the Payout Method object](https://docs.stripe.com/changelog/dahlia/2026-03-25/payout-method-restricted-property.md)
- [Expands Global Payouts cross-border payout destinations to three additional countries](https://docs.stripe.com/changelog/dahlia/2026-03-25/cross-border-payouts-new-countries.md)
