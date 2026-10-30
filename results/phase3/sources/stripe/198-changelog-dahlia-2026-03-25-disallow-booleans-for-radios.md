# Removes support for boolean values in options.layout.radios

## What’s new

When using a Payment Element, you can no longer set [options.layout.radios](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-layout-radios) to true or false. You must use one of the enum values:

- `always`
- `auto`
- `if_multiple`
- `never`

## Why is this a breaking change?

If your existing code sets `options.layout.radios` to true or false, you must update it to use the enum values instead.

## Impact

Attempting to set `options.layout.radios` to a value not on its enum list now throws an integration error.

## Related changes

- [Changes the Address Element state field to default to Latin-formatted characters](https://docs.stripe.com/changelog/dahlia/2026-03-25/address-element-getvalue-and-change-event-formatting.md)
- [Updates the elements.update() method to return a Promise](https://docs.stripe.com/changelog/dahlia/2026-03-25/elements-update-returns-promise.md)
- [Removes deprecated Payment Intents, Setup Intents, and Sources methods from Stripe.js](https://docs.stripe.com/changelog/dahlia/2026-03-25/remove-legacy-stripejs-methods.md)
- [Renames Checkout initialisation method](https://docs.stripe.com/changelog/dahlia/2026-03-25/rename-init-checkout-to-init-checkout-elements.md)
- [Renames Embedded Checkout initialisation method](https://docs.stripe.com/changelog/dahlia/2026-03-25/rename-init-embedded-checkout-to-create-embedded-checkout-page.md)
