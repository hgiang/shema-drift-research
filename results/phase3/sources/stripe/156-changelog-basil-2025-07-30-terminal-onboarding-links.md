# Adds support for accepting Apple's Tap to Pay on iPhone Terms and Conditions on the web

## What’s new

Adds the Terminal onboarding link resource that lets you give a `link_type` to generate a `redirect_url` to accept Apple’s Tap to Pay on iPhone Terms and Conditions on the web.

## Impact

You can now accept Apple’s Tap to Pay on iPhone Terms and Conditions on the web. Learn more about [account linking](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=ios&reader-type=tap-to-pay#account-linking-and-apple-terms-and-conditions) for Tap to Pay on iPhone.

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Terminal.OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

| Endpoint | Change | Resource |
| --- | --- | --- |
| `create` | Added | [Terminal.OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

#### Ruby

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Terminal::OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

| Method | Change | Resource |
| --- | --- | --- |
| `create` | Added | [Terminal::OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [terminal.OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

| Method | Change | Resource |
| --- | --- | --- |
| `create` | Added | [terminal.OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

#### PHP

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Terminal.OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

| Method | Change | Resource |
| --- | --- | --- |
| `create` | Added | [Terminal.OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [terminal.OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

| Method | Change | Resource |
| --- | --- | --- |
| `create` | Added | [terminal.OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

#### Node.js

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Terminal.OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

| Method | Change | Resource |
| --- | --- | --- |
| `create` | Added | [Terminal.OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

#### Go

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [TerminalOnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

| Method | Change | Resource |
| --- | --- | --- |
| `New` | Added | [TerminalOnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Terminal.OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

| Method | Change | Resource |
| --- | --- | --- |
| `Create` | Added | [Terminal.OnboardingLink](/api/terminal/onboarding-link?api-version=2025-07-30.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-07-30.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.5.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v15.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.5.0b1](https://github.com/stripe/stripe-python/releases/tag/v12.5.0b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.6.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v17.6.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.5.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v29.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.5.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v18.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.5.0-beta.1](https://github.com/stripe/stripe-go/releases/tag/v82.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.5.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v48.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
