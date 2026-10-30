# Renames a purchase_details attribute of the Transaction object 

## What’s new

Renames `purchase_details.fuel.volume_decimal` to `purchase_details.fuel.quantity_decimal` on the [Issuing Transaction](https://docs.stripe.com/api/issuing/transactions/object.md?api-version=2024-06-20) resource and related `test_helper` APIs.

## Impact

Renames a `purchase_details` attribute of the `Transaction` object from `volume_decimal` to `quantity_decimal` to more precisely describe the number of items purchased.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `purchase_details.fuel.volume_decimal` | Changed | [Issuing.Transaction](/api/issuing/transactions/object?api-version=2024-06-20) |
| `quantity_decimal` | Added | [Issuing.Transaction.purchase_details.fuel](/api/issuing/transactions/object?api-version=2024-06-20#issuing_transaction_object-purchase_details-fuel-quantity_decimal) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `quantity_decimal` | Added | [Issuing::Transaction::PurchaseDetail::Fuel](/api/issuing/transactions/object?api-version=2024-06-20#issuing_transaction_object-purchase_details-fuel-quantity_decimal) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `quantity_decimal` | Added | [Issuing.Transaction.PurchaseDetail.Fuel](/api/issuing/transactions/object?api-version=2024-06-20#issuing_transaction_object-purchase_details-fuel-quantity_decimal) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `quantity_decimal` | Added | [Issuing.Transaction.purchase_details.fuel](/api/issuing/transactions/object?api-version=2024-06-20#issuing_transaction_object-purchase_details-fuel-quantity_decimal) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `quantityDecimal` | Added | [issuing.Transaction.purchase_details.fuel](/api/issuing/transactions/object?api-version=2024-06-20#issuing_transaction_object-purchase_details-fuel-quantity_decimal) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `quantity_decimal` | Added | [Issuing.Transaction.purchase_details.fuel](/api/issuing/transactions/object?api-version=2024-06-20#issuing_transaction_object-purchase_details-fuel-quantity_decimal) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `QuantityDecimal` | Added | [IssuingTransactionPurchaseDetailsFuel](/api/issuing/transactions/object?api-version=2024-06-20#issuing_transaction_object-purchase_details-fuel-quantity_decimal) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `QuantityDecimal` | Added | [Issuing.Transaction.PurchaseDetails.Fuel](/api/issuing/transactions/object?api-version=2024-06-20#issuing_transaction_object-purchase_details-fuel-quantity_decimal) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-06-20`
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
