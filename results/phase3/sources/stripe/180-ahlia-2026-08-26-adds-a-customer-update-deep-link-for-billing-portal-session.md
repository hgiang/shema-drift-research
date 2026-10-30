# Adds a customer update deep link for billing portal sessions

## What’s new

Adds `customer_update` as a value for the [flow_data.type](https://docs.stripe.com/api/customer_portal/sessions/create.md?api-version=2026-08-26.dahlia#create_portal_session-flow_data-type) parameter when you [create a billing portal session](https://docs.stripe.com/api/customer_portal/sessions/create.md?api-version=2026-08-26.dahlia). Setting this value creates a deep link that navigates your customer directly to the billing information page in the customer portal, where they can update their details. This is consistent with existing deep-link flow types such as `payment_method_update`, `subscription_cancel` and `subscription_update`.

## Impact

You can now create billing portal sessions that link customers directly to the billing information update page by setting `flow_data.type` to `customer_update`. No changes are required for existing integrations.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `customer_update` | Added | [BillingPortal.Session.flow](/api/customer_portal/sessions/object?api-version=2026-08-26.dahlia#portal_session_object-flow) |

| Value | Change | Enums |
| --- | --- | --- |
| `customer_update` | Added | [BillingPortal.Session#create.flow_data.type](/api/customer_portal/sessions/create?api-version=2026-08-26.dahlia#create_portal_session-flow_data-type), [BillingPortal.Session.flow.type](/api/customer_portal/sessions/object?api-version=2026-08-26.dahlia#portal_session_object-flow-type) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `customer_update` | Added | [BillingPortal::Session::Flow](/api/customer_portal/sessions/object?api-version=2026-08-26.dahlia#portal_session_object-flow) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `customer_update` | Added | [BillingPortal.Session.Flow](/api/customer_portal/sessions/object?api-version=2026-08-26.dahlia#portal_session_object-flow) |

| Value | Change | Enums |
| --- | --- | --- |
| `customer_update` | Added | [billing_portal.SessionCreateParamsFlowDatum.type](/api/customer_portal/sessions/create?api-version=2026-08-26.dahlia#create_portal_session-flow_data-type), [BillingPortal.Session.Flow.type](/api/customer_portal/sessions/object?api-version=2026-08-26.dahlia#portal_session_object-flow-type) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `customer_update` | Added | [BillingPortal.Session.flow](/api/customer_portal/sessions/object?api-version=2026-08-26.dahlia#portal_session_object-flow) |

| Value | Change | Enum |
| --- | --- | --- |
| `customer_update` | Added | [BillingPortal.Session.flow.type](/api/customer_portal/sessions/object?api-version=2026-08-26.dahlia#portal_session_object-flow-type) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `customerUpdate` | Added | [billingportal.Session.flow](/api/customer_portal/sessions/object?api-version=2026-08-26.dahlia#portal_session_object-flow) |

| Value | Change | Enum |
| --- | --- | --- |
| `customer_update` | Added | [billingportal.SessionCreateParams.flow_data.type](/api/customer_portal/sessions/create?api-version=2026-08-26.dahlia#create_portal_session-flow_data-type) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `customer_update` | Added | [BillingPortal.Session.flow](/api/customer_portal/sessions/object?api-version=2026-08-26.dahlia#portal_session_object-flow) |

| Value | Change | Enums |
| --- | --- | --- |
| `customer_update` | Added | [BillingPortal.SessionCreateParams.flow_data.type](/api/customer_portal/sessions/create?api-version=2026-08-26.dahlia#create_portal_session-flow_data-type), [BillingPortal.Session.flow.type](/api/customer_portal/sessions/object?api-version=2026-08-26.dahlia#portal_session_object-flow-type) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CustomerUpdate` | Added | [BillingPortalSessionFlow](/api/customer_portal/sessions/object?api-version=2026-08-26.dahlia#portal_session_object-flow) |

| Value | Change | Enum |
| --- | --- | --- |
| `customer_update` | Added | [BillingPortalSessionFlow.Type](/api/customer_portal/sessions/object?api-version=2026-08-26.dahlia#portal_session_object-flow-Type) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CustomerUpdate` | Added | [BillingPortal.Session.Flow](/api/customer_portal/sessions/object?api-version=2026-08-26.dahlia#portal_session_object-flow) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-08-26.dahlia`
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

- [Adds the ability to query entitlements and launch the customer portal in Customer Sessions](https://docs.stripe.com/changelog/dahlia/2026-08-26/customer-session-improvements.md)
- [Adds frozen fields property to Invoice Items](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-frozen-fields-property-to-invoice-items.md)
- [Adds support for the Billie payment method for invoices and subscriptions](https://docs.stripe.com/changelog/dahlia/2026-08-26/billie-support-for-invoices-and-subscriptions.md)
- [Increases the subscription item limit](https://docs.stripe.com/changelog/dahlia/2026-08-26/flexible-subscription-item-limits.md)
