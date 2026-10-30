# Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference prefixes in Checkout Sessions

## What’s new

We added the following API parameter to payment method options for SEPA Direct Debit and Bacs Direct Debit in [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md?api-version=2024-11-20.acacia):

- `bacs_debit.mandate_options.reference_prefix`
- `sepa_debit.mandate_options.reference_prefix`

## Impact

This change lets you specify mandate options when using Checkout with SEPA Direct Debit or Bacs Direct Debit.

You can specify a prefix in the `mandate_options.reference_prefix` parameter to customise either the [SEPA Direct Debit Mandate reference](https://docs.stripe.com/api/mandates/object.md?api-version=2024-11-20.acacia#mandate_object-payment_method_details-sepa_debit-reference) or [Bacs Direct Debit Mandate reference](https://docs.stripe.com/api/mandates/object.md?api-version=2024-11-20.acacia#mandate_object-payment_method_details-bacs_debit-reference) in Payment and Setup modes.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `mandate_options` | Added | [Checkout.Session#create.payment_method_options.bacs_debit](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-bacs_debit), [Checkout.Session#create.payment_method_options.sepa_debit](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-sepa_debit), [Checkout.Session.payment_method_options.bacs_debit](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-bacs_debit), [Checkout.Session.payment_method_options.sepa_debit](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-sepa_debit) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `mandate_options` | Added | [stripe.checkout.Session.CreateParamsPaymentMethodOptionsBacsDebit](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-bacs_debit), [stripe.checkout.Session.CreateParamsPaymentMethodOptionsSepaDebit](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-sepa_debit), [stripe.checkout.Session.PaymentMethodOptions.BacsDebit](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-bacs_debit), [stripe.checkout.Session.PaymentMethodOptions.SepaDebit](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-sepa_debit) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `mandate_options` | Added | [Checkout.Session.payment_method_options.bacs_debit](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-bacs_debit), [Checkout.Session.payment_method_options.sepa_debit](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-sepa_debit), [checkout.SessionCreateParams.payment_method_options.bacs_debit](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-bacs_debit), [checkout.SessionCreateParams.payment_method_options.sepa_debit](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-sepa_debit) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `mandate_options` | Added | [Checkout.Session.payment_method_options.bacs_debit](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-bacs_debit), [Checkout.Session.payment_method_options.sepa_debit](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-sepa_debit), [Checkout.SessionCreateParams.payment_method_options.bacs_debit](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-bacs_debit), [Checkout.SessionCreateParams.payment_method_options.sepa_debit](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-sepa_debit) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `MandateOptions` | Added | [CheckoutSessionPaymentMethodOptionsBacsDebitParams](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-bacs_debit), [CheckoutSessionPaymentMethodOptionsBacsDebit](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-bacs_debit), [CheckoutSessionPaymentMethodOptionsSepaDebitParams](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-sepa_debit), [CheckoutSessionPaymentMethodOptionsSepaDebit](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-sepa_debit) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `MandateOptions` | Added | [CheckoutSessionPaymentMethodOptionsBacsDebitOptions](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-bacs_debit), [CheckoutSessionPaymentMethodOptionsBacsDebit](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-bacs_debit), [CheckoutSessionPaymentMethodOptionsSepaDebitOptions](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-sepa_debit), [CheckoutSessionPaymentMethodOptionsSepaDebit](/api/checkout/sessions/object?api-version=2024-11-20.acacia#checkout_session_object-payment_method_options-sepa_debit) |

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

- [Adds network decline code field for Swish and BLIK refunds](https://docs.stripe.com/changelog/acacia/2024-11-20/refunds-network-decline-code.md)
- [Specifying an originating payment method for Inbound Transfers is now optional](https://docs.stripe.com/changelog/acacia/2024-11-20/inbound-transfers-optional-pm.md)
- [Use configurable capture methods and set up future usage for South Korean payment methods](https://docs.stripe.com/changelog/acacia/2024-11-20/south-korea-payment-methods.md)
