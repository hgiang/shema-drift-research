# Allows empty optional address fields in Elements with Checkout Sessions

## What’s new

Stops applying format validation to empty optional address fields in [Elements with the Checkout Sessions API](https://docs.stripe.com/payments/quickstart.md). Previously, an empty optional field, such as a postal code in a country where postal codes aren’t required, could prevent confirmation because the empty value failed format validation.

## Why is this a breaking change?

Starting with Endive, customers can confirm a Checkout Session without entering address fields that are optional for their country. Previous Stripe.js major versions retain the stricter behaviour, which might affect integrations that rely on Stripe.js to require these fields.

## Impact

Customers are no longer blocked from confirming because they left an optional address field empty. Stripe.js continues to validate the format when a customer provides a value. If your integration requires a field that Stripe considers optional, [collect and validate the address in your own form](https://docs.stripe.com/payments/advanced/collect-addresses.md?payment-ui=embedded-components) before confirming the Checkout Session.
