# Removes deprecated messaging and bank elements that were replaced

## What’s new

We removed deprecated elements for:

- Showing Affirm and Afterpay (Clearpay) messaging
- Collecting bank payments.

We replaced these elements with the [Payment Method Messaging Element](https://docs.stripe.com/elements/payment-method-messaging.md) and the [Payment Element](https://docs.stripe.com/payments/payment-element.md).

## Why is this a breaking change?

This release removes the following deprecated elements for messaging and accepting payments from Stripe.js:

- `affirmMessage`
- `afterpayClearpayMessage`
- `epsBank`
- `fpxBank`
- `p24Bank`
- `idealBank`

References to them in your integration will cause failures.

## Impact

If your integration uses the `epsBank`, `fpxBank`, `p24Bank` or `idealBank` elements, update it to use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) instead. This new UI component for the web accepts 40+ payment methods, validates input and handles errors.

If your integration uses the `affirmMessage` or `afterpayClearpayMessage` elements, update it to use the [Payment Method Messaging Element](https://docs.stripe.com/elements/payment-method-messaging.md). The new element dynamically shows your customers relevant buy now, pay later payment options for their purchase.

## Related changes

- [Updates default behaviour for saved payment methods in Elements with Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/custom-checkout-saved-payment-method-defaults.md)
- [Prevents reusing client secrets for Intents in certain states when initialising Elements](https://docs.stripe.com/changelog/clover/2025-09-30/client-secret-reuse.md)
