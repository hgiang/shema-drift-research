# Changes the Address Element state field to default to Latin-formatted characters

## What’s new

Changes the [state](https://docs.stripe.com/js/elements_object/create_address_element#address_element_create-options-defaultValues-address-state) property of the Address Element to default to Latin character formatting. Previously, the [getValue()](https://docs.stripe.com/js/elements_object/get_value_address_element) method and [billing or shipping address change event](https://docs.stripe.com/js/custom_checkout/element_events/on_change?type=billingAddressElement#custom_checkout_element_on_change-event) would return the `state` value in a format matching the user’s browser locale.

## Why is this a breaking change?

If your code expects the Address Element `state` to be in a browser-localised format by default, you must update it to expect a Latin-formatted `state` or to explicitly request the localised format. You can only request a localised value by passing the `format: localized` option to `getValue()`. The address change event always returns a Latin-formatted `state`.

## Impact

You can now expect the `state` property of the Address Element to be formatted in Latin characters unless you explicitly request a localised value. To retrieve the value localised according to the user’s browser settings, call `getValue()` with the `format` option set to `localized`.

If you want to retrieve the localised value from an address change event, you can call `getValue({format: 'localized'})` in the event callback.

## Related changes

- [Updates the elements.update() method to return a Promise](https://docs.stripe.com/changelog/dahlia/2026-03-25/elements-update-returns-promise.md)
- [Removes support for boolean values in options.layout.radios](https://docs.stripe.com/changelog/dahlia/2026-03-25/disallow-booleans-for-radios.md)
- [Removes deprecated Payment Intents, Setup Intents, and Sources methods from Stripe.js](https://docs.stripe.com/changelog/dahlia/2026-03-25/remove-legacy-stripejs-methods.md)
- [Renames Checkout initialisation method](https://docs.stripe.com/changelog/dahlia/2026-03-25/rename-init-checkout-to-init-checkout-elements.md)
- [Renames Embedded Checkout initialisation method](https://docs.stripe.com/changelog/dahlia/2026-03-25/rename-init-embedded-checkout-to-create-embedded-checkout-page.md)
