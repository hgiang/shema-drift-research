# Requires billing details when Payment Element collection is disabled

## What’s new

Requires [Elements with the Checkout Sessions API](https://docs.stripe.com/payments/quickstart.md) integrations to provide required billing details for any field disabled on the Payment Element, starting with Endive. If you set a billing field to `never` in the [Payment Element configuration](https://docs.stripe.com/js/custom_checkout/create_payment_element#custom_checkout_create_payment_element-options-fields-billingDetails), the Payment Element no longer collects that field and you’re responsible for supplying required billing data through another Element or a supported Custom Checkout SDK method.

If a required billing field is still missing when you call [checkout.confirm()](https://docs.stripe.com/js/custom_checkout/confirm), Stripe.js throws an integration error. Optional fields such as `address.line2` are exempt from this validation.

## Why is this a breaking change?

Previously, `checkout.confirm()` could succeed even when a required billing field configured as `never` wasn’t provided through another source. Starting with Endive, these integrations fail at confirmation with an integration error.

If you currently set any [fields.billingDetails](https://docs.stripe.com/js/custom_checkout/create_payment_element#custom_checkout_create_payment_element-options-fields-billingDetails) value to `never` without providing the corresponding required data, your integration is affected. Previous Stripe.js major versions retain the earlier behaviour.

## Impact

If your integration disables any billing-details fields on the Payment Element, provide the corresponding data before calling `checkout.confirm()`. Use one of the following approaches depending on the type of billing data. For a full walkthrough of address collection with Custom Checkout, see [Collect physical addresses](https://docs.stripe.com/payments/collect-addresses.md).

If your integration collects specific billing details itself, set only those fields to `never` and leave the remaining fields as `auto`. The Payment Element can then collect the remaining fields when the selected payment method requires them.

Set `fields.billingDetails` to `never` only if your integration collects all billing details itself. In this configuration, the Payment Element doesn’t collect any billing details, so you must collect and provide every applicable billing field through another Element or supported Custom Checkout SDK method.

### Name and address

- Call [updateBillingAddress](https://docs.stripe.com/js/custom_checkout/update_billing_address) to set the billing address before confirmation.
- Pass a [billingAddress](https://docs.stripe.com/js/custom_checkout/confirm#custom_checkout_session_confirm-options-billingAddress) option to `checkout.confirm()`.
- Use the [Billing Address Element](https://docs.stripe.com/js/custom_checkout/create_billing_address_element) to collect billing addresses through a dedicated Element.

If you use automatic tax and disable billing address collection in the Payment Element, don’t pass `billingAddress` to `checkout.confirm()`. Instead, provide the tax address using the [Address Element](https://docs.stripe.com/elements/address-element.md) or `updateBillingAddress()`. See [Collect tax with Elements](https://docs.stripe.com/tax/checkout/elements.md) for details.

### Email

- Call [updateEmail](https://docs.stripe.com/js/custom_checkout/update_email) to set the email before confirmation.
- Pass an [email](https://docs.stripe.com/js/custom_checkout/confirm#custom_checkout_session_confirm-options-email) option to `checkout.confirm()`.

### Phone

- Enable [phone_number_collection.enabled](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-09-30.endive#create_checkout_session-phone_number_collection-enabled) on the Checkout Session.
- Call [updatePhoneNumber](https://docs.stripe.com/js/custom_checkout/update_phone_number) to set the phone number before confirmation.
- Pass a [phoneNumber](https://docs.stripe.com/js/custom_checkout/confirm#custom_checkout_session_confirm-options-phoneNumber) option to `checkout.confirm()`.
