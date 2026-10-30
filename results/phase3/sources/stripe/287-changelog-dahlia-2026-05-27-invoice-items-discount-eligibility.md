# Adds discount eligibility options for add-on invoice items on Subscriptions and Preview Invoice APIs

## What’s new

Adds an optional [discountable](https://docs.stripe.com/api/subscriptions/create.md?api-version=2026-05-27.dahlia#create_subscription-add_invoice_items-discountable) parameter when creating add-on invoice items using `add_invoice_items` on the [Subscriptions](https://docs.stripe.com/api/subscriptions.md?api-version=2026-05-27.dahlia), [Subscription Schedules](https://docs.stripe.com/api/subscription_schedules.md?api-version=2026-05-27.dahlia) and [Preview Invoice](https://docs.stripe.com/api/invoices/create_preview.md?api-version=2026-05-27.dahlia) APIs. The discountable parameter controls whether an invoice item is eligible for discounts. Discounts are only applied to discountable invoice items.

The discountable value is also returned as a new property in the [phases.add_invoice_items](https://docs.stripe.com/api/subscription_schedules/object.md?api-version=2026-05-27.dahlia#subscription_schedule_object-phases-add_invoice_items) array on the [Subscription Schedule](https://docs.stripe.com/api/subscription_schedules/object.md?api-version=2026-05-27.dahlia) object.

## Impact

With the new `discountable` parameter, you can explicitly set whether each add-on invoice item is eligible for discounts. This feature gives you more precise control over how discounts interact with one-time charges and credits on your subscriptions. If you don’t provide a value, invoice items default to being discountable. This change doesn’t modify the behaviour of existing integrations, and you must explicitly state in the request when an add-on invoice item must be non-discountable.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `discountable` | Added | [Invoice#create_preview.schedule_details.phases[].add_invoice_items[]](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-schedule_details-phases-add_invoice_items), [Subscription#create.add_invoice_items[]](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription-add_invoice_items), [Subscription#update.add_invoice_items[]](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription-add_invoice_items), [SubscriptionSchedule#create.phases[].add_invoice_items[]](/api/subscription_schedules/create?api-version=2026-05-27.dahlia#create_subscription_schedule-phases-add_invoice_items), [SubscriptionSchedule#update.phases[].add_invoice_items[]](/api/subscription_schedules/update?api-version=2026-05-27.dahlia#update_subscription_schedule-phases-add_invoice_items), [SubscriptionSchedule.phases[].add_invoice_items[]](/api/subscription_schedules/object?api-version=2026-05-27.dahlia#subscription_schedule_object-phases-add_invoice_items) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `discountable` | Added | [InvoiceCreatePreviewParams::ScheduleDetail::Phase::AddInvoiceItem](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-schedule_details-phases-add_invoice_items), [SubscriptionCreateParams::AddInvoiceItem](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription-add_invoice_items), [SubscriptionSchedule::Phase::AddInvoiceItem](/api/subscription_schedules/object?api-version=2026-05-27.dahlia#subscription_schedule_object-phases-add_invoice_items), [SubscriptionScheduleCreateParams::Phase::AddInvoiceItem](/api/subscription_schedules/create?api-version=2026-05-27.dahlia#create_subscription_schedule-phases-add_invoice_items), [SubscriptionScheduleUpdateParams::Phase::AddInvoiceItem](/api/subscription_schedules/update?api-version=2026-05-27.dahlia#update_subscription_schedule-phases-add_invoice_items), [SubscriptionUpdateParams::AddInvoiceItem](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription-add_invoice_items) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `discountable` | Added | [InvoiceCreatePreviewParamsScheduleDetailPhaseAddInvoiceItem](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-schedule_details-phases-add_invoice_items), [SubscriptionCreateParamsAddInvoiceItem](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription-add_invoice_items), [SubscriptionModifyParamsAddInvoiceItem](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription-add_invoice_items), [SubscriptionSchedule.Phase.AddInvoiceItem](/api/subscription_schedules/object?api-version=2026-05-27.dahlia#subscription_schedule_object-phases-add_invoice_items), [SubscriptionScheduleCreateParamsPhaseAddInvoiceItem](/api/subscription_schedules/create?api-version=2026-05-27.dahlia#create_subscription_schedule-phases-add_invoice_items), [SubscriptionScheduleModifyParamsPhaseAddInvoiceItem](/api/subscription_schedules/update?api-version=2026-05-27.dahlia#update_subscription_schedule-phases-add_invoice_items) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `discountable` | Added | [Invoice.create_preview().$params.schedule_detail.phase.add_invoice_item](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-schedule_details-phases-add_invoice_items), [Subscription.create().$params.add_invoice_item](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription-add_invoice_items), [Subscription.update().$params.add_invoice_item](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription-add_invoice_items), [SubscriptionSchedule.create().$params.phase.add_invoice_item](/api/subscription_schedules/create?api-version=2026-05-27.dahlia#create_subscription_schedule-phases-add_invoice_items), [SubscriptionSchedule.phases[].add_invoice_items[]](/api/subscription_schedules/object?api-version=2026-05-27.dahlia#subscription_schedule_object-phases-add_invoice_items), [SubscriptionSchedule.update().$params.phase.add_invoice_item](/api/subscription_schedules/update?api-version=2026-05-27.dahlia#update_subscription_schedule-phases-add_invoice_items) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `discountable` | Added | [InvoiceCreatePreviewParams.schedule_details.phases[].add_invoice_items[]](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-schedule_details-phases-add_invoice_items), [SubscriptionCreateParams.add_invoice_items[]](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription-add_invoice_items), [SubscriptionSchedule.phases[].add_invoice_items[]](/api/subscription_schedules/object?api-version=2026-05-27.dahlia#subscription_schedule_object-phases-add_invoice_items), [SubscriptionScheduleCreateParams.phases[].add_invoice_items[]](/api/subscription_schedules/create?api-version=2026-05-27.dahlia#create_subscription_schedule-phases-add_invoice_items), [SubscriptionScheduleUpdateParams.phases[].add_invoice_items[]](/api/subscription_schedules/update?api-version=2026-05-27.dahlia#update_subscription_schedule-phases-add_invoice_items), [SubscriptionUpdateParams.add_invoice_items[]](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription-add_invoice_items) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `discountable` | Added | [InvoiceCreatePreviewParams.schedule_details.phases[].add_invoice_items[]](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-schedule_details-phases-add_invoice_items), [SubscriptionCreateParams.add_invoice_items[]](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription-add_invoice_items), [SubscriptionSchedule.phases[].add_invoice_items[]](/api/subscription_schedules/object?api-version=2026-05-27.dahlia#subscription_schedule_object-phases-add_invoice_items), [SubscriptionScheduleCreateParams.phases[].add_invoice_items[]](/api/subscription_schedules/create?api-version=2026-05-27.dahlia#create_subscription_schedule-phases-add_invoice_items), [SubscriptionScheduleUpdateParams.phases[].add_invoice_items[]](/api/subscription_schedules/update?api-version=2026-05-27.dahlia#update_subscription_schedule-phases-add_invoice_items), [SubscriptionUpdateParams.add_invoice_items[]](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription-add_invoice_items) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Discountable` | Added | [InvoiceCreatePreviewScheduleDetailsPhaseAddInvoiceItemParams](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-schedule_details-phases-add_invoice_items), [SubscriptionAddInvoiceItemParams](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription-add_invoice_items), [SubscriptionSchedulePhaseAddInvoiceItem](/api/subscription_schedules/object?api-version=2026-05-27.dahlia#subscription_schedule_object-phases-add_invoice_items), [SubscriptionSchedulePhaseAddInvoiceItemParams](/api/subscription_schedules/create?api-version=2026-05-27.dahlia#create_subscription_schedule-phases-add_invoice_items) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Discountable` | Added | [InvoiceScheduleDetailsPhaseAddInvoiceItemOptions](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-schedule_details-phases-add_invoice_items), [SubscriptionAddInvoiceItemOptions](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription-add_invoice_items), [SubscriptionSchedule.Phase.AddInvoiceItem](/api/subscription_schedules/object?api-version=2026-05-27.dahlia#subscription_schedule_object-phases-add_invoice_items), [SubscriptionSchedulePhaseAddInvoiceItemOptions](/api/subscription_schedules/create?api-version=2026-05-27.dahlia#create_subscription_schedule-phases-add_invoice_items) |

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

- [Adds amount paid off Stripe property to Invoice object](https://docs.stripe.com/changelog/dahlia/2026-05-27/invoice-object-amount-paid-off-stripe-property.md)
- [Adds billing schedules to enable prebilling on subscriptions](https://docs.stripe.com/changelog/dahlia/2026-05-27/subscriptions-billing-schedules.md)
- [Adds discount and discounts properties to pending subscription updates](https://docs.stripe.com/changelog/dahlia/2026-05-27/pending-subscription-updates-discount-and-discounts-properties.md)
- [Adds metadata support to pending subscription updates](https://docs.stripe.com/changelog/dahlia/2026-05-27/pending-subscription-update-metadata.md)
- [Adds credited items information to invoice item proration details](https://docs.stripe.com/changelog/dahlia/2026-05-27/invoice-item-proration-credited-items.md)
- [Adds customer parameter to test clock creation](https://docs.stripe.com/changelog/dahlia/2026-05-27/test-clock-creation-customer-parameter.md)
