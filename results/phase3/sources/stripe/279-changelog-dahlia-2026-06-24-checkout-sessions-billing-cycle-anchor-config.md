# Makes billing cycle anchor configuration available for Checkout Sessions in subscription mode

## What’s new

Makes the [billing_cycle_anchor_config](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-06-24.dahlia#create_checkout_session-subscription_data-billing_cycle_anchor_config) parameter available in the [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md?api-version=2026-06-24.dahlia) API.

The parameter accepts a required `day_of_month` property and optional `hour`, `minute`, `month` and `second` properties to precisely control when the billing cycle resets. `billing_cycle_anchor_config` is mutually exclusive with `billing_cycle_anchor` and any trial period parameters.

## Impact

You can now set a fixed billing cycle anchor date when creating a [subscription mode](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-06-24.dahlia#create_checkout_session-mode) Checkout Session. If you want all subscribers who sign up through a Checkout Session to be billed on the same calendar date (for example, the 1st of every month) set `subscription_data[billing_cycle_anchor_config][day_of_month]` to that day when you create the session. See the [billing cycle anchor documentation](https://docs.stripe.com/billing/subscriptions/billing-cycle.md) for more details about how anchor dates affect proration and invoice timing.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `billing_cycle_anchor_config` | Added | [Checkout.Session#create.subscription_data](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-subscription_data) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billing_cycle_anchor_config` | Added | [Checkout::SessionCreateParams::SubscriptionDatum](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-subscription_data) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billing_cycle_anchor_config` | Added | [checkout.SessionCreateParamsSubscriptionDatum](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-subscription_data) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billing_cycle_anchor_config` | Added | [Checkout\Session.create().$params.subscription_datum](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-subscription_data) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billingCycleAnchorConfig` | Added | [checkout.SessionCreateParams.subscription_data](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-subscription_data) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `billing_cycle_anchor_config` | Added | [Checkout.SessionCreateParams.subscription_data](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-subscription_data) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `BillingCycleAnchorConfig` | Added | [CheckoutSessionSubscriptionDataParams](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-subscription_data) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `BillingCycleAnchorConfig` | Added | [CheckoutSessionSubscriptionDataOptions](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-subscription_data) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-06-24.dahlia`
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

- [Adds WeChat Pay payment method options to the Checkout Session response](https://docs.stripe.com/changelog/dahlia/2026-06-24/checkout-session-response-wechat-pay-payment-method-options.md)
