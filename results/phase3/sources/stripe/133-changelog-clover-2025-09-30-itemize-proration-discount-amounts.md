# Adds the ability to itemise proration discount amounts

## What’s new

Adds the ability to itemise proration discount amounts, so proration amounts and discount amounts are displayed consistently with non-prorations. When enabled, the proration [amount](https://docs.stripe.com/api/invoice-line-item/object.md?api-version=2025-09-30.clover#invoice_line_item_object-amount) properties show gross amounts before discounts are applied and [discount amounts](https://docs.stripe.com/api/invoice-line-item/object.md?api-version=2025-09-30.clover#invoice_line_item_object-discount_amounts) include the actual applied discount amounts. When disabled, the proration discount properties include discount IDs, but discount amounts are 0.

## Impact

You can now itemise proration discount amounts by setting the [proration_discounts](https://docs.stripe.com/api/subscriptions/create.md?api-version=2025-09-30.clover#create_subscription-billing_mode-flexible-proration_discounts) parameter to `itemised` when creating subscriptions, subscription schedules, quotes, checkout sessions or preview invoices. You can also set this parameter to `itemised` for an existing subscription by [migrating](https://docs.stripe.com/api/subscriptions/migrate.md?api-version=2025-09-30.clover#migrate_subscription-billing_mode-flexible-proration_discounts) it. However, you can’t migrate a subscription from `itemised` to `included`.

### Changes summary

| Object | Property | Included | Itemised (new behaviour) |
| --- | --- | --- | --- |
| **Proration Line Item** | `amount` | Net amount (after discounts) | Gross amount (before discounts) |
|  | `discount_amounts` | Missing item-level discounts; group-level discounts show `amount=0` | All discounts included with accurate amounts |
| **Invoice Item** | `amount` | Net amount | Gross amount |
|  | `net_amount` (new property) | Net amount for non-discountable invoice items; otherwise null | Net amount for non-discountable invoice items; otherwise null |
|  | `proration_details` (new property) | All discounts included with `amount=0` | All discounts included with accurate amounts |
| **Invoice** | `total_discount_amounts` | Excludes proration discounts | Includes proration discounts |
|  | `subtotal` | Includes net proration amounts (discounts already applied) | Includes proration amounts after item-level discounts (group-level discounts applied separately) |

### Example

10 USD gross debit proration with 10% item-level discount and 2 USD group-level discount

**Included:**

The following example shows the existing behaviour, with discounts already applied:

Response:

```json
// Line Item
{
  "proration": true,
  "amount": 700,  // Net: 7 USD after discounts (10 USD - 1 USD item - 2 USD group)
  "discount_amounts": [
    // Item-level discount missing entirely
    {"amount": 0, "discount": "di_group_2off"}  // Group-level shows ID but no amount
  ]
}

// Invoice Item
{
  "proration": true,
  "amount": 700  // Net amount only
}

// Invoice
{
  "total_discount_amounts": [
    {"amount": 0, "discount": "di_group_2off"}  // Missing item-level proration discount
  ],
  "subtotal": 700  // Adds proration amount after all discounts
}
```

**Itemised:**

Request:

```json
// POST /v1/subscriptions
{
   // ... omitting irrelevant fields ...
   billing_mode: {
      type: "flexible",
      flexible: {  // New parameter: only available when billing mode type is flexible
         proration_discounts: "itemized"  // Default value is "included"
      }
   }
   // ... omitting irrelevant fields ...
}

```

Response:

```json
// Line Item
{
  "proration": true,
  "amount": 1000,  // Gross: 10 USD before discounts
  "discount_amounts": [
    {"amount": 100, "discount": "di_item_10pct"},  // Item-level discount now visible
    {"amount": 200, "discount": "di_group_2off"}   // Group-level with actual amount
  ]
}

// Invoice Item
{
  "proration": true,
  "amount": 1000,         // Gross amount
  "net_amount": 700,      // New property: net amount after both discounts
  "proration_details": {  // New property: populated when the invoice item is a proration
    "discount_amounts": [
      {"amount": 100, "discount": "di_item_10pct"},
      {"amount": 200, "discount": "di_group_2off"}
    ]
  }
}

// Invoice
{
  "total_discount_amounts": [
    {"amount": 100, "discount": "di_item_10pct"},  // Now includes item-level proration discount
    {"amount": 200, "discount": "di_group_2off"}   // Now includes group-level proration discount
  ],
  "subtotal": 900  // Includes proration amount after item-level discounts
}
```

### Upgrade considerations

- **Scope**: This functionality is only available on subscriptions with flexible billing mode.
- **One-way migration**: After you enable itemised discount amounts for a subscription, you can’t revert to included.
- **Code changes required**: If your integration reads proration [amount](https://docs.stripe.com/api/invoiceitems/object.md?api-version=2025-09-30.clover#invoiceitem_object-amount) properties expecting net values, update to use the new [net_amount](https://docs.stripe.com/api/invoiceitems/object.md?api-version=2025-09-30.clover#invoiceitem_object-net_amount) property instead.
- **Historical invoices**: Existing invoices reflect the behaviour that was active when you created them.
- **Mixed invoice support**: Single invoices can contain both included and itemised proration line items if you migrate a subscription between creating prorations.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `flexible` | Added | [Checkout.Session#create.subscription_data.billing_mode](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-subscription_data-billing_mode), [Invoice#create_preview.schedule_details.billing_mode](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-schedule_details-billing_mode), [Invoice#create_preview.subscription_details.billing_mode](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-subscription_details-billing_mode), [Quote#create.subscription_data.billing_mode](/api/quotes/create?api-version=2025-09-30.clover#create_quote-subscription_data-billing_mode), [Quote.subscription_data.billing_mode](/api/quotes/object?api-version=2025-09-30.clover#quote_object-subscription_data-billing_mode), [Subscription#create.billing_mode](/api/subscriptions/create?api-version=2025-09-30.clover#create_subscription-billing_mode), [Subscription#migrate.billing_mode](/api/subscriptions/migrate?api-version=2025-09-30.clover#migrate_subscription-billing_mode), [Subscription.billing_mode](/api/subscriptions/object?api-version=2025-09-30.clover#subscription_object-billing_mode), [SubscriptionSchedule#create.billing_mode](/api/subscription_schedules/create?api-version=2025-09-30.clover#create_subscription_schedule-billing_mode), [SubscriptionSchedule.billing_mode](/api/subscription_schedules/object?api-version=2025-09-30.clover#subscription_schedule_object-billing_mode) |
| `net_amount`, `proration_details` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2025-09-30.clover) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `flexible` | Added | [Checkout::Session::CreateParams::SubscriptionDatum::BillingMode](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-subscription_data-billing_mode), [Invoice::CreatePreviewParams::ScheduleDetail::BillingMode](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-schedule_details-billing_mode), [Invoice::CreatePreviewParams::SubscriptionDetail::BillingMode](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-subscription_details-billing_mode), [Quote::CreateParams::SubscriptionDatum::BillingMode](/api/quotes/create?api-version=2025-09-30.clover#create_quote-subscription_data-billing_mode), [Quote::SubscriptionDatum::BillingMode](/api/quotes/object?api-version=2025-09-30.clover#quote_object-subscription_data-billing_mode), [Subscription::BillingMode](/api/subscriptions/object?api-version=2025-09-30.clover#subscription_object-billing_mode), [Subscription::CreateParams::BillingMode](/api/subscriptions/create?api-version=2025-09-30.clover#create_subscription-billing_mode), [Subscription::MigrateParams::BillingMode](/api/subscriptions/migrate?api-version=2025-09-30.clover#migrate_subscription-billing_mode), [SubscriptionSchedule::BillingMode](/api/subscription_schedules/object?api-version=2025-09-30.clover#subscription_schedule_object-billing_mode), [SubscriptionSchedule::CreateParams::BillingMode](/api/subscription_schedules/create?api-version=2025-09-30.clover#create_subscription_schedule-billing_mode) |
| `net_amount`, `proration_details` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2025-09-30.clover) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `flexible` | Added | [Invoice.CreatePreviewParamsScheduleDetailBillingMode](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-schedule_details-billing_mode), [Invoice.CreatePreviewParamsSubscriptionDetailBillingMode](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-subscription_details-billing_mode), [Quote.CreateParamsSubscriptionDatumBillingMode](/api/quotes/create?api-version=2025-09-30.clover#create_quote-subscription_data-billing_mode), [Quote.SubscriptionDatum.BillingMode](/api/quotes/object?api-version=2025-09-30.clover#quote_object-subscription_data-billing_mode), [Subscription.BillingMode](/api/subscriptions/object?api-version=2025-09-30.clover#subscription_object-billing_mode), [Subscription.CreateParamsBillingMode](/api/subscriptions/create?api-version=2025-09-30.clover#create_subscription-billing_mode), [Subscription.MigrateParamsBillingMode](/api/subscriptions/migrate?api-version=2025-09-30.clover#migrate_subscription-billing_mode), [SubscriptionSchedule.BillingMode](/api/subscription_schedules/object?api-version=2025-09-30.clover#subscription_schedule_object-billing_mode), [SubscriptionSchedule.CreateParamsBillingMode](/api/subscription_schedules/create?api-version=2025-09-30.clover#create_subscription_schedule-billing_mode), [checkout.Session.CreateParamsSubscriptionDatumBillingMode](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-subscription_data-billing_mode) |
| `net_amount`, `proration_details` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2025-09-30.clover) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `flexible` | Added | [Checkout\Session.create().$params.subscription_datum.billing_mode](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-subscription_data-billing_mode), [Invoice.create_preview().$params.schedule_detail.billing_mode](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-schedule_details-billing_mode), [Invoice.create_preview().$params.subscription_detail.billing_mode](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-subscription_details-billing_mode), [Quote.create().$params.subscription_datum.billing_mode](/api/quotes/create?api-version=2025-09-30.clover#create_quote-subscription_data-billing_mode), [Quote.subscription_data.billing_mode](/api/quotes/object?api-version=2025-09-30.clover#quote_object-subscription_data-billing_mode), [Subscription.billing_mode](/api/subscriptions/object?api-version=2025-09-30.clover#subscription_object-billing_mode), [Subscription.create().$params.billing_mode](/api/subscriptions/create?api-version=2025-09-30.clover#create_subscription-billing_mode), [Subscription.migrate().$params.billing_mode](/api/subscriptions/migrate?api-version=2025-09-30.clover#migrate_subscription-billing_mode), [SubscriptionSchedule.billing_mode](/api/subscription_schedules/object?api-version=2025-09-30.clover#subscription_schedule_object-billing_mode), [SubscriptionSchedule.create().$params.billing_mode](/api/subscription_schedules/create?api-version=2025-09-30.clover#create_subscription_schedule-billing_mode) |
| `net_amount`, `proration_details` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2025-09-30.clover) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `flexible` | Added | [InvoiceCreatePreviewParams.schedule_details.billing_mode](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-schedule_details-billing_mode), [InvoiceCreatePreviewParams.subscription_details.billing_mode](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-subscription_details-billing_mode), [Quote.subscription_data.billing_mode](/api/quotes/object?api-version=2025-09-30.clover#quote_object-subscription_data-billing_mode), [QuoteCreateParams.subscription_data.billing_mode](/api/quotes/create?api-version=2025-09-30.clover#create_quote-subscription_data-billing_mode), [Subscription.billing_mode](/api/subscriptions/object?api-version=2025-09-30.clover#subscription_object-billing_mode), [SubscriptionCreateParams.billing_mode](/api/subscriptions/create?api-version=2025-09-30.clover#create_subscription-billing_mode), [SubscriptionMigrateParams.billing_mode](/api/subscriptions/migrate?api-version=2025-09-30.clover#migrate_subscription-billing_mode), [SubscriptionSchedule.billing_mode](/api/subscription_schedules/object?api-version=2025-09-30.clover#subscription_schedule_object-billing_mode), [SubscriptionScheduleCreateParams.billing_mode](/api/subscription_schedules/create?api-version=2025-09-30.clover#create_subscription_schedule-billing_mode), [checkout.SessionCreateParams.subscription_data.billing_mode](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-subscription_data-billing_mode) |
| `netAmount`, `prorationDetails` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2025-09-30.clover) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `flexible` | Added | [Checkout.SessionCreateParams.subscription_data.billing_mode](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-subscription_data-billing_mode), [InvoiceCreatePreviewParams.schedule_details.billing_mode](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-schedule_details-billing_mode), [InvoiceCreatePreviewParams.subscription_details.billing_mode](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-subscription_details-billing_mode), [Quote.subscription_data.billing_mode](/api/quotes/object?api-version=2025-09-30.clover#quote_object-subscription_data-billing_mode), [QuoteCreateParams.subscription_data.billing_mode](/api/quotes/create?api-version=2025-09-30.clover#create_quote-subscription_data-billing_mode), [Subscription.billing_mode](/api/subscriptions/object?api-version=2025-09-30.clover#subscription_object-billing_mode), [SubscriptionCreateParams.billing_mode](/api/subscriptions/create?api-version=2025-09-30.clover#create_subscription-billing_mode), [SubscriptionMigrateParams.billing_mode](/api/subscriptions/migrate?api-version=2025-09-30.clover#migrate_subscription-billing_mode), [SubscriptionSchedule.billing_mode](/api/subscription_schedules/object?api-version=2025-09-30.clover#subscription_schedule_object-billing_mode), [SubscriptionScheduleCreateParams.billing_mode](/api/subscription_schedules/create?api-version=2025-09-30.clover#create_subscription_schedule-billing_mode) |
| `net_amount`, `proration_details` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2025-09-30.clover) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Flexible` | Added | [CheckoutSessionSubscriptionDataBillingModeParams](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-subscription_data-billing_mode), [InvoiceCreatePreviewScheduleDetailsBillingModeParams](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-schedule_details-billing_mode), [InvoiceCreatePreviewSubscriptionDetailsBillingModeParams](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-subscription_details-billing_mode), [QuoteSubscriptionDataBillingMode](/api/quotes/object?api-version=2025-09-30.clover#quote_object-subscription_data-billing_mode), [QuoteSubscriptionDataBillingModeParams](/api/quotes/create?api-version=2025-09-30.clover#create_quote-subscription_data-billing_mode), [SubscriptionBillingMode](/api/subscriptions/object?api-version=2025-09-30.clover#subscription_object-billing_mode), [SubscriptionBillingModeParams](/api/subscriptions/create?api-version=2025-09-30.clover#create_subscription-billing_mode), [SubscriptionMigrateBillingModeParams](/api/subscriptions/migrate?api-version=2025-09-30.clover#migrate_subscription-billing_mode), [SubscriptionScheduleBillingMode](/api/subscription_schedules/object?api-version=2025-09-30.clover#subscription_schedule_object-billing_mode), [SubscriptionScheduleBillingModeParams](/api/subscription_schedules/create?api-version=2025-09-30.clover#create_subscription_schedule-billing_mode) |
| `NetAmount`, `ProrationDetails` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2025-09-30.clover) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Flexible` | Added | [CheckoutSessionSubscriptionDataBillingModeOptions](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-subscription_data-billing_mode), [InvoiceScheduleDetailsBillingModeOptions](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-schedule_details-billing_mode), [InvoiceSubscriptionDetailsBillingModeOptions](/api/invoices/create_preview?api-version=2025-09-30.clover#create_invoice-subscription_details-billing_mode), [Quote.SubscriptionData.BillingMode](/api/quotes/object?api-version=2025-09-30.clover#quote_object-subscription_data-billing_mode), [QuoteSubscriptionDataBillingModeOptions](/api/quotes/create?api-version=2025-09-30.clover#create_quote-subscription_data-billing_mode), [Subscription.BillingMode](/api/subscriptions/object?api-version=2025-09-30.clover#subscription_object-billing_mode), [SubscriptionBillingModeOptions](/api/subscriptions/create?api-version=2025-09-30.clover#create_subscription-billing_mode), [SubscriptionSchedule.BillingMode](/api/subscription_schedules/object?api-version=2025-09-30.clover#subscription_schedule_object-billing_mode), [SubscriptionScheduleBillingModeOptions](/api/subscription_schedules/create?api-version=2025-09-30.clover#create_subscription_schedule-billing_mode) |
| `NetAmount`, `ProrationDetails` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2025-09-30.clover) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-09-30.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v16.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.0.1](https://github.com/stripe/stripe-python/releases/tag/v13.0.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.0.0](https://github.com/stripe/stripe-php/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.0.0](https://github.com/stripe/stripe-java/releases/tag/v30.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.1.0](https://github.com/stripe/stripe-node/releases/tag/v19.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.0.0](https://github.com/stripe/stripe-go/releases/tag/v83.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Removes iterations parameter for subscription schedules](https://docs.stripe.com/changelog/clover/2025-09-30/remove-iterations.md)
- [Promotion Codes now reference Coupons using a polymorphic field for promotions](https://docs.stripe.com/changelog/clover/2025-09-30/polymorphic-coupon.md)
- [Adds the Discount source property and removes the Discount coupon property](https://docs.stripe.com/changelog/clover/2025-09-30/add-discount-source-property.md)
- [Makes flexible billing mode the default for new subscriptions](https://docs.stripe.com/changelog/clover/2025-09-30/billing-mode-default-flexible.md)
- [Updates computation of subscription schedule phase end date to consider billing cycle anchor changes](https://docs.stripe.com/changelog/clover/2025-09-30/billing-cycle-anchor-resets-during-phase-computation.md)
- [Adds customer portal configuration trial behaviour](https://docs.stripe.com/changelog/clover/2025-09-30/customer-portal-trial-behavior.md)
