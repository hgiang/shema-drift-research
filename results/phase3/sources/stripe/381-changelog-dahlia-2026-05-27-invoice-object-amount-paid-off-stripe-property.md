# Adds amount paid off Stripe property to Invoice object

## What’s new

Adds the [amount_paid_off_stripe](https://docs.stripe.com/api/invoices/object.md?api-version=2026-05-27.dahlia#invoice_object-amount_paid_off_stripe) property to the [Invoice](https://docs.stripe.com/api/invoices/object.md?api-version=2026-05-27.dahlia) object. This integer property represents the total amount, in the invoice’s currency, that was paid on the invoice outside of Stripe (out of band). The property supports both full and partial out-of-band payments and is dynamically computed from [Payment Record](https://docs.stripe.com/api/payment-record.md?api-version=2026-05-27.dahlia) data where the payment processor isn’t Stripe.

You can include this property in API requests (for example, retrieving an invoice). The property isn’t available in event payloads or Sigma.

```curl
curl -G https://api.stripe.com/v1/invoices/{{INVOICE_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "expand[]=amount_paid_off_stripe"
```

## Impact

You can now track payments made outside of Stripe directly on the Invoice object, making it easier to perform accounting reconciliation for off-Stripe payments. This replaces the need to rely on the deprecated `paid_out_of_band` boolean property, which only indicated whether any out-of-band payment occurred but didn’t specify the amount.

If you previously used the `paid_out_of_band` property for reconciliation purposes, you can now use `amount_paid_off_stripe` to get more precise information about the actual amounts paid outside of Stripe.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `amount_paid_off_stripe` | Added | [Invoice](/api/invoices/object?api-version=2026-05-27.dahlia#invoice_object) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `amount_paid_off_stripe` | Added | [Invoice](/api/invoices/object?api-version=2026-05-27.dahlia#invoice_object) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `amount_paid_off_stripe` | Added | [Invoice](/api/invoices/object?api-version=2026-05-27.dahlia#invoice_object) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `amount_paid_off_stripe` | Added | [Invoice](/api/invoices/object?api-version=2026-05-27.dahlia#invoice_object) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `amountPaidOffStripe` | Added | [Invoice](/api/invoices/object?api-version=2026-05-27.dahlia#invoice_object) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `amount_paid_off_stripe` | Added | [Invoice](/api/invoices/object?api-version=2026-05-27.dahlia#invoice_object) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AmountPaidOffStripe` | Added | [Invoice](/api/invoices/object?api-version=2026-05-27.dahlia#invoice_object) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AmountPaidOffStripe` | Added | [Invoice](/api/invoices/object?api-version=2026-05-27.dahlia#invoice_object) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-05-27.dahlia`
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

- [Adds discount eligibility options for add-on invoice items on Subscriptions and Preview Invoice APIs](https://docs.stripe.com/changelog/dahlia/2026-05-27/invoice-items-discount-eligibility.md)
- [Adds billing schedules to enable prebilling on subscriptions](https://docs.stripe.com/changelog/dahlia/2026-05-27/subscriptions-billing-schedules.md)
- [Adds discount and discounts properties to pending subscription updates](https://docs.stripe.com/changelog/dahlia/2026-05-27/pending-subscription-updates-discount-and-discounts-properties.md)
- [Adds metadata support to pending subscription updates](https://docs.stripe.com/changelog/dahlia/2026-05-27/pending-subscription-update-metadata.md)
- [Adds credited items information to invoice item proration details](https://docs.stripe.com/changelog/dahlia/2026-05-27/invoice-item-proration-credited-items.md)
- [Adds customer parameter to test clock creation](https://docs.stripe.com/changelog/dahlia/2026-05-27/test-clock-creation-customer-parameter.md)
