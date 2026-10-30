# Updates consent modelling for saving cards with Terminal

## What’s new

Removes the `customer_consent_collected` parameter and replaces it with  [allow_redisplay](https://docs.stripe.com/api/terminal/readers/process_setup_intent.md?api-version=2024-09-30.acacia#process_setup_intent-allow_redisplay).

Requires `allow_redisplay` when using `setup_future_usage`.

## Why is this a breaking change?

This is a breaking change because it requires `allow_redisplay` when saving card details with Terminal. For SetupIntents, `customer_consent_collected` has been removed and replaced with `allow_redisplay`. For PaymentIntents that specify `setup_future_usage`, then `allow_redisplay` must also be passed before collecting card details. With the new version, you must use `allow_redisplay` to control whether a payment can be shown to a customer again.

## Impact

Lets you save cards in more regions using Terminal, expanding your service coverage. Additionally, the improved alignment with industry requirements for customer consent collection ensures regulatory compliance.

You must add the new parameter to your integration before 31 March 2025 and ensure that it’s set to `always` or `limited` on all Setup Intents transactions and Payment Intents that specify `setup_future_usage`.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `allow_redisplay` | Added | [Terminal.Reader#process_payment_intent.process_config](/api/terminal/readers/process_payment_intent?api-version=2024-09-30.acacia#process_payment_intent-process_config), [Terminal.Reader#process_setup_intent](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |
| `customer_consent_collected` | Removed | [Terminal.Reader#process_setup_intent](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `allow_redisplay` | Added | [Terminal::ReaderProcessPaymentIntentParams.process_config](/api/terminal/readers/process_payment_intent?api-version=2024-09-30.acacia#process_payment_intent-process_config), [Terminal::ReaderProcessSetupIntentParams](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |
| `customer_consent_collected` | Removed | [Terminal::ReaderProcessSetupIntentParams](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `allow_redisplay` | Added | [stripe.terminal.Reader.ProcessPaymentIntentParamsProcessConfig](/api/terminal/readers/process_payment_intent?api-version=2024-09-30.acacia#process_payment_intent-process_config), [stripe.terminal.Reader.ProcessSetupIntentParams](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |
| `customer_consent_collected` | Removed | [stripe.terminal.Reader.ProcessSetupIntentParams](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `allow_redisplay` | Added | [Terminal\Reader.process_setup_intent().$params](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia), [Terminal\Reader.process_payment_intent().$params.process_config](/api/terminal/readers/process_payment_intent?api-version=2024-09-30.acacia#process_payment_intent-process_config) |
| `customer_consent_collected` | Removed | [Terminal\Reader.process_setup_intent().$params](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `allow_redisplay` | Added | [terminal.ReaderProcessPaymentIntentParams.process_config](/api/terminal/readers/process_payment_intent?api-version=2024-09-30.acacia#process_payment_intent-process_config), [terminal.ReaderProcessSetupIntentParams](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |
| `customer_consent_collected` | Removed | [terminal.ReaderProcessSetupIntentParams](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `allow_redisplay` | Added | [Terminal.ReaderProcessPaymentIntentParams.process_config](/api/terminal/readers/process_payment_intent?api-version=2024-09-30.acacia#process_payment_intent-process_config), [Terminal.ReaderProcessSetupIntentParams](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |
| `customer_consent_collected` | Removed | [Terminal.ReaderProcessSetupIntentParams](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AllowRedisplay` | Added | [TerminalReaderProcessPaymentIntentProcessConfigParams](/api/terminal/readers/process_payment_intent?api-version=2024-09-30.acacia#process_payment_intent-process_config), [TerminalReaderProcessSetupIntentParams](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |
| `CustomerConsentCollected` | Removed | [TerminalReaderProcessSetupIntentParams](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AllowRedisplay` | Added | [Terminal.ReaderProcessSetupIntentOptions](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia), [TerminalReaderProcessConfigOptions](/api/terminal/readers/process_payment_intent?api-version=2024-09-30.acacia#process_payment_intent-process_config) |
| `CustomerConsentCollected` | Removed | [Terminal.ReaderProcessSetupIntentOptions](/api/terminal/readers/process_setup_intent?api-version=2024-09-30.acacia) |

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

- [Adds support for configuring the reboot time setting](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reboot-window.md)
- [Adds the Stripe S700 reader as a valid device type](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reader-s700.md)
- [Adds details about offline collection on `card_present` PaymentMethod objects](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-offline-details-card-present-paymentmethods.md)
