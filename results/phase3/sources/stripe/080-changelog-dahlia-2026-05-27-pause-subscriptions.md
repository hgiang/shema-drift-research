# Adds the subscription pause endpoint

## What’s new

Adds the [pause](https://docs.stripe.com/api/subscriptions/pause.md?api-version=2026-05-27.preview) endpoint to the [Subscriptions](https://docs.stripe.com/api/subscriptions.md?api-version=2026-05-27.preview) API. Paused subscriptions have `paused` status and include a [status_details](https://docs.stripe.com/api/subscriptions/object.md?api-version=2026-05-27.preview#subscription_object-status_details) field.

Also adds the [payment_behavior](https://docs.stripe.com/api/subscriptions/resume.md?api-version=2026-05-27.preview#resume_subscription-payment_behavior) parameter to the [resume](https://docs.stripe.com/api/subscriptions/resume.md?api-version=2026-05-27.preview) endpoint to control how the subscription resumes:

- `resume_on_payment_success` (Recommended): attempts payment during the resume request. The subscription stays `paused` until payment succeeds, and Stripe retries failed payments.
- `resume_on_payment_attempt` (Default): no payment attempt during the resume request. If collecting payment on the resumed subscription’s invoice fails (for example with Pay Invoice), the subscription moves to `past_due` and Stripe doesn’t retry failed payments.

## Impact

You can now pause an active subscription to suspend both service delivery and invoice generation until you resume it. This gives your customers a temporary alternative to cancelling for scenarios like vacations, temporary non-usage, or goodwill holds. This differs from [pause payment collection](https://docs.stripe.com/billing/subscriptions/pause-payment.md), which keeps access and invoicing running and only pauses collection. Pausing requires [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md).

You can listen for [customer.subscription.paused](https://docs.stripe.com/api/events/types.md?api-version=2026-05-27.preview#event_types-customer.subscription.paused) to revoke service access and [customer.subscription.resumed](https://docs.stripe.com/api/events/types.md?api-version=2026-05-27.preview#event_types-customer.subscription.resumed) to restore it.

For full integration guidance, including restrictions, events and code examples, see [Pause subscriptions](https://docs.stripe.com/billing/subscriptions/pause.md).

## Changes

#### REST API

| Endpoint | Change | Resource |
| --- | --- | --- |
| `pause` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `payment_behavior` | Added | [Subscription#resume](/api/subscriptions/resume?api-version=2026-05-27.preview#resume_subscription) |
| `status_details` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

#### Ruby

| Method | Change | Resource |
| --- | --- | --- |
| `pause` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `payment_behavior` | Added | [SubscriptionResumeParams](/api/subscriptions/resume?api-version=2026-05-27.preview#resume_subscription) |
| `status_details` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

#### Python

| Method | Change | Resource |
| --- | --- | --- |
| `pause` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `payment_behavior` | Added | [SubscriptionResumeParams](/api/subscriptions/resume?api-version=2026-05-27.preview#resume_subscription) |
| `status_details` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

#### PHP

| Method | Change | Resource |
| --- | --- | --- |
| `pause` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `payment_behavior` | Added | [Subscription.resume().$params](/api/subscriptions/resume?api-version=2026-05-27.preview#resume_subscription) |
| `status_details` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

#### Java

| Method | Change | Resource |
| --- | --- | --- |
| `pause` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `paymentBehavior` | Added | [SubscriptionResumeParams](/api/subscriptions/resume?api-version=2026-05-27.preview#resume_subscription) |
| `statusDetails` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

#### Node.js

| Method | Change | Resource |
| --- | --- | --- |
| `pause` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `payment_behavior` | Added | [SubscriptionResumeParams](/api/subscriptions/resume?api-version=2026-05-27.preview#resume_subscription) |
| `status_details` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

#### Go

| Method | Change | Resource |
| --- | --- | --- |
| `Pause` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PaymentBehavior` | Added | [SubscriptionResumeParams](/api/subscriptions/resume?api-version=2026-05-27.preview#resume_subscription) |
| `StatusDetails` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

#### .NET

| Method | Change | Resource |
| --- | --- | --- |
| `Pause` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PaymentBehavior` | Added | [SubscriptionResumeOptions](/api/subscriptions/resume?api-version=2026-05-27.preview#resume_subscription) |
| `StatusDetails` | Added | [Subscription](/api/subscriptions/object?api-version=2026-05-27.preview#subscription_object) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-05-27.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Billed until property on subscription items is no longer included in responses by default](https://docs.stripe.com/changelog/dahlia/2026-05-27/subscription-item-billed-until-includable.md)
- [Enables expansion of trial offer prices](https://docs.stripe.com/changelog/dahlia/2026-05-27/trial-offer-prices-expansion.md)
