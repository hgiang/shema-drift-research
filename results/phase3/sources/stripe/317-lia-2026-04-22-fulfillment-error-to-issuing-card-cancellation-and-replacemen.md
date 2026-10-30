# Adds fulfilment error to issuing card cancellation and replacement reasons

## What’s new

Adds the `fulfillment_error` enum value for the [cancellation_reason](https://docs.stripe.com/api/issuing/cards/object.md?api-version=2026-04-22.dahlia#issuing_card_object-cancellation_reason) and [replacement_reason](https://docs.stripe.com/api/issuing/cards/object.md?api-version=2026-04-22.dahlia#issuing_card_object-replacement_reason) properties on the [Issuing cards](https://docs.stripe.com/api/issuing/cards.md?api-version=2026-04-22.dahlia) API.

If a physical card was cancelled and reissued due to fulfilment issues, the [retrieve a card](https://docs.stripe.com/api/issuing/cards/retrieve.md?api-version=2026-04-22.dahlia) endpoint returns a `fulfillment_error` status.

## Impact

If your Issuing cards integration reads [cancellation_reason](https://docs.stripe.com/api/issuing/cards/object.md?api-version=2026-04-22.dahlia#issuing_card_object-cancellation_reason) and [replacement_reason](https://docs.stripe.com/api/issuing/cards/object.md?api-version=2026-04-22.dahlia#issuing_card_object-replacement_reason), you now must also support `fulfillment_error`.

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `fulfillment_error` | Added | [Issuing.Card#replacement_reason](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-replacement_reason), [Issuing.Card#cancellation_reason](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-cancellation_reason) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enums |
| --- | --- | --- |
| `fulfillment_error` | Added | [Issuing.Card#replacement_reason](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-replacement_reason), [Issuing.Card#cancellation_reason](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-cancellation_reason) |

#### PHP

| Value | Change | Enums |
| --- | --- | --- |
| `fulfillment_error` | Added | [Issuing.Card#replacement_reason](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-replacement_reason), [Issuing.Card#cancellation_reason](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-cancellation_reason) |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `fulfillment_error` | Added | [Issuing.Card#replacement_reason](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-replacement_reason), [Issuing.Card#cancellation_reason](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-cancellation_reason) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `fulfillment_error` | Added | [IssuingCard#ReplacementReason](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-replacement_reason), [IssuingCard#CancellationReason](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-cancellation_reason) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-04-22.dahlia`
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
