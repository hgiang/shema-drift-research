# Adds third-party tax providers for automatic tax calculation

## What’s new

Adds the [automatic_tax.provider](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-10-29.clover#checkout_session_object-automatic_tax-provider) property to identify the tax calculation provider that Stripe used for a given [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md?api-version=2025-10-29.clover), [Invoice](https://docs.stripe.com/api/invoices/object.md?api-version=2025-10-29.clover) or [Quote](https://docs.stripe.com/api/quotes/object.md?api-version=2025-10-29.clover).

## Impact

You can now use third-party tax providers to natively calculate tax across all automatic tax integrations. Install the required [third-party tax application](https://marketplace.stripe.com/categories/tax), then enable it in your [automatic tax settings](https://dashboard.stripe.com/settings/tax/integrations). Learn more about [third-party tax applications](https://docs.stripe.com/tax/third-party-apps.md).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `provider` | Added | `Checkout.Session.automatic_tax`, [Invoice.automatic_tax](/api/invoices/object?api-version=2025-10-29.clover#invoice_object-automatic_tax), `Quote.automatic_tax` |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `provider` | Added | `CheckoutSession::AutomaticTax`, `Invoice::AutomaticTax`, `Quote::AutomaticTax` |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `provider` | Added | `CheckoutSession.AutomaticTax`, `Invoice.AutomaticTax`, `Quote.AutomaticTax` |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `provider` | Added | `Checkout.Session.automatic_tax`, [Invoice.automatic_tax](/api/invoices/object?api-version=2025-10-29.clover#invoice_object-automatic_tax), `Quote.automatic_tax` |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `provider` | Added | `Checkout.Session.automatic_tax`, [Invoice.automatic_tax](/api/invoices/object?api-version=2025-10-29.clover#invoice_object-automatic_tax), `Quote.automatic_tax` |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Provider` | Added | `CheckoutSessionAutomaticTax`, [InvoiceAutomaticTax](/api/invoices/object?api-version=2025-10-29.clover#invoice_object-automatic_tax), `QuoteAutomaticTax` |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Provider` | Added | `CheckoutSessionAutomaticTax`, [InvoiceAutomaticTax](/api/invoices/object?api-version=2025-10-29.clover#invoice_object-automatic_tax), `QuoteAutomaticTax` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-10-29.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v17.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v17.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.1.0](https://github.com/stripe/stripe-python/releases/tag/v13.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.1.0](https://github.com/stripe/stripe-php/releases/tag/v18.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.1.0](https://github.com/stripe/stripe-java/releases/tag/v30.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.2.0](https://github.com/stripe/stripe-node/releases/tag/v19.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.1.0](https://github.com/stripe/stripe-go/releases/tag/v83.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds support for remote sellers in Taiwan to Stripe Tax](https://docs.stripe.com/changelog/clover/2025-10-29/stripe-tax-taiwan-remote-support.md)
