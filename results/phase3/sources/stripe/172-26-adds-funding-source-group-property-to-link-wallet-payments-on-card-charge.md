# Adds a funding source identifier to Link wallet card payments

## What’s new

Adds the [funding_source_group](https://docs.stripe.com/api/charges/object.md?api-version=2026-08-26.dahlia#charge_object-payment_method_details) property to `payment_method_details.card.wallet.link` of the Charge object. This property contains an identifier, prefixed with `lfsg_`, for the funding-source group selected for a Link payment. It maps to the applicable pricing configuration in your Stripe pricing contract.

## Impact

You can inspect `payment_method_details.card.wallet.link.funding_source_group` of a Charge to identify the funding-source group associated with a Link payment and reconcile it with the applicable pricing configuration in your Stripe pricing contract.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `funding_source_group` | Added | [Charge.payment_method_details.card.wallet.link](/api/charges/object?api-version=2026-08-26.dahlia#charge_object-payment_method_details-card-wallet-link) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `funding_source_group` | Added | [Charge::PaymentMethodDetail::Card::Wallet::Link](/api/charges/object?api-version=2026-08-26.dahlia#charge_object-payment_method_details-card-wallet-link) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `funding_source_group` | Added | [Charge.PaymentMethodDetail.Card.Wallet.Link](/api/charges/object?api-version=2026-08-26.dahlia#charge_object-payment_method_details-card-wallet-link) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `funding_source_group` | Added | [Charge.payment_method_details.card.wallet.link](/api/charges/object?api-version=2026-08-26.dahlia#charge_object-payment_method_details-card-wallet-link) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `fundingSourceGroup` | Added | [Charge.payment_method_details.card.wallet.link](/api/charges/object?api-version=2026-08-26.dahlia#charge_object-payment_method_details-card-wallet-link) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `funding_source_group` | Added | [Charge.payment_method_details.card.wallet.link](/api/charges/object?api-version=2026-08-26.dahlia#charge_object-payment_method_details-card-wallet-link) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `FundingSourceGroup` | Added | [ChargePaymentMethodDetailsCardWalletLink](/api/charges/object?api-version=2026-08-26.dahlia#charge_object-payment_method_details-card-wallet-link) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `FundingSourceGroup` | Added | [Charge.PaymentMethodDetails.Card.Wallet.Link](/api/charges/object?api-version=2026-08-26.dahlia#charge_object-payment_method_details-card-wallet-link) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-08-26.dahlia`
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

- [Adds support for updating Connect parameters of an existing Payment Link](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-connect-parameters-to-the-payment-link-update-method.md)
- [Adds a funding source identifier to Link payments](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-funding-source-group-property-for-link-payments.md)
- [Adds new error codes for payment method failures](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-payment-method-error-codes.md)
- [Adds the ability to restrict card funding types in Checkout Sessions](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-card-funding-type-filtering-to-checkout-sessions.md)
- [Adds support for metadata in confirmation tokens](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-metadata-support-to-confirmation-tokens.md)
