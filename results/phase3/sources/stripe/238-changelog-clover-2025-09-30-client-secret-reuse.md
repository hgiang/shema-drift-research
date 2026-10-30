# Prevents reusing client secrets for Intents in certain states when initialising Elements

## What’s new

Introduces validation to prevent reusing client secrets from [Payment Intents](https://docs.stripe.com/api/payment_intents.md?api-version=2025-09-30.clover) or [Setup Intents](https://docs.stripe.com/api/setup_intents.md?api-version=2025-09-30.clover) that are in `succeeded`, `cancelled`, `processing`, `requires_capture` or `requires_action` states with non-detachable payment methods ([Boleto](https://docs.stripe.com/payments/boleto.md), [knet](https://docs.stripe.com/api/payment_methods/object.md?api-version=2025-08-27.preview&rds=1#payment_method_object-knet), [Oxxo](https://docs.stripe.com/payments/oxxo.md), [us_cash_voucher](https://docs.stripe.com/api/payment_methods/object.md?api-version=2025-08-27.preview&rds=1#payment_method_object-us_cash_voucher)) when you create an [Elements](https://docs.stripe.com/payments/elements.md) instance.

## Why is this a breaking change?

Previously, Elements allowed you to initialise a instance with any valid client secret, regardless of the associated PaymentIntent or SetupIntent’s state.

Now, Elements validates that the Intent is in an appropriate state before allowing the instance to be created. If you reuse client secrets from PaymentIntents or SetupIntents that are already completed or processing, they now produce validation errors.

## Impact

This change prevents Elements from rendering payment forms in a broken state, which ensures that your customers don’t see broken forms on your checkout page.

Previously, you could create an Elements instance with a client secret from a completed or processing Intent, but any payment attempts by your customers would fail. Now, Elements validates the Intent state and returns an error to your integration instead of rendering a non-functional payment form.

To ensure your integration continues to work:

- **Handle the new validation errors**: Update your [error handling](https://docs.stripe.com/js/element/events/on_loaderror) to catch these validation errors when creating an Elements instance.
- **Create new PaymentIntents or SetupIntents**: When you receive a validation error, create a new PaymentIntent or SetupIntent and use its [client secret](https://docs.stripe.com/api/payment_intents/object.md?api-version=2025-08-27.preview#payment_intent_object-client_secret) to initialise Elements.
- **Avoid reusing client secrets**: Always use fresh client secrets for new payment flows or verify that the associated intent is in a valid state (typically `requires_payment_method` or `requires_confirmation`).

This validation only applies when using API version `2025-09-30.clover` or later, so existing integrations on earlier API versions are unaffected.

## Related changes

- [Updates default behaviour for saved payment methods in Elements with Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/custom-checkout-saved-payment-method-defaults.md)
- [Removes deprecated messaging and bank elements that were replaced](https://docs.stripe.com/changelog/clover/2025-09-30/stripejs-deprecated-elements-removal.md)
