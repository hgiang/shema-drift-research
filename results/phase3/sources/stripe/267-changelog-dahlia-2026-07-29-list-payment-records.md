# Adds the ability to list Payment Records

## What’s new

Adds a [list](https://docs.stripe.com/api/payment-record/list.md?api-version=2026-07-29.dahlia) endpoint for [Payment Records](https://docs.stripe.com/api/payment-record.md?api-version=2026-07-29.dahlia). You can retrieve all Payment Records for your account using `GET /v1/payment_records`, with results returned in reverse chronological order. You can paginate results with `starting_after` and `ending_before` and filter by creation time range (`created_after` and `created_before`) and processor type (`processor_details_type`).

## Impact

If you use [Payment Records](https://docs.stripe.com/payments/payment-records.md) to track payments processed through external processors, you can now query them directly without expanding from a [PaymentIntent](https://docs.stripe.com/payments/payment-intents.md). This gives you a single flow to load both on-Stripe and off-Stripe payments for reporting or orchestration.

## Changes

#### REST API

| Endpoint | Change | Resource |
| --- | --- | --- |
| `list` | Added | [PaymentRecord](/api/payment-record/object?api-version=2026-07-29.dahlia) |

#### Ruby

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [PaymentRecord](/api/payment-record/object?api-version=2026-07-29.dahlia) |

#### Python

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [PaymentRecord](/api/payment-record/object?api-version=2026-07-29.dahlia) |

#### PHP

| Method | Change | Resource |
| --- | --- | --- |
| `all` | Added | [PaymentRecord](/api/payment-record/object?api-version=2026-07-29.dahlia) |

#### Java

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [PaymentRecord](/api/payment-record/object?api-version=2026-07-29.dahlia) |

#### Node.js

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [PaymentRecord](/api/payment-record/object?api-version=2026-07-29.dahlia) |

#### Go

| Method | Change | Resource |
| --- | --- | --- |
| `List` | Added | [PaymentRecord](/api/payment-record/object?api-version=2026-07-29.dahlia) |

#### .NET

| Method | Change | Resource |
| --- | --- | --- |
| `List` | Added | [PaymentRecord](/api/payment-record/object?api-version=2026-07-29.dahlia) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-07-29.dahlia`
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

- [Adds the ability to update shipping options, consent collection, and future usage support on Payment Links](https://docs.stripe.com/changelog/dahlia/2026-07-29/payment-links-update-endpoint-new-parameters.md)
- [Adds the ability to indicate that you don’t intend to reuse Samsung Pay and PAYCO payment method types](https://docs.stripe.com/changelog/dahlia/2026-07-29/samsung-pay-and-payco-setup-future-usage-none-only.md)
- [Adds customer and payment method details to the Refunds API](https://docs.stripe.com/changelog/dahlia/2026-07-29/adds-customer-and-payment-method-details-to-the-refunds-api.md)
- [Adds support for new banks to FPX payments](https://docs.stripe.com/changelog/dahlia/2026-07-29/fpx-payments-new-banks.md)
- [Adds CHAPS as a supported network for funding instructions](https://docs.stripe.com/changelog/dahlia/2026-07-29/chaps-as-supported-networks.md)
- [Adds the allowed payment method types parameter to Payment Intents and Setup Intents](https://docs.stripe.com/changelog/dahlia/2026-07-29/allowed-payment-method-types-parameter.md)
- [Adds MB WAY support to the hosted invoice page](https://docs.stripe.com/changelog/dahlia/2026-07-29/hosted-invoice-page-mb-way-support.md)
- [Adds card network details to the Dispute object](https://docs.stripe.com/changelog/dahlia/2026-07-29/dispute-payment-method-details-card-network.md)
