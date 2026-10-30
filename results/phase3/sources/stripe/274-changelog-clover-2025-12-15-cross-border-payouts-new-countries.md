# Global Payouts adds support for 13 new countries for cross-border payouts

## What’s new

Adds 13 additional countries where your recipients can create bank accounts and receive payouts for cross-border payouts using [Global Payouts](https://docs.stripe.com/global-payouts.md) and [Accounts v2](https://docs.stripe.com/api/v2/accounts.md?api-version=2025-12-15.preview). The read-only [default_outbound_destination](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2025-12-15.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) enum on the [Account v2](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2025-12-15.preview#v2_account_object) object can now also be populated with the following destinations:

- `al_bank_account`: Albania
- `dz_bank_account`: Algeria
- `am_bank_account`: Armenia
- `bw_bank_account`: Botswana
- `bn_bank_account`: Brunei
- `gy_bank_account`: Guyana
- `jm_bank_account`: Jamaica
- `jo_bank_account`: Jordan
- `kw_bank_account`: Kuwait
- `ma_bank_account`: Morocco
- `om_bank_account`: Oman
- `lk_bank_account`: Sri Lanka
- `tz_bank_account`: Tanzania

## Impact

Recipients in these 13 countries can now create bank accounts and receive cross-border payouts using Global Payouts. You can use [Outbound Setup Intents](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents.md?api-version=2025-12-15.preview) to create bank accounts, and receive payouts from [Outbound Payments](https://docs.stripe.com/api/v2/money-management/outbound-payments.md?api-version=2025-12-15.preview). These bank accounts can also serve as the default outbound destination on the recipient accounts.

## Changes

#### REST API

| Values | Change | Enum |
| --- | --- | --- |
| `al_bank_account`, `am_bank_account`, `bn_bank_account`, `bw_bank_account`, `dz_bank_account`, `gy_bank_account`, `jm_bank_account`, `jo_bank_account`, `kw_bank_account`, `lk_bank_account`, `ma_bank_account`, `om_bank_account`, `tz_bank_account` | Added | [V2.Core.Account.configuration.recipient.default_outbound_destination](/api/v2/core/accounts/object?api-version=2025-12-15.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enum |
| --- | --- | --- |
| `al_bank_account`, `am_bank_account`, `bn_bank_account`, `bw_bank_account`, `dz_bank_account`, `gy_bank_account`, `jm_bank_account`, `jo_bank_account`, `kw_bank_account`, `lk_bank_account`, `ma_bank_account`, `om_bank_account`, `tz_bank_account` | Added | [V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination](/api/v2/core/accounts/object?api-version=2025-12-15.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |

#### PHP

| Values | Change | Enum |
| --- | --- | --- |
| `al_bank_account`, `am_bank_account`, `bn_bank_account`, `bw_bank_account`, `dz_bank_account`, `gy_bank_account`, `jm_bank_account`, `jo_bank_account`, `kw_bank_account`, `lk_bank_account`, `ma_bank_account`, `om_bank_account`, `tz_bank_account` | Added | [V2.Core.Account.configuration.recipient.default_outbound_destination](/api/v2/core/accounts/object?api-version=2025-12-15.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Values | Change | Enum |
| --- | --- | --- |
| `al_bank_account`, `am_bank_account`, `bn_bank_account`, `bw_bank_account`, `dz_bank_account`, `gy_bank_account`, `jm_bank_account`, `jo_bank_account`, `kw_bank_account`, `lk_bank_account`, `ma_bank_account`, `om_bank_account`, `tz_bank_account` | Added | [V2.Core.Account.configuration.recipient.default_outbound_destination](/api/v2/core/accounts/object?api-version=2025-12-15.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |

#### Go

| Values | Change | Enum |
| --- | --- | --- |
| `al_bank_account`, `am_bank_account`, `bn_bank_account`, `bw_bank_account`, `dz_bank_account`, `gy_bank_account`, `jm_bank_account`, `jo_bank_account`, `kw_bank_account`, `lk_bank_account`, `ma_bank_account`, `om_bank_account`, `tz_bank_account` | Added | [V2CoreAccountConfigurationRecipientDefaultOutboundDestination](/api/v2/core/accounts/object?api-version=2025-12-15.preview#v2_account_object-configuration-recipient-default_outbound_destination-Type) |

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

- [Adds generic error types for Payout Methods](https://docs.stripe.com/changelog/clover/2025-12-15/generic-error-types-payout-methods.md)
- [Creating a Payout Method now triggers an event](https://docs.stripe.com/changelog/clover/2025-12-15/payout-method-created-event.md)
