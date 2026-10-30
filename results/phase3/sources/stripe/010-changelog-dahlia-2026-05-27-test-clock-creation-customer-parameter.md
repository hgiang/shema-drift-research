# Adds customer parameter to test clock creation

## What’s new

You can now attach an existing customer when you [create a test clock](https://docs.stripe.com/api/test_clocks/create.md?api-version=2026-05-27.dahlia) by using the new [customer](https://docs.stripe.com/api/test_clocks/create.md?api-version=2026-05-27.dahlia#create_test_clock-customer) parameter.

The `customer` parameter accepts an existing customer ID and attaches that customer to the test clock during creation. After you attach a customer to a test clock, it can’t be removed.

## Impact

You can now programmatically create test clocks that are pre-attached to specific customers, streamlining your testing workflows. This eliminates the need to use the Dashboard for this functionality and allows you to fully automate your test clock setup through the API.

If you previously relied on Dashboard-only functionality to attach customers to test clocks, you can now incorporate this step directly into your API-based testing processes.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `customer` | Added | [TestHelpers.TestClock#create](/api/test_clocks/create?api-version=2026-05-27.dahlia#create_test_clock) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `customer` | Added | [TestHelpers::TestClockCreateParams](/api/test_clocks/create?api-version=2026-05-27.dahlia#create_test_clock) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `customer` | Added | [test_helpers.TestClockCreateParams](/api/test_clocks/create?api-version=2026-05-27.dahlia#create_test_clock) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `customer` | Added | [TestHelpers\TestClock.create().$params](/api/test_clocks/create?api-version=2026-05-27.dahlia#create_test_clock) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `customer` | Added | [testhelpers.TestClockCreateParams](/api/test_clocks/create?api-version=2026-05-27.dahlia#create_test_clock) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `customer` | Added | [TestHelpers.TestClockCreateParams](/api/test_clocks/create?api-version=2026-05-27.dahlia#create_test_clock) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Customer` | Added | [TestHelpersTestClockParams](/api/test_clocks/create?api-version=2026-05-27.dahlia#create_test_clock) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Customer` | Added | [TestHelpers.TestClockCreateOptions](/api/test_clocks/create?api-version=2026-05-27.dahlia#create_test_clock) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-05-27.dahlia`
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

- [Adds discount eligibility options for add-on invoice items on Subscriptions and Preview Invoice APIs](https://docs.stripe.com/changelog/dahlia/2026-05-27/invoice-items-discount-eligibility.md)
- [Adds amount paid off Stripe property to Invoice object](https://docs.stripe.com/changelog/dahlia/2026-05-27/invoice-object-amount-paid-off-stripe-property.md)
- [Adds billing schedules to enable prebilling on subscriptions](https://docs.stripe.com/changelog/dahlia/2026-05-27/subscriptions-billing-schedules.md)
- [Adds discount and discounts properties to pending subscription updates](https://docs.stripe.com/changelog/dahlia/2026-05-27/pending-subscription-updates-discount-and-discounts-properties.md)
- [Adds metadata support to pending subscription updates](https://docs.stripe.com/changelog/dahlia/2026-05-27/pending-subscription-update-metadata.md)
- [Adds credited items information to invoice item proration details](https://docs.stripe.com/changelog/dahlia/2026-05-27/invoice-item-proration-credited-items.md)
