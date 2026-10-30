# Adds address validation for physical cards

## What’s new

Lets you specify the address validation mode for shipping addresses on physical cards when you [Create a card](https://docs.stripe.com/api/issuing/cards/create.md?api-version=2024-09-30.acacia). You can also update the shipping addresses on physical cards when you [Update a card](https://docs.stripe.com/api/issuing/cards/update.md?api-version=2024-09-30.acacia).

## Impact

This change increases the accuracy of the shipping address provided by the user by validating and normalising the address provided by the user

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `address_validation` | Added | [Issuing.Card#create.shipping](/api/issuing/cards/create?api-version=2024-09-30.acacia#create_issuing_card-shipping), [Issuing.Card.shipping](/api/issuing/cards/object?api-version=2024-09-30.acacia#issuing_card_object-shipping) |
| `shipping` | Added | [Issuing.Card#update](/api/issuing/cards/update?api-version=2024-09-30.acacia) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `address_validation` | Added | [stripe.issuing.Card.CreateParamsShipping](/api/issuing/cards/create?api-version=2024-09-30.acacia#create_issuing_card-shipping), [stripe.issuing.Card.Shipping](/api/issuing/cards/object?api-version=2024-09-30.acacia#issuing_card_object-shipping) |
| `shipping` | Added | [stripe.issuing.Card.ModifyParams](/api/issuing/cards/update?api-version=2024-09-30.acacia) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `address_validation` | Added | [Issuing.Card.shipping](/api/issuing/cards/object?api-version=2024-09-30.acacia#issuing_card_object-shipping), [issuing.CardCreateParams.shipping](/api/issuing/cards/create?api-version=2024-09-30.acacia#create_issuing_card-shipping) |
| `shipping` | Added | [issuing.CardUpdateParams](/api/issuing/cards/update?api-version=2024-09-30.acacia) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `address_validation` | Added | [Issuing.Card.shipping](/api/issuing/cards/object?api-version=2024-09-30.acacia#issuing_card_object-shipping), [Issuing.CardCreateParams.shipping](/api/issuing/cards/create?api-version=2024-09-30.acacia#create_issuing_card-shipping) |
| `shipping` | Added | [Issuing.CardUpdateParams](/api/issuing/cards/update?api-version=2024-09-30.acacia) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AddressValidation` | Added | [IssuingCardShippingParams](/api/issuing/cards/create?api-version=2024-09-30.acacia#create_issuing_card-shipping), [IssuingCardShipping](/api/issuing/cards/object?api-version=2024-09-30.acacia#issuing_card_object-shipping) |
| `Shipping` | Added | [IssuingCardParams](/api/issuing/cards/update?api-version=2024-09-30.acacia) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AddressValidation` | Added | [IssuingCardShippingOptions](/api/issuing/cards/create?api-version=2024-09-30.acacia#create_issuing_card-shipping), [IssuingCardShipping](/api/issuing/cards/object?api-version=2024-09-30.acacia#issuing_card_object-shipping) |
| `Shipping` | Added | [Issuing.CardUpdateOptions](/api/issuing/cards/update?api-version=2024-09-30.acacia) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-09-30.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.0.0](https://github.com/stripe/stripe-python/releases/tag/v11.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.0.0](https://github.com/stripe/stripe-php/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v27.0.0](https://github.com/stripe/stripe-java/releases/tag/v27.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.0.0](https://github.com/stripe/stripe-node/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v80.0.0](https://github.com/stripe/stripe-go/releases/tag/v80.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v46.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v46.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Updates the default value for shipping address validation](https://docs.stripe.com/changelog/acacia/2024-09-30/card-shipping-status-submitted-address-validation.md)
- [Adds a new webhook event for when funds are deducted as part of a dispute](https://docs.stripe.com/changelog/acacia/2024-09-30/issuing-webhook-fund-deduction.md)
