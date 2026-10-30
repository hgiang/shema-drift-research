# Adds network fee details to estimated fees on Outbound Payment Quotes

## What’s new

Adds a `network_fee` value to the [estimated_fees[].type](https://docs.stripe.com/api/v2/money-management/outbound-payment-quotes/object.md?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees-type) enum and a [network_fee_details](https://docs.stripe.com/api/v2/money-management/outbound-payment-quotes/object.md?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees-network_fee_details) property on estimated fee items for [Outbound Payment Quotes](https://docs.stripe.com/api/v2/money-management/outbound-payment-quotes.md?api-version=2026-09-30.preview). The `network_fee_details` property is an optional object that contains the payment network (for example, `ach`, `swift`, `sepa` or `rtp`) and any network-specific options.

## Impact

If your integration reads `estimated_fees[].type` on [Outbound Payment Quotes](https://docs.stripe.com/api/v2/money-management/outbound-payment-quotes/object.md?api-version=2026-09-30.preview), you might receive the `network_fee` value. Make sure your code handles this additional enum value. When `type` is `network_fee`, use the `network_fee_details` property to identify the specific network and any network-specific options. For guidance on selecting a payment network and reviewing estimated fees, see [Send money](https://docs.stripe.com/global-payouts/send-money.md#select-a-payment-network).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `network_fee_details` | Added | [V2.MoneyManagement.OutboundPaymentQuote.estimated_fees[]](/api/v2/money-management/outbound-payment-quotes/object?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees) |

| Value | Change | Enum |
| --- | --- | --- |
| `network_fee` | Added | [V2.MoneyManagement.OutboundPaymentQuote.estimated_fees[].type](/api/v2/money-management/outbound-payment-quotes/object?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees-type) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `network_fee_details` | Added | [V2::MoneyManagement::OutboundPaymentQuote::EstimatedFee](/api/v2/money-management/outbound-payment-quotes/object?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `network_fee_details` | Added | [V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee](/api/v2/money-management/outbound-payment-quotes/object?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees) |

| Value | Change | Enum |
| --- | --- | --- |
| `network_fee` | Added | [V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee.type](/api/v2/money-management/outbound-payment-quotes/object?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees-type) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `network_fee_details` | Added | [V2.MoneyManagement.OutboundPaymentQuote.estimated_fees[]](/api/v2/money-management/outbound-payment-quotes/object?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees) |

| Value | Change | Enum |
| --- | --- | --- |
| `network_fee` | Added | [V2.MoneyManagement.OutboundPaymentQuote.estimated_fees[].type](/api/v2/money-management/outbound-payment-quotes/object?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees-type) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `networkFeeDetails` | Added | [v2.moneymanagement.OutboundPaymentQuote.EstimatedFee](/api/v2/money-management/outbound-payment-quotes/object?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `network_fee_details` | Added | [V2.MoneyManagement.OutboundPaymentQuote.estimated_fees[]](/api/v2/money-management/outbound-payment-quotes/object?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees) |

| Value | Change | Enum |
| --- | --- | --- |
| `network_fee` | Added | [V2.MoneyManagement.OutboundPaymentQuote.estimated_fees[].type](/api/v2/money-management/outbound-payment-quotes/object?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees-type) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `NetworkFeeDetails` | Added | [V2MoneyManagementOutboundPaymentQuoteEstimatedFee](/api/v2/money-management/outbound-payment-quotes/object?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees) |

| Value | Change | Enum |
| --- | --- | --- |
| `network_fee` | Added | [V2MoneyManagementOutboundPaymentQuoteEstimatedFee.Type](/api/v2/money-management/outbound-payment-quotes/object?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees-type) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `NetworkFeeDetails` | Added | [V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee](/api/v2/money-management/outbound-payment-quotes/object?api-version=2026-09-30.preview#v2_outbound_payment_quote_object-estimated_fees) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.preview`
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

- [Updates the shapes of v2 Financial Address and v2 Received Credit objects](https://docs.stripe.com/changelog/endive/2026-09-30/financial-address-and-received-credit-shape-updates.md)
- [Removes level property from inbound transfer history and changes date filtering syntax for list endpoints](https://docs.stripe.com/changelog/endive/2026-09-30/removes-level-property-from-inbound-transfer-history-and-changes-date-filtering-syntax-for-list-endpoints.md)
- [Moves Financial Address test helper endpoints to the money management namespace](https://docs.stripe.com/changelog/endive/2026-09-30/moves-financial-address-test-helper-endpoints-to-the-money-management-namespace.md)
- [Opens the adjusted flow type enum and changes the list filters for v2 Adjustments and v2 Transactions](https://docs.stripe.com/changelog/endive/2026-09-30/opens-adjusted-flow-type-enum-and-changes-date-filtering-syntax.md)
- [Updates Financial Address request and response structure](https://docs.stripe.com/changelog/endive/2026-09-30/updating-financial-address-request-and-response-structure.md)
- [Expands Reserve Plan listing access and adds filters](https://docs.stripe.com/changelog/endive/2026-09-30/expands-reserve-plan-listing-access.md)
- [Adds a Treasury Transaction property to the Money Management Transaction update events](https://docs.stripe.com/changelog/endive/2026-09-30/treasury-transaction-property-for-money-management-transaction-update-events.md)
- [Adds deposit insurance eligibility details to Financial Accounts](https://docs.stripe.com/changelog/endive/2026-09-30/includable-insurance-eligibility-field-for-v2-financial-accounts.md)
