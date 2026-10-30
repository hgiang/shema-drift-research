# Adds support for script coupons

## What’s new

You can now customise business logic on Stripe using [scripts](https://docs.stripe.com/billing/scripts.md). With scripts, you can define custom logic expressed as code that runs on our infrastructure, extending Stripe’s core functionality. Use scripts to customise business login on Stripe logic using Stripe’s [Coupon](https://docs.stripe.com/api/coupons/object.md?api-version=2025-04-30.preview) object. Currently, you can only associate a script with this specific type of object.

### Custom discounting logic

To support the customisation of discounting logic with scripts, we added a new `script` parameter on the [Coupon create](https://docs.stripe.com/api/coupons/create.md?api-version=2025-04-30.preview) method. With this new parameter, you can configure a `Coupon` to use the custom discounting logic.

The `script` parameter has two required nested parameters: `id` and `configuration`. `id` is the script ID and [configuration](https://docs.stripe.com/billing/scripts.md) is any input parameter to the script.

The following example illustrates how to set up a coupon that gives the buyer 20% off up to 100 USD:

```curl
curl https://api.stripe.com/v1/coupons \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d duration=once \
  -d "name=My coupon" \
  -d "script[id]=bfsimpl_61S9T2y7zlKu9YlG116S8pZoN2SQpuwOX348dhXM0R9c" \
  -d "script[configuration][max_discount_amount][amount]=10000" \
  -d "script[configuration][max_discount_amount][currency]=usd" \
  -d "script[configuration][discount_percent]=20"
```

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `script` | Added | [Coupon#create](/api/coupons/create?api-version=2025-04-30.preview), [Coupon](/api/coupons/object?api-version=2025-04-30.preview) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `script` | Added | [Coupon::CreateParams](/api/coupons/create?api-version=2025-04-30.preview), [Coupon](/api/coupons/object?api-version=2025-04-30.preview) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `script` | Added | [Coupon.CreateParams](/api/coupons/create?api-version=2025-04-30.preview), [Coupon](/api/coupons/object?api-version=2025-04-30.preview) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `script`, `type` | Added | [Coupon](/api/coupons/object?api-version=2025-04-30.preview) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `script` | Added | [CouponCreateParams](/api/coupons/create?api-version=2025-04-30.preview), [Coupon](/api/coupons/object?api-version=2025-04-30.preview) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `script` | Added | [CouponCreateParams](/api/coupons/create?api-version=2025-04-30.preview), [Coupon](/api/coupons/object?api-version=2025-04-30.preview) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Script` | Added | [CouponParams](/api/coupons/create?api-version=2025-04-30.preview), [Coupon](/api/coupons/object?api-version=2025-04-30.preview) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Script` | Added | [CouponCreateOptions](/api/coupons/create?api-version=2025-04-30.preview), [Coupon](/api/coupons/object?api-version=2025-04-30.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-04-30.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.2.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v15.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.2.0b1](https://github.com/stripe/stripe-python/releases/tag/v12.2.0b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.3.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v17.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.2.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v29.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.2.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v18.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.2.0-beta.2](https://github.com/stripe/stripe-go/releases/tag/v82.2.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.2.0-beta.2](https://github.com/stripe/stripe-dotnet/releases/tag/v48.2.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
