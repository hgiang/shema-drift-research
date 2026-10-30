# Adds the Orchestrated Commerce Agreements API to manage relationships for agentic commerce integrations

## What’s new

Adds the Orchestrated Commerce Agreements (OCAs) API to help you manage relationships with other businesses for agentic commerce integrations. You can use the [Agreements](https://docs.stripe.com/api/v2/orchestrated-commerce/agreements.md?api-version=2026-04-22.preview) API to create, confirm, list, retrieve and terminate agreements programmatically.

This API also includes webhook events that notify you when an agreement state changes, including: `created`, `partially_confirmed`, `confirmed` or `terminated`.

## Impact

Orchestrated Commerce Agreements establish the permissions needed to issue and process [Shared Payment Tokens (SPTs)](https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens.md) between an agent and seller. When an agent issues their first SPT to a seller, Stripe automatically creates and confirms an agreement on behalf of the agent. Processing a payment with the SPT confirms the agreement on behalf of the seller.

To establish agreements manually, use the `create` method to initiate an agreement and the `confirm` method to finalise it. Either party can terminate the agreement at any time to revoke access.

Set up webhook endpoints to listen for agreement state change events (`created`, `confirmed`, `partially_confirmed`, `terminated`) so your application can automatically respond to agreement updates and trigger the applicable business workflows in your system.

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [V2.OrchestratedCommerce.Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

| Endpoints | Change | Resource |
| --- | --- | --- |
| `confirm`, `create`, `list`, `retrieve`, `terminate` | Added | [V2.OrchestratedCommerce.Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2OrchestratedCommerceAgreementConfirmedEvent`, `V2OrchestratedCommerceAgreementCreatedEvent`, `V2OrchestratedCommerceAgreementPartiallyConfirmedEvent`, `V2OrchestratedCommerceAgreementTerminatedEvent` | Added | `V2.OrchestratedCommerce.Agreement` |

#### Ruby

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [V2::OrchestratedCommerce::Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `confirm`, `create`, `list`, `retrieve`, `terminate` | Added | [V2::OrchestratedCommerce::Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2OrchestratedCommerceAgreementConfirmedEvent`, `V2OrchestratedCommerceAgreementCreatedEvent`, `V2OrchestratedCommerceAgreementPartiallyConfirmedEvent`, `V2OrchestratedCommerceAgreementTerminatedEvent` | Added | `V2::OrchestratedCommerce::Agreement` |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [v2.orchestrated_commerce.Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `confirm`, `create`, `list`, `retrieve`, `terminate` | Added | [v2.orchestrated_commerce.Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2OrchestratedCommerceAgreementConfirmedEvent`, `V2OrchestratedCommerceAgreementCreatedEvent`, `V2OrchestratedCommerceAgreementPartiallyConfirmedEvent`, `V2OrchestratedCommerceAgreementTerminatedEvent` | Added | `v2.orchestrated_commerce.Agreement` |

#### PHP

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [V2.OrchestratedCommerce.Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `all`, `confirm`, `create`, `retrieve`, `terminate` | Added | [V2.OrchestratedCommerce.Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2OrchestratedCommerceAgreementConfirmedEvent`, `V2OrchestratedCommerceAgreementCreatedEvent`, `V2OrchestratedCommerceAgreementPartiallyConfirmedEvent`, `V2OrchestratedCommerceAgreementTerminatedEvent` | Added | `V2.OrchestratedCommerce.Agreement` |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [v2.orchestratedcommerce.Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `confirm`, `create`, `list`, `retrieve`, `terminate` | Added | [v2.orchestratedcommerce.Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2OrchestratedCommerceAgreementConfirmedEvent`, `V2OrchestratedCommerceAgreementCreatedEvent`, `V2OrchestratedCommerceAgreementPartiallyConfirmedEvent`, `V2OrchestratedCommerceAgreementTerminatedEvent` | Added | `v2.orchestratedcommerce.Agreement` |

#### Node.js

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [V2.OrchestratedCommerce.Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `confirm`, `create`, `list`, `retrieve`, `terminate` | Added | [V2.OrchestratedCommerce.Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2OrchestratedCommerceAgreementConfirmedEvent`, `V2OrchestratedCommerceAgreementCreatedEvent`, `V2OrchestratedCommerceAgreementPartiallyConfirmedEvent`, `V2OrchestratedCommerceAgreementTerminatedEvent` | Added | `V2.OrchestratedCommerce.Agreement` |

#### Go

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [V2OrchestratedCommerceAgreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Confirm`, `Get`, `List`, `New`, `Terminate` | Added | [V2OrchestratedCommerceAgreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2OrchestratedCommerceAgreementConfirmedEvent`, `V2OrchestratedCommerceAgreementCreatedEvent`, `V2OrchestratedCommerceAgreementPartiallyConfirmedEvent`, `V2OrchestratedCommerceAgreementTerminatedEvent` | Added | `V2OrchestratedCommerceAgreement` |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [V2.OrchestratedCommerce.Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Confirm`, `Create`, `Get`, `List`, `Terminate` | Added | [V2.OrchestratedCommerce.Agreement](/api/v2/orchestrated-commerce/agreements?api-version=2026-04-22.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2OrchestratedCommerceAgreementConfirmedEvent`, `V2OrchestratedCommerceAgreementCreatedEvent`, `V2OrchestratedCommerceAgreementPartiallyConfirmedEvent`, `V2OrchestratedCommerceAgreementTerminatedEvent` | Added | `V2.OrchestratedCommerce.Agreement` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-04-22.preview`
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

- [Adds the Shared Payment Granted Token for managing payment methods shared by agents](https://docs.stripe.com/changelog/dahlia/2026-04-22/shared-payment-granted-token.md)
- [Adds the SharedPaymentIssuedToken resource to allow agents to give sellers scoped access to a customer’s credentials](https://docs.stripe.com/changelog/dahlia/2026-04-22/shared-payment-issued-token.md)
