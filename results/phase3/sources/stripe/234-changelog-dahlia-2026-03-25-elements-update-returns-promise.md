# Updates the elements.update() method to return a Promise

## What’s new

Adds support for `async` and `await` patterns when updating an `Elements` object by changing the [elements.update()](https://docs.stripe.com/js/elements_object/update) method to return a `Promise<void>`.

The method returns the `Promise` when the update has been applied to all rendered `Elements`.

This update aligns `elements.update()` with other async Elements methods like `elements.submit()` and `elements.fetchUpdates()`. The `update-end` event remains available for backward compatibility.

## Why is this a breaking change?

The return type of `elements.update()` has changed from `void` to `Promise<void>`. TypeScript integrations that explicitly type the return value need to update their types. If your integration otherwise expects `elements.update()` to return `void`, you might also need to update your code.

## Impact

You can now use `async` or `await` when calling `elements.update()` to wait for the update to complete before performing subsequent operations.

The following code shows an example of using the `update-end` event listener:

```js
// Existing event-based pattern
elements.update({locale: 'fr'});
elements.on('update-end', () => {
// Update is complete
});
```

If your integration uses the event listener, you can update it to use `async` or `await`, as in the following example:

```js
// New await pattern
await elements.update({locale: 'fr'});
// Update is complete
```

You can also continue to use the event listener. However, if you have any TypeScript code that explicitly types the return value of `elements.update()` as `void`, you must update it to type the return value as `Promise<void>`.

## Related changes

- [Changes the Address Element state field to default to Latin-formatted characters](https://docs.stripe.com/changelog/dahlia/2026-03-25/address-element-getvalue-and-change-event-formatting.md)
- [Removes support for boolean values in options.layout.radios](https://docs.stripe.com/changelog/dahlia/2026-03-25/disallow-booleans-for-radios.md)
- [Removes deprecated Payment Intents, Setup Intents, and Sources methods from Stripe.js](https://docs.stripe.com/changelog/dahlia/2026-03-25/remove-legacy-stripejs-methods.md)
- [Renames Checkout initialisation method](https://docs.stripe.com/changelog/dahlia/2026-03-25/rename-init-checkout-to-init-checkout-elements.md)
- [Renames Embedded Checkout initialisation method](https://docs.stripe.com/changelog/dahlia/2026-03-25/rename-init-embedded-checkout-to-create-embedded-checkout-page.md)
