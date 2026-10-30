# Renames Checkout initialisation method

## What’s new

Renames the `stripe.initCheckout()` method for [Stripe.js](https://docs.stripe.com/js.md) to [stripe.initCheckoutElementsSdk()](https://docs.stripe.com/js/custom_checkout/init). It accepts the same options and returns the same Checkout object as `initCheckout()`.

Additionally, introduces `stripe.initCheckoutFormSdk()` as a new entry point for [Checkout form](https://docs.stripe.com/checkout/form/quickstart.md) integrations. Use `initCheckoutFormSdk()` instead of `initCheckoutElementsSdk()` when your integration uses `ui_mode: "form"`.

## Why is this a breaking change?

`stripe.initCheckout()` has been renamed, so calling it throws an `IntegrationError`. If your integration uses [Elements with the Checkout Sessions API](https://docs.stripe.com/payments/quickstart.md) and calls `initCheckout()`, you need to update your code to instead call `initCheckoutElementsSdk()`.

The update depends on whether you use HTML+JS or React:

#### HTML + JS

Replace `stripe.initCheckout()` with `stripe.initCheckoutElementsSdk()`:

```javascript

const checkout = stripe.initCheckoutElementsSdk({clientSecret});
```

#### React

Replace `CheckoutProvider` with `CheckoutElementsProvider`:

```jsx

import {CheckoutElementsProvider} from '@stripe/react-stripe-js/checkout';

<CheckoutElementsProvider stripe={stripePromise} options={{clientSecret}}>
  <CheckoutForm />
</CheckoutElementsProvider>
```

If you use the Payment Form Element, use a [Checkout form](https://docs.stripe.com/checkout/form/quickstart.md). The update depends on whether you use HTML+JS or React:

#### HTML + JS

Replace `stripe.initCheckout()` with `stripe.initCheckoutFormSdk()` and use `createForm()` from the returned Checkout form SDK:

```javascript

const checkoutFormSdk = stripe.initCheckoutFormSdk({clientSecret});
const checkoutForm = checkoutFormSdk.createForm();
```

#### React

Replace `CheckoutProvider` with `CheckoutFormProvider` and use the new `CheckoutForm` export from `@stripe/react-stripe-js` instead of the `PaymentFormElement`:

```jsx

import {CheckoutFormProvider, CheckoutForm} from '@stripe/react-stripe-js/checkout';

<CheckoutFormProvider stripe={stripePromise} options={{clientSecret}}>
  <CheckoutForm />
</CheckoutFormProvider>
```

## Impact

The rename from `initCheckout` to `initCheckoutElementsSdk` clarifies the method’s purpose as the entry point for [Elements with Checkout Sessions](https://docs.stripe.com/payments/quickstart.md) integrations, where you compose individual Elements (Payment Element, Address Element and so on) on your checkout page.

The new `initCheckoutFormSdk()` method provides a dedicated entry point for [Checkout form](https://docs.stripe.com/checkout/form/quickstart.md) integrations, corresponding to `ui_mode: "form"`.

## Related changes

- [Changes the Address Element state field to default to Latin-formatted characters](https://docs.stripe.com/changelog/dahlia/2026-03-25/address-element-getvalue-and-change-event-formatting.md)
- [Updates the elements.update() method to return a Promise](https://docs.stripe.com/changelog/dahlia/2026-03-25/elements-update-returns-promise.md)
- [Removes support for boolean values in options.layout.radios](https://docs.stripe.com/changelog/dahlia/2026-03-25/disallow-booleans-for-radios.md)
- [Removes deprecated Payment Intents, Setup Intents, and Sources methods from Stripe.js](https://docs.stripe.com/changelog/dahlia/2026-03-25/remove-legacy-stripejs-methods.md)
- [Renames Embedded Checkout initialisation method](https://docs.stripe.com/changelog/dahlia/2026-03-25/rename-init-embedded-checkout-to-create-embedded-checkout-page.md)
