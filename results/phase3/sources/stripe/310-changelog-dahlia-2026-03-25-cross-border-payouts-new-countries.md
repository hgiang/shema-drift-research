# Expands Global Payouts cross-border payout destinations to three additional countries

## What’s new

Adds support for [Global Payouts](https://docs.stripe.com/global-payouts.md) recipient bank accounts in Argentina, Colombia and Egypt. It also adds the following values for those countries to the read-only [default_outbound_destination](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) enum on the v2 [Account](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-03-25.preview) object’s `recipient` configuration:

- `ar_bank_account`: Argentina
- `co_bank_account`: Colombia
- `eg_bank_account`: Egypt

## Impact

Your recipients in these three countries can now create bank accounts and receive cross-border payouts using Global Payouts. You can use [OutboundSetupIntents](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents.md?api-version=2026-03-25.preview) to create the bank accounts and [OutboundPayments](https://docs.stripe.com/api/v2/money-management/outbound-payments.md?api-version=2026-03-25.preview) to send the payouts. These bank accounts can also serve as the default outbound destination on the recipient accounts.

## Changes

#### REST API

| Values | Change | Enum |
| --- | --- | --- |
| `ar_bank_account`, `co_bank_account`, `eg_bank_account` | Added | [V2.Core.Account.configuration.recipient.default_outbound_destination](/api/v2/core/accounts/object?api-version=2026-03-25.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enum |
| --- | --- | --- |
| `ar_bank_account`, `co_bank_account`, `eg_bank_account` | Added | [V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination](/api/v2/core/accounts/object?api-version=2026-03-25.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |

#### PHP

| Values | Change | Enum |
| --- | --- | --- |
| `ar_bank_account`, `co_bank_account`, `eg_bank_account` | Added | [V2.Core.Account.configuration.recipient.default_outbound_destination](/api/v2/core/accounts/object?api-version=2026-03-25.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Values | Change | Enum |
| --- | --- | --- |
| `ar_bank_account`, `co_bank_account`, `eg_bank_account` | Added | [V2.Core.Account.configuration.recipient.default_outbound_destination](/api/v2/core/accounts/object?api-version=2026-03-25.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |

#### Go

| Values | Change | Enum |
| --- | --- | --- |
| `ar_bank_account`, `co_bank_account`, `eg_bank_account` | Added | [V2CoreAccountConfigurationRecipientDefaultOutboundDestination](/api/v2/core/accounts/object?api-version=2026-03-25.preview#v2_account_object-configuration-recipient-default_outbound_destination-Type) |

#### .NET

This change doesn’t affect the .NET SDK.

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
- [Restricts Accounts v2 identity properties for some Global Payouts use cases](https://docs.stripe.com/changelog/dahlia/2026-03-25/accounts-identity-fields-global-payouts.md)
- [Adds the restricted property to the Payout Method object](https://docs.stripe.com/changelog/dahlia/2026-03-25/payout-method-restricted-property.md)
