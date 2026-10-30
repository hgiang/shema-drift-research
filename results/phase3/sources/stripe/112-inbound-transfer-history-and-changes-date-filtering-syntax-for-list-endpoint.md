# Removes level property from inbound transfer history and changes date filtering syntax for list endpoints

## What’s new

Removes the [level](https://docs.stripe.com/api/v2/money-management/inbound-transfers/object.md?api-version=2026-08-26.preview#v2_inbound_transfer_object-transfer_history-level) property from [transfer_history](https://docs.stripe.com/api/v2/money-management/inbound-transfers/object.md?api-version=2026-09-30.preview#v2_inbound_transfer_object-transfer_history) entries on a [v2 Inbound Transfer](https://docs.stripe.com/api/v2/money-management/inbound-transfers/object.md?api-version=2026-09-30.preview). Previously, each transfer history entry included a `level` property with a value of `canonical` or `debug`, but only `canonical` was ever used. This property no longer appears in responses.

Changes the date filtering syntax on [List Inbound Transfers](https://docs.stripe.com/api/v2/money-management/inbound-transfers/list.md?api-version=2026-09-30.preview) and [List Received Credits](https://docs.stripe.com/api/v2/money-management/received-credits/list.md?api-version=2026-09-30.preview). Previously, you could filter by [created_gt](https://docs.stripe.com/api/v2/money-management/inbound-transfers/list.md?api-version=2026-08-26.preview#v2_list_inbound_transfers-created_gt), [created_gte](https://docs.stripe.com/api/v2/money-management/inbound-transfers/list.md?api-version=2026-08-26.preview#v2_list_inbound_transfers-created_gte), [created_lt](https://docs.stripe.com/api/v2/money-management/inbound-transfers/list.md?api-version=2026-08-26.preview#v2_list_inbound_transfers-created_lt) and [created_lte](https://docs.stripe.com/api/v2/money-management/inbound-transfers/list.md?api-version=2026-08-26.preview#v2_list_inbound_transfers-created_lte) as top-level query parameters. These parameters are now nested under a [created](https://docs.stripe.com/api/v2/money-management/inbound-transfers/list.md?api-version=2026-09-30.preview#v2_list_inbound_transfers-created) hash using bracket syntax (for example, `created[gt]`, `created[gte]`). The [created](https://docs.stripe.com/api/v2/money-management/inbound-transfers/list.md?api-version=2026-08-26.preview#v2_list_inbound_transfers-created) equality filter is removed entirely.

## Why is this a breaking change?

These changes remove the `level` property from `transfer_history` entries on a v2 Inbound Transfer and replace flat date filtering parameters with bracket syntax when you [List Inbound Transfers](https://docs.stripe.com/api/v2/money-management/inbound-transfers/list.md?api-version=2026-09-30.preview) or [List Received Credits](https://docs.stripe.com/api/v2/money-management/received-credits/list.md?api-version=2026-09-30.preview). If your code reads `transfer_history[].level`, that property no longer exists in the response. If your code passes `created_gt`, `created_gte`, `created_lt`, `created_lte`, or `created` as top-level query parameters, those parameters are no longer accepted. Use `created[gt]`, `created[gte]`, `created[lt]`, and `created[lte]` instead.

## Impact

If your integration reads the `level` property from `transfer_history` entries on [v2 Inbound Transfers](https://docs.stripe.com/api/v2/money-management/inbound-transfers/object.md?api-version=2026-09-30.preview), remove references to that property.

If your integration uses flat date filtering parameters (such as `created_gt` or `created_lte`) when [Listing Inbound Transfers](https://docs.stripe.com/api/v2/money-management/inbound-transfers/list.md?api-version=2026-09-30.preview) or [Listing Received Credits](https://docs.stripe.com/api/v2/money-management/received-credits/list.md?api-version=2026-09-30.preview), update those calls to pass a nested `created` hash instead. For the REST API, use bracket syntax (for example, `created[gt]`). For SDKs, set the corresponding nested parameters on the `created` parameter hash (see the per-SDK changes table below). Previously, you could also filter by exact `created` timestamp equality. This is no longer supported. Remove any use of the `created` equality filter from your requests.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `level` | Removed | [V2.MoneyManagement.InboundTransfer.transfer_history[]](/api/v2/money-management/inbound-transfers/object?api-version=2026-09-30.preview#v2_inbound_transfer_object-transfer_history) |
| `created_gt`, `created_gte`, `created_lt`, `created_lte` | Removed | [V2.MoneyManagement.InboundTransfer#list](/api/v2/money-management/inbound-transfers/list?api-version=2026-09-30.preview#v2_list_inbound_transfers), [V2.MoneyManagement.ReceivedCredit#list](/api/v2/money-management/received-credits/list?api-version=2026-09-30.preview#v2_list_received_credits) |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2.MoneyManagement.InboundTransfer#list.created`, `V2.MoneyManagement.ReceivedCredit#list.created` | Changed | `DateTime → an object` |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `level` | Removed | [V2::MoneyManagement::InboundTransfer::TransferHistory](/api/v2/money-management/inbound-transfers/object?api-version=2026-09-30.preview#v2_inbound_transfer_object-transfer_history) |
| `created_gt`, `created_gte`, `created_lt`, `created_lte` | Removed | [V2::MoneyManagement::InboundTransferListParams](/api/v2/money-management/inbound-transfers/list?api-version=2026-09-30.preview#v2_list_inbound_transfers), [V2::MoneyManagement::ReceivedCreditListParams](/api/v2/money-management/received-credits/list?api-version=2026-09-30.preview#v2_list_received_credits) |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2::MoneyManagement::InboundTransferListParams.created`, `V2::MoneyManagement::ReceivedCreditListParams.created` | Changed | `DateTime → an object` |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `level` | Removed | [V2.MoneyManagement.InboundTransfer.TransferHistory](/api/v2/money-management/inbound-transfers/object?api-version=2026-09-30.preview#v2_inbound_transfer_object-transfer_history) |
| `created_gt`, `created_gte`, `created_lt`, `created_lte` | Removed | [v2.money_management.InboundTransferListParams](/api/v2/money-management/inbound-transfers/list?api-version=2026-09-30.preview#v2_list_inbound_transfers), [v2.money_management.ReceivedCreditListParams](/api/v2/money-management/received-credits/list?api-version=2026-09-30.preview#v2_list_received_credits) |

| Fields | Change | From → to |
| --- | --- | --- |
| `v2.money_management.InboundTransferListParams.created`, `v2.money_management.ReceivedCreditListParams.created` | Changed | `DateTime → an object` |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `level` | Removed | [V2.MoneyManagement.InboundTransfer.transfer_history[]](/api/v2/money-management/inbound-transfers/object?api-version=2026-09-30.preview#v2_inbound_transfer_object-transfer_history) |
| `created_gt`, `created_gte`, `created_lt`, `created_lte` | Removed | [V2\MoneyManagement\InboundTransfer.all().$params](/api/v2/money-management/inbound-transfers/list?api-version=2026-09-30.preview#v2_list_inbound_transfers), [V2\MoneyManagement\ReceivedCredit.all().$params](/api/v2/money-management/received-credits/list?api-version=2026-09-30.preview#v2_list_received_credits) |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2\MoneyManagement\InboundTransfer.all().$params.created`, `V2\MoneyManagement\ReceivedCredit.all().$params.created` | Changed | `DateTime → an object` |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `level` | Removed | [v2.moneymanagement.InboundTransfer.transfer_history[]](/api/v2/money-management/inbound-transfers/object?api-version=2026-09-30.preview#v2_inbound_transfer_object-transfer_history) |
| `createdGt`, `createdGte`, `createdLt`, `createdLte` | Removed | [v2.moneymanagement.InboundTransferListParams](/api/v2/money-management/inbound-transfers/list?api-version=2026-09-30.preview#v2_list_inbound_transfers), [v2.moneymanagement.ReceivedCreditListParams](/api/v2/money-management/received-credits/list?api-version=2026-09-30.preview#v2_list_received_credits) |

| Fields | Change | From → to |
| --- | --- | --- |
| `v2.moneymanagement.InboundTransferListParams.created`, `v2.moneymanagement.ReceivedCreditListParams.created` | Changed | `DateTime → an object` |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `level` | Removed | [V2.MoneyManagement.InboundTransfer.transfer_history[]](/api/v2/money-management/inbound-transfers/object?api-version=2026-09-30.preview#v2_inbound_transfer_object-transfer_history) |
| `created_gt`, `created_gte`, `created_lt`, `created_lte` | Removed | [V2.MoneyManagement.InboundTransferListParams](/api/v2/money-management/inbound-transfers/list?api-version=2026-09-30.preview#v2_list_inbound_transfers), [V2.MoneyManagement.ReceivedCreditListParams](/api/v2/money-management/received-credits/list?api-version=2026-09-30.preview#v2_list_received_credits) |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2.MoneyManagement.InboundTransferListParams.created`, `V2.MoneyManagement.ReceivedCreditListParams.created` | Changed | `DateTime → an object` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Level` | Removed | [V2MoneyManagementInboundTransferTransferHistory](/api/v2/money-management/inbound-transfers/object?api-version=2026-09-30.preview#v2_inbound_transfer_object-transfer_history) |
| `CreatedGTE`, `CreatedGt`, `CreatedLT`, `CreatedLte` | Removed | [V2MoneyManagementInboundTransferListParams](/api/v2/money-management/inbound-transfers/list?api-version=2026-09-30.preview#v2_list_inbound_transfers), [V2MoneyManagementReceivedCreditListParams](/api/v2/money-management/received-credits/list?api-version=2026-09-30.preview#v2_list_received_credits) |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2MoneyManagementInboundTransferListParams.Created`, `V2MoneyManagementReceivedCreditListParams.Created` | Changed | `DateTime → an object` |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Level` | Removed | [V2.MoneyManagement.InboundTransfer.TransferHistory](/api/v2/money-management/inbound-transfers/object?api-version=2026-09-30.preview#v2_inbound_transfer_object-transfer_history) |
| `CreatedGt`, `CreatedGte`, `CreatedLt`, `CreatedLte` | Removed | [V2.MoneyManagement.InboundTransferListOptions](/api/v2/money-management/inbound-transfers/list?api-version=2026-09-30.preview#v2_list_inbound_transfers), [V2.MoneyManagement.ReceivedCreditListOptions](/api/v2/money-management/received-credits/list?api-version=2026-09-30.preview#v2_list_received_credits) |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2.MoneyManagement.InboundTransferListOptions.Created`, `V2.MoneyManagement.ReceivedCreditListOptions.Created` | Changed | `DateTime → an object` |

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
- [Moves Financial Address test helper endpoints to the money management namespace](https://docs.stripe.com/changelog/endive/2026-09-30/moves-financial-address-test-helper-endpoints-to-the-money-management-namespace.md)
- [Opens the adjusted flow type enum and changes the list filters for v2 Adjustments and v2 Transactions](https://docs.stripe.com/changelog/endive/2026-09-30/opens-adjusted-flow-type-enum-and-changes-date-filtering-syntax.md)
- [Updates Financial Address request and response structure](https://docs.stripe.com/changelog/endive/2026-09-30/updating-financial-address-request-and-response-structure.md)
- [Expands Reserve Plan listing access and adds filters](https://docs.stripe.com/changelog/endive/2026-09-30/expands-reserve-plan-listing-access.md)
- [Adds a Treasury Transaction property to the Money Management Transaction update events](https://docs.stripe.com/changelog/endive/2026-09-30/treasury-transaction-property-for-money-management-transaction-update-events.md)
- [Adds deposit insurance eligibility details to Financial Accounts](https://docs.stripe.com/changelog/endive/2026-09-30/includable-insurance-eligibility-field-for-v2-financial-accounts.md)
- [Adds network fee details to estimated fees on Outbound Payment Quotes](https://docs.stripe.com/changelog/endive/2026-09-30/adds-network-fee-details-to-estimated-fees.md)
