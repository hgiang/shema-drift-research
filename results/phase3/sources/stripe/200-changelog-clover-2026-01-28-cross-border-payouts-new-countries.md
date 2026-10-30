# Global Payouts adds support for 15 new countries for cross-border payouts

## What’s new

There are now 15 additional countries where your recipients can create bank accounts and receive payouts for cross-border payouts using [Global Payouts](https://docs.stripe.com/global-payouts.md) and [Accounts v2](https://docs.stripe.com/api/v2/accounts.md?api-version=2026-01-28.preview). The read-only [default_outbound_destination](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-01-28.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) enum on the [Account v2](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-01-28.preview) object can now also be populated with the following destinations:

- `ae_bank_account`: United Arab Emirates
- `ag_bank_account`: Antigua and Barbuda
- `bh_bank_account`: Bahrain
- `gm_bank_account`: Gambia
- `hk_bank_account`: Hong Kong
- `kh_bank_account`: Cambodia
- `lc_bank_account`: Saint Lucia
- `mc_bank_account`: Monaco
- `mg_bank_account`: Madagascar
- `my_bank_account`: Malaysia
- `qa_bank_account`: Qatar
- `rw_bank_account`: Rwanda
- `th_bank_account`: Thailand
- `tt_bank_account`: Trinidad and Tobago
- `vn_bank_account`: Vietnam

## Impact

Recipients in these 15 countries can now create bank accounts and receive cross-border payouts using Global Payouts. You can use [Outbound Setup Intents](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents.md?api-version=2026-01-28.preview) to create bank accounts and receive payouts from [Outbound Payments](https://docs.stripe.com/api/v2/money-management/outbound-payments.md?api-version=2026-01-28.preview). These bank accounts can also serve as the default outbound destination on the recipient accounts.

## Changes

#### REST API

| Values | Change | Enum |
| --- | --- | --- |
| `ae_bank_account`, `ag_bank_account`, `bh_bank_account`, `gm_bank_account`, `hk_bank_account`, `kh_bank_account`, `lc_bank_account`, `mc_bank_account`, `mg_bank_account`, `my_bank_account`, `qa_bank_account`, `rw_bank_account`, `th_bank_account`, `tt_bank_account`, `vn_bank_account` | Added | [V2.Core.Account.configuration.recipient.default_outbound_destination](/api/v2/core/accounts/object?api-version=2026-01-28.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enum |
| --- | --- | --- |
| `ae_bank_account`, `ag_bank_account`, `bh_bank_account`, `gm_bank_account`, `hk_bank_account`, `kh_bank_account`, `lc_bank_account`, `mc_bank_account`, `mg_bank_account`, `my_bank_account`, `qa_bank_account`, `rw_bank_account`, `th_bank_account`, `tt_bank_account`, `vn_bank_account` | Added | [V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination](/api/v2/core/accounts/object?api-version=2026-01-28.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |

#### PHP

| Values | Change | Enum |
| --- | --- | --- |
| `ae_bank_account`, `ag_bank_account`, `bh_bank_account`, `gm_bank_account`, `hk_bank_account`, `kh_bank_account`, `lc_bank_account`, `mc_bank_account`, `mg_bank_account`, `my_bank_account`, `qa_bank_account`, `rw_bank_account`, `th_bank_account`, `tt_bank_account`, `vn_bank_account` | Added | [V2.Core.Account.configuration.recipient.default_outbound_destination](/api/v2/core/accounts/object?api-version=2026-01-28.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Values | Change | Enum |
| --- | --- | --- |
| `ae_bank_account`, `ag_bank_account`, `bh_bank_account`, `gm_bank_account`, `hk_bank_account`, `kh_bank_account`, `lc_bank_account`, `mc_bank_account`, `mg_bank_account`, `my_bank_account`, `qa_bank_account`, `rw_bank_account`, `th_bank_account`, `tt_bank_account`, `vn_bank_account` | Added | [V2.Core.Account.configuration.recipient.default_outbound_destination](/api/v2/core/accounts/object?api-version=2026-01-28.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |

#### Go

| Values | Change | Enum |
| --- | --- | --- |
| `ae_bank_account`, `ag_bank_account`, `bh_bank_account`, `gm_bank_account`, `hk_bank_account`, `kh_bank_account`, `lc_bank_account`, `mc_bank_account`, `mg_bank_account`, `my_bank_account`, `qa_bank_account`, `rw_bank_account`, `th_bank_account`, `tt_bank_account`, `vn_bank_account` | Added | [V2CoreAccountConfigurationRecipientDefaultOutboundDestination](/api/v2/core/accounts/object?api-version=2026-01-28.preview#v2_account_object-configuration-recipient-default_outbound_destination-Type) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-01-28.preview`
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

- [Updates error codes for the Outbound Setup Intents API](https://docs.stripe.com/changelog/clover/2026-01-28/outbound-setup-intents-error-codes.md)
- [Adds alternative reference field to bank account and payout method resources](https://docs.stripe.com/changelog/clover/2026-01-28/alternative-reference-field.md)
- [Adds fingerprint property to card payout methods](https://docs.stripe.com/changelog/clover/2026-01-28/card-payout-methods-fingerprint-property.md)
