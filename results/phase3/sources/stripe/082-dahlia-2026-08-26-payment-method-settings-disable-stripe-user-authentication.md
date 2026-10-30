# Adds control over Stripe user authentication to Payment Method Settings

## What’s new

Adds the nullable `disable_stripe_user_authentication` boolean property to the `features` hash for the [Payment Method Settings embedded component](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings.md) when you [create an Account Session](https://docs.stripe.com/api/account_sessions/create.md?api-version=2026-08-26.preview).

## Impact

You can now disable Stripe authentication in the Payment Method Settings embedded component for eligible connected accounts where your platform collects requirements. Set `components.payment_method_settings.features.disable_stripe_user_authentication` to `true`. The property defaults to `false`, so existing integrations aren’t affected. See [Disable Stripe user authentication](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings.md#disable-stripe-user-authentication) for eligibility and configuration details.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `disable_stripe_user_authentication` | Added | [AccountSession#create.components.payment_method_settings.features](/api/account_sessions/create?api-version=2026-08-26.preview#create_account_session-components-payment_method_settings-features), [AccountSession.components.payment_method_settings.features](/api/account_sessions/object?api-version=2026-08-26.preview#account_session_object-components-payment_method_settings-features) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `disable_stripe_user_authentication` | Added | [AccountSession::Component::PaymentMethodSetting::Feature](/api/account_sessions/object?api-version=2026-08-26.preview#account_session_object-components-payment_method_settings-features), [AccountSessionCreateParams::Component::PaymentMethodSetting::Feature](/api/account_sessions/create?api-version=2026-08-26.preview#create_account_session-components-payment_method_settings-features) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `disable_stripe_user_authentication` | Added | [AccountSession.Component.PaymentMethodSetting.Feature](/api/account_sessions/object?api-version=2026-08-26.preview#account_session_object-components-payment_method_settings-features), [AccountSessionCreateParamsComponentPaymentMethodSettingFeature](/api/account_sessions/create?api-version=2026-08-26.preview#create_account_session-components-payment_method_settings-features) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `disable_stripe_user_authentication` | Added | [AccountSession.components.payment_method_settings.features](/api/account_sessions/object?api-version=2026-08-26.preview#account_session_object-components-payment_method_settings-features), [AccountSession.create().$params.component.payment_method_settings.feature](/api/account_sessions/create?api-version=2026-08-26.preview#create_account_session-components-payment_method_settings-features) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `disableStripeUserAuthentication` | Added | [AccountSession.components.payment_method_settings.features](/api/account_sessions/object?api-version=2026-08-26.preview#account_session_object-components-payment_method_settings-features), [AccountSessionCreateParams.components.payment_method_settings.features](/api/account_sessions/create?api-version=2026-08-26.preview#create_account_session-components-payment_method_settings-features) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `disable_stripe_user_authentication` | Added | [AccountSession.components.payment_method_settings.features](/api/account_sessions/object?api-version=2026-08-26.preview#account_session_object-components-payment_method_settings-features), [AccountSessionCreateParams.components.payment_method_settings.features](/api/account_sessions/create?api-version=2026-08-26.preview#create_account_session-components-payment_method_settings-features) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `DisableStripeUserAuthentication` | Added | [AccountSessionComponentsPaymentMethodSettingsFeatures](/api/account_sessions/object?api-version=2026-08-26.preview#account_session_object-components-payment_method_settings-features), [AccountSessionComponentsPaymentMethodSettingsFeaturesParams](/api/account_sessions/create?api-version=2026-08-26.preview#create_account_session-components-payment_method_settings-features) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `DisableStripeUserAuthentication` | Added | [AccountSession.Components.PaymentMethodSettings.Features](/api/account_sessions/object?api-version=2026-08-26.preview#account_session_object-components-payment_method_settings-features), [AccountSessionComponentsPaymentMethodSettingsFeaturesOptions](/api/account_sessions/create?api-version=2026-08-26.preview#create_account_session-components-payment_method_settings-features) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-08-26.preview`
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

- [Redirects new Connect platforms away from unsupported integration patterns](https://docs.stripe.com/changelog/dahlia/2026-08-26/2026-08-17-blocks-unsupported-integration-patterns.md)
- [Adds Account Signals, Account Evaluations and Account Activity APIs in public preview](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-account-signals-account-evaluations-and-account-activity-apis-in-public-preview.md)
