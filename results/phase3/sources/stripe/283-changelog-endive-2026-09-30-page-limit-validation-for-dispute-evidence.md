# Adds page limit validation for dispute evidence

## What’s new

Stripe now validates the estimated compiled page count of [evidence](https://docs.stripe.com/api/disputes/update.md?api-version=2026-09-30.preview#update_dispute-evidence) submitted when you [update a dispute](https://docs.stripe.com/api/disputes/update.md?api-version=2026-09-30.preview). If the estimated page count of your text fields and file uploads exceeds the network page limit, the API returns a `400` [error](https://docs.stripe.com/api/errors.md?api-version=2026-09-30.preview) with the code `dispute_evidence_page_limit_exceeded`. This validation applies whether or not you set [submit](https://docs.stripe.com/api/disputes/update.md?api-version=2026-09-30.preview#update_dispute-submit) to `true`, so you can catch oversized evidence before final submission.

## Why is this a breaking change?

Previously, you could [update a dispute](https://docs.stripe.com/api/disputes/update.md?api-version=2026-09-30.preview) with evidence of any length. Now, if evidence exceeds the compiled page limit, the request fails and returns a `400` `invalid_request_error` with the code `dispute_evidence_page_limit_exceeded`.

## Impact

If your integration submits [dispute](https://docs.stripe.com/disputes.md) evidence through the API, requests that exceed the page limit now return a `400` error instead of succeeding. Update your error handling to check for the `dispute_evidence_page_limit_exceeded` error code. To resolve the error, shorten text fields or reduce the number of pages in uploaded files to stay within the limit.

## Changes

#### REST API

| Code | Change |  |
| --- | --- | --- |
| `dispute_evidence_page_limit_exceeded` | Added | `QuotePreviewInvoice.last_finalization_error` |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Code | Change |  |
| --- | --- | --- |
| `dispute_evidence_page_limit_exceeded` | Added | `QuotePreviewInvoice.LastFinalizationError` |

#### PHP

| Code | Change |  |
| --- | --- | --- |
| `dispute_evidence_page_limit_exceeded` | Added | `QuotePreviewInvoice.last_finalization_error` |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Code | Change |  |
| --- | --- | --- |
| `dispute_evidence_page_limit_exceeded` | Added | `QuotePreviewInvoice.last_finalization_error` |

#### Go

| Code | Change |  |
| --- | --- | --- |
| `dispute_evidence_page_limit_exceeded` | Added | `QuotePreviewInvoiceLastFinalizationError` |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.preview`
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

- [Removes the capture method parameter for PayPay payments](https://docs.stripe.com/changelog/endive/2026-09-30/removes-capture-method-parameter-for-paypay-payments.md)
- [Adds the ability to update payment intent data on Checkout Sessions](https://docs.stripe.com/changelog/endive/2026-09-30/update-payment-intent-data-on-checkout-sessions.md)
- [Adds support for submitting evidence to appeal a dispute decision](https://docs.stripe.com/changelog/endive/2026-09-30/submit-evidence-to-appeal-dispute-decision.md)
- [Adds support for specifying card-on-file usage when saving and charging saved cards](https://docs.stripe.com/changelog/endive/2026-09-30/add-card-on-file-usage-indicators.md)
