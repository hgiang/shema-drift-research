# Removes manual capture method for Interac cards

## What’s new

The `interac_present` payment method type no longer supports the `manual` [capture_method](https://docs.stripe.com/api/payment_intents/object.md?api-version=2025-03-31.basil#payment_intent_object-capture_method) for [PaymentIntents](https://docs.stripe.com/api/payment_intents.md?api-version=2025-03-31.basil). We still support synchronous and asynchronous automatic capture methods.

## Why is this a breaking change?

We’re removing support for the `manual` [capture_method](https://docs.stripe.com/api/payment_intents/object.md?api-version=2025-03-31.basil#payment_intent_object-capture_method) for PaymentIntents that use the Interac payment method.

## Impact

This change makes the behaviour of the [capture_method](https://docs.stripe.com/api/payment_intents/object.md?api-version=2025-03-31.basil#payment_intent_object-capture_method) parameter consistent with the Interac network’s single-message behaviour.

To use this version, update the [capture_method](https://docs.stripe.com/api/payment_intents/object.md?api-version=2025-03-31.basil#payment_intent_object-capture_method) in your integration to use `automatic_async` or `automatic`.

Setting the [capture_method](https://docs.stripe.com/api/payment_intents/object.md?api-version=2025-03-31.basil#payment_intent_object-capture_method) to either `automatic_async` or `automatic` means Stripe captures funds when the customer authorises the payment.

If you need to manually capture `card_present` payments in addition to automatically captured `interac_present` payments, use the [payment_method_options.card_present.capture_method](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-03-31.basil#create_payment_intent-payment_method_options-card_present-capture_method) parameter.

### Before

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=cad \
  -d "allowed_payment_method_types[]=card_present" \
  -d "allowed_payment_method_types[]=interac_present" \
  -d capture_method=manual
```

### After

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=cad \
  -d "allowed_payment_method_types[]=card_present" \
  -d "allowed_payment_method_types[]=interac_present" \
  -d "payment_method_options[card_present][capture_method]=manual"
```

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-03-31.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.0.0](https://github.com/stripe/stripe-python/releases/tag/v12.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.0.0](https://github.com/stripe/stripe-php/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.0.0](https://github.com/stripe/stripe-java/releases/tag/v29.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.0.0](https://github.com/stripe/stripe-node/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.0.0](https://github.com/stripe/stripe-go/releases/tag/v82.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Updates the Vault and Forward API to return a 402 status code for upstream request timeouts](https://docs.stripe.com/changelog/basil/2025-03-31/vault-forward-api-returns-402.md)
- [Payment Methods won’t allow modifying fields for Naver Pay after the object is first created](https://docs.stripe.com/changelog/basil/2025-03-31/naver-pay-payment-method.md)
- [Partially capturing or cancelling payments no longer creates a Refund](https://docs.stripe.com/changelog/basil/2025-03-31/remove-refund-from-partial-capture-and-payment-cancellation-flow.md)
- [Adds support for Klarna in the hosted invoice page](https://docs.stripe.com/changelog/basil/2025-03-31/klarna-send-invoice.md)
- [Adds ability to configure saved payment methods for one-time payments on the hosted invoice page](https://docs.stripe.com/changelog/basil/2025-03-31/hosted-payment-method-save.md)
- [Adds support for saving and reusing Naver Pay payment methods](https://docs.stripe.com/changelog/basil/2025-03-31/naver-pay-recurring.md)
- [Adds support for the Billie local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/add-billie.md)
- [Adds support for the Satispay local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/satispay-lpm.md)
- [Makes the client parameter optional for WeChat Pay until confirmation](https://docs.stripe.com/changelog/basil/2025-03-31/lient-param-optional-wechatpay-before-confirmation.md)
- [Adds support for the New Zealand BECS Direct Debit local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/nz-bank-account.md)
