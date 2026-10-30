# Removes legacy usage-based billing

## What’s new

We’ve removed support for legacy usage-based billing. You can no longer create a [price](https://docs.stripe.com/api/prices/object.md?api-version=2025-03-31.basil) with a [usage_type](https://docs.stripe.com/api/prices/object.md?api-version=2025-02-24.acacia#price_object-recurring-usage_type) of `metered` without a specified [meter](https://docs.stripe.com/api/prices/object.md?api-version=2025-02-24.acacia#price_object-recurring-meter). We’ve also removed the [billing_thresholds](https://docs.stripe.com/api/subscriptions/object.md?api-version=2025-02-24.acacia#subscription_object-billing_thresholds) from the subscription endpoints.

We’ve removed [billing_thresholds](https://docs.stripe.com/api/subscriptions/object.md?api-version=2025-02-24.acacia#subscription_object-billing_thresholds) and [aggregate_usage](https://docs.stripe.com/api/prices/object.md?api-version=2025-02-24.acacia#price_object-recurring-aggregate_usage) from all API endpoints. You can no longer create legacy usage-based prices or attach existing legacy usage-based prices to quotes, upcoming invoices, or subscriptions.

A legacy usage-based price is defined as a price with a [usage_type](https://docs.stripe.com/api/prices/object.md?api-version=2025-02-24.acacia#price_object-recurring-usage_type) of `metered` without a specified [meter](https://docs.stripe.com/api/prices/object.md?api-version=2025-02-24.acacia#price_object-recurring-meter).

## Why is this a breaking change?

- Removed `billing_thresholds` from [Subscription](https://docs.stripe.com/api/subscriptions/object.md?api-version=2025-03-31.basil) endpoints.
- Removed `aggregate_usage` from [Price](https://docs.stripe.com/api/prices/object.md?api-version=2025-03-31.basil) endpoints.
- Using `usage_type` of `metered` without a specified `meter` now returns an error on [Price](https://docs.stripe.com/api/prices/object.md?api-version=2025-03-31.basil) creation.
- Removed support for attaching prices of `usage_type=metered` without a set `meter` to Subscriptions, Subscription Schedules and Quotes.

## Impact

Follow our [migration guide](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/migration-guide.md) to update your integration to use [meters](https://docs.stripe.com/api/billing/meter.md?api-version=2025-03-31.basil).

### Using the legacy UsageRecords API via RawRequest

You can continue using the legacy UsageRecords API after upgrading your SDK by calling it via RawRequest with a pinned pre-Basil API version. See [Upgrade your SDK without migrating from usage records](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/sdk-upgrade.md).

## Changes

#### REST API

|  | Change | Resources |
| --- | --- | --- |
|  | Removed | [UsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil), [UsageRecord](/api/usage_records/object?api-version=2025-03-31.basil) |

| Endpoints | Change | Resources |
| --- | --- | --- |
| `create` | Removed | [UsageRecord](/api/usage_records/object?api-version=2025-03-31.basil) |
| `list` | Removed | [UsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil) |
| `usage_record_summaries` | Removed | [SubscriptionItem](/api/subscription_items/object?api-version=2025-03-31.basil) |

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `aggregate_usage` | Removed | [Plan#create](/api/plans/create?api-version=2025-03-31.basil), [Plan](/api/plans?api-version=2025-03-31.basil), `Price#create.recurring`, `Price.recurring` |
| `billing_thresholds` | Removed | [Invoice#create_preview.schedule_details.phases[].items[]](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-schedule_details-phases-items), [Invoice#create_preview.schedule_details.phases[]](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-schedule_details-phases), [Invoice#create_preview.subscription_details.items[]](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-subscription_details-items), [Subscription#create.items[]](/api/subscriptions/create?api-version=2025-03-31.basil#create_subscription-items), [Subscription#create](/api/subscriptions/create?api-version=2025-03-31.basil), [Subscription#update.items[]](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-items), [Subscription#update](/api/subscriptions/update?api-version=2025-03-31.basil), [SubscriptionItem#create](/api/subscriptions/create?api-version=2025-03-31.basil#create_subscription-items), [SubscriptionItem#update](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-items), [SubscriptionItem](/api/subscription_items/object?api-version=2025-03-31.basil), [SubscriptionSchedule#create.default_settings](/api/subscription_schedules/create?api-version=2025-03-31.basil#create_subscription_schedule-default_settings), [SubscriptionSchedule#create.phases[].items[]](/api/subscription_schedules/create?api-version=2025-03-31.basil#create_subscription_schedule-phases-items), [SubscriptionSchedule#create.phases[]](/api/subscription_schedules/create?api-version=2025-03-31.basil#create_subscription_schedule-phases), [SubscriptionSchedule#update.default_settings](/api/subscription_schedules/update?api-version=2025-03-31.basil#update_subscription_schedule-default_settings), [SubscriptionSchedule#update.phases[].items[]](/api/subscription_schedules/update?api-version=2025-03-31.basil#update_subscription_schedule-phases-items), [SubscriptionSchedule#update.phases[]](/api/subscription_schedules/update?api-version=2025-03-31.basil#update_subscription_schedule-phases), [SubscriptionSchedule.default_settings](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-default_settings), [SubscriptionSchedule.phases[].items[]](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases-items), [SubscriptionSchedule.phases[]](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases), [Subscription](/api/subscriptions/object?api-version=2025-03-31.basil) |

#### Ruby

|  | Change | Resources |
| --- | --- | --- |
|  | Removed | [SubscriptionItemUsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil#usage_record_summary-subscription_item), [SubscriptionItemUsageRecord](/api/usage_records/object?api-version=2025-03-31.basil#usage_record_object-subscription_item) |

| Methods | Change | Resources |
| --- | --- | --- |
| `create` | Removed | [SubscriptionItemUsageRecord](/api/usage_records/object?api-version=2025-03-31.basil#usage_record_object-subscription_item) |
| `list` | Removed | [SubscriptionItemUsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil#usage_record_summary-subscription_item) |

#### Python

|  | Change | Resources |
| --- | --- | --- |
|  | Removed | [SubscriptionItemUsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil#usage_record_summary-subscription_item), [SubscriptionItemUsageRecord](/api/usage_records/object?api-version=2025-03-31.basil#usage_record_object-subscription_item) |

| Methods | Change | Resources |
| --- | --- | --- |
| `create` | Removed | [SubscriptionItemUsageRecord](/api/usage_records/object?api-version=2025-03-31.basil#usage_record_object-subscription_item) |
| `list` | Removed | [SubscriptionItemUsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil#usage_record_summary-subscription_item) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `aggregate_usage` | Removed | [Plan.CreateParams](/api/plans/create?api-version=2025-03-31.basil), [Plan](/api/plans?api-version=2025-03-31.basil), `Price.CreateParamsRecurring`, `Price.Recurring` |
| `billing_thresholds` | Removed | [Invoice.CreatePreviewParamsScheduleDetailPhaseItem](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-schedule_details-phases-items), [Invoice.CreatePreviewParamsScheduleDetailPhase](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-schedule_details-phases), [Invoice.CreatePreviewParamsSubscriptionDetailItem](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-subscription_details-items), [Subscription.CreateParamsItem](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-subscription_details-items), [Subscription.CreateParams](/api/subscriptions/create?api-version=2025-03-31.basil#create_subscription-items), [Subscription.UpdateParamsItem](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-items), [Subscription.UpdateParams](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-items), [SubscriptionItem.CreateParams](/api/subscriptions/create?api-version=2025-03-31.basil#create_subscription-items), [SubscriptionItem.UpdateParams](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-items), [SubscriptionItem](/api/subscription_items/object?api-version=2025-03-31.basil), [SubscriptionSchedule.CreateParamsDefaultSetting](/api/subscription_schedules/create?api-version=2025-03-31.basil#create_subscription_schedule-default_settings), [SubscriptionSchedule.CreateParamsPhaseItem](/api/subscription_schedules/create?api-version=2025-03-31.basil#create_subscription_schedule-phases-items), [SubscriptionSchedule.CreateParamsPhase](/api/subscription_schedules/create?api-version=2025-03-31.basil#create_subscription_schedule-phases), [SubscriptionSchedule.DefaultSetting](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-default_settings), [SubscriptionSchedule.Phase.Item](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases-items), [SubscriptionSchedule.Phase](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases), [SubscriptionSchedule.UpdateParamsDefaultSetting](/api/subscription_schedules/update?api-version=2025-03-31.basil#update_subscription_schedule-default_settings), [SubscriptionSchedule.UpdateParamsPhaseItem](/api/subscription_schedules/update?api-version=2025-03-31.basil#update_subscription_schedule-phases-items), [SubscriptionSchedule.UpdateParamsPhase](/api/subscription_schedules/update?api-version=2025-03-31.basil#update_subscription_schedule-phases), [Subscription](/api/subscriptions/object?api-version=2025-03-31.basil) |

#### PHP

|  | Change | Resources |
| --- | --- | --- |
|  | Removed | [UsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil), [UsageRecord](/api/usage_records/object?api-version=2025-03-31.basil) |

| Methods | Change | Resources |
| --- | --- | --- |
| `create` | Removed | [UsageRecord](/api/usage_records/object?api-version=2025-03-31.basil) |
| `all` | Removed | [UsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `aggregate_usage` | Removed | [Plan](/api/plans?api-version=2025-03-31.basil) |
| `billing_thresholds` | Removed | [SubscriptionItem](/api/subscription_items/object?api-version=2025-03-31.basil), [Subscription](/api/subscriptions/object?api-version=2025-03-31.basil) |

#### Java

|  | Change | Resources |
| --- | --- | --- |
|  | Removed | [SubscriptionItemUsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil#usage_record_summary-subscription_item), [SubscriptionItemUsageRecord](/api/usage_records/object?api-version=2025-03-31.basil#usage_record_object-subscription_item) |

| Methods | Change | Resources |
| --- | --- | --- |
| `create` | Removed | [SubscriptionItemUsageRecord](/api/usage_records/object?api-version=2025-03-31.basil#usage_record_object-subscription_item) |
| `list` | Removed | [SubscriptionItemUsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil#usage_record_summary-subscription_item) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `aggregateUsage` | Removed | [PlanCreateParams](/api/plans/create?api-version=2025-03-31.basil), [Plan](/api/plans?api-version=2025-03-31.basil), `Price.recurring`, `PriceCreateParams.recurring` |
| `billingThresholds` | Removed | [InvoiceCreatePreviewParams.schedule_details.phases[].items[]](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-schedule_details-phases-items), [InvoiceCreatePreviewParams.schedule_details.phases[]](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-schedule_details-phases), [InvoiceCreatePreviewParams.subscription_details.items[]](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-default_settings), [SubscriptionCreateParams.items[]](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-subscription_details-items), [SubscriptionCreateParams](/api/subscriptions/create?api-version=2025-03-31.basil), [SubscriptionItemCreateParams](/api/subscriptions/create?api-version=2025-03-31.basil#create_subscription-items), [SubscriptionItemUpdateParams](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-items), [SubscriptionItem](/api/subscription_items/object?api-version=2025-03-31.basil), `SubscriptionSchedule.default_settings`, [SubscriptionSchedule.phases[].items[]](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases-items), [SubscriptionSchedule.phases[]](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases), [SubscriptionScheduleCreateParams.default_settings](/api/subscription_schedules/create?api-version=2025-03-31.basil#create_subscription_schedule-default_settings), [SubscriptionScheduleCreateParams.phases[].items[]](/api/subscription_schedules/create?api-version=2025-03-31.basil#create_subscription_schedule-phases-items), [SubscriptionScheduleCreateParams.phases[]](/api/subscription_schedules/create?api-version=2025-03-31.basil#create_subscription_schedule-phases), [SubscriptionScheduleUpdateParams.default_settings](/api/subscription_schedules/update?api-version=2025-03-31.basil#update_subscription_schedule-default_settings), [SubscriptionScheduleUpdateParams.phases[].items[]](/api/subscription_schedules/update?api-version=2025-03-31.basil#update_subscription_schedule-phases-items), [SubscriptionScheduleUpdateParams.phases[]](/api/subscription_schedules/update?api-version=2025-03-31.basil#update_subscription_schedule-phases), [SubscriptionUpdateParams.items[]](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-items), [SubscriptionUpdateParams](/api/subscriptions/update?api-version=2025-03-31.basil), [Subscription](/api/subscriptions/object?api-version=2025-03-31.basil) |

#### Node.js

|  | Change | Resources |
| --- | --- | --- |
|  | Removed | [SubscriptionItemUsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil#usage_record_summary-subscription_item), [SubscriptionItemUsageRecord](/api/usage_records/object?api-version=2025-03-31.basil#usage_record_object-subscription_item) |

| Methods | Change | Resources |
| --- | --- | --- |
| `create` | Removed | [SubscriptionItemUsageRecord](/api/usage_records/object?api-version=2025-03-31.basil#usage_record_object-subscription_item) |
| `list` | Removed | [SubscriptionItemUsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil#usage_record_summary-subscription_item) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `aggregate_usage` | Removed | [PlanCreateParams](/api/plans/create?api-version=2025-03-31.basil), [Plan](/api/plans?api-version=2025-03-31.basil), `Price.recurring`, `PriceCreateParams.recurring` |
| `billing_thresholds` | Removed | [InvoiceCreatePreviewParams.schedule_details.phases[].items[]](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-schedule_details-phases-items), [InvoiceCreatePreviewParams.schedule_details.phases[]](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-schedule_details-phases), [InvoiceCreatePreviewParams.subscription_details.items[]](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-subscription_details-items), [SubscriptionCreateParams.items[]](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-subscription_details-items), [SubscriptionCreateParams](/api/subscriptions/create?api-version=2025-03-31.basil), [SubscriptionItemCreateParams](/api/subscriptions/create?api-version=2025-03-31.basil#create_subscription-items), [SubscriptionItemUpdateParams](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-items), [SubscriptionItem](/api/subscription_items/object?api-version=2025-03-31.basil), [SubscriptionSchedule.default_settings](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-default_settings), [SubscriptionSchedule.phases[].items[]](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases-items), [SubscriptionSchedule.phases[]](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases), [SubscriptionScheduleCreateParams.default_settings](/api/subscription_schedules/create?api-version=2025-03-31.basil#create_subscription_schedule-default_settings), [SubscriptionScheduleCreateParams.phases[].items[]](/api/subscription_schedules/create?api-version=2025-03-31.basil#create_subscription_schedule-phases-items), [SubscriptionScheduleCreateParams.phases[]](/api/subscription_schedules/create?api-version=2025-03-31.basil#create_subscription_schedule-phases), [SubscriptionScheduleUpdateParams.default_settings](/api/subscription_schedules/update?api-version=2025-03-31.basil#update_subscription_schedule-default_settings), [SubscriptionScheduleUpdateParams.phases[].items[]](/api/subscription_schedules/update?api-version=2025-03-31.basil#update_subscription_schedule-phases-items), [SubscriptionScheduleUpdateParams.phases[]](/api/subscription_schedules/update?api-version=2025-03-31.basil#update_subscription_schedule-phases), [SubscriptionUpdateParams.items[]](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-items), [SubscriptionUpdateParams](/api/subscriptions/update?api-version=2025-03-31.basil), [Subscription](/api/subscriptions/object?api-version=2025-03-31.basil) |

#### Go

|  | Change | Resources |
| --- | --- | --- |
|  | Removed | [UsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil), [UsageRecord](/api/usage_records/object?api-version=2025-03-31.basil) |

| Methods | Change | Resources |
| --- | --- | --- |
| `New` | Removed | [UsageRecord](/api/usage_records/object?api-version=2025-03-31.basil) |
| `List` | Removed | [UsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil) |
| `UsageRecordSummaries` | Removed | [SubscriptionItem](/api/subscription_items/object?api-version=2025-03-31.basil) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AggregateUsage` | Removed | [PlanParams](/api/plans?api-version=2025-03-31.basil), [Plan](/api/plans?api-version=2025-03-31.basil), `PriceRecurringParams`, `PriceRecurring` |
| `BillingThresholds` | Removed | [InvoiceCreatePreviewScheduleDetailsPhasesItemsParams](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-schedule_details-phases-items), [InvoiceCreatePreviewScheduleDetailsPhasesParams](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-schedule_details-phases), [InvoiceCreatePreviewSubscriptionDetailsItemsParams](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-subscription_details-items), [SubscriptionItemParams](/api/subscription_items/object?api-version=2025-03-31.basil), [SubscriptionItem](/api/subscription_items/object?api-version=2025-03-31.basil), [SubscriptionItemsParams](/api/subscription_items?api-version=2025-03-31.basil), [SubscriptionParams](/api/subscriptions?api-version=2025-03-31.basil), [SubscriptionScheduleDefaultSettingsParams](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-default_settings), [SubscriptionScheduleDefaultSettings](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-default_settings), [SubscriptionSchedulePhasesItemsParams](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases-items), [SubscriptionSchedulePhasesItems](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases-items), [SubscriptionSchedulePhasesParams](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases), [SubscriptionSchedulePhases](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases), [Subscription](/api/subscriptions/object?api-version=2025-03-31.basil) |

#### .NET

|  | Change | Resources |
| --- | --- | --- |
|  | Removed | [SubscriptionItemUsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil#usage_record_summary-subscription_item), [SubscriptionItemUsageRecord](/api/usage-record-summary/object?api-version=2025-03-31.basil#usage_record_summary-subscription_item) |

| Methods | Change | Resources |
| --- | --- | --- |
| `Create` | Removed | [SubscriptionItemUsageRecord](/api/usage-record-summary/object?api-version=2025-03-31.basil#usage_record_summary-subscription_item) |
| `List` | Removed | [SubscriptionItemUsageRecordSummary](/api/usage-record-summary/object?api-version=2025-03-31.basil#usage_record_summary-subscription_item) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AggregateUsage` | Removed | [PlanCreateOptions](/api/plans/create?api-version=2025-03-31.basil), [Plan](/api/plans?api-version=2025-03-31.basil), `PriceRecurringOptions`, `PriceRecurring` |
| `BillingThresholds` | Removed | [InvoiceScheduleDetailsPhasesItemsOptions](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-schedule_details-phases-items), [InvoiceScheduleDetailsPhasesOptions](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-schedule_details-phases), [InvoiceSubscriptionDetailsItemsOptions](/api/invoices/create_preview?api-version=2025-03-31.basil#create_create_preview-subscription_details-items), [SubscriptionCreateOptions](/api/subscriptions/create?api-version=2025-03-31.basil), [SubscriptionItemCreateOptions](/api/subscriptions/create?api-version=2025-03-31.basil#create_subscription-items), [SubscriptionItemUpdateOptions](/api/subscriptions/update?api-version=2025-03-31.basil#update_subscription-items), [SubscriptionItem](/api/subscription_items/object?api-version=2025-03-31.basil), [SubscriptionItemsOptions](/api/subscription_items?api-version=2025-03-31.basil), [SubscriptionScheduleDefaultSettingsOptions](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-default_settings), [SubscriptionScheduleDefaultSettings](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-default_settings), [SubscriptionSchedulePhasesItemsOptions](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases-items), [SubscriptionSchedulePhasesItems](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases-items), [SubscriptionSchedulePhasesOptions](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases), [SubscriptionSchedulePhases](/api/subscription_schedules/object?api-version=2025-03-31.basil#subscription_schedule_object-phases), [SubscriptionUpdateOptions](/api/subscriptions/update?api-version=2025-03-31.basil), [Subscription](/api/subscriptions/object?api-version=2025-03-31.basil) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-03-31.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.0.0](https://github.com/stripe/stripe-python/releases/tag/v12.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.0.0](https://github.com/stripe/stripe-php/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.0.0](https://github.com/stripe/stripe-java/releases/tag/v29.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.0.0](https://github.com/stripe/stripe-node/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.0.0](https://github.com/stripe/stripe-go/releases/tag/v82.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Replaces Upcoming Invoice API methods with the Create Preview Invoice API](https://docs.stripe.com/changelog/basil/2025-03-31/invoice-preview-api-deprecations.md)
