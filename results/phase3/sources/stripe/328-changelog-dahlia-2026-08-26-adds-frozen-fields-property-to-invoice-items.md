# Adds frozen fields property to Invoice Items

## What’s new

Adds the [frozen_fields](https://docs.stripe.com/api/invoiceitems/object.md?api-version=2026-08-26.dahlia#invoiceitem_object-frozen_fields) property to the [Invoice Item](https://docs.stripe.com/api/invoiceitems/object.md?api-version=2026-08-26.dahlia) object. This read-only array indicates which properties a user can’t modify when updating an [invoice item](https://docs.stripe.com/api/invoiceitems/update.md?api-version=2026-08-26.dahlia), [invoice line item](https://docs.stripe.com/api/invoice-line-item/update.md?api-version=2026-08-26.dahlia) or [bulk line items](https://docs.stripe.com/api/invoice-line-item/invoices/update-lines/bulk.md?api-version=2026-08-26.dahlia). Possible values might include `discounts`, `pricing` and `quantity`. Attempting to update a frozen property returns an error.

## Impact

If your integration updates invoice items programmatically, check the `frozen_fields` property before making update requests. Modifying a property listed in `frozen_fields` returns a 400 error. Only invoice items with derived values (for example, prorations) have properties in `frozen_fields`.

To make changes to a property listed in the `frozen_fields` array, you must [delete the invoice item](https://docs.stripe.com/api/invoiceitems/delete.md?api-version=2026-08-26.dahlia) from the [Invoice](https://docs.stripe.com/api/invoices.md?api-version=2026-08-26.dahlia) and then [recreate the invoice item](https://docs.stripe.com/api/invoiceitems/create.md?api-version=2026-08-26.dahlia) that includes the updated values.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `frozen_fields` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-08-26.dahlia#invoiceitem_object) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `frozen_fields` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-08-26.dahlia#invoiceitem_object) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `frozen_fields` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-08-26.dahlia#invoiceitem_object) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `frozen_fields` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-08-26.dahlia#invoiceitem_object) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `frozenFields` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-08-26.dahlia#invoiceitem_object) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `frozen_fields` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-08-26.dahlia#invoiceitem_object) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `FrozenFields` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-08-26.dahlia#invoiceitem_object) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `FrozenFields` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-08-26.dahlia#invoiceitem_object) |

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

- [Adds a customer update deep link for billing portal sessions](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-a-customer-update-deep-link-for-billing-portal-sessions.md)
- [Adds the ability to query entitlements and launch the customer portal in Customer Sessions](https://docs.stripe.com/changelog/dahlia/2026-08-26/customer-session-improvements.md)
- [Adds support for the Billie payment method for invoices and subscriptions](https://docs.stripe.com/changelog/dahlia/2026-08-26/billie-support-for-invoices-and-subscriptions.md)
- [Increases the subscription item limit](https://docs.stripe.com/changelog/dahlia/2026-08-26/flexible-subscription-item-limits.md)
