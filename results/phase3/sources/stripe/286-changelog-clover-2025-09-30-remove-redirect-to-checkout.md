# Removes support for the redirectToCheckout method

## What’s new

The `stripe.redirectToCheckout` method is no longer supported in Stripe.js.

## Why is this a breaking change?

You can no longer use `stripe.redirectToCheckout` for both client-only and [client and server](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) integrations.

## Impact

If you use the client-only integration for Checkout, migrate to [Payment Links](https://docs.stripe.com/payment-links.md) and [Buy Buttons](https://docs.stripe.com/payment-links/buy-button.md). For client-side redirects, use standard redirect functions (such as `window.location.href = session.url`) or equivalent methods in your environment to redirect users to the Checkout Session.

## Related changes

- [Removes postal code for card payments in certain regions on Checkout and Payment Element](https://docs.stripe.com/changelog/clover/2025-09-30/postal_code_in_card_form_for_non_us_countries.md)
- [Removes currency conversion field from Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/remove-checkout-session-currency-conversion-field.md)
- [Updates initCheckout to be synchronous](https://docs.stripe.com/changelog/clover/2025-09-30/update-init-checkout-synchronous.md)
- [Adds support for collecting business and individual names in Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-name-collection.md)
- [Adds the ability to exclude payment methods from Checkout Sessions and Payment Intents](https://docs.stripe.com/changelog/clover/2025-09-30/exclude-payment-methods-checkout-sessions.md)
- [Adds support for setting the capture method for specific payment methods with the Checkout Sessions API](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-capture-method-per-payment-method.md)
- [Adds support for configuring branding settings for Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-sessions-branding-settings.md)
- [Enables specifying units of measurement for Products](https://docs.stripe.com/changelog/clover/2025-09-30/product-data-unit-label.md)
