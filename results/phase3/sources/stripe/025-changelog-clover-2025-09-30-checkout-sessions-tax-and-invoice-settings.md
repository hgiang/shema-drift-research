# Adds the ability to update automatic tax, invoice creation and invoice settings for Checkout Sessions

## What’s new

Adds the ability to update automatic tax, invoice creation and Invoice settings for Checkout Sessions to address tax liability updates and invoice issuer updates.

## Impact

You can now shift tax liability to and from the Connect platform and connected account for custom Connect Checkout Sessions. This provides flexibility to Connect platforms that are subject to digital marketplace regulations. You can also update the invoice issuer to comply with EU regulations, which require the merchant that’s liable for tax to issue the invoice.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `automatic_tax`, `invoice_creation` | Added | [Checkout.Session#update](/api/checkout/sessions/update?api-version=2025-09-30.preview) |
| `invoice_settings` | Added | [Checkout.Session#update.subscription_data](/api/checkout/sessions/update-subscription_data?api-version=2025-09-30.preview) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `automatic_tax`, `invoice_creation` | Added | [Checkout::Session::UpdateParams](/api/checkout/sessions/update?api-version=2025-09-30.preview) |
| `invoice_settings` | Added | [Checkout::Session::UpdateParams::SubscriptionDatum](/api/checkout/sessions/update-subscription_data?api-version=2025-09-30.preview) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `automatic_tax`, `invoice_creation` | Added | [checkout.Session.ModifyParams](/api/checkout/sessions/update?api-version=2025-09-30.preview) |
| `invoice_settings` | Added | [checkout.Session.ModifyParamsSubscriptionDatum](/api/checkout/sessions/update-subscription_data?api-version=2025-09-30.preview) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `automatic_tax`, `invoice_creation` | Added | [Checkout\Session.update().$params](/api/checkout/sessions/update?api-version=2025-09-30.preview) |
| `invoice_settings` | Added | [Checkout\Session.update().$params.subscription_datum](/api/checkout/sessions/update-subscription_data?api-version=2025-09-30.preview) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `automaticTax`, `invoiceCreation` | Added | [checkout.SessionUpdateParams](/api/checkout/sessions/update?api-version=2025-09-30.preview) |
| `invoiceSettings` | Added | [checkout.SessionUpdateParams.subscription_data](/api/checkout/sessions/update-subscription_data?api-version=2025-09-30.preview) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `automatic_tax`, `invoice_creation` | Added | [Checkout.SessionUpdateParams](/api/checkout/sessions/update?api-version=2025-09-30.preview) |
| `invoice_settings` | Added | [Checkout.SessionUpdateParams.subscription_data](/api/checkout/sessions/update-subscription_data?api-version=2025-09-30.preview) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AutomaticTax`, `InvoiceCreation` | Added | [CheckoutSessionParams](/api/checkout/sessions/update?api-version=2025-09-30.preview) |
| `InvoiceSettings` | Added | [CheckoutSessionSubscriptionDataParams](/api/checkout/sessions/update-subscription_data?api-version=2025-09-30.preview) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AutomaticTax`, `InvoiceCreation` | Added | [Checkout.SessionUpdateOptions](/api/checkout/sessions/update?api-version=2025-09-30.preview) |
| `InvoiceSettings` | Added | [CheckoutSessionSubscriptionDataOptions](/api/checkout/sessions/update-subscription_data?api-version=2025-09-30.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-09-30.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v16.1.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v16.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.1.2b1](https://github.com/stripe/stripe-python/releases/tag/v13.1.2b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.1.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v18.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.1.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v30.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.2.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v19.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.1.0-beta.1](https://github.com/stripe/stripe-go/releases/tag/v83.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.1.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v49.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds pagination and updates fields for aggregated Billing meter usage data](https://docs.stripe.com/changelog/clover/2025-09-30/update-meter-usage-fields.md)
- [Enables prebilling for subscriptions](https://docs.stripe.com/changelog/clover/2025-09-30/subscriptions-prebilling.md)
- [Adds the unit label parameter to the product data hash](https://docs.stripe.com/changelog/clover/2025-09-30/add-product-data-unit-label-preview.md)
