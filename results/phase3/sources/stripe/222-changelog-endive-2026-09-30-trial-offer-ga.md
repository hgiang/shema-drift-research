# Makes trial offers generally available

## What’s new

Adds [Trial Offers](https://docs.stripe.com/api/product-catalog/trial-offer.md?api-version=2026-09-30.endive) for subscriptions, which define reusable free or paid introductory pricing for individual [Subscription Items](https://docs.stripe.com/api/subscription_items.md?api-version=2026-09-30.endive), each with their own price and billing period. Previously, a subscription used a single trial period for the entire subscription.

A Trial Offer specifies the recurring [price](https://docs.stripe.com/api/product-catalog/trial-offer/object.md?api-version=2026-09-30.endive#product_catalog_trial_offer_object-price) to charge during the trial, the number of billing intervals that the trial lasts, and the [post-trial price](https://docs.stripe.com/api/product-catalog/trial-offer/object.md?api-version=2026-09-30.endive#product_catalog_trial_offer_object-end_behavior-transition-price) to use when the trial ends. Because Trial Offers define the trial price, they support both free and paid trialing periods. When the trial ends, we automatically change the Subscription Item to the configured post-trial price.

You can apply a trial offer when:

- You [create](https://docs.stripe.com/api/subscriptions/create.md?api-version=2026-09-30.endive) a Subscription
- Add one to an existing Subscription Item
- Replace an item’s existing trial offer

A subscription can contain both trial and non-trial items, each with its own price and billing period. This lets you offer a trial for an add-on or premium product without changing the billing behaviour of the subscription’s other items.

Trial offers are reusable across multiple subscriptions. You can’t change their pricing and duration after creation. [Archiving an offer](https://docs.stripe.com/api/product-catalog/trial-offer/object.md?api-version=2026-09-30.endive#product_catalog_trial_offer_object-active) prevents it from being used for new subscription items, and doesn’t affect trials already in progress.

When a trial ends, you can configure whether Stripe [sends an invoice, cancels or pauses the subscription](https://docs.stripe.com/api/subscriptions/object.md?api-version=2026-09-30.endive#subscription_object-trial_settings-end_behavior-missing_payment_method) if the customer has no payment method. You can also configure whether the subscription’s [billing cycle anchor](https://docs.stripe.com/api/subscriptions/create.md?api-version=2026-09-30.endive#create_subscription-trial_settings-end_behavior-billing_cycle_anchor) resets when a trial offer ends.

Trial offers provide [subscription events](https://docs.stripe.com/billing/subscriptions/webhooks.md) to communicate trial timing. We send `customer.subscription.trial_will_end` before each trial offer ends and `customer.subscription.updated` when an item’s price transitions at the end of a trial.

Trial offers are only supported by subscriptions in [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md) and can’t be combined with legacy subscription-level free trials.

For setup guidance, supported workflows and limitations, see our guide to [configuring trial offers on subscriptions](https://docs.stripe.com/billing/subscriptions/trials.md).

## Impact

You can now use trial offers to establish an introductory pricing model. Previously, free trials for Subscriptions applied the same trial period to the entire subscription.

For example, you can now bill a customer for a base subscription, while also:

- Offering a free trial for an add-on
- Charging a discounted price for the first few billing intervals
- Letting a customer try a premium product at an introductory price before automatically moving them to the standard price

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [ProductCatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Endpoints | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve`, `update` | Added | [ProductCatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `current_trial` | Added | [Invoice#create_preview.subscription_details.items[]](/api/invoices/create_preview?api-version=2026-09-30.endive#create_invoice-subscription_details-items), [Subscription#create.items[]](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-items), [Subscription#update.items[]](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-items), [SubscriptionItem](/api/subscription_items/object?api-version=2026-09-30.endive#subscription_item_object), [SubscriptionItem#create](/api/subscription_items/create?api-version=2026-09-30.endive#create_subscription_item), [SubscriptionItem#update](/api/subscription_items/update?api-version=2026-09-30.endive#update_subscription_item) |
| `billing_cycle_anchor` | Added | [Subscription#create.trial_settings.end_behavior](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-trial_settings-end_behavior), [Subscription#update.trial_settings.end_behavior](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-trial_settings-end_behavior), [Subscription.trial_settings.end_behavior](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-trial_settings-end_behavior) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Subscription#create.trial_settings.end_behavior.missing_payment_method`, `Subscription#update.trial_settings.end_behavior.missing_payment_method` | Changed | `required → optional` |

#### Ruby

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [ProductCatalog::TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve`, `update` | Added | [ProductCatalog::TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `current_trial` | Added | [InvoiceCreatePreviewParams::SubscriptionDetail::Item](/api/invoices/create_preview?api-version=2026-09-30.endive#create_invoice-subscription_details-items), [SubscriptionCreateParams::Item](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-items), [SubscriptionItem](/api/subscription_items/object?api-version=2026-09-30.endive#subscription_item_object), [SubscriptionItemCreateParams](/api/subscription_items/create?api-version=2026-09-30.endive#create_subscription_item), [SubscriptionItemUpdateParams](/api/subscription_items/update?api-version=2026-09-30.endive#update_subscription_item), [SubscriptionUpdateParams::Item](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-items) |
| `billing_cycle_anchor` | Added | [Subscription::TrialSetting::EndBehavior](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-trial_settings-end_behavior), [SubscriptionCreateParams::TrialSetting::EndBehavior](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-trial_settings-end_behavior), [SubscriptionUpdateParams::TrialSetting::EndBehavior](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-trial_settings-end_behavior) |

| Fields | Change | From → to |
| --- | --- | --- |
| `SubscriptionCreateParams::TrialSetting::EndBehavior.missing_payment_method`, `SubscriptionUpdateParams::TrialSetting::EndBehavior.missing_payment_method` | Changed | `required → optional` |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [product_catalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `modify`, `retrieve` | Added | [product_catalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `current_trial` | Added | [InvoiceCreatePreviewParamsSubscriptionDetailItem](/api/invoices/create_preview?api-version=2026-09-30.endive#create_invoice-subscription_details-items), [SubscriptionCreateParamsItem](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-items), [SubscriptionItem](/api/subscription_items/object?api-version=2026-09-30.endive#subscription_item_object), [SubscriptionItemCreateParams](/api/subscription_items/create?api-version=2026-09-30.endive#create_subscription_item), [SubscriptionItemModifyParams](/api/subscription_items/update?api-version=2026-09-30.endive#update_subscription_item), [SubscriptionModifyParamsItem](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-items) |
| `billing_cycle_anchor` | Added | [Subscription.TrialSetting.EndBehavior](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-trial_settings-end_behavior), [SubscriptionCreateParamsTrialSettingEndBehavior](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-trial_settings-end_behavior), [SubscriptionModifyParamsTrialSettingEndBehavior](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-trial_settings-end_behavior) |

| Fields | Change | From → to |
| --- | --- | --- |
| `SubscriptionCreateParamsTrialSettingEndBehavior.missing_payment_method`, `SubscriptionModifyParamsTrialSettingEndBehavior.missing_payment_method` | Changed | `required → optional` |

#### PHP

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [ProductCatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `all`, `create`, `retrieve`, `update` | Added | [ProductCatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `current_trial` | Added | [Invoice.create_preview().$params.subscription_detail.item](/api/invoices/create_preview?api-version=2026-09-30.endive#create_invoice-subscription_details-items), [Subscription.create().$params.item](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-items), [Subscription.update().$params.item](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-items), [SubscriptionItem](/api/subscription_items/object?api-version=2026-09-30.endive#subscription_item_object), [SubscriptionItem.create().$params](/api/subscription_items/create?api-version=2026-09-30.endive#create_subscription_item), [SubscriptionItem.update().$params](/api/subscription_items/update?api-version=2026-09-30.endive#update_subscription_item) |
| `billing_cycle_anchor` | Added | [Subscription.create().$params.trial_setting.end_behavior](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-trial_settings-end_behavior), [Subscription.trial_settings.end_behavior](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-trial_settings-end_behavior), [Subscription.update().$params.trial_setting.end_behavior](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-trial_settings-end_behavior) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Subscription.create().$params.trial_setting.end_behavior.missing_payment_method`, `Subscription.update().$params.trial_setting.end_behavior.missing_payment_method` | Changed | `required → optional` |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [productcatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve`, `update` | Added | [productcatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `currentTrial` | Added | [InvoiceCreatePreviewParams.subscription_details.items[]](/api/invoices/create_preview?api-version=2026-09-30.endive#create_invoice-subscription_details-items), [SubscriptionCreateParams.items[]](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-items), [SubscriptionItem](/api/subscription_items/object?api-version=2026-09-30.endive#subscription_item_object), [SubscriptionItemCreateParams](/api/subscription_items/create?api-version=2026-09-30.endive#create_subscription_item), [SubscriptionItemUpdateParams](/api/subscription_items/update?api-version=2026-09-30.endive#update_subscription_item), [SubscriptionUpdateParams.items[]](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-items) |
| `billingCycleAnchor` | Added | [Subscription.trial_settings.end_behavior](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-trial_settings-end_behavior), [SubscriptionCreateParams.trial_settings.end_behavior](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-trial_settings-end_behavior), [SubscriptionUpdateParams.trial_settings.end_behavior](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-trial_settings-end_behavior) |

| Fields | Change | From → to |
| --- | --- | --- |
| `SubscriptionCreateParams.trial_settings.end_behavior.missingPaymentMethod`, `SubscriptionUpdateParams.trial_settings.end_behavior.missingPaymentMethod` | Changed | `required → optional` |

#### Node.js

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [ProductCatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve`, `update` | Added | [ProductCatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `current_trial` | Added | [InvoiceCreatePreviewParams.subscription_details.items[]](/api/invoices/create_preview?api-version=2026-09-30.endive#create_invoice-subscription_details-items), [SubscriptionCreateParams.items[]](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-items), [SubscriptionItem](/api/subscription_items/object?api-version=2026-09-30.endive#subscription_item_object), [SubscriptionItemCreateParams](/api/subscription_items/create?api-version=2026-09-30.endive#create_subscription_item), [SubscriptionItemUpdateParams](/api/subscription_items/update?api-version=2026-09-30.endive#update_subscription_item), [SubscriptionUpdateParams.items[]](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-items) |
| `billing_cycle_anchor` | Added | [Subscription.trial_settings.end_behavior](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-trial_settings-end_behavior), [SubscriptionCreateParams.trial_settings.end_behavior](/api/subscriptions/create?api-version=2026-09-30.endive#create_subscription-trial_settings-end_behavior), [SubscriptionUpdateParams.trial_settings.end_behavior](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-trial_settings-end_behavior) |

| Fields | Change | From → to |
| --- | --- | --- |
| `SubscriptionCreateParams.trial_settings.end_behavior.missing_payment_method`, `SubscriptionUpdateParams.trial_settings.end_behavior.missing_payment_method` | Changed | `required → optional` |

#### Go

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [ProductCatalogTrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Get`, `List`, `New`, `Update` | Added | [ProductCatalogTrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CurrentTrial` | Added | [InvoiceCreatePreviewSubscriptionDetailsItemParams](/api/invoices/create_preview?api-version=2026-09-30.endive#create_invoice-subscription_details-items), [SubscriptionItem](/api/subscription_items/object?api-version=2026-09-30.endive#subscription_item_object), [SubscriptionItemParams](/api/subscription_items/update?api-version=2026-09-30.endive#update_subscription_item) |
| `BillingCycleAnchor` | Added | [SubscriptionTrialSettingsEndBehavior](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-trial_settings-end_behavior), [SubscriptionTrialSettingsEndBehaviorParams](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-trial_settings-end_behavior) |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [ProductCatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Create`, `Get`, `List`, `Update` | Added | [ProductCatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-09-30.endive#product_catalog_trial_offer_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CurrentTrial` | Added | [InvoiceSubscriptionDetailsItemOptions](/api/invoices/create_preview?api-version=2026-09-30.endive#create_invoice-subscription_details-items), [SubscriptionItem](/api/subscription_items/object?api-version=2026-09-30.endive#subscription_item_object), [SubscriptionItemCreateOptions](/api/subscription_items/create?api-version=2026-09-30.endive#create_subscription_item), [SubscriptionItemOptions](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-items), [SubscriptionItemUpdateOptions](/api/subscription_items/update?api-version=2026-09-30.endive#update_subscription_item) |
| `BillingCycleAnchor` | Added | [Subscription.TrialSettings.EndBehavior](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-trial_settings-end_behavior), [SubscriptionTrialSettingsEndBehaviorOptions](/api/subscriptions/update?api-version=2026-09-30.endive#update_subscription-trial_settings-end_behavior) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.endive`
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

- [Unifies the billing cycle anchor format across Subscriptions and Invoices](https://docs.stripe.com/changelog/endive/2026-09-30/polymorphic-billing-cycle-anchor.md)
- [Adds invoicing rules to Invoice Items](https://docs.stripe.com/changelog/endive/2026-09-30/invoicing-rules-for-invoice-items.md)
- [Adds reference and company details parameters for Billie](https://docs.stripe.com/changelog/endive/2026-09-30/reference-and-company-details-billie.md)
- [Adds the ability to clear invoicing rules on Invoice Items](https://docs.stripe.com/changelog/endive/2026-09-30/clear-invoicing-rules-on-invoice-items.md)
- [Adds proration details for Invoice Items using classic billing mode](https://docs.stripe.com/changelog/endive/2026-09-30/invoice-items-proration-details.md)
- [Adds detailed status to explain why an invoice is uncollectible](https://docs.stripe.com/changelog/endive/2026-09-30/invoice-uncollectible-status-detail.md)
- [Adds support for scheduling Subscription cancellation as part of pending update](https://docs.stripe.com/changelog/endive/2026-09-30/scheduled-subscription-cancellation.md)
- [Adds the ability to pause and resume Subscriptions on demand](https://docs.stripe.com/changelog/endive/2026-09-30/pause-subscription.md)
- [Adds the Feedback Options API](https://docs.stripe.com/changelog/endive/2026-09-30/feedback-options-api.md)
