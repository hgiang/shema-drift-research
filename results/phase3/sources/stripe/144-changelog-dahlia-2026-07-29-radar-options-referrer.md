# Adds a referrer parameter to Radar options on Payment Intents

## What’s new

Adds an optional [referrer](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-07-29.dahlia#create_payment_intent-radar_options-referrer) parameter to [radar_options](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-07-29.dahlia#create_payment_intent-radar_options) when you [create](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-07-29.dahlia) or [confirm](https://docs.stripe.com/api/payment_intents/confirm.md?api-version=2026-07-29.dahlia) a PaymentIntent. This parameter accepts the referrer URL of the current Checkout Session and provides it to [Radar](https://docs.stripe.com/radar.md) and Supportability for risk evaluation. The referrer parameter is request-only and doesn’t appear in the PaymentIntent response or webhook events. It acts as a fallback, so if a referrer is already available from a [Radar Session](https://docs.stripe.com/radar/radar-session.md) or another source, the value you pass in [radar_options.referrer](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-07-29.dahlia#create_payment_intent-radar_options-referrer) doesn’t override it.

## Impact

You can now supply per-transaction referrer data directly on PaymentIntent creation or confirmation for [Radar](https://docs.stripe.com/radar.md) and Supportability risk evaluation. Use [Radar Sessions](https://docs.stripe.com/radar/radar-session.md) to collect complete browser and device information. Use [radar_options.referrer](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-07-29.dahlia#create_payment_intent-radar_options-referrer) when a Radar Session is unavailable or doesn’t contain a referrer. If your integration previously relied on the deprecated Risk Metadata API to pass referrer information, you can use this parameter instead.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `referrer` | Added | [PaymentIntent#create.radar_options](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-radar_options), [PaymentIntent#confirm.radar_options](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-radar_options) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `referrer` | Added | [PaymentIntentCreateParams::RadarOptions](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-radar_options), [PaymentIntentConfirmParams::RadarOptions](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-radar_options) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `referrer` | Added | [PaymentIntentCreateParamsRadarOptions](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-radar_options), [PaymentIntentConfirmParamsRadarOptions](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-radar_options) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `referrer` | Added | [PaymentIntent.create().$params.radar_options](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-radar_options), [PaymentIntent.confirm().$params.radar_options](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-radar_options) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `referrer` | Added | [PaymentIntentCreateParams.radar_options](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-radar_options), [PaymentIntentConfirmParams.radar_options](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-radar_options) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `referrer` | Added | [PaymentIntentCreateParams.radar_options](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-radar_options), [PaymentIntentConfirmParams.radar_options](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-radar_options) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Referrer` | Added | [PaymentIntentParams.RadarOptions](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-radar_options), [PaymentIntentConfirmParams.RadarOptions](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-radar_options) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Referrer` | Added | [PaymentIntentCreateOptions.RadarOptions](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-radar_options), [PaymentIntentConfirmOptions.RadarOptions](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-radar_options) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-07-29.dahlia`
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
