# Adds two new Connect embedded components for Disputes

## What’s new

The following [Connect embedded components](https://docs.stripe.com/connect/supported-embedded-components.md) are now generally available:

- [Disputes for a payment](https://docs.stripe.com/connect/supported-embedded-components/disputes-for-a-payment.md)
- [Disputes list](https://docs.stripe.com/connect/supported-embedded-components/disputes-list.md)

## Impact

These components provide you with modular and efficient tools to allow your connected accounts to manage disputes.

The [Disputes for a payment](https://docs.stripe.com/connect/supported-embedded-components/disputes-for-a-payment.md) component lets you embed dispute details and management functionality, without relying on the [Payments](https://docs.stripe.com/connect/supported-embedded-components/payments.md) or [Payment details](https://docs.stripe.com/connect/supported-embedded-components/payment-details.md) components.

The [Disputes list](https://docs.stripe.com/connect/supported-embedded-components/disputes-list.md) component provides a streamlined way for connected accounts to manage disputes directly and resolve disputes efficiently.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `disputes_list` | Added | [AccountSession#create.components](/api/account_sessions/create?api-version=2025-05-28.basil#create_account_session-components), [AccountSession.components](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components) |
| `payment_disputes` | Added | [AccountSession.components](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `disputes_list` | Added | [AccountSession::Component](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components), [AccountSession::CreateParams::Component](/api/account_sessions/create?api-version=2025-05-28.basil#create_account_session-components) |
| `payment_disputes` | Added | [AccountSession::Component](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `disputes_list` | Added | [AccountSession.Component](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components), [AccountSession.CreateParamsComponent](/api/account_sessions/create?api-version=2025-05-28.basil#create_account_session-components) |
| `payment_disputes` | Added | [AccountSession.Component](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `disputesList` | Added | [AccountSession.components](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components), [AccountSessionCreateParams.components](/api/account_sessions/create?api-version=2025-05-28.basil#create_account_session-components) |
| `paymentDisputes` | Added | [AccountSession.components](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `disputes_list` | Added | [AccountSession.components](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components), [AccountSessionCreateParams.components](/api/account_sessions/create?api-version=2025-05-28.basil#create_account_session-components) |
| `payment_disputes` | Added | [AccountSession.components](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `DisputesList` | Added | [AccountSessionComponents](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components), [AccountSessionComponentsParams](/api/account_sessions/create?api-version=2025-05-28.basil#create_account_session-components) |
| `PaymentDisputes` | Added | [AccountSessionComponents](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `DisputesList` | Added | [AccountSession.Components](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components), [AccountSessionComponentsOptions](/api/account_sessions/create?api-version=2025-05-28.basil#create_account_session-components) |
| `PaymentDisputes` | Added | [AccountSession.Components](/api/account_sessions/object?api-version=2025-05-28.basil#account_session_object-components) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-05-28.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.2.0](https://github.com/stripe/stripe-python/releases/tag/v12.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.3.0](https://github.com/stripe/stripe-php/releases/tag/v17.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.2.0](https://github.com/stripe/stripe-java/releases/tag/v29.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.2.0](https://github.com/stripe/stripe-node/releases/tag/v18.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.2.0](https://github.com/stripe/stripe-go/releases/tag/v82.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
