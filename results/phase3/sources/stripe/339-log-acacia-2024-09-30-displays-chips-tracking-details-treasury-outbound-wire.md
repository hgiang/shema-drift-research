# Displays CHIPS tracking details for outbound wire payments and transfers

## What’s new

Tracking details for US domestic wires sent through the CHIPS network is now available in the `tracking_details.us_domestic_wire.chips` field for [Outbound Payments](https://docs.stripe.com/api/treasury/outbound_payments.md?api-version=2024-09-30.acacia) and [Outbound Transfers](https://docs.stripe.com/api/treasury/outbound_transfers.md?api-version=2024-09-30.acacia). See the [upgrade guide](https://docs.stripe.com/treasury/connect/legacy/v1/moving-money/moving-money-out.md) for more information about how to upgrade and use this feature.

## Impact

Enables tracking of a US domestic wires sent through the CHIPS network.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `chips` | Added | [Treasury.OutboundPayment.testHelpers#update.tracking_details.us_domestic_wire](/api/treasury/outbound_payments/test_mode_update?api-version=2024-09-30.acacia#test_mode_outbound_payment_update-tracking_details-us_domestic_wire), [Treasury.OutboundPayment.tracking_details.us_domestic_wire](/api/treasury/outbound_payments/object?api-version=2024-09-30.acacia#outbound_payment_object-tracking_details-us_domestic_wire), [Treasury.OutboundTransfer.testHelpers#update.tracking_details.us_domestic_wire](/api/treasury/outbound_transfers/test_mode_update?api-version=2024-09-30.acacia#test_mode_update_outbound_transfer-tracking_details-us_domestic_wire), [Treasury.OutboundTransfer.tracking_details.us_domestic_wire](/api/treasury/outbound_transfers/object?api-version=2024-09-30.acacia#outbound_transfer_object-tracking_details-us_domestic_wire) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Treasury.OutboundPayment.tracking_details.us_domestic_wire.imad`, `Treasury.OutboundTransfer.tracking_details.us_domestic_wire.imad` | Changed | `string → nullable(string)` |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

This change doesn’t affect the Python SDK.

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `chips` | Added | [Treasury.OutboundPayment.tracking_details.us_domestic_wire](/api/treasury/outbound_payments/object?api-version=2024-09-30.acacia#outbound_payment_object-tracking_details-us_domestic_wire), [Treasury.OutboundTransfer.tracking_details.us_domestic_wire](/api/treasury/outbound_transfers/object?api-version=2024-09-30.acacia#outbound_transfer_object-tracking_details-us_domestic_wire), [treasury.OutboundPaymentUpdateParams.tracking_details.us_domestic_wire](/api/treasury/outbound_payments/test_mode_update?api-version=2024-09-30.acacia#test_mode_outbound_payment_update-tracking_details-us_domestic_wire), [treasury.OutboundTransferUpdateParams.tracking_details.us_domestic_wire](/api/treasury/outbound_transfers/test_mode_update?api-version=2024-09-30.acacia#test_mode_update_outbound_transfer-tracking_details-us_domestic_wire) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `chips` | Added | [Treasury.OutboundPayment.tracking_details.us_domestic_wire](/api/treasury/outbound_payments/object?api-version=2024-09-30.acacia#outbound_payment_object-tracking_details-us_domestic_wire), [Treasury.OutboundPaymentUpdateParams.testHelpers.tracking_details.us_domestic_wire](/api/treasury/outbound_payments/test_mode_update?api-version=2024-09-30.acacia#test_mode_outbound_payment_update-tracking_details-us_domestic_wire), [Treasury.OutboundTransfer.tracking_details.us_domestic_wire](/api/treasury/outbound_transfers/object?api-version=2024-09-30.acacia#outbound_transfer_object-tracking_details-us_domestic_wire), [Treasury.OutboundTransferUpdateParams.testHelpers.tracking_details.us_domestic_wire](/api/treasury/outbound_transfers/test_mode_update?api-version=2024-09-30.acacia#test_mode_update_outbound_transfer-tracking_details-us_domestic_wire) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Treasury.OutboundPayment.tracking_details.us_domestic_wire.imad`, `Treasury.OutboundTransfer.tracking_details.us_domestic_wire.imad` | Changed | `string → string | null` |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Chips` | Added | [TreasuryOutboundPaymentTrackingDetailsUsDomesticWireParams](/api/treasury/outbound_payments/test_mode_update?api-version=2024-09-30.acacia#test_mode_outbound_payment_update-tracking_details-us_domestic_wire), [TreasuryOutboundPaymentTrackingDetailsUsDomesticWire](/api/treasury/outbound_payments/object?api-version=2024-09-30.acacia#outbound_payment_object-tracking_details-us_domestic_wire), [TreasuryOutboundTransferTrackingDetailsUsDomesticWireParams](/api/treasury/outbound_transfers/test_mode_update?api-version=2024-09-30.acacia#test_mode_update_outbound_transfer-tracking_details-us_domestic_wire), [TreasuryOutboundTransferTrackingDetailsUsDomesticWire](/api/treasury/outbound_transfers/object?api-version=2024-09-30.acacia#outbound_transfer_object-tracking_details-us_domestic_wire) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Chips` | Added | [TreasuryOutboundPaymentTrackingDetailsUsDomesticWireOptions](/api/treasury/outbound_payments/test_mode_update?api-version=2024-09-30.acacia#test_mode_outbound_payment_update-tracking_details-us_domestic_wire), [TreasuryOutboundPaymentTrackingDetailsUsDomesticWire](/api/treasury/outbound_payments/object?api-version=2024-09-30.acacia#outbound_payment_object-tracking_details-us_domestic_wire), [TreasuryOutboundTransferTrackingDetailsUsDomesticWireOptions](/api/treasury/outbound_transfers/test_mode_update?api-version=2024-09-30.acacia#test_mode_update_outbound_transfer-tracking_details-us_domestic_wire), [TreasuryOutboundTransferTrackingDetailsUsDomesticWire](/api/treasury/outbound_transfers/object?api-version=2024-09-30.acacia#outbound_transfer_object-tracking_details-us_domestic_wire) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-09-30.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.0.0](https://github.com/stripe/stripe-python/releases/tag/v11.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.0.0](https://github.com/stripe/stripe-php/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v27.0.0](https://github.com/stripe/stripe-java/releases/tag/v27.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.0.0](https://github.com/stripe/stripe-node/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v80.0.0](https://github.com/stripe/stripe-go/releases/tag/v80.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v46.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v46.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
