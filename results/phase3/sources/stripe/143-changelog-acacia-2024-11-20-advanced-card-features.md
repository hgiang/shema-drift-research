# Adds support for advanced card features on Checkout Sessions

## What’s new

Adds advanced card features [incremental authorisation](https://docs.stripe.com/payments/incremental-authorization.md?platform=web&ui=stripe-hosted), [extended authorisation](https://docs.stripe.com/payments/extended-authorization.md?platform=web&ui=stripe-hosted), [multicapture](https://docs.stripe.com/payments/multicapture.md?platform=web&ui=stripe-hosted), and [overcapture](https://docs.stripe.com/payments/overcapture.md?platform=web&ui=stripe-hosted) for *IC+* (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs) users creating `mode: 'payment'` and `capture_method: 'manual'` Checkout Sessions.

## Impact

These features were previously only available for Payment Intents. Users can now adapt to these [flexible payment scenarios](https://docs.stripe.com/payments/flexible-payments.md) on Checkout Sessions.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `request_extended_authorization`, `request_incremental_authorization`, `request_multicapture`, `request_overcapture` | Added | [Checkout.Session#create.payment_method_options.card](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-card), [Checkout.Session.payment_method_options.card](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-card) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `request_extended_authorization`, `request_incremental_authorization`, `request_multicapture`, `request_overcapture` | Added | [stripe.checkout.Session.CreateParamsPaymentMethodOptionsCard](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-card), [stripe.checkout.Session.PaymentMethodOptions.Card](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-card) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `request_extended_authorization`, `request_incremental_authorization`, `request_multicapture`, `request_overcapture` | Added | [Checkout.Session.payment_method_options.card](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-card), [checkout.SessionCreateParams.payment_method_options.card](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-card) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `request_extended_authorization`, `request_incremental_authorization`, `request_multicapture`, `request_overcapture` | Added | [Checkout.Session.payment_method_options.card](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-card), [Checkout.SessionCreateParams.payment_method_options.card](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-card) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `RequestExtendedAuthorization`, `RequestIncrementalAuthorization`, `RequestMulticapture`, `RequestOvercapture` | Added | [CheckoutSessionPaymentMethodOptionsCardParams](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-card), [CheckoutSessionPaymentMethodOptionsCard](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-card) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `RequestExtendedAuthorization`, `RequestIncrementalAuthorization`, `RequestMulticapture`, `RequestOvercapture` | Added | [CheckoutSessionPaymentMethodOptionsCardOptions](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-card), [CheckoutSessionPaymentMethodOptionsCard](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-card) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-11-20.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.3.0](https://github.com/stripe/stripe-python/releases/tag/v11.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.3.0](https://github.com/stripe/stripe-php/releases/tag/v16.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.1.0](https://github.com/stripe/stripe-java/releases/tag/v28.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.4.0](https://github.com/stripe/stripe-node/releases/tag/v17.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.1.0](https://github.com/stripe/stripe-go/releases/tag/v81.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds support for enabling Adaptive Pricing per Checkout Session](https://docs.stripe.com/changelog/acacia/2024-11-20/adaptive-pricing-param.md)
- [Customise the submit button recurring Payment Links and Checkout Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/submit-type-recurring-cpl.md)
- [Allows Link card-only integrations to accept non-card payments under Link card brand](https://docs.stripe.com/changelog/acacia/2024-11-20/link-card-brand.md)
- [Adds additional beneficiary information for bank transfer payments](https://docs.stripe.com/changelog/acacia/2024-11-20/new-bank-transfer-beneficiary-information.md)
