# Adds support for automatic surcharge calculations on Checkout Sessions

## What’s new

Adds support for automatic surcharge calculations on [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md?api-version=2026-04-22.preview). When you set [automatic_surcharge.enabled](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-04-22.preview#create_checkout_session-automatic_surcharge-enabled) to `true`, Stripe calculates a surcharge after the customer provides their payment details and billing address.

## Impact

You can now collect surcharge fees when using Checkout Sessions. A surcharge is a fee added to a transaction to offset payment processing costs. It’s typically a percentage of the order amount you charge customers when they use certain payment methods (primarily credit cards).

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `automatic_surcharge` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object), [Checkout.Session#create](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session) |
| `surcharge_cost` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object) |
| `amount_surcharge` | Added | [Checkout.Session.total_details](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object-total_details) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `automatic_surcharge` | Added | [Checkout::Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object), [Checkout::SessionCreateParams](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session) |
| `surcharge_cost` | Added | [Checkout::Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object) |
| `amount_surcharge` | Added | [Checkout::Session::TotalDetail](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object-total_details) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `automatic_surcharge` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object), [checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session) |
| `surcharge_cost` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object) |
| `amount_surcharge` | Added | [Checkout.Session.TotalDetail](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object-total_details) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `automatic_surcharge` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object), [Checkout\Session.create().$params](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session) |
| `surcharge_cost` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object) |
| `amount_surcharge` | Added | [Checkout.Session.total_details](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object-total_details) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `automaticSurcharge` | Added | [checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object), [checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session) |
| `surchargeCost` | Added | [checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object) |
| `amountSurcharge` | Added | [checkout.Session.total_details](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object-total_details) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `automatic_surcharge` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object), [Checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session) |
| `surcharge_cost` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object) |
| `amount_surcharge` | Added | [Checkout.Session.total_details](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object-total_details) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AutomaticSurcharge` | Added | [CheckoutSession](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object), [CheckoutSessionParams](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session) |
| `SurchargeCost` | Added | [CheckoutSession](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object) |
| `AmountSurcharge` | Added | [CheckoutSessionTotalDetails](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object-total_details) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AutomaticSurcharge` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object), [Checkout.SessionCreateOptions](/api/checkout/sessions/create?api-version=2026-04-22.preview#create_checkout_session) |
| `SurchargeCost` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object) |
| `AmountSurcharge` | Added | [Checkout.Session.TotalDetails](/api/checkout/sessions/object?api-version=2026-04-22.preview#checkout_session_object-total_details) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-04-22.preview`
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
