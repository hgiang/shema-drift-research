# Adds support for Customer Sessions for the Mobile Payment Element and Customer Sheet

## What’s new

Lets you create a [Customer Session](https://docs.stripe.com/api/customer_sessions.md?api-version=2025-10-29.clover) for [Payment Sheet](https://docs.stripe.com/payments/mobile/payment-sheet.md) and [Payment Method Settings Sheet](https://docs.stripe.com/elements/customer-sheet.md), which you can use to save a customer’s payment method.

## Impact

This enables support for Customer Sessions when saving payment methods in [Payment Sheet](https://docs.stripe.com/payments/mobile/payment-sheet.md) and [Payment Method Settings Sheet](https://docs.stripe.com/elements/customer-sheet.md). To use the latest features, we recommend updating your integrations to use [Customer Sessions](https://docs.stripe.com/api/customer_sessions.md?api-version=2025-10-29.clover) instead of customer ephemeral keys.

For example, if your existing integration uses SetupIntents to set up future payments by saving a payment method with an ephemeral key, replace the request to create an ephemeral key:

```bash
curl https://api.stripe.com/v1/ephemeral_keys \
  -u <<YOUR_SECRET_KEY>>: \
  -H "Stripe-Version: 2026-10-28.endive" \
  -X "POST" \
  -d "customer"={{CUSTOMER_ID}} \
```

With a request to create a Customer Session:

```curl
curl https://api.stripe.com/v1/customer_sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "components[mobile_payment_element][enabled]=true" \
  -d "components[mobile_payment_element][features][payment_method_save]=enabled" \
  -d "components[mobile_payment_element][features][payment_method_redisplay]=enabled" \
  -d "components[mobile_payment_element][features][payment_method_remove]=enabled"
```

If your existing integration uses PaymentIntents to [save payment details during the payment](https://docs.stripe.com/payments/mobile/save-during-payment.md#add-server-endpoint), make the same replacement, following the examples in the guide.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `customer_sheet`, `mobile_payment_element` | Added | [CustomerSession#create.components](/api/customer_sessions/create?api-version=2025-10-29.clover#create_customer_session-components), [CustomerSession.components](/api/customer_sessions/object?api-version=2025-10-29.clover#customer_session_object-components) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customer_sheet`, `mobile_payment_element` | Added | [CustomerSession::Component](/api/customer_sessions/object?api-version=2025-10-29.clover#customer_session_object-components), [CustomerSession::CreateParams::Component](/api/customer_sessions/create?api-version=2025-10-29.clover#create_customer_session-components) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customer_sheet`, `mobile_payment_element` | Added | [CustomerSession.Component](/api/customer_sessions/object?api-version=2025-10-29.clover#customer_session_object-components), [CustomerSession.CreateParamsComponent](/api/customer_sessions/create?api-version=2025-10-29.clover#create_customer_session-components) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customer_sheet`, `mobile_payment_element` | Added | [CustomerSession.components](/api/customer_sessions/object?api-version=2025-10-29.clover#customer_session_object-components), [CustomerSession.create().$params.component](/api/customer_sessions/create?api-version=2025-10-29.clover#create_customer_session-components) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customerSheet`, `mobilePaymentElement` | Added | [CustomerSession.components](/api/customer_sessions/object?api-version=2025-10-29.clover#customer_session_object-components), [CustomerSessionCreateParams.components](/api/customer_sessions/create?api-version=2025-10-29.clover#create_customer_session-components) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customer_sheet`, `mobile_payment_element` | Added | [CustomerSession.components](/api/customer_sessions/object?api-version=2025-10-29.clover#customer_session_object-components), [CustomerSessionCreateParams.components](/api/customer_sessions/create?api-version=2025-10-29.clover#create_customer_session-components) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CustomerSheet`, `MobilePaymentElement` | Added | [CustomerSessionComponents](/api/customer_sessions/object?api-version=2025-10-29.clover#customer_session_object-components), [CustomerSessionComponentsParams](/api/customer_sessions/create?api-version=2025-10-29.clover#create_customer_session-components) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CustomerSheet`, `MobilePaymentElement` | Added | [CustomerSession.Components](/api/customer_sessions/object?api-version=2025-10-29.clover#customer_session_object-components), [CustomerSessionComponentsOptions](/api/customer_sessions/create?api-version=2025-10-29.clover#create_customer_session-components) |

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
