# Adds support for requiring a customer tax ID on Checkout and Payment Links

## What’s new

Adds support for requiring a customer tax ID on `Checkout.Session` and `PaymentLink` using the new `tax_id_collection[required]` parameter. When this parameter is set to `if_supported`, customers paying from a country where tax ID [collection is supported](https://docs.stripe.com/tax/checkout/tax-ids.md#supported-types) will be required to provide their tax ID information as part of the payment.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `required` | Added | [Checkout.Session#create.tax_id_collection](/api/checkout/sessions/create?api-version=2024-09-30.acacia#create_checkout_session-tax_id_collection), [Checkout.Session.tax_id_collection](/api/checkout/sessions/object?api-version=2024-09-30.acacia#checkout_session_object-tax_id_collection), [PaymentLink#create.tax_id_collection](/api/payment-link/create?api-version=2024-09-30.acacia#create_payment_link-tax_id_collection), [PaymentLink#update.tax_id_collection](/api/payment-link/update?api-version=2024-09-30.acacia#update_payment_link-tax_id_collection), [PaymentLink.tax_id_collection](/api/payment-link/object?api-version=2024-09-30.acacia#payment_link_object-tax_id_collection) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `required` | Added | [stripe.PaymentLink.CreateParamsTaxIdCollection](/api/payment-link/create?api-version=2024-09-30.acacia#create_payment_link-tax_id_collection), [stripe.PaymentLink.ModifyParamsTaxIdCollection](/api/payment-link/update?api-version=2024-09-30.acacia#update_payment_link-tax_id_collection), [stripe.checkout.Session.CreateParamsTaxIdCollection](/api/checkout/sessions/create?api-version=2024-09-30.acacia#create_checkout_session-tax_id_collection), [stripe.PaymentLink.TaxIdCollection](/api/payment-link/object?api-version=2024-09-30.acacia#payment_link_object-tax_id_collection), [stripe.checkout.Session.TaxIdCollection](/api/checkout/sessions/object?api-version=2024-09-30.acacia#checkout_session_object-tax_id_collection) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `required` | Added | [Checkout.Session.tax_id_collection](/api/checkout/sessions/object?api-version=2024-09-30.acacia#checkout_session_object-tax_id_collection), [PaymentLink.tax_id_collection](/api/payment-link/object?api-version=2024-09-30.acacia#payment_link_object-tax_id_collection), [PaymentLinkCreateParams.tax_id_collection](/api/payment-link/create?api-version=2024-09-30.acacia#create_payment_link-tax_id_collection), [PaymentLinkUpdateParams.tax_id_collection](/api/payment-link/update?api-version=2024-09-30.acacia#update_payment_link-tax_id_collection), [checkout.SessionCreateParams.tax_id_collection](/api/checkout/sessions/create?api-version=2024-09-30.acacia#create_checkout_session-tax_id_collection) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `required` | Added | [Checkout.Session.tax_id_collection](/api/checkout/sessions/object?api-version=2024-09-30.acacia#checkout_session_object-tax_id_collection), [Checkout.SessionCreateParams.tax_id_collection](/api/checkout/sessions/create?api-version=2024-09-30.acacia#create_checkout_session-tax_id_collection), [PaymentLink.tax_id_collection](/api/payment-link/object?api-version=2024-09-30.acacia#payment_link_object-tax_id_collection), [PaymentLinkCreateParams.tax_id_collection](/api/payment-link/create?api-version=2024-09-30.acacia#create_payment_link-tax_id_collection), [PaymentLinkUpdateParams.tax_id_collection](/api/payment-link/update?api-version=2024-09-30.acacia#update_payment_link-tax_id_collection) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Required` | Added | [CheckoutSessionTaxIdCollectionParams](/api/checkout/sessions/create?api-version=2024-09-30.acacia#create_checkout_session-tax_id_collection), [CheckoutSessionTaxIdCollection](/api/checkout/sessions/object?api-version=2024-09-30.acacia#checkout_session_object-tax_id_collection), [PaymentLinkTaxIdCollectionParams](/api/payment-link/create?api-version=2024-09-30.acacia#create_payment_link-tax_id_collection), [PaymentLinkTaxIdCollection](/api/payment-link/object?api-version=2024-09-30.acacia#payment_link_object-tax_id_collection) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Required` | Added | [CheckoutSessionTaxIdCollectionOptions](/api/checkout/sessions/create?api-version=2024-09-30.acacia#create_checkout_session-tax_id_collection), [CheckoutSessionTaxIdCollection](/api/checkout/sessions/object?api-version=2024-09-30.acacia#checkout_session_object-tax_id_collection), [PaymentLinkTaxIdCollectionOptions](/api/payment-link/update?api-version=2024-09-30.acacia#update_payment_link-tax_id_collection), [PaymentLinkTaxIdCollection](/api/payment-link/object?api-version=2024-09-30.acacia#payment_link_object-tax_id_collection) |

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

## Related changes

- [Adds Switzerland UID as a supported customer tax ID](https://docs.stripe.com/changelog/acacia/2024-09-30/switzerland-tax-uid.md)
- [Adds Croatian Personal Identification Number to supported Tax IDs](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-tax-id-type-hr_oib-croatian-personal-id-number.md)
