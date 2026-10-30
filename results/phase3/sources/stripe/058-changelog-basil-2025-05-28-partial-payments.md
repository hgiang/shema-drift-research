# Adds support for partial payments on invoices

## What’s new

We added support for attaching multiple Payment Intents to an Invoice. Allowing partial payments and multiple payments on invoices provides greater flexibility for businesses and customers in managing payments and cash flow. We also introduced the `invoice_payment.paid` webhook to track when an attached payment transitions to the `paid` status. To support issuing credit notes for partially paid invoices, we added a `mixed` type, `pre_payment_amount` field, and `post_payment_amount` field to credit note objects.

## Impact

### Attach multiple payments to an invoice

You can now use the [Attach Payment API](https://docs.stripe.com/api/invoices/attach_payment.md?api-version=2025-05-28.basil) to attach multiple payments to an invoice:

```curl
curl https://api.stripe.com/v1/invoices/{INVOICE_ID}/attach_payment \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d payment_intent={PAYMENT_INTENT_ID} \
  -d "expand[]=payments"
```

### Issue credit notes for partially paid invoices

You can continue to use the [Create Credit Note](https://docs.stripe.com/api/credit_notes/create.md?api-version=2025-05-28.basil) method to issue credit notes for partially paid invoices. A credit note first reduces the invoice’s `amount_remaining` (and `amount_due`), but not below zero. The `pre_payment_amount` field on the credit note object tracks this portion. The remaining amount after reducing the invoice’s `amount_remaining` to zero applies to the `post_payment_amount` field on the credit note object. A credit note has a `mixed` type if both the `pre_payment_amount` and the `post_payment_amount` are non-zero.

For more information about issuing credit notes, see the [Create Credit Notes API](https://docs.stripe.com/api/credit_notes/create.md?api-version=2025-05-28.basil).

## Changes

#### REST API

| Endpoint | Change | Resource |
| --- | --- | --- |
| `attach_payment` | Added | [Invoice](/api/invoices/object?api-version=2025-05-28.basil) |

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `post_payment_amount`, `pre_payment_amount` | Added | [CreditNote](/api/credit_notes/object?api-version=2025-05-28.basil) |

| Values | Change | Enums |
| --- | --- | --- |
| `invoice_payment.paid` | Added | [Event.type](/api/events/object?api-version=2025-05-28.basil#event_object-type) |
| `invoice_payment.paid` | Added | [WebhookEndpoint#create.enabled_events](/api/webhook_endpoints/create?api-version=2025-05-28.basil#create_webhook_endpoint-enabled_events), [WebhookEndpoint#update.enabled_events](/api/webhook_endpoints/update?api-version=2025-05-28.basil#update_webhook_endpoint-enabled_events) |
| `mixed` | Added | [CreditNote.type](/api/credit_notes/object?api-version=2025-05-28.basil#credit_note_object-type) |

|  | Change | Event type |
| --- | --- | --- |
| `invoice_payment.paid` | Added | [InvoicePayment](/api/invoice-payment/object?api-version=2025-05-28.basil) |

#### Ruby

| Method | Change | Resource |
| --- | --- | --- |
| `attach_payment` | Added | [Invoice](/api/invoices/object?api-version=2025-05-28.basil) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `post_payment_amount`, `pre_payment_amount` | Added | [CreditNote](/api/credit_notes/object?api-version=2025-05-28.basil) |

#### Python

| Method | Change | Resource |
| --- | --- | --- |
| `attach_payment` | Added | [Invoice](/api/invoices/object?api-version=2025-05-28.basil) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `post_payment_amount`, `pre_payment_amount` | Added | [CreditNote](/api/credit_notes/object?api-version=2025-05-28.basil) |

| Values | Change | Enums |
| --- | --- | --- |
| `mixed` | Added | [CreditNote.type](/api/credit_notes/object?api-version=2025-05-28.basil#credit_note_object-type) |
| `invoice_payment.paid` | Added | [Event.type](/api/events/object?api-version=2025-05-28.basil#event_object-type) |

#### PHP

| Method | Change | Resource |
| --- | --- | --- |
| `attach_payment` | Added | [Invoice](/api/invoices/object?api-version=2025-05-28.basil) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `post_payment_amount`, `pre_payment_amount` | Added | [CreditNote](/api/credit_notes/object?api-version=2025-05-28.basil) |

| Values | Change | Enums |
| --- | --- | --- |
| `mixed` | Added | [CreditNote.type](/api/credit_notes/object?api-version=2025-05-28.basil#credit_note_object-type) |
| `invoice_payment.paid` | Added | [Event.type](/api/events/object?api-version=2025-05-28.basil#event_object-type) |

#### Java

| Method | Change | Resource |
| --- | --- | --- |
| `attach_payment` | Added | [Invoice](/api/invoices/object?api-version=2025-05-28.basil) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `postPaymentAmount`, `prePaymentAmount` | Added | [CreditNote](/api/credit_notes/object?api-version=2025-05-28.basil) |

| Value | Change | Enums |
| --- | --- | --- |
| `invoice_payment.paid` | Added | [WebhookEndpointCreateParams.enabledEvents](/api/webhook_endpoints/create?api-version=2025-05-28.basil#create_webhook_endpoint-enabled_events), [WebhookEndpointUpdateParams.enabledEvents](/api/webhook_endpoints/update?api-version=2025-05-28.basil#update_webhook_endpoint-enabled_events) |

|  | Change | Event type |
| --- | --- | --- |
| `invoice_payment.paid` | Added | [InvoicePayment](/api/invoice-payment/object?api-version=2025-05-28.basil) |

#### Node.js

| Method | Change | Resource |
| --- | --- | --- |
| `attach_payment` | Added | [Invoice](/api/invoices/object?api-version=2025-05-28.basil) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `post_payment_amount`, `pre_payment_amount` | Added | [CreditNote](/api/credit_notes/object?api-version=2025-05-28.basil) |

| Values | Change | Enums |
| --- | --- | --- |
| `mixed` | Added | [CreditNote.type](/api/credit_notes/object?api-version=2025-05-28.basil#credit_note_object-type) |
| `invoice_payment.paid` | Added | [Event.type](/api/events/object?api-version=2025-05-28.basil#event_object-type) |

#### Go

| Method | Change | Resource |
| --- | --- | --- |
| `AttachPayment` | Added | [Invoice](/api/invoices/object?api-version=2025-05-28.basil) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PostPaymentAmount`, `PrePaymentAmount` | Added | [CreditNote](/api/credit_notes/object?api-version=2025-05-28.basil) |

| Values | Change | Enums |
| --- | --- | --- |
| `invoice_payment.paid` | Added | [Event.Type](/api/events/object?api-version=2025-05-28.basil#event_object-type) |
| `mixed` | Added | [CreditNote.Type](/api/credit_notes/object?api-version=2025-05-28.basil#credit_note_object-type) |

#### .NET

| Method | Change | Resource |
| --- | --- | --- |
| `AttachPayment` | Added | [Invoice](/api/invoices/object?api-version=2025-05-28.basil) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PostPaymentAmount`, `PrePaymentAmount` | Added | [CreditNote](/api/credit_notes/object?api-version=2025-05-28.basil) |

|  | Change | Event type |
| --- | --- | --- |
| `InvoicePaymentPaid` | Added | [InvoicePayment](/api/invoice-payment/object?api-version=2025-05-28.basil) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-05-28.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.2.0](https://github.com/stripe/stripe-python/releases/tag/v12.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.3.0](https://github.com/stripe/stripe-php/releases/tag/v17.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.2.0](https://github.com/stripe/stripe-java/releases/tag/v29.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.2.0](https://github.com/stripe/stripe-node/releases/tag/v18.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.2.0](https://github.com/stripe/stripe-go/releases/tag/v82.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
