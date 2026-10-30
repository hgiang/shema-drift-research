# Updates initCheckout to be synchronous

## What’s new

The [stripe.initCheckout](https://docs.stripe.com/js/custom_checkout/init) method is now synchronous instead of asynchronous.

## Why is this a breaking change?

This breaking change affects you if your integration uses [Elements with the Checkout Sessions API](https://docs.stripe.com/payments/quickstart.md).

#### HTML + JS

To migrate, you need to:

1. Remove any `await` or `.then()` calls associated with `initCheckout`.
2. Replace your `fetchClientSecret` function with a client secret string or Promise that resolves to a client secret string.
3. Call the new asynchronous function `checkout.loadActions()` in order to access actions such as `getSession()`, which replaces `session()` or `confirm()`. You only need to call `loadActions()` once.
4. If you previously wrapped `initCheckout` in a `try...catch` block, you should examine the resolved `type` value of `loadActions()` instead to check for errors.

```javascript
const clientSecret = fetch("/create-checkout-session", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
})
  .then((r) => r.json())
  .then((r) => r.clientSecret);

const checkout = stripe.initCheckout({
  clientSecret
});
const paymentElement = checkout.createPaymentElement();
paymentElement.mount("#payment-element");

const loadActionsResult = await checkout.loadActions();
if (loadActionsResult.type === 'success') {
  const session = loadActionsResult.actions.getSession();
}
```

#### React

Upgrade your `@stripe/react-stripe-js` dependency to at least version 5.0.0. If you upgrade from a version earlier than 4.0.0, make sure you read the [release notes](https://github.com/stripe/react-stripe-js/releases/tag/v4.0.0) to see what changed.

If you upgrade from version 4.0.0 or later, you need to replace your `fetchClientSecret` function with a client secret string or Promise that resolves to a client secret string. You can also render any Element without first checking if `useCheckout` returned `type: 'success'`, to reduce latency in your integration and enable Elements to show their skeleton loaders earlier.

```jsx
const App = () => {
  const promise = useMemo(() => {
    return fetch('/create-checkout-session', {
      method: 'POST',
      headers: { "Content-Type": "application/json" },
    })
      .then((res) => res.json())
      .then((data) => data.clientSecret);
  }, []);

  return (
    <CheckoutProvider
      stripe={stripePromise}
      options={{
        clientSecret: promise
      }}
    >
      <CheckoutPage />
    </CheckoutProvider>
  );
}

const CheckoutPage = () => {
  const {type, ...rest} = useCheckout();

  return (
    <div>
      <PaymentElement />
    </div>
  );
}
```

## Impact

The synchronous nature of `initCheckout` enables you to mount Elements earlier, which reduces the render latency of any Elements you mount immediately after `initCheckout`. This also enables Elements to display the skeleton loader UI after it’s mounted but the session state hasn’t fully loaded yet.

## Related changes

- [Removes postal code for card payments in certain regions on Checkout and Payment Element](https://docs.stripe.com/changelog/clover/2025-09-30/postal_code_in_card_form_for_non_us_countries.md)
- [Removes currency conversion field from Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/remove-checkout-session-currency-conversion-field.md)
- [Removes support for the redirectToCheckout method](https://docs.stripe.com/changelog/clover/2025-09-30/remove-redirect-to-checkout.md)
- [Adds support for collecting business and individual names in Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-name-collection.md)
- [Adds the ability to exclude payment methods from Checkout Sessions and Payment Intents](https://docs.stripe.com/changelog/clover/2025-09-30/exclude-payment-methods-checkout-sessions.md)
- [Adds support for setting the capture method for specific payment methods with the Checkout Sessions API](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-capture-method-per-payment-method.md)
- [Adds support for configuring branding settings for Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-sessions-branding-settings.md)
- [Enables specifying units of measurement for Products](https://docs.stripe.com/changelog/clover/2025-09-30/product-data-unit-label.md)
