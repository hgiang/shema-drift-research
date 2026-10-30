# Makes thin events for API v1 resources generally available

## What’s new

Expands thin events support to API v1 resources. You can now subscribe to thin events for supported API v1 resources and receive notifications when those resources change.

Thin events provide lightweight notifications that identify the affected resource. The notification includes a [related_object](https://docs.stripe.com/api/v2/core/events/object.md?api-version=2026-09-30.endive#v2_event_object-related_object) reference that identifies the affected resource and its API path, which you can use to retrieve the resource’s latest state. The [snapshot_event](https://docs.stripe.com/api/v2/core/events/object.md?api-version=2026-09-30.endive#v2_event_object-snapshot_event) property on a v2 Event identifies the corresponding API v1 Snapshot event. When available, the [changes](https://docs.stripe.com/api/v2/core/events/object.md?api-version=2026-09-30.endive#v2_event_object-changes) property provides the values captured before and after the event, equivalent to [previous_attributes](https://docs.stripe.com/api/events/object.md?api-version=2026-09-30.endive) on v1 [Events](https://docs.stripe.com/api/events/object.md?api-version=2026-09-30.endive).

API v1 thin event names use the `v1.` prefix. For example, subscribe to `v1.customer.created` instead of `customer.created`.

## Impact

You can use thin events for supported API v1 resources to receive lightweight, version-independent notifications and retrieve the latest state of the related resource.

### Migrate from snapshot events

To start using thin events instead of snapshot events, select **Thin** as the event format, and subscribe to the supported `v1.*` event types when you create or update an event destination. Update your event handler to retrieve the latest state of the related resource or the complete event.

See the [migration guide](https://docs.stripe.com/webhooks/migrate-snapshot-to-thin-events.md) for more details.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `snapshot_event` | Added | [V2.Core.Event](/api/v2/core/events/object?api-version=2026-09-30.endive#v2_event_object) |
| `customer`, `subscription` | Added | [EventsV1InvoiceUpcomingEvent](/api/v2/core/events/event-types?api-version=2026-09-30.endive#v2_event_types-v1.invoice.upcoming) |

|  | Change | Event types |
| --- | --- | --- |
| `V1AccountApplicationAuthorizedEvent`, `V1AccountApplicationDeauthorizedEvent`, `V1AccountExternalAccountCreatedEvent`, `V1AccountExternalAccountDeletedEvent`, `V1AccountExternalAccountUpdatedEvent`, `V1BillingPortalSessionCreatedEvent`, `V1EntitlementsActiveEntitlementSummaryUpdatedEvent` | Added | `` |
| `V1AccountUpdatedEvent` | Added | `Account` |
| `V1ApplicationFeeCreatedEvent`, `V1ApplicationFeeRefundedEvent` | Added | `ApplicationFee` |
| `V1ApplicationFeeRefundUpdatedEvent` | Added | `FeeRefund` |
| `V1BalanceAvailableEvent` | Added | `Balance` |
| `V1BalanceSettingsUpdatedEvent` | Added | `BalanceSettings` |
| `V1BillingAlertTriggeredEvent` | Added | `Billing.Alert` |
| `V1BillingCreditBalanceTransactionCreatedEvent` | Added | `Billing.CreditBalanceTransaction` |
| `V1BillingCreditGrantCreatedEvent`, `V1BillingCreditGrantUpdatedEvent` | Added | `Billing.CreditGrant` |
| `V1BillingMeterCreatedEvent`, `V1BillingMeterDeactivatedEvent`, `V1BillingMeterReactivatedEvent`, `V1BillingMeterUpdatedEvent` | Added | `Billing.Meter` |
| `V1BillingPortalConfigurationCreatedEvent`, `V1BillingPortalConfigurationUpdatedEvent` | Added | `BillingPortal.Configuration` |
| `V1CapabilityUpdatedEvent` | Added | `Capability` |
| `V1CashBalanceFundsAvailableEvent` | Added | `CashBalance` |
| `V1ChargeCapturedEvent`, `V1ChargeExpiredEvent`, `V1ChargeFailedEvent`, `V1ChargePendingEvent`, `V1ChargeRefundedEvent`, `V1ChargeSucceededEvent`, `V1ChargeUpdatedEvent` | Added | `Charge` |
| `V1ChargeDisputeClosedEvent`, `V1ChargeDisputeCreatedEvent`, `V1ChargeDisputeFundsReinstatedEvent`, `V1ChargeDisputeFundsWithdrawnEvent`, `V1ChargeDisputeUpdatedEvent` | Added | `Dispute` |
| `V1ChargeRefundUpdatedEvent`, `V1RefundCreatedEvent`, `V1RefundFailedEvent`, `V1RefundUpdatedEvent` | Added | `Refund` |
| `V1CheckoutSessionAsyncPaymentFailedEvent`, `V1CheckoutSessionAsyncPaymentSucceededEvent`, `V1CheckoutSessionCompletedEvent`, `V1CheckoutSessionExpiredEvent` | Added | `Checkout.Session` |
| `V1ClimateOrderCanceledEvent`, `V1ClimateOrderCreatedEvent`, `V1ClimateOrderDelayedEvent`, `V1ClimateOrderDeliveredEvent`, `V1ClimateOrderProductSubstitutedEvent` | Added | `Climate.Order` |
| `V1ClimateProductCreatedEvent`, `V1ClimateProductPricingUpdatedEvent` | Added | `Climate.Product` |
| `V1CouponCreatedEvent`, `V1CouponDeletedEvent`, `V1CouponUpdatedEvent` | Added | `Coupon` |
| `V1CreditNoteCreatedEvent`, `V1CreditNoteUpdatedEvent`, `V1CreditNoteVoidedEvent` | Added | `CreditNote` |
| `V1CustomerCreatedEvent`, `V1CustomerDeletedEvent`, `V1CustomerUpdatedEvent` | Added | `Customer` |
| `V1CustomerDiscountCreatedEvent`, `V1CustomerDiscountDeletedEvent`, `V1CustomerDiscountUpdatedEvent` | Added | `Discount` |
| `V1CustomerSubscriptionCreatedEvent`, `V1CustomerSubscriptionDeletedEvent`, `V1CustomerSubscriptionPausedEvent`, `V1CustomerSubscriptionPendingUpdateAppliedEvent`, `V1CustomerSubscriptionPendingUpdateExpiredEvent`, `V1CustomerSubscriptionResumedEvent`, `V1CustomerSubscriptionTrialWillEndEvent`, `V1CustomerSubscriptionUpdatedEvent` | Added | `Subscription` |
| `V1CustomerTaxIdCreatedEvent`, `V1CustomerTaxIdDeletedEvent`, `V1CustomerTaxIdUpdatedEvent` | Added | `TaxId` |
| `V1CustomerCashBalanceTransactionCreatedEvent` | Added | `CustomerCashBalanceTransaction` |
| `V1FileCreatedEvent` | Added | `File` |
| `V1FinancialConnectionsAccountAccountNumbersUpdatedEvent`, `V1FinancialConnectionsAccountCreatedEvent`, `V1FinancialConnectionsAccountDeactivatedEvent`, `V1FinancialConnectionsAccountDisconnectedEvent`, `V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent`, `V1FinancialConnectionsAccountReactivatedEvent`, `V1FinancialConnectionsAccountRefreshedBalanceEvent`, `V1FinancialConnectionsAccountRefreshedOwnershipEvent`, `V1FinancialConnectionsAccountRefreshedTransactionsEvent`, `V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent`, `V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent`, `V1FinancialConnectionsAccountUpcomingDeactivationEvent` | Added | `FinancialConnections.Account` |
| `V1IdentityVerificationSessionCanceledEvent`, `V1IdentityVerificationSessionCreatedEvent`, `V1IdentityVerificationSessionProcessingEvent`, `V1IdentityVerificationSessionRedactedEvent`, `V1IdentityVerificationSessionRequiresInputEvent`, `V1IdentityVerificationSessionVerifiedEvent` | Added | `Identity.VerificationSession` |
| `V1InvoiceCreatedEvent`, `V1InvoiceDeletedEvent`, `V1InvoiceFinalizationFailedEvent`, `V1InvoiceFinalizedEvent`, `V1InvoiceMarkedUncollectibleEvent`, `V1InvoiceOverdueEvent`, `V1InvoiceOverpaidEvent`, `V1InvoicePaidEvent`, `V1InvoicePaymentActionRequiredEvent`, `V1InvoicePaymentAttemptRequiredEvent`, `V1InvoicePaymentFailedEvent`, `V1InvoicePaymentSucceededEvent`, `V1InvoiceSentEvent`, `V1InvoiceUpcomingEvent`, `V1InvoiceUpdatedEvent`, `V1InvoiceVoidedEvent`, `V1InvoiceWillBeDueEvent` | Added | `Invoice` |
| `V1InvoicePaymentPaidEvent` | Added | `InvoicePayment` |
| `V1InvoiceitemCreatedEvent`, `V1InvoiceitemDeletedEvent` | Added | `InvoiceItem` |
| `V1IssuingAuthorizationCreatedEvent`, `V1IssuingAuthorizationRequestEvent`, `V1IssuingAuthorizationUpdatedEvent` | Added | `Issuing.Authorization` |
| `V1IssuingCardCreatedEvent`, `V1IssuingCardUpdatedEvent` | Added | `Issuing.Card` |
| `V1IssuingCardholderCreatedEvent`, `V1IssuingCardholderUpdatedEvent` | Added | `Issuing.Cardholder` |
| `V1IssuingDisputeClosedEvent`, `V1IssuingDisputeCreatedEvent`, `V1IssuingDisputeFundsReinstatedEvent`, `V1IssuingDisputeFundsRescindedEvent`, `V1IssuingDisputeSubmittedEvent`, `V1IssuingDisputeUpdatedEvent` | Added | `Issuing.Dispute` |
| `V1IssuingPersonalizationDesignActivatedEvent`, `V1IssuingPersonalizationDesignDeactivatedEvent`, `V1IssuingPersonalizationDesignRejectedEvent`, `V1IssuingPersonalizationDesignUpdatedEvent` | Added | `Issuing.PersonalizationDesign` |
| `V1IssuingTokenCreatedEvent`, `V1IssuingTokenUpdatedEvent` | Added | `Issuing.Token` |
| `V1IssuingTransactionCreatedEvent`, `V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent`, `V1IssuingTransactionUpdatedEvent` | Added | `Issuing.Transaction` |
| `V1MandateUpdatedEvent` | Added | `Mandate` |
| `V1PaymentIntentAmountCapturableUpdatedEvent`, `V1PaymentIntentCanceledEvent`, `V1PaymentIntentCreatedEvent`, `V1PaymentIntentPartiallyFundedEvent`, `V1PaymentIntentPaymentFailedEvent`, `V1PaymentIntentProcessingEvent`, `V1PaymentIntentRequiresActionEvent`, `V1PaymentIntentSucceededEvent` | Added | `PaymentIntent` |
| `V1PaymentLinkCreatedEvent`, `V1PaymentLinkUpdatedEvent` | Added | `PaymentLink` |
| `V1PaymentMethodAttachedEvent`, `V1PaymentMethodAutomaticallyUpdatedEvent`, `V1PaymentMethodDetachedEvent`, `V1PaymentMethodUpdatedEvent` | Added | `PaymentMethod` |
| `V1PayoutCanceledEvent`, `V1PayoutCreatedEvent`, `V1PayoutFailedEvent`, `V1PayoutPaidEvent`, `V1PayoutReconciliationCompletedEvent`, `V1PayoutUpdatedEvent` | Added | `Payout` |
| `V1PersonCreatedEvent`, `V1PersonDeletedEvent`, `V1PersonUpdatedEvent` | Added | `Person` |
| `V1PlanCreatedEvent`, `V1PlanDeletedEvent`, `V1PlanUpdatedEvent` | Added | `Plan` |
| `V1PriceCreatedEvent`, `V1PriceDeletedEvent`, `V1PriceUpdatedEvent` | Added | `Price` |
| `V1ProductCreatedEvent`, `V1ProductDeletedEvent`, `V1ProductUpdatedEvent` | Added | `Product` |
| `V1PromotionCodeCreatedEvent`, `V1PromotionCodeUpdatedEvent` | Added | `PromotionCode` |
| `V1QuoteAcceptedEvent`, `V1QuoteCanceledEvent`, `V1QuoteCreatedEvent`, `V1QuoteFinalizedEvent` | Added | `Quote` |
| `V1RadarEarlyFraudWarningCreatedEvent`, `V1RadarEarlyFraudWarningUpdatedEvent` | Added | `Radar.EarlyFraudWarning` |
| `V1ReviewClosedEvent`, `V1ReviewOpenedEvent` | Added | `Review` |
| `V1SetupIntentCanceledEvent`, `V1SetupIntentCreatedEvent`, `V1SetupIntentRequiresActionEvent`, `V1SetupIntentSetupFailedEvent`, `V1SetupIntentSucceededEvent` | Added | `SetupIntent` |
| `V1SigmaScheduledQueryRunCreatedEvent` | Added | `Sigma.ScheduledQueryRun` |
| `V1SourceCanceledEvent`, `V1SourceChargeableEvent`, `V1SourceFailedEvent`, `V1SourceRefundAttributesRequiredEvent` | Added | `Source` |
| `V1SubscriptionScheduleAbortedEvent`, `V1SubscriptionScheduleCanceledEvent`, `V1SubscriptionScheduleCompletedEvent`, `V1SubscriptionScheduleCreatedEvent`, `V1SubscriptionScheduleExpiringEvent`, `V1SubscriptionScheduleReleasedEvent`, `V1SubscriptionScheduleUpdatedEvent` | Added | `SubscriptionSchedule` |
| `V1TaxSettingsUpdatedEvent` | Added | `Tax.Settings` |
| `V1TaxRateCreatedEvent`, `V1TaxRateUpdatedEvent` | Added | `TaxRate` |
| `V1TerminalReaderActionFailedEvent`, `V1TerminalReaderActionSucceededEvent`, `V1TerminalReaderActionUpdatedEvent` | Added | `Terminal.Reader` |
| `V1TestHelpersTestClockAdvancingEvent`, `V1TestHelpersTestClockCreatedEvent`, `V1TestHelpersTestClockDeletedEvent`, `V1TestHelpersTestClockInternalFailureEvent`, `V1TestHelpersTestClockReadyEvent` | Added | `TestHelpers.TestClock` |
| `V1TopupCanceledEvent`, `V1TopupCreatedEvent`, `V1TopupFailedEvent`, `V1TopupReversedEvent`, `V1TopupSucceededEvent` | Added | `Topup` |
| `V1TransferCreatedEvent`, `V1TransferReversedEvent`, `V1TransferUpdatedEvent` | Added | `Transfer` |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `snapshot_event` | Added | [V2::Core::Event](/api/v2/core/events/object?api-version=2026-09-30.endive#v2_event_object) |
| `customer`, `subscription` | Added | [EventsV1InvoiceUpcomingEvent](/api/v2/core/events/event-types?api-version=2026-09-30.endive#v2_event_types-v1.invoice.upcoming) |

|  | Change | Event types |
| --- | --- | --- |
| `V1AccountApplicationAuthorizedEvent`, `V1AccountApplicationDeauthorizedEvent`, `V1AccountExternalAccountCreatedEvent`, `V1AccountExternalAccountDeletedEvent`, `V1AccountExternalAccountUpdatedEvent`, `V1BillingPortalSessionCreatedEvent`, `V1EntitlementsActiveEntitlementSummaryUpdatedEvent` | Added | `` |
| `V1AccountUpdatedEvent` | Added | `Account` |
| `V1ApplicationFeeCreatedEvent`, `V1ApplicationFeeRefundedEvent` | Added | `ApplicationFee` |
| `V1ApplicationFeeRefundUpdatedEvent` | Added | `ApplicationFeeRefund` |
| `V1BalanceAvailableEvent` | Added | `Balance` |
| `V1BalanceSettingsUpdatedEvent` | Added | `BalanceSettings` |
| `V1BillingAlertTriggeredEvent` | Added | `Billing::Alert` |
| `V1BillingCreditBalanceTransactionCreatedEvent` | Added | `Billing::CreditBalanceTransaction` |
| `V1BillingCreditGrantCreatedEvent`, `V1BillingCreditGrantUpdatedEvent` | Added | `Billing::CreditGrant` |
| `V1BillingMeterCreatedEvent`, `V1BillingMeterDeactivatedEvent`, `V1BillingMeterReactivatedEvent`, `V1BillingMeterUpdatedEvent` | Added | `Billing::Meter` |
| `V1BillingPortalConfigurationCreatedEvent`, `V1BillingPortalConfigurationUpdatedEvent` | Added | `BillingPortal::Configuration` |
| `V1CapabilityUpdatedEvent` | Added | `Capability` |
| `V1CashBalanceFundsAvailableEvent` | Added | `CashBalance` |
| `V1ChargeCapturedEvent`, `V1ChargeExpiredEvent`, `V1ChargeFailedEvent`, `V1ChargePendingEvent`, `V1ChargeRefundedEvent`, `V1ChargeSucceededEvent`, `V1ChargeUpdatedEvent` | Added | `Charge` |
| `V1ChargeDisputeClosedEvent`, `V1ChargeDisputeCreatedEvent`, `V1ChargeDisputeFundsReinstatedEvent`, `V1ChargeDisputeFundsWithdrawnEvent`, `V1ChargeDisputeUpdatedEvent` | Added | `Dispute` |
| `V1ChargeRefundUpdatedEvent`, `V1RefundCreatedEvent`, `V1RefundFailedEvent`, `V1RefundUpdatedEvent` | Added | `Refund` |
| `V1CheckoutSessionAsyncPaymentFailedEvent`, `V1CheckoutSessionAsyncPaymentSucceededEvent`, `V1CheckoutSessionCompletedEvent`, `V1CheckoutSessionExpiredEvent` | Added | `Checkout::Session` |
| `V1ClimateOrderCanceledEvent`, `V1ClimateOrderCreatedEvent`, `V1ClimateOrderDelayedEvent`, `V1ClimateOrderDeliveredEvent`, `V1ClimateOrderProductSubstitutedEvent` | Added | `Climate::Order` |
| `V1ClimateProductCreatedEvent`, `V1ClimateProductPricingUpdatedEvent` | Added | `Climate::Product` |
| `V1CouponCreatedEvent`, `V1CouponDeletedEvent`, `V1CouponUpdatedEvent` | Added | `Coupon` |
| `V1CreditNoteCreatedEvent`, `V1CreditNoteUpdatedEvent`, `V1CreditNoteVoidedEvent` | Added | `CreditNote` |
| `V1CustomerCreatedEvent`, `V1CustomerDeletedEvent`, `V1CustomerUpdatedEvent` | Added | `Customer` |
| `V1CustomerDiscountCreatedEvent`, `V1CustomerDiscountDeletedEvent`, `V1CustomerDiscountUpdatedEvent` | Added | `Discount` |
| `V1CustomerSubscriptionCreatedEvent`, `V1CustomerSubscriptionDeletedEvent`, `V1CustomerSubscriptionPausedEvent`, `V1CustomerSubscriptionPendingUpdateAppliedEvent`, `V1CustomerSubscriptionPendingUpdateExpiredEvent`, `V1CustomerSubscriptionResumedEvent`, `V1CustomerSubscriptionTrialWillEndEvent`, `V1CustomerSubscriptionUpdatedEvent` | Added | `Subscription` |
| `V1CustomerTaxIdCreatedEvent`, `V1CustomerTaxIdDeletedEvent`, `V1CustomerTaxIdUpdatedEvent` | Added | `TaxId` |
| `V1CustomerCashBalanceTransactionCreatedEvent` | Added | `CustomerCashBalanceTransaction` |
| `V1FileCreatedEvent` | Added | `File` |
| `V1FinancialConnectionsAccountAccountNumbersUpdatedEvent`, `V1FinancialConnectionsAccountCreatedEvent`, `V1FinancialConnectionsAccountDeactivatedEvent`, `V1FinancialConnectionsAccountDisconnectedEvent`, `V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent`, `V1FinancialConnectionsAccountReactivatedEvent`, `V1FinancialConnectionsAccountRefreshedBalanceEvent`, `V1FinancialConnectionsAccountRefreshedOwnershipEvent`, `V1FinancialConnectionsAccountRefreshedTransactionsEvent`, `V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent`, `V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent`, `V1FinancialConnectionsAccountUpcomingDeactivationEvent` | Added | `FinancialConnections::Account` |
| `V1IdentityVerificationSessionCanceledEvent`, `V1IdentityVerificationSessionCreatedEvent`, `V1IdentityVerificationSessionProcessingEvent`, `V1IdentityVerificationSessionRedactedEvent`, `V1IdentityVerificationSessionRequiresInputEvent`, `V1IdentityVerificationSessionVerifiedEvent` | Added | `Identity::VerificationSession` |
| `V1InvoiceCreatedEvent`, `V1InvoiceDeletedEvent`, `V1InvoiceFinalizationFailedEvent`, `V1InvoiceFinalizedEvent`, `V1InvoiceMarkedUncollectibleEvent`, `V1InvoiceOverdueEvent`, `V1InvoiceOverpaidEvent`, `V1InvoicePaidEvent`, `V1InvoicePaymentActionRequiredEvent`, `V1InvoicePaymentAttemptRequiredEvent`, `V1InvoicePaymentFailedEvent`, `V1InvoicePaymentSucceededEvent`, `V1InvoiceSentEvent`, `V1InvoiceUpcomingEvent`, `V1InvoiceUpdatedEvent`, `V1InvoiceVoidedEvent`, `V1InvoiceWillBeDueEvent` | Added | `Invoice` |
| `V1InvoicePaymentPaidEvent` | Added | `InvoicePayment` |
| `V1InvoiceitemCreatedEvent`, `V1InvoiceitemDeletedEvent` | Added | `InvoiceItem` |
| `V1IssuingAuthorizationCreatedEvent`, `V1IssuingAuthorizationRequestEvent`, `V1IssuingAuthorizationUpdatedEvent` | Added | `Issuing::Authorization` |
| `V1IssuingCardCreatedEvent`, `V1IssuingCardUpdatedEvent` | Added | `Issuing::Card` |
| `V1IssuingCardholderCreatedEvent`, `V1IssuingCardholderUpdatedEvent` | Added | `Issuing::Cardholder` |
| `V1IssuingDisputeClosedEvent`, `V1IssuingDisputeCreatedEvent`, `V1IssuingDisputeFundsReinstatedEvent`, `V1IssuingDisputeFundsRescindedEvent`, `V1IssuingDisputeSubmittedEvent`, `V1IssuingDisputeUpdatedEvent` | Added | `Issuing::Dispute` |
| `V1IssuingPersonalizationDesignActivatedEvent`, `V1IssuingPersonalizationDesignDeactivatedEvent`, `V1IssuingPersonalizationDesignRejectedEvent`, `V1IssuingPersonalizationDesignUpdatedEvent` | Added | `Issuing::PersonalizationDesign` |
| `V1IssuingTokenCreatedEvent`, `V1IssuingTokenUpdatedEvent` | Added | `Issuing::Token` |
| `V1IssuingTransactionCreatedEvent`, `V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent`, `V1IssuingTransactionUpdatedEvent` | Added | `Issuing::Transaction` |
| `V1MandateUpdatedEvent` | Added | `Mandate` |
| `V1PaymentIntentAmountCapturableUpdatedEvent`, `V1PaymentIntentCanceledEvent`, `V1PaymentIntentCreatedEvent`, `V1PaymentIntentPartiallyFundedEvent`, `V1PaymentIntentPaymentFailedEvent`, `V1PaymentIntentProcessingEvent`, `V1PaymentIntentRequiresActionEvent`, `V1PaymentIntentSucceededEvent` | Added | `PaymentIntent` |
| `V1PaymentLinkCreatedEvent`, `V1PaymentLinkUpdatedEvent` | Added | `PaymentLink` |
| `V1PaymentMethodAttachedEvent`, `V1PaymentMethodAutomaticallyUpdatedEvent`, `V1PaymentMethodDetachedEvent`, `V1PaymentMethodUpdatedEvent` | Added | `PaymentMethod` |
| `V1PayoutCanceledEvent`, `V1PayoutCreatedEvent`, `V1PayoutFailedEvent`, `V1PayoutPaidEvent`, `V1PayoutReconciliationCompletedEvent`, `V1PayoutUpdatedEvent` | Added | `Payout` |
| `V1PersonCreatedEvent`, `V1PersonDeletedEvent`, `V1PersonUpdatedEvent` | Added | `Person` |
| `V1PlanCreatedEvent`, `V1PlanDeletedEvent`, `V1PlanUpdatedEvent` | Added | `Plan` |
| `V1PriceCreatedEvent`, `V1PriceDeletedEvent`, `V1PriceUpdatedEvent` | Added | `Price` |
| `V1ProductCreatedEvent`, `V1ProductDeletedEvent`, `V1ProductUpdatedEvent` | Added | `Product` |
| `V1PromotionCodeCreatedEvent`, `V1PromotionCodeUpdatedEvent` | Added | `PromotionCode` |
| `V1QuoteAcceptedEvent`, `V1QuoteCanceledEvent`, `V1QuoteCreatedEvent`, `V1QuoteFinalizedEvent` | Added | `Quote` |
| `V1RadarEarlyFraudWarningCreatedEvent`, `V1RadarEarlyFraudWarningUpdatedEvent` | Added | `Radar::EarlyFraudWarning` |
| `V1ReviewClosedEvent`, `V1ReviewOpenedEvent` | Added | `Review` |
| `V1SetupIntentCanceledEvent`, `V1SetupIntentCreatedEvent`, `V1SetupIntentRequiresActionEvent`, `V1SetupIntentSetupFailedEvent`, `V1SetupIntentSucceededEvent` | Added | `SetupIntent` |
| `V1SigmaScheduledQueryRunCreatedEvent` | Added | `Sigma::ScheduledQueryRun` |
| `V1SourceCanceledEvent`, `V1SourceChargeableEvent`, `V1SourceFailedEvent`, `V1SourceRefundAttributesRequiredEvent` | Added | `Source` |
| `V1SubscriptionScheduleAbortedEvent`, `V1SubscriptionScheduleCanceledEvent`, `V1SubscriptionScheduleCompletedEvent`, `V1SubscriptionScheduleCreatedEvent`, `V1SubscriptionScheduleExpiringEvent`, `V1SubscriptionScheduleReleasedEvent`, `V1SubscriptionScheduleUpdatedEvent` | Added | `SubscriptionSchedule` |
| `V1TaxSettingsUpdatedEvent` | Added | `Tax::Settings` |
| `V1TaxRateCreatedEvent`, `V1TaxRateUpdatedEvent` | Added | `TaxRate` |
| `V1TerminalReaderActionFailedEvent`, `V1TerminalReaderActionSucceededEvent`, `V1TerminalReaderActionUpdatedEvent` | Added | `Terminal::Reader` |
| `V1TestHelpersTestClockAdvancingEvent`, `V1TestHelpersTestClockCreatedEvent`, `V1TestHelpersTestClockDeletedEvent`, `V1TestHelpersTestClockInternalFailureEvent`, `V1TestHelpersTestClockReadyEvent` | Added | `TestHelpers::TestClock` |
| `V1TopupCanceledEvent`, `V1TopupCreatedEvent`, `V1TopupFailedEvent`, `V1TopupReversedEvent`, `V1TopupSucceededEvent` | Added | `Topup` |
| `V1TransferCreatedEvent`, `V1TransferReversedEvent`, `V1TransferUpdatedEvent` | Added | `Transfer` |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `snapshot_event` | Added | [V2.Core.Event](/api/v2/core/events/object?api-version=2026-09-30.endive#v2_event_object) |
| `customer`, `subscription` | Added | [EventsV1InvoiceUpcomingEvent](/api/v2/core/events/event-types?api-version=2026-09-30.endive#v2_event_types-v1.invoice.upcoming) |

|  | Change | Event types |
| --- | --- | --- |
| `V1AccountApplicationAuthorizedEvent`, `V1AccountApplicationDeauthorizedEvent`, `V1AccountExternalAccountCreatedEvent`, `V1AccountExternalAccountDeletedEvent`, `V1AccountExternalAccountUpdatedEvent`, `V1BillingPortalSessionCreatedEvent`, `V1EntitlementsActiveEntitlementSummaryUpdatedEvent` | Added | `` |
| `V1AccountUpdatedEvent` | Added | `Account` |
| `V1ApplicationFeeCreatedEvent`, `V1ApplicationFeeRefundedEvent` | Added | `ApplicationFee` |
| `V1ApplicationFeeRefundUpdatedEvent` | Added | `ApplicationFeeRefund` |
| `V1BalanceAvailableEvent` | Added | `Balance` |
| `V1BalanceSettingsUpdatedEvent` | Added | `BalanceSettings` |
| `V1BillingAlertTriggeredEvent` | Added | `billing.Alert` |
| `V1BillingCreditBalanceTransactionCreatedEvent` | Added | `billing.CreditBalanceTransaction` |
| `V1BillingCreditGrantCreatedEvent`, `V1BillingCreditGrantUpdatedEvent` | Added | `billing.CreditGrant` |
| `V1BillingMeterCreatedEvent`, `V1BillingMeterDeactivatedEvent`, `V1BillingMeterReactivatedEvent`, `V1BillingMeterUpdatedEvent` | Added | `billing.Meter` |
| `V1BillingPortalConfigurationCreatedEvent`, `V1BillingPortalConfigurationUpdatedEvent` | Added | `billing_portal.Configuration` |
| `V1CapabilityUpdatedEvent` | Added | `Capability` |
| `V1CashBalanceFundsAvailableEvent` | Added | `CashBalance` |
| `V1ChargeCapturedEvent`, `V1ChargeExpiredEvent`, `V1ChargeFailedEvent`, `V1ChargePendingEvent`, `V1ChargeRefundedEvent`, `V1ChargeSucceededEvent`, `V1ChargeUpdatedEvent` | Added | `Charge` |
| `V1ChargeDisputeClosedEvent`, `V1ChargeDisputeCreatedEvent`, `V1ChargeDisputeFundsReinstatedEvent`, `V1ChargeDisputeFundsWithdrawnEvent`, `V1ChargeDisputeUpdatedEvent` | Added | `Dispute` |
| `V1ChargeRefundUpdatedEvent`, `V1RefundCreatedEvent`, `V1RefundFailedEvent`, `V1RefundUpdatedEvent` | Added | `Refund` |
| `V1CheckoutSessionAsyncPaymentFailedEvent`, `V1CheckoutSessionAsyncPaymentSucceededEvent`, `V1CheckoutSessionCompletedEvent`, `V1CheckoutSessionExpiredEvent` | Added | `checkout.Session` |
| `V1ClimateOrderCanceledEvent`, `V1ClimateOrderCreatedEvent`, `V1ClimateOrderDelayedEvent`, `V1ClimateOrderDeliveredEvent`, `V1ClimateOrderProductSubstitutedEvent` | Added | `climate.Order` |
| `V1ClimateProductCreatedEvent`, `V1ClimateProductPricingUpdatedEvent` | Added | `climate.Product` |
| `V1CouponCreatedEvent`, `V1CouponDeletedEvent`, `V1CouponUpdatedEvent` | Added | `Coupon` |
| `V1CreditNoteCreatedEvent`, `V1CreditNoteUpdatedEvent`, `V1CreditNoteVoidedEvent` | Added | `CreditNote` |
| `V1CustomerCreatedEvent`, `V1CustomerDeletedEvent`, `V1CustomerUpdatedEvent` | Added | `Customer` |
| `V1CustomerDiscountCreatedEvent`, `V1CustomerDiscountDeletedEvent`, `V1CustomerDiscountUpdatedEvent` | Added | `Discount` |
| `V1CustomerSubscriptionCreatedEvent`, `V1CustomerSubscriptionDeletedEvent`, `V1CustomerSubscriptionPausedEvent`, `V1CustomerSubscriptionPendingUpdateAppliedEvent`, `V1CustomerSubscriptionPendingUpdateExpiredEvent`, `V1CustomerSubscriptionResumedEvent`, `V1CustomerSubscriptionTrialWillEndEvent`, `V1CustomerSubscriptionUpdatedEvent` | Added | `Subscription` |
| `V1CustomerTaxIdCreatedEvent`, `V1CustomerTaxIdDeletedEvent`, `V1CustomerTaxIdUpdatedEvent` | Added | `TaxId` |
| `V1CustomerCashBalanceTransactionCreatedEvent` | Added | `CustomerCashBalanceTransaction` |
| `V1FileCreatedEvent` | Added | `File` |
| `V1FinancialConnectionsAccountAccountNumbersUpdatedEvent`, `V1FinancialConnectionsAccountCreatedEvent`, `V1FinancialConnectionsAccountDeactivatedEvent`, `V1FinancialConnectionsAccountDisconnectedEvent`, `V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent`, `V1FinancialConnectionsAccountReactivatedEvent`, `V1FinancialConnectionsAccountRefreshedBalanceEvent`, `V1FinancialConnectionsAccountRefreshedOwnershipEvent`, `V1FinancialConnectionsAccountRefreshedTransactionsEvent`, `V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent`, `V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent`, `V1FinancialConnectionsAccountUpcomingDeactivationEvent` | Added | `financial_connections.Account` |
| `V1IdentityVerificationSessionCanceledEvent`, `V1IdentityVerificationSessionCreatedEvent`, `V1IdentityVerificationSessionProcessingEvent`, `V1IdentityVerificationSessionRedactedEvent`, `V1IdentityVerificationSessionRequiresInputEvent`, `V1IdentityVerificationSessionVerifiedEvent` | Added | `identity.VerificationSession` |
| `V1InvoiceCreatedEvent`, `V1InvoiceDeletedEvent`, `V1InvoiceFinalizationFailedEvent`, `V1InvoiceFinalizedEvent`, `V1InvoiceMarkedUncollectibleEvent`, `V1InvoiceOverdueEvent`, `V1InvoiceOverpaidEvent`, `V1InvoicePaidEvent`, `V1InvoicePaymentActionRequiredEvent`, `V1InvoicePaymentAttemptRequiredEvent`, `V1InvoicePaymentFailedEvent`, `V1InvoicePaymentSucceededEvent`, `V1InvoiceSentEvent`, `V1InvoiceUpcomingEvent`, `V1InvoiceUpdatedEvent`, `V1InvoiceVoidedEvent`, `V1InvoiceWillBeDueEvent` | Added | `Invoice` |
| `V1InvoicePaymentPaidEvent` | Added | `InvoicePayment` |
| `V1InvoiceitemCreatedEvent`, `V1InvoiceitemDeletedEvent` | Added | `InvoiceItem` |
| `V1IssuingAuthorizationCreatedEvent`, `V1IssuingAuthorizationRequestEvent`, `V1IssuingAuthorizationUpdatedEvent` | Added | `issuing.Authorization` |
| `V1IssuingCardCreatedEvent`, `V1IssuingCardUpdatedEvent` | Added | `issuing.Card` |
| `V1IssuingCardholderCreatedEvent`, `V1IssuingCardholderUpdatedEvent` | Added | `issuing.Cardholder` |
| `V1IssuingDisputeClosedEvent`, `V1IssuingDisputeCreatedEvent`, `V1IssuingDisputeFundsReinstatedEvent`, `V1IssuingDisputeFundsRescindedEvent`, `V1IssuingDisputeSubmittedEvent`, `V1IssuingDisputeUpdatedEvent` | Added | `issuing.Dispute` |
| `V1IssuingPersonalizationDesignActivatedEvent`, `V1IssuingPersonalizationDesignDeactivatedEvent`, `V1IssuingPersonalizationDesignRejectedEvent`, `V1IssuingPersonalizationDesignUpdatedEvent` | Added | `issuing.PersonalizationDesign` |
| `V1IssuingTokenCreatedEvent`, `V1IssuingTokenUpdatedEvent` | Added | `issuing.Token` |
| `V1IssuingTransactionCreatedEvent`, `V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent`, `V1IssuingTransactionUpdatedEvent` | Added | `issuing.Transaction` |
| `V1MandateUpdatedEvent` | Added | `Mandate` |
| `V1PaymentIntentAmountCapturableUpdatedEvent`, `V1PaymentIntentCanceledEvent`, `V1PaymentIntentCreatedEvent`, `V1PaymentIntentPartiallyFundedEvent`, `V1PaymentIntentPaymentFailedEvent`, `V1PaymentIntentProcessingEvent`, `V1PaymentIntentRequiresActionEvent`, `V1PaymentIntentSucceededEvent` | Added | `PaymentIntent` |
| `V1PaymentLinkCreatedEvent`, `V1PaymentLinkUpdatedEvent` | Added | `PaymentLink` |
| `V1PaymentMethodAttachedEvent`, `V1PaymentMethodAutomaticallyUpdatedEvent`, `V1PaymentMethodDetachedEvent`, `V1PaymentMethodUpdatedEvent` | Added | `PaymentMethod` |
| `V1PayoutCanceledEvent`, `V1PayoutCreatedEvent`, `V1PayoutFailedEvent`, `V1PayoutPaidEvent`, `V1PayoutReconciliationCompletedEvent`, `V1PayoutUpdatedEvent` | Added | `Payout` |
| `V1PersonCreatedEvent`, `V1PersonDeletedEvent`, `V1PersonUpdatedEvent` | Added | `Person` |
| `V1PlanCreatedEvent`, `V1PlanDeletedEvent`, `V1PlanUpdatedEvent` | Added | `Plan` |
| `V1PriceCreatedEvent`, `V1PriceDeletedEvent`, `V1PriceUpdatedEvent` | Added | `Price` |
| `V1ProductCreatedEvent`, `V1ProductDeletedEvent`, `V1ProductUpdatedEvent` | Added | `Product` |
| `V1PromotionCodeCreatedEvent`, `V1PromotionCodeUpdatedEvent` | Added | `PromotionCode` |
| `V1QuoteAcceptedEvent`, `V1QuoteCanceledEvent`, `V1QuoteCreatedEvent`, `V1QuoteFinalizedEvent` | Added | `Quote` |
| `V1RadarEarlyFraudWarningCreatedEvent`, `V1RadarEarlyFraudWarningUpdatedEvent` | Added | `radar.EarlyFraudWarning` |
| `V1ReviewClosedEvent`, `V1ReviewOpenedEvent` | Added | `Review` |
| `V1SetupIntentCanceledEvent`, `V1SetupIntentCreatedEvent`, `V1SetupIntentRequiresActionEvent`, `V1SetupIntentSetupFailedEvent`, `V1SetupIntentSucceededEvent` | Added | `SetupIntent` |
| `V1SigmaScheduledQueryRunCreatedEvent` | Added | `sigma.ScheduledQueryRun` |
| `V1SourceCanceledEvent`, `V1SourceChargeableEvent`, `V1SourceFailedEvent`, `V1SourceRefundAttributesRequiredEvent` | Added | `Source` |
| `V1SubscriptionScheduleAbortedEvent`, `V1SubscriptionScheduleCanceledEvent`, `V1SubscriptionScheduleCompletedEvent`, `V1SubscriptionScheduleCreatedEvent`, `V1SubscriptionScheduleExpiringEvent`, `V1SubscriptionScheduleReleasedEvent`, `V1SubscriptionScheduleUpdatedEvent` | Added | `SubscriptionSchedule` |
| `V1TaxSettingsUpdatedEvent` | Added | `tax.Settings` |
| `V1TaxRateCreatedEvent`, `V1TaxRateUpdatedEvent` | Added | `TaxRate` |
| `V1TerminalReaderActionFailedEvent`, `V1TerminalReaderActionSucceededEvent`, `V1TerminalReaderActionUpdatedEvent` | Added | `terminal.Reader` |
| `V1TestHelpersTestClockAdvancingEvent`, `V1TestHelpersTestClockCreatedEvent`, `V1TestHelpersTestClockDeletedEvent`, `V1TestHelpersTestClockInternalFailureEvent`, `V1TestHelpersTestClockReadyEvent` | Added | `test_helpers.TestClock` |
| `V1TopupCanceledEvent`, `V1TopupCreatedEvent`, `V1TopupFailedEvent`, `V1TopupReversedEvent`, `V1TopupSucceededEvent` | Added | `Topup` |
| `V1TransferCreatedEvent`, `V1TransferReversedEvent`, `V1TransferUpdatedEvent` | Added | `Transfer` |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `snapshot_event` | Added | [V2.Core.Event](/api/v2/core/events/object?api-version=2026-09-30.endive#v2_event_object) |
| `customer`, `subscription` | Added | [EventsV1InvoiceUpcomingEvent](/api/v2/core/events/event-types?api-version=2026-09-30.endive#v2_event_types-v1.invoice.upcoming) |

|  | Change | Event types |
| --- | --- | --- |
| `V1AccountApplicationAuthorizedEvent`, `V1AccountApplicationDeauthorizedEvent`, `V1AccountExternalAccountCreatedEvent`, `V1AccountExternalAccountDeletedEvent`, `V1AccountExternalAccountUpdatedEvent`, `V1BillingPortalSessionCreatedEvent`, `V1EntitlementsActiveEntitlementSummaryUpdatedEvent` | Added | `` |
| `V1AccountUpdatedEvent` | Added | `Account` |
| `V1ApplicationFeeCreatedEvent`, `V1ApplicationFeeRefundedEvent` | Added | `ApplicationFee` |
| `V1ApplicationFeeRefundUpdatedEvent` | Added | `ApplicationFeeRefund` |
| `V1BalanceAvailableEvent` | Added | `Balance` |
| `V1BalanceSettingsUpdatedEvent` | Added | `BalanceSettings` |
| `V1BillingAlertTriggeredEvent` | Added | `Billing.Alert` |
| `V1BillingCreditBalanceTransactionCreatedEvent` | Added | `Billing.CreditBalanceTransaction` |
| `V1BillingCreditGrantCreatedEvent`, `V1BillingCreditGrantUpdatedEvent` | Added | `Billing.CreditGrant` |
| `V1BillingMeterCreatedEvent`, `V1BillingMeterDeactivatedEvent`, `V1BillingMeterReactivatedEvent`, `V1BillingMeterUpdatedEvent` | Added | `Billing.Meter` |
| `V1BillingPortalConfigurationCreatedEvent`, `V1BillingPortalConfigurationUpdatedEvent` | Added | `BillingPortal.Configuration` |
| `V1CapabilityUpdatedEvent` | Added | `Capability` |
| `V1CashBalanceFundsAvailableEvent` | Added | `CashBalance` |
| `V1ChargeCapturedEvent`, `V1ChargeExpiredEvent`, `V1ChargeFailedEvent`, `V1ChargePendingEvent`, `V1ChargeRefundedEvent`, `V1ChargeSucceededEvent`, `V1ChargeUpdatedEvent` | Added | `Charge` |
| `V1ChargeDisputeClosedEvent`, `V1ChargeDisputeCreatedEvent`, `V1ChargeDisputeFundsReinstatedEvent`, `V1ChargeDisputeFundsWithdrawnEvent`, `V1ChargeDisputeUpdatedEvent` | Added | `Dispute` |
| `V1ChargeRefundUpdatedEvent`, `V1RefundCreatedEvent`, `V1RefundFailedEvent`, `V1RefundUpdatedEvent` | Added | `Refund` |
| `V1CheckoutSessionAsyncPaymentFailedEvent`, `V1CheckoutSessionAsyncPaymentSucceededEvent`, `V1CheckoutSessionCompletedEvent`, `V1CheckoutSessionExpiredEvent` | Added | `Checkout.Session` |
| `V1ClimateOrderCanceledEvent`, `V1ClimateOrderCreatedEvent`, `V1ClimateOrderDelayedEvent`, `V1ClimateOrderDeliveredEvent`, `V1ClimateOrderProductSubstitutedEvent` | Added | `Climate.Order` |
| `V1ClimateProductCreatedEvent`, `V1ClimateProductPricingUpdatedEvent` | Added | `Climate.Product` |
| `V1CouponCreatedEvent`, `V1CouponDeletedEvent`, `V1CouponUpdatedEvent` | Added | `Coupon` |
| `V1CreditNoteCreatedEvent`, `V1CreditNoteUpdatedEvent`, `V1CreditNoteVoidedEvent` | Added | `CreditNote` |
| `V1CustomerCreatedEvent`, `V1CustomerDeletedEvent`, `V1CustomerUpdatedEvent` | Added | `Customer` |
| `V1CustomerDiscountCreatedEvent`, `V1CustomerDiscountDeletedEvent`, `V1CustomerDiscountUpdatedEvent` | Added | `Discount` |
| `V1CustomerSubscriptionCreatedEvent`, `V1CustomerSubscriptionDeletedEvent`, `V1CustomerSubscriptionPausedEvent`, `V1CustomerSubscriptionPendingUpdateAppliedEvent`, `V1CustomerSubscriptionPendingUpdateExpiredEvent`, `V1CustomerSubscriptionResumedEvent`, `V1CustomerSubscriptionTrialWillEndEvent`, `V1CustomerSubscriptionUpdatedEvent` | Added | `Subscription` |
| `V1CustomerTaxIdCreatedEvent`, `V1CustomerTaxIdDeletedEvent`, `V1CustomerTaxIdUpdatedEvent` | Added | `TaxId` |
| `V1CustomerCashBalanceTransactionCreatedEvent` | Added | `CustomerCashBalanceTransaction` |
| `V1FileCreatedEvent` | Added | `File` |
| `V1FinancialConnectionsAccountAccountNumbersUpdatedEvent`, `V1FinancialConnectionsAccountCreatedEvent`, `V1FinancialConnectionsAccountDeactivatedEvent`, `V1FinancialConnectionsAccountDisconnectedEvent`, `V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent`, `V1FinancialConnectionsAccountReactivatedEvent`, `V1FinancialConnectionsAccountRefreshedBalanceEvent`, `V1FinancialConnectionsAccountRefreshedOwnershipEvent`, `V1FinancialConnectionsAccountRefreshedTransactionsEvent`, `V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent`, `V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent`, `V1FinancialConnectionsAccountUpcomingDeactivationEvent` | Added | `FinancialConnections.Account` |
| `V1IdentityVerificationSessionCanceledEvent`, `V1IdentityVerificationSessionCreatedEvent`, `V1IdentityVerificationSessionProcessingEvent`, `V1IdentityVerificationSessionRedactedEvent`, `V1IdentityVerificationSessionRequiresInputEvent`, `V1IdentityVerificationSessionVerifiedEvent` | Added | `Identity.VerificationSession` |
| `V1InvoiceCreatedEvent`, `V1InvoiceDeletedEvent`, `V1InvoiceFinalizationFailedEvent`, `V1InvoiceFinalizedEvent`, `V1InvoiceMarkedUncollectibleEvent`, `V1InvoiceOverdueEvent`, `V1InvoiceOverpaidEvent`, `V1InvoicePaidEvent`, `V1InvoicePaymentActionRequiredEvent`, `V1InvoicePaymentAttemptRequiredEvent`, `V1InvoicePaymentFailedEvent`, `V1InvoicePaymentSucceededEvent`, `V1InvoiceSentEvent`, `V1InvoiceUpcomingEvent`, `V1InvoiceUpdatedEvent`, `V1InvoiceVoidedEvent`, `V1InvoiceWillBeDueEvent` | Added | `Invoice` |
| `V1InvoicePaymentPaidEvent` | Added | `InvoicePayment` |
| `V1InvoiceitemCreatedEvent`, `V1InvoiceitemDeletedEvent` | Added | `InvoiceItem` |
| `V1IssuingAuthorizationCreatedEvent`, `V1IssuingAuthorizationRequestEvent`, `V1IssuingAuthorizationUpdatedEvent` | Added | `Issuing.Authorization` |
| `V1IssuingCardCreatedEvent`, `V1IssuingCardUpdatedEvent` | Added | `Issuing.Card` |
| `V1IssuingCardholderCreatedEvent`, `V1IssuingCardholderUpdatedEvent` | Added | `Issuing.Cardholder` |
| `V1IssuingDisputeClosedEvent`, `V1IssuingDisputeCreatedEvent`, `V1IssuingDisputeFundsReinstatedEvent`, `V1IssuingDisputeFundsRescindedEvent`, `V1IssuingDisputeSubmittedEvent`, `V1IssuingDisputeUpdatedEvent` | Added | `Issuing.Dispute` |
| `V1IssuingPersonalizationDesignActivatedEvent`, `V1IssuingPersonalizationDesignDeactivatedEvent`, `V1IssuingPersonalizationDesignRejectedEvent`, `V1IssuingPersonalizationDesignUpdatedEvent` | Added | `Issuing.PersonalizationDesign` |
| `V1IssuingTokenCreatedEvent`, `V1IssuingTokenUpdatedEvent` | Added | `Issuing.Token` |
| `V1IssuingTransactionCreatedEvent`, `V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent`, `V1IssuingTransactionUpdatedEvent` | Added | `Issuing.Transaction` |
| `V1MandateUpdatedEvent` | Added | `Mandate` |
| `V1PaymentIntentAmountCapturableUpdatedEvent`, `V1PaymentIntentCanceledEvent`, `V1PaymentIntentCreatedEvent`, `V1PaymentIntentPartiallyFundedEvent`, `V1PaymentIntentPaymentFailedEvent`, `V1PaymentIntentProcessingEvent`, `V1PaymentIntentRequiresActionEvent`, `V1PaymentIntentSucceededEvent` | Added | `PaymentIntent` |
| `V1PaymentLinkCreatedEvent`, `V1PaymentLinkUpdatedEvent` | Added | `PaymentLink` |
| `V1PaymentMethodAttachedEvent`, `V1PaymentMethodAutomaticallyUpdatedEvent`, `V1PaymentMethodDetachedEvent`, `V1PaymentMethodUpdatedEvent` | Added | `PaymentMethod` |
| `V1PayoutCanceledEvent`, `V1PayoutCreatedEvent`, `V1PayoutFailedEvent`, `V1PayoutPaidEvent`, `V1PayoutReconciliationCompletedEvent`, `V1PayoutUpdatedEvent` | Added | `Payout` |
| `V1PersonCreatedEvent`, `V1PersonDeletedEvent`, `V1PersonUpdatedEvent` | Added | `Person` |
| `V1PlanCreatedEvent`, `V1PlanDeletedEvent`, `V1PlanUpdatedEvent` | Added | `Plan` |
| `V1PriceCreatedEvent`, `V1PriceDeletedEvent`, `V1PriceUpdatedEvent` | Added | `Price` |
| `V1ProductCreatedEvent`, `V1ProductDeletedEvent`, `V1ProductUpdatedEvent` | Added | `Product` |
| `V1PromotionCodeCreatedEvent`, `V1PromotionCodeUpdatedEvent` | Added | `PromotionCode` |
| `V1QuoteAcceptedEvent`, `V1QuoteCanceledEvent`, `V1QuoteCreatedEvent`, `V1QuoteFinalizedEvent` | Added | `Quote` |
| `V1RadarEarlyFraudWarningCreatedEvent`, `V1RadarEarlyFraudWarningUpdatedEvent` | Added | `Radar.EarlyFraudWarning` |
| `V1ReviewClosedEvent`, `V1ReviewOpenedEvent` | Added | `Review` |
| `V1SetupIntentCanceledEvent`, `V1SetupIntentCreatedEvent`, `V1SetupIntentRequiresActionEvent`, `V1SetupIntentSetupFailedEvent`, `V1SetupIntentSucceededEvent` | Added | `SetupIntent` |
| `V1SigmaScheduledQueryRunCreatedEvent` | Added | `Sigma.ScheduledQueryRun` |
| `V1SourceCanceledEvent`, `V1SourceChargeableEvent`, `V1SourceFailedEvent`, `V1SourceRefundAttributesRequiredEvent` | Added | `Source` |
| `V1SubscriptionScheduleAbortedEvent`, `V1SubscriptionScheduleCanceledEvent`, `V1SubscriptionScheduleCompletedEvent`, `V1SubscriptionScheduleCreatedEvent`, `V1SubscriptionScheduleExpiringEvent`, `V1SubscriptionScheduleReleasedEvent`, `V1SubscriptionScheduleUpdatedEvent` | Added | `SubscriptionSchedule` |
| `V1TaxSettingsUpdatedEvent` | Added | `Tax.Settings` |
| `V1TaxRateCreatedEvent`, `V1TaxRateUpdatedEvent` | Added | `TaxRate` |
| `V1TerminalReaderActionFailedEvent`, `V1TerminalReaderActionSucceededEvent`, `V1TerminalReaderActionUpdatedEvent` | Added | `Terminal.Reader` |
| `V1TestHelpersTestClockAdvancingEvent`, `V1TestHelpersTestClockCreatedEvent`, `V1TestHelpersTestClockDeletedEvent`, `V1TestHelpersTestClockInternalFailureEvent`, `V1TestHelpersTestClockReadyEvent` | Added | `TestHelpers.TestClock` |
| `V1TopupCanceledEvent`, `V1TopupCreatedEvent`, `V1TopupFailedEvent`, `V1TopupReversedEvent`, `V1TopupSucceededEvent` | Added | `Topup` |
| `V1TransferCreatedEvent`, `V1TransferReversedEvent`, `V1TransferUpdatedEvent` | Added | `Transfer` |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `snapshotEvent` | Added | [v2.core.Event](/api/v2/core/events/object?api-version=2026-09-30.endive#v2_event_object) |
| `customer`, `subscription` | Added | [EventsV1InvoiceUpcomingEvent](/api/v2/core/events/event-types?api-version=2026-09-30.endive#v2_event_types-v1.invoice.upcoming) |

|  | Change | Event types |
| --- | --- | --- |
| `V1AccountApplicationAuthorizedEvent`, `V1AccountApplicationDeauthorizedEvent`, `V1AccountExternalAccountCreatedEvent`, `V1AccountExternalAccountDeletedEvent`, `V1AccountExternalAccountUpdatedEvent`, `V1BillingPortalSessionCreatedEvent`, `V1EntitlementsActiveEntitlementSummaryUpdatedEvent` | Added | `` |
| `V1AccountUpdatedEvent` | Added | `Account` |
| `V1ApplicationFeeCreatedEvent`, `V1ApplicationFeeRefundedEvent` | Added | `ApplicationFee` |
| `V1ApplicationFeeRefundUpdatedEvent` | Added | `FeeRefund` |
| `V1BalanceAvailableEvent` | Added | `Balance` |
| `V1BalanceSettingsUpdatedEvent` | Added | `BalanceSettings` |
| `V1BillingAlertTriggeredEvent` | Added | `billing.Alert` |
| `V1BillingCreditBalanceTransactionCreatedEvent` | Added | `billing.CreditBalanceTransaction` |
| `V1BillingCreditGrantCreatedEvent`, `V1BillingCreditGrantUpdatedEvent` | Added | `billing.CreditGrant` |
| `V1BillingMeterCreatedEvent`, `V1BillingMeterDeactivatedEvent`, `V1BillingMeterReactivatedEvent`, `V1BillingMeterUpdatedEvent` | Added | `billing.Meter` |
| `V1BillingPortalConfigurationCreatedEvent`, `V1BillingPortalConfigurationUpdatedEvent` | Added | `billingportal.Configuration` |
| `V1CapabilityUpdatedEvent` | Added | `Capability` |
| `V1CashBalanceFundsAvailableEvent` | Added | `CashBalance` |
| `V1ChargeCapturedEvent`, `V1ChargeExpiredEvent`, `V1ChargeFailedEvent`, `V1ChargePendingEvent`, `V1ChargeRefundedEvent`, `V1ChargeSucceededEvent`, `V1ChargeUpdatedEvent` | Added | `Charge` |
| `V1ChargeDisputeClosedEvent`, `V1ChargeDisputeCreatedEvent`, `V1ChargeDisputeFundsReinstatedEvent`, `V1ChargeDisputeFundsWithdrawnEvent`, `V1ChargeDisputeUpdatedEvent` | Added | `Dispute` |
| `V1ChargeRefundUpdatedEvent`, `V1RefundCreatedEvent`, `V1RefundFailedEvent`, `V1RefundUpdatedEvent` | Added | `Refund` |
| `V1CheckoutSessionAsyncPaymentFailedEvent`, `V1CheckoutSessionAsyncPaymentSucceededEvent`, `V1CheckoutSessionCompletedEvent`, `V1CheckoutSessionExpiredEvent` | Added | `checkout.Session` |
| `V1ClimateOrderCanceledEvent`, `V1ClimateOrderCreatedEvent`, `V1ClimateOrderDelayedEvent`, `V1ClimateOrderDeliveredEvent`, `V1ClimateOrderProductSubstitutedEvent` | Added | `climate.Order` |
| `V1ClimateProductCreatedEvent`, `V1ClimateProductPricingUpdatedEvent` | Added | `climate.Product` |
| `V1CouponCreatedEvent`, `V1CouponDeletedEvent`, `V1CouponUpdatedEvent` | Added | `Coupon` |
| `V1CreditNoteCreatedEvent`, `V1CreditNoteUpdatedEvent`, `V1CreditNoteVoidedEvent` | Added | `CreditNote` |
| `V1CustomerCreatedEvent`, `V1CustomerDeletedEvent`, `V1CustomerUpdatedEvent` | Added | `Customer` |
| `V1CustomerDiscountCreatedEvent`, `V1CustomerDiscountDeletedEvent`, `V1CustomerDiscountUpdatedEvent` | Added | `Discount` |
| `V1CustomerSubscriptionCreatedEvent`, `V1CustomerSubscriptionDeletedEvent`, `V1CustomerSubscriptionPausedEvent`, `V1CustomerSubscriptionPendingUpdateAppliedEvent`, `V1CustomerSubscriptionPendingUpdateExpiredEvent`, `V1CustomerSubscriptionResumedEvent`, `V1CustomerSubscriptionTrialWillEndEvent`, `V1CustomerSubscriptionUpdatedEvent` | Added | `Subscription` |
| `V1CustomerTaxIdCreatedEvent`, `V1CustomerTaxIdDeletedEvent`, `V1CustomerTaxIdUpdatedEvent` | Added | `TaxId` |
| `V1CustomerCashBalanceTransactionCreatedEvent` | Added | `CustomerCashBalanceTransaction` |
| `V1FileCreatedEvent` | Added | `File` |
| `V1FinancialConnectionsAccountAccountNumbersUpdatedEvent`, `V1FinancialConnectionsAccountCreatedEvent`, `V1FinancialConnectionsAccountDeactivatedEvent`, `V1FinancialConnectionsAccountDisconnectedEvent`, `V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent`, `V1FinancialConnectionsAccountReactivatedEvent`, `V1FinancialConnectionsAccountRefreshedBalanceEvent`, `V1FinancialConnectionsAccountRefreshedOwnershipEvent`, `V1FinancialConnectionsAccountRefreshedTransactionsEvent`, `V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent`, `V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent`, `V1FinancialConnectionsAccountUpcomingDeactivationEvent` | Added | `financialconnections.Account` |
| `V1IdentityVerificationSessionCanceledEvent`, `V1IdentityVerificationSessionCreatedEvent`, `V1IdentityVerificationSessionProcessingEvent`, `V1IdentityVerificationSessionRedactedEvent`, `V1IdentityVerificationSessionRequiresInputEvent`, `V1IdentityVerificationSessionVerifiedEvent` | Added | `identity.VerificationSession` |
| `V1InvoiceCreatedEvent`, `V1InvoiceDeletedEvent`, `V1InvoiceFinalizationFailedEvent`, `V1InvoiceFinalizedEvent`, `V1InvoiceMarkedUncollectibleEvent`, `V1InvoiceOverdueEvent`, `V1InvoiceOverpaidEvent`, `V1InvoicePaidEvent`, `V1InvoicePaymentActionRequiredEvent`, `V1InvoicePaymentAttemptRequiredEvent`, `V1InvoicePaymentFailedEvent`, `V1InvoicePaymentSucceededEvent`, `V1InvoiceSentEvent`, `V1InvoiceUpcomingEvent`, `V1InvoiceUpdatedEvent`, `V1InvoiceVoidedEvent`, `V1InvoiceWillBeDueEvent` | Added | `Invoice` |
| `V1InvoicePaymentPaidEvent` | Added | `InvoicePayment` |
| `V1InvoiceitemCreatedEvent`, `V1InvoiceitemDeletedEvent` | Added | `InvoiceItem` |
| `V1IssuingAuthorizationCreatedEvent`, `V1IssuingAuthorizationRequestEvent`, `V1IssuingAuthorizationUpdatedEvent` | Added | `issuing.Authorization` |
| `V1IssuingCardCreatedEvent`, `V1IssuingCardUpdatedEvent` | Added | `issuing.Card` |
| `V1IssuingCardholderCreatedEvent`, `V1IssuingCardholderUpdatedEvent` | Added | `issuing.Cardholder` |
| `V1IssuingDisputeClosedEvent`, `V1IssuingDisputeCreatedEvent`, `V1IssuingDisputeFundsReinstatedEvent`, `V1IssuingDisputeFundsRescindedEvent`, `V1IssuingDisputeSubmittedEvent`, `V1IssuingDisputeUpdatedEvent` | Added | `issuing.Dispute` |
| `V1IssuingPersonalizationDesignActivatedEvent`, `V1IssuingPersonalizationDesignDeactivatedEvent`, `V1IssuingPersonalizationDesignRejectedEvent`, `V1IssuingPersonalizationDesignUpdatedEvent` | Added | `issuing.PersonalizationDesign` |
| `V1IssuingTokenCreatedEvent`, `V1IssuingTokenUpdatedEvent` | Added | `issuing.Token` |
| `V1IssuingTransactionCreatedEvent`, `V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent`, `V1IssuingTransactionUpdatedEvent` | Added | `issuing.Transaction` |
| `V1MandateUpdatedEvent` | Added | `Mandate` |
| `V1PaymentIntentAmountCapturableUpdatedEvent`, `V1PaymentIntentCanceledEvent`, `V1PaymentIntentCreatedEvent`, `V1PaymentIntentPartiallyFundedEvent`, `V1PaymentIntentPaymentFailedEvent`, `V1PaymentIntentProcessingEvent`, `V1PaymentIntentRequiresActionEvent`, `V1PaymentIntentSucceededEvent` | Added | `PaymentIntent` |
| `V1PaymentLinkCreatedEvent`, `V1PaymentLinkUpdatedEvent` | Added | `PaymentLink` |
| `V1PaymentMethodAttachedEvent`, `V1PaymentMethodAutomaticallyUpdatedEvent`, `V1PaymentMethodDetachedEvent`, `V1PaymentMethodUpdatedEvent` | Added | `PaymentMethod` |
| `V1PayoutCanceledEvent`, `V1PayoutCreatedEvent`, `V1PayoutFailedEvent`, `V1PayoutPaidEvent`, `V1PayoutReconciliationCompletedEvent`, `V1PayoutUpdatedEvent` | Added | `Payout` |
| `V1PersonCreatedEvent`, `V1PersonDeletedEvent`, `V1PersonUpdatedEvent` | Added | `Person` |
| `V1PlanCreatedEvent`, `V1PlanDeletedEvent`, `V1PlanUpdatedEvent` | Added | `Plan` |
| `V1PriceCreatedEvent`, `V1PriceDeletedEvent`, `V1PriceUpdatedEvent` | Added | `Price` |
| `V1ProductCreatedEvent`, `V1ProductDeletedEvent`, `V1ProductUpdatedEvent` | Added | `Product` |
| `V1PromotionCodeCreatedEvent`, `V1PromotionCodeUpdatedEvent` | Added | `PromotionCode` |
| `V1QuoteAcceptedEvent`, `V1QuoteCanceledEvent`, `V1QuoteCreatedEvent`, `V1QuoteFinalizedEvent` | Added | `Quote` |
| `V1RadarEarlyFraudWarningCreatedEvent`, `V1RadarEarlyFraudWarningUpdatedEvent` | Added | `radar.EarlyFraudWarning` |
| `V1ReviewClosedEvent`, `V1ReviewOpenedEvent` | Added | `Review` |
| `V1SetupIntentCanceledEvent`, `V1SetupIntentCreatedEvent`, `V1SetupIntentRequiresActionEvent`, `V1SetupIntentSetupFailedEvent`, `V1SetupIntentSucceededEvent` | Added | `SetupIntent` |
| `V1SigmaScheduledQueryRunCreatedEvent` | Added | `sigma.ScheduledQueryRun` |
| `V1SourceCanceledEvent`, `V1SourceChargeableEvent`, `V1SourceFailedEvent`, `V1SourceRefundAttributesRequiredEvent` | Added | `Source` |
| `V1SubscriptionScheduleAbortedEvent`, `V1SubscriptionScheduleCanceledEvent`, `V1SubscriptionScheduleCompletedEvent`, `V1SubscriptionScheduleCreatedEvent`, `V1SubscriptionScheduleExpiringEvent`, `V1SubscriptionScheduleReleasedEvent`, `V1SubscriptionScheduleUpdatedEvent` | Added | `SubscriptionSchedule` |
| `V1TaxSettingsUpdatedEvent` | Added | `tax.Settings` |
| `V1TaxRateCreatedEvent`, `V1TaxRateUpdatedEvent` | Added | `TaxRate` |
| `V1TerminalReaderActionFailedEvent`, `V1TerminalReaderActionSucceededEvent`, `V1TerminalReaderActionUpdatedEvent` | Added | `terminal.Reader` |
| `V1TestHelpersTestClockAdvancingEvent`, `V1TestHelpersTestClockCreatedEvent`, `V1TestHelpersTestClockDeletedEvent`, `V1TestHelpersTestClockInternalFailureEvent`, `V1TestHelpersTestClockReadyEvent` | Added | `testhelpers.TestClock` |
| `V1TopupCanceledEvent`, `V1TopupCreatedEvent`, `V1TopupFailedEvent`, `V1TopupReversedEvent`, `V1TopupSucceededEvent` | Added | `Topup` |
| `V1TransferCreatedEvent`, `V1TransferReversedEvent`, `V1TransferUpdatedEvent` | Added | `Transfer` |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `snapshot_event` | Added | [V2.Core.Event](/api/v2/core/events/object?api-version=2026-09-30.endive#v2_event_object) |
| `customer`, `subscription` | Added | [EventsV1InvoiceUpcomingEvent](/api/v2/core/events/event-types?api-version=2026-09-30.endive#v2_event_types-v1.invoice.upcoming) |

|  | Change | Event types |
| --- | --- | --- |
| `V1AccountApplicationAuthorizedEvent`, `V1AccountApplicationDeauthorizedEvent`, `V1AccountExternalAccountCreatedEvent`, `V1AccountExternalAccountDeletedEvent`, `V1AccountExternalAccountUpdatedEvent`, `V1BillingPortalSessionCreatedEvent`, `V1EntitlementsActiveEntitlementSummaryUpdatedEvent` | Added | `` |
| `V1AccountUpdatedEvent` | Added | `Account` |
| `V1ApplicationFeeCreatedEvent`, `V1ApplicationFeeRefundedEvent` | Added | `ApplicationFee` |
| `V1ApplicationFeeRefundUpdatedEvent` | Added | `FeeRefund` |
| `V1BalanceAvailableEvent` | Added | `Balance` |
| `V1BalanceSettingsUpdatedEvent` | Added | `BalanceSettings` |
| `V1BillingAlertTriggeredEvent` | Added | `Billing.Alert` |
| `V1BillingCreditBalanceTransactionCreatedEvent` | Added | `Billing.CreditBalanceTransaction` |
| `V1BillingCreditGrantCreatedEvent`, `V1BillingCreditGrantUpdatedEvent` | Added | `Billing.CreditGrant` |
| `V1BillingMeterCreatedEvent`, `V1BillingMeterDeactivatedEvent`, `V1BillingMeterReactivatedEvent`, `V1BillingMeterUpdatedEvent` | Added | `Billing.Meter` |
| `V1BillingPortalConfigurationCreatedEvent`, `V1BillingPortalConfigurationUpdatedEvent` | Added | `BillingPortal.Configuration` |
| `V1CapabilityUpdatedEvent` | Added | `Capability` |
| `V1CashBalanceFundsAvailableEvent` | Added | `CashBalance` |
| `V1ChargeCapturedEvent`, `V1ChargeExpiredEvent`, `V1ChargeFailedEvent`, `V1ChargePendingEvent`, `V1ChargeRefundedEvent`, `V1ChargeSucceededEvent`, `V1ChargeUpdatedEvent` | Added | `Charge` |
| `V1ChargeDisputeClosedEvent`, `V1ChargeDisputeCreatedEvent`, `V1ChargeDisputeFundsReinstatedEvent`, `V1ChargeDisputeFundsWithdrawnEvent`, `V1ChargeDisputeUpdatedEvent` | Added | `Dispute` |
| `V1ChargeRefundUpdatedEvent`, `V1RefundCreatedEvent`, `V1RefundFailedEvent`, `V1RefundUpdatedEvent` | Added | `Refund` |
| `V1CheckoutSessionAsyncPaymentFailedEvent`, `V1CheckoutSessionAsyncPaymentSucceededEvent`, `V1CheckoutSessionCompletedEvent`, `V1CheckoutSessionExpiredEvent` | Added | `Checkout.Session` |
| `V1ClimateOrderCanceledEvent`, `V1ClimateOrderCreatedEvent`, `V1ClimateOrderDelayedEvent`, `V1ClimateOrderDeliveredEvent`, `V1ClimateOrderProductSubstitutedEvent` | Added | `Climate.Order` |
| `V1ClimateProductCreatedEvent`, `V1ClimateProductPricingUpdatedEvent` | Added | `Climate.Product` |
| `V1CouponCreatedEvent`, `V1CouponDeletedEvent`, `V1CouponUpdatedEvent` | Added | `Coupon` |
| `V1CreditNoteCreatedEvent`, `V1CreditNoteUpdatedEvent`, `V1CreditNoteVoidedEvent` | Added | `CreditNote` |
| `V1CustomerCreatedEvent`, `V1CustomerDeletedEvent`, `V1CustomerUpdatedEvent` | Added | `Customer` |
| `V1CustomerDiscountCreatedEvent`, `V1CustomerDiscountDeletedEvent`, `V1CustomerDiscountUpdatedEvent` | Added | `Discount` |
| `V1CustomerSubscriptionCreatedEvent`, `V1CustomerSubscriptionDeletedEvent`, `V1CustomerSubscriptionPausedEvent`, `V1CustomerSubscriptionPendingUpdateAppliedEvent`, `V1CustomerSubscriptionPendingUpdateExpiredEvent`, `V1CustomerSubscriptionResumedEvent`, `V1CustomerSubscriptionTrialWillEndEvent`, `V1CustomerSubscriptionUpdatedEvent` | Added | `Subscription` |
| `V1CustomerTaxIdCreatedEvent`, `V1CustomerTaxIdDeletedEvent`, `V1CustomerTaxIdUpdatedEvent` | Added | `TaxId` |
| `V1CustomerCashBalanceTransactionCreatedEvent` | Added | `CustomerCashBalanceTransaction` |
| `V1FileCreatedEvent` | Added | `File` |
| `V1FinancialConnectionsAccountAccountNumbersUpdatedEvent`, `V1FinancialConnectionsAccountCreatedEvent`, `V1FinancialConnectionsAccountDeactivatedEvent`, `V1FinancialConnectionsAccountDisconnectedEvent`, `V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent`, `V1FinancialConnectionsAccountReactivatedEvent`, `V1FinancialConnectionsAccountRefreshedBalanceEvent`, `V1FinancialConnectionsAccountRefreshedOwnershipEvent`, `V1FinancialConnectionsAccountRefreshedTransactionsEvent`, `V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent`, `V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent`, `V1FinancialConnectionsAccountUpcomingDeactivationEvent` | Added | `FinancialConnections.Account` |
| `V1IdentityVerificationSessionCanceledEvent`, `V1IdentityVerificationSessionCreatedEvent`, `V1IdentityVerificationSessionProcessingEvent`, `V1IdentityVerificationSessionRedactedEvent`, `V1IdentityVerificationSessionRequiresInputEvent`, `V1IdentityVerificationSessionVerifiedEvent` | Added | `Identity.VerificationSession` |
| `V1InvoiceCreatedEvent`, `V1InvoiceDeletedEvent`, `V1InvoiceFinalizationFailedEvent`, `V1InvoiceFinalizedEvent`, `V1InvoiceMarkedUncollectibleEvent`, `V1InvoiceOverdueEvent`, `V1InvoiceOverpaidEvent`, `V1InvoicePaidEvent`, `V1InvoicePaymentActionRequiredEvent`, `V1InvoicePaymentAttemptRequiredEvent`, `V1InvoicePaymentFailedEvent`, `V1InvoicePaymentSucceededEvent`, `V1InvoiceSentEvent`, `V1InvoiceUpcomingEvent`, `V1InvoiceUpdatedEvent`, `V1InvoiceVoidedEvent`, `V1InvoiceWillBeDueEvent` | Added | `Invoice` |
| `V1InvoicePaymentPaidEvent` | Added | `InvoicePayment` |
| `V1InvoiceitemCreatedEvent`, `V1InvoiceitemDeletedEvent` | Added | `InvoiceItem` |
| `V1IssuingAuthorizationCreatedEvent`, `V1IssuingAuthorizationRequestEvent`, `V1IssuingAuthorizationUpdatedEvent` | Added | `Issuing.Authorization` |
| `V1IssuingCardCreatedEvent`, `V1IssuingCardUpdatedEvent` | Added | `Issuing.Card` |
| `V1IssuingCardholderCreatedEvent`, `V1IssuingCardholderUpdatedEvent` | Added | `Issuing.Cardholder` |
| `V1IssuingDisputeClosedEvent`, `V1IssuingDisputeCreatedEvent`, `V1IssuingDisputeFundsReinstatedEvent`, `V1IssuingDisputeFundsRescindedEvent`, `V1IssuingDisputeSubmittedEvent`, `V1IssuingDisputeUpdatedEvent` | Added | `Issuing.Dispute` |
| `V1IssuingPersonalizationDesignActivatedEvent`, `V1IssuingPersonalizationDesignDeactivatedEvent`, `V1IssuingPersonalizationDesignRejectedEvent`, `V1IssuingPersonalizationDesignUpdatedEvent` | Added | `Issuing.PersonalizationDesign` |
| `V1IssuingTokenCreatedEvent`, `V1IssuingTokenUpdatedEvent` | Added | `Issuing.Token` |
| `V1IssuingTransactionCreatedEvent`, `V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent`, `V1IssuingTransactionUpdatedEvent` | Added | `Issuing.Transaction` |
| `V1MandateUpdatedEvent` | Added | `Mandate` |
| `V1PaymentIntentAmountCapturableUpdatedEvent`, `V1PaymentIntentCanceledEvent`, `V1PaymentIntentCreatedEvent`, `V1PaymentIntentPartiallyFundedEvent`, `V1PaymentIntentPaymentFailedEvent`, `V1PaymentIntentProcessingEvent`, `V1PaymentIntentRequiresActionEvent`, `V1PaymentIntentSucceededEvent` | Added | `PaymentIntent` |
| `V1PaymentLinkCreatedEvent`, `V1PaymentLinkUpdatedEvent` | Added | `PaymentLink` |
| `V1PaymentMethodAttachedEvent`, `V1PaymentMethodAutomaticallyUpdatedEvent`, `V1PaymentMethodDetachedEvent`, `V1PaymentMethodUpdatedEvent` | Added | `PaymentMethod` |
| `V1PayoutCanceledEvent`, `V1PayoutCreatedEvent`, `V1PayoutFailedEvent`, `V1PayoutPaidEvent`, `V1PayoutReconciliationCompletedEvent`, `V1PayoutUpdatedEvent` | Added | `Payout` |
| `V1PersonCreatedEvent`, `V1PersonDeletedEvent`, `V1PersonUpdatedEvent` | Added | `Person` |
| `V1PlanCreatedEvent`, `V1PlanDeletedEvent`, `V1PlanUpdatedEvent` | Added | `Plan` |
| `V1PriceCreatedEvent`, `V1PriceDeletedEvent`, `V1PriceUpdatedEvent` | Added | `Price` |
| `V1ProductCreatedEvent`, `V1ProductDeletedEvent`, `V1ProductUpdatedEvent` | Added | `Product` |
| `V1PromotionCodeCreatedEvent`, `V1PromotionCodeUpdatedEvent` | Added | `PromotionCode` |
| `V1QuoteAcceptedEvent`, `V1QuoteCanceledEvent`, `V1QuoteCreatedEvent`, `V1QuoteFinalizedEvent` | Added | `Quote` |
| `V1RadarEarlyFraudWarningCreatedEvent`, `V1RadarEarlyFraudWarningUpdatedEvent` | Added | `Radar.EarlyFraudWarning` |
| `V1ReviewClosedEvent`, `V1ReviewOpenedEvent` | Added | `Review` |
| `V1SetupIntentCanceledEvent`, `V1SetupIntentCreatedEvent`, `V1SetupIntentRequiresActionEvent`, `V1SetupIntentSetupFailedEvent`, `V1SetupIntentSucceededEvent` | Added | `SetupIntent` |
| `V1SigmaScheduledQueryRunCreatedEvent` | Added | `Sigma.ScheduledQueryRun` |
| `V1SourceCanceledEvent`, `V1SourceChargeableEvent`, `V1SourceFailedEvent`, `V1SourceRefundAttributesRequiredEvent` | Added | `Source` |
| `V1SubscriptionScheduleAbortedEvent`, `V1SubscriptionScheduleCanceledEvent`, `V1SubscriptionScheduleCompletedEvent`, `V1SubscriptionScheduleCreatedEvent`, `V1SubscriptionScheduleExpiringEvent`, `V1SubscriptionScheduleReleasedEvent`, `V1SubscriptionScheduleUpdatedEvent` | Added | `SubscriptionSchedule` |
| `V1TaxSettingsUpdatedEvent` | Added | `Tax.Settings` |
| `V1TaxRateCreatedEvent`, `V1TaxRateUpdatedEvent` | Added | `TaxRate` |
| `V1TerminalReaderActionFailedEvent`, `V1TerminalReaderActionSucceededEvent`, `V1TerminalReaderActionUpdatedEvent` | Added | `Terminal.Reader` |
| `V1TestHelpersTestClockAdvancingEvent`, `V1TestHelpersTestClockCreatedEvent`, `V1TestHelpersTestClockDeletedEvent`, `V1TestHelpersTestClockInternalFailureEvent`, `V1TestHelpersTestClockReadyEvent` | Added | `TestHelpers.TestClock` |
| `V1TopupCanceledEvent`, `V1TopupCreatedEvent`, `V1TopupFailedEvent`, `V1TopupReversedEvent`, `V1TopupSucceededEvent` | Added | `Topup` |
| `V1TransferCreatedEvent`, `V1TransferReversedEvent`, `V1TransferUpdatedEvent` | Added | `Transfer` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `SnapshotEvent` | Added | [V2CoreEvent](/api/v2/core/events/object?api-version=2026-09-30.endive#v2_event_object) |
| `Customer`, `Subscription` | Added | [EventsV1InvoiceUpcomingEvent](/api/v2/core/events/event-types?api-version=2026-09-30.endive#v2_event_types-v1.invoice.upcoming) |

|  | Change | Event types |
| --- | --- | --- |
| `V1AccountApplicationAuthorizedEvent`, `V1AccountApplicationDeauthorizedEvent`, `V1AccountExternalAccountCreatedEvent`, `V1AccountExternalAccountDeletedEvent`, `V1AccountExternalAccountUpdatedEvent`, `V1BillingPortalSessionCreatedEvent`, `V1EntitlementsActiveEntitlementSummaryUpdatedEvent` | Added | `` |
| `V1AccountUpdatedEvent` | Added | `Account` |
| `V1ApplicationFeeCreatedEvent`, `V1ApplicationFeeRefundedEvent` | Added | `ApplicationFee` |
| `V1ApplicationFeeRefundUpdatedEvent` | Added | `FeeRefund` |
| `V1BalanceAvailableEvent` | Added | `Balance` |
| `V1BalanceSettingsUpdatedEvent` | Added | `BalanceSettings` |
| `V1BillingAlertTriggeredEvent` | Added | `BillingAlert` |
| `V1BillingCreditBalanceTransactionCreatedEvent` | Added | `BillingCreditBalanceTransaction` |
| `V1BillingCreditGrantCreatedEvent`, `V1BillingCreditGrantUpdatedEvent` | Added | `BillingCreditGrant` |
| `V1BillingMeterCreatedEvent`, `V1BillingMeterDeactivatedEvent`, `V1BillingMeterReactivatedEvent`, `V1BillingMeterUpdatedEvent` | Added | `BillingMeter` |
| `V1BillingPortalConfigurationCreatedEvent`, `V1BillingPortalConfigurationUpdatedEvent` | Added | `BillingPortalConfiguration` |
| `V1CapabilityUpdatedEvent` | Added | `Capability` |
| `V1CashBalanceFundsAvailableEvent` | Added | `CashBalance` |
| `V1ChargeCapturedEvent`, `V1ChargeExpiredEvent`, `V1ChargeFailedEvent`, `V1ChargePendingEvent`, `V1ChargeRefundedEvent`, `V1ChargeSucceededEvent`, `V1ChargeUpdatedEvent` | Added | `Charge` |
| `V1ChargeDisputeClosedEvent`, `V1ChargeDisputeCreatedEvent`, `V1ChargeDisputeFundsReinstatedEvent`, `V1ChargeDisputeFundsWithdrawnEvent`, `V1ChargeDisputeUpdatedEvent` | Added | `Dispute` |
| `V1ChargeRefundUpdatedEvent`, `V1RefundCreatedEvent`, `V1RefundFailedEvent`, `V1RefundUpdatedEvent` | Added | `Refund` |
| `V1CheckoutSessionAsyncPaymentFailedEvent`, `V1CheckoutSessionAsyncPaymentSucceededEvent`, `V1CheckoutSessionCompletedEvent`, `V1CheckoutSessionExpiredEvent` | Added | `CheckoutSession` |
| `V1ClimateOrderCanceledEvent`, `V1ClimateOrderCreatedEvent`, `V1ClimateOrderDelayedEvent`, `V1ClimateOrderDeliveredEvent`, `V1ClimateOrderProductSubstitutedEvent` | Added | `ClimateOrder` |
| `V1ClimateProductCreatedEvent`, `V1ClimateProductPricingUpdatedEvent` | Added | `ClimateProduct` |
| `V1CouponCreatedEvent`, `V1CouponDeletedEvent`, `V1CouponUpdatedEvent` | Added | `Coupon` |
| `V1CreditNoteCreatedEvent`, `V1CreditNoteUpdatedEvent`, `V1CreditNoteVoidedEvent` | Added | `CreditNote` |
| `V1CustomerCreatedEvent`, `V1CustomerDeletedEvent`, `V1CustomerUpdatedEvent` | Added | `Customer` |
| `V1CustomerDiscountCreatedEvent`, `V1CustomerDiscountDeletedEvent`, `V1CustomerDiscountUpdatedEvent` | Added | `Discount` |
| `V1CustomerSubscriptionCreatedEvent`, `V1CustomerSubscriptionDeletedEvent`, `V1CustomerSubscriptionPausedEvent`, `V1CustomerSubscriptionPendingUpdateAppliedEvent`, `V1CustomerSubscriptionPendingUpdateExpiredEvent`, `V1CustomerSubscriptionResumedEvent`, `V1CustomerSubscriptionTrialWillEndEvent`, `V1CustomerSubscriptionUpdatedEvent` | Added | `Subscription` |
| `V1CustomerTaxIdCreatedEvent`, `V1CustomerTaxIdDeletedEvent`, `V1CustomerTaxIdUpdatedEvent` | Added | `TaxID` |
| `V1CustomerCashBalanceTransactionCreatedEvent` | Added | `CustomerCashBalanceTransaction` |
| `V1FileCreatedEvent` | Added | `File` |
| `V1FinancialConnectionsAccountAccountNumbersUpdatedEvent`, `V1FinancialConnectionsAccountCreatedEvent`, `V1FinancialConnectionsAccountDeactivatedEvent`, `V1FinancialConnectionsAccountDisconnectedEvent`, `V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent`, `V1FinancialConnectionsAccountReactivatedEvent`, `V1FinancialConnectionsAccountRefreshedBalanceEvent`, `V1FinancialConnectionsAccountRefreshedOwnershipEvent`, `V1FinancialConnectionsAccountRefreshedTransactionsEvent`, `V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent`, `V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent`, `V1FinancialConnectionsAccountUpcomingDeactivationEvent` | Added | `FinancialConnectionsAccount` |
| `V1IdentityVerificationSessionCanceledEvent`, `V1IdentityVerificationSessionCreatedEvent`, `V1IdentityVerificationSessionProcessingEvent`, `V1IdentityVerificationSessionRedactedEvent`, `V1IdentityVerificationSessionRequiresInputEvent`, `V1IdentityVerificationSessionVerifiedEvent` | Added | `IdentityVerificationSession` |
| `V1InvoiceCreatedEvent`, `V1InvoiceDeletedEvent`, `V1InvoiceFinalizationFailedEvent`, `V1InvoiceFinalizedEvent`, `V1InvoiceMarkedUncollectibleEvent`, `V1InvoiceOverdueEvent`, `V1InvoiceOverpaidEvent`, `V1InvoicePaidEvent`, `V1InvoicePaymentActionRequiredEvent`, `V1InvoicePaymentAttemptRequiredEvent`, `V1InvoicePaymentFailedEvent`, `V1InvoicePaymentSucceededEvent`, `V1InvoiceSentEvent`, `V1InvoiceUpcomingEvent`, `V1InvoiceUpdatedEvent`, `V1InvoiceVoidedEvent`, `V1InvoiceWillBeDueEvent` | Added | `Invoice` |
| `V1InvoicePaymentPaidEvent` | Added | `InvoicePayment` |
| `V1InvoiceitemCreatedEvent`, `V1InvoiceitemDeletedEvent` | Added | `InvoiceItem` |
| `V1IssuingAuthorizationCreatedEvent`, `V1IssuingAuthorizationRequestEvent`, `V1IssuingAuthorizationUpdatedEvent` | Added | `IssuingAuthorization` |
| `V1IssuingCardCreatedEvent`, `V1IssuingCardUpdatedEvent` | Added | `IssuingCard` |
| `V1IssuingCardholderCreatedEvent`, `V1IssuingCardholderUpdatedEvent` | Added | `IssuingCardholder` |
| `V1IssuingDisputeClosedEvent`, `V1IssuingDisputeCreatedEvent`, `V1IssuingDisputeFundsReinstatedEvent`, `V1IssuingDisputeFundsRescindedEvent`, `V1IssuingDisputeSubmittedEvent`, `V1IssuingDisputeUpdatedEvent` | Added | `IssuingDispute` |
| `V1IssuingPersonalizationDesignActivatedEvent`, `V1IssuingPersonalizationDesignDeactivatedEvent`, `V1IssuingPersonalizationDesignRejectedEvent`, `V1IssuingPersonalizationDesignUpdatedEvent` | Added | `IssuingPersonalizationDesign` |
| `V1IssuingTokenCreatedEvent`, `V1IssuingTokenUpdatedEvent` | Added | `IssuingToken` |
| `V1IssuingTransactionCreatedEvent`, `V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent`, `V1IssuingTransactionUpdatedEvent` | Added | `IssuingTransaction` |
| `V1MandateUpdatedEvent` | Added | `Mandate` |
| `V1PaymentIntentAmountCapturableUpdatedEvent`, `V1PaymentIntentCanceledEvent`, `V1PaymentIntentCreatedEvent`, `V1PaymentIntentPartiallyFundedEvent`, `V1PaymentIntentPaymentFailedEvent`, `V1PaymentIntentProcessingEvent`, `V1PaymentIntentRequiresActionEvent`, `V1PaymentIntentSucceededEvent` | Added | `PaymentIntent` |
| `V1PaymentLinkCreatedEvent`, `V1PaymentLinkUpdatedEvent` | Added | `PaymentLink` |
| `V1PaymentMethodAttachedEvent`, `V1PaymentMethodAutomaticallyUpdatedEvent`, `V1PaymentMethodDetachedEvent`, `V1PaymentMethodUpdatedEvent` | Added | `PaymentMethod` |
| `V1PayoutCanceledEvent`, `V1PayoutCreatedEvent`, `V1PayoutFailedEvent`, `V1PayoutPaidEvent`, `V1PayoutReconciliationCompletedEvent`, `V1PayoutUpdatedEvent` | Added | `Payout` |
| `V1PersonCreatedEvent`, `V1PersonDeletedEvent`, `V1PersonUpdatedEvent` | Added | `Person` |
| `V1PlanCreatedEvent`, `V1PlanDeletedEvent`, `V1PlanUpdatedEvent` | Added | `Plan` |
| `V1PriceCreatedEvent`, `V1PriceDeletedEvent`, `V1PriceUpdatedEvent` | Added | `Price` |
| `V1ProductCreatedEvent`, `V1ProductDeletedEvent`, `V1ProductUpdatedEvent` | Added | `Product` |
| `V1PromotionCodeCreatedEvent`, `V1PromotionCodeUpdatedEvent` | Added | `PromotionCode` |
| `V1QuoteAcceptedEvent`, `V1QuoteCanceledEvent`, `V1QuoteCreatedEvent`, `V1QuoteFinalizedEvent` | Added | `Quote` |
| `V1RadarEarlyFraudWarningCreatedEvent`, `V1RadarEarlyFraudWarningUpdatedEvent` | Added | `RadarEarlyFraudWarning` |
| `V1ReviewClosedEvent`, `V1ReviewOpenedEvent` | Added | `Review` |
| `V1SetupIntentCanceledEvent`, `V1SetupIntentCreatedEvent`, `V1SetupIntentRequiresActionEvent`, `V1SetupIntentSetupFailedEvent`, `V1SetupIntentSucceededEvent` | Added | `SetupIntent` |
| `V1SigmaScheduledQueryRunCreatedEvent` | Added | `SigmaScheduledQueryRun` |
| `V1SourceCanceledEvent`, `V1SourceChargeableEvent`, `V1SourceFailedEvent`, `V1SourceRefundAttributesRequiredEvent` | Added | `Source` |
| `V1SubscriptionScheduleAbortedEvent`, `V1SubscriptionScheduleCanceledEvent`, `V1SubscriptionScheduleCompletedEvent`, `V1SubscriptionScheduleCreatedEvent`, `V1SubscriptionScheduleExpiringEvent`, `V1SubscriptionScheduleReleasedEvent`, `V1SubscriptionScheduleUpdatedEvent` | Added | `SubscriptionSchedule` |
| `V1TaxSettingsUpdatedEvent` | Added | `TaxSettings` |
| `V1TaxRateCreatedEvent`, `V1TaxRateUpdatedEvent` | Added | `TaxRate` |
| `V1TerminalReaderActionFailedEvent`, `V1TerminalReaderActionSucceededEvent`, `V1TerminalReaderActionUpdatedEvent` | Added | `TerminalReader` |
| `V1TestHelpersTestClockAdvancingEvent`, `V1TestHelpersTestClockCreatedEvent`, `V1TestHelpersTestClockDeletedEvent`, `V1TestHelpersTestClockInternalFailureEvent`, `V1TestHelpersTestClockReadyEvent` | Added | `TestHelpersTestClock` |
| `V1TopupCanceledEvent`, `V1TopupCreatedEvent`, `V1TopupFailedEvent`, `V1TopupReversedEvent`, `V1TopupSucceededEvent` | Added | `Topup` |
| `V1TransferCreatedEvent`, `V1TransferReversedEvent`, `V1TransferUpdatedEvent` | Added | `Transfer` |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `SnapshotEvent` | Added | [V2.Core.Event](/api/v2/core/events/object?api-version=2026-09-30.endive#v2_event_object) |
| `Customer`, `Subscription` | Added | [EventsV1InvoiceUpcomingEvent](/api/v2/core/events/event-types?api-version=2026-09-30.endive#v2_event_types-v1.invoice.upcoming) |

|  | Change | Event types |
| --- | --- | --- |
| `V1AccountApplicationAuthorizedEvent`, `V1AccountApplicationDeauthorizedEvent`, `V1AccountExternalAccountCreatedEvent`, `V1AccountExternalAccountDeletedEvent`, `V1AccountExternalAccountUpdatedEvent`, `V1BillingPortalSessionCreatedEvent`, `V1EntitlementsActiveEntitlementSummaryUpdatedEvent` | Added | `` |
| `V1AccountUpdatedEvent` | Added | `Account` |
| `V1ApplicationFeeCreatedEvent`, `V1ApplicationFeeRefundedEvent` | Added | `ApplicationFee` |
| `V1ApplicationFeeRefundUpdatedEvent` | Added | `ApplicationFeeRefund` |
| `V1BalanceAvailableEvent` | Added | `Balance` |
| `V1BalanceSettingsUpdatedEvent` | Added | `BalanceSettings` |
| `V1BillingAlertTriggeredEvent` | Added | `Billing.Alert` |
| `V1BillingCreditBalanceTransactionCreatedEvent` | Added | `Billing.CreditBalanceTransaction` |
| `V1BillingCreditGrantCreatedEvent`, `V1BillingCreditGrantUpdatedEvent` | Added | `Billing.CreditGrant` |
| `V1BillingMeterCreatedEvent`, `V1BillingMeterDeactivatedEvent`, `V1BillingMeterReactivatedEvent`, `V1BillingMeterUpdatedEvent` | Added | `Billing.Meter` |
| `V1BillingPortalConfigurationCreatedEvent`, `V1BillingPortalConfigurationUpdatedEvent` | Added | `BillingPortal.Configuration` |
| `V1CapabilityUpdatedEvent` | Added | `Capability` |
| `V1CashBalanceFundsAvailableEvent` | Added | `CashBalance` |
| `V1ChargeCapturedEvent`, `V1ChargeExpiredEvent`, `V1ChargeFailedEvent`, `V1ChargePendingEvent`, `V1ChargeRefundedEvent`, `V1ChargeSucceededEvent`, `V1ChargeUpdatedEvent` | Added | `Charge` |
| `V1ChargeDisputeClosedEvent`, `V1ChargeDisputeCreatedEvent`, `V1ChargeDisputeFundsReinstatedEvent`, `V1ChargeDisputeFundsWithdrawnEvent`, `V1ChargeDisputeUpdatedEvent` | Added | `Dispute` |
| `V1ChargeRefundUpdatedEvent`, `V1RefundCreatedEvent`, `V1RefundFailedEvent`, `V1RefundUpdatedEvent` | Added | `Refund` |
| `V1CheckoutSessionAsyncPaymentFailedEvent`, `V1CheckoutSessionAsyncPaymentSucceededEvent`, `V1CheckoutSessionCompletedEvent`, `V1CheckoutSessionExpiredEvent` | Added | `Checkout.Session` |
| `V1ClimateOrderCanceledEvent`, `V1ClimateOrderCreatedEvent`, `V1ClimateOrderDelayedEvent`, `V1ClimateOrderDeliveredEvent`, `V1ClimateOrderProductSubstitutedEvent` | Added | `Climate.Order` |
| `V1ClimateProductCreatedEvent`, `V1ClimateProductPricingUpdatedEvent` | Added | `Climate.Product` |
| `V1CouponCreatedEvent`, `V1CouponDeletedEvent`, `V1CouponUpdatedEvent` | Added | `Coupon` |
| `V1CreditNoteCreatedEvent`, `V1CreditNoteUpdatedEvent`, `V1CreditNoteVoidedEvent` | Added | `CreditNote` |
| `V1CustomerCreatedEvent`, `V1CustomerDeletedEvent`, `V1CustomerUpdatedEvent` | Added | `Customer` |
| `V1CustomerDiscountCreatedEvent`, `V1CustomerDiscountDeletedEvent`, `V1CustomerDiscountUpdatedEvent` | Added | `Discount` |
| `V1CustomerSubscriptionCreatedEvent`, `V1CustomerSubscriptionDeletedEvent`, `V1CustomerSubscriptionPausedEvent`, `V1CustomerSubscriptionPendingUpdateAppliedEvent`, `V1CustomerSubscriptionPendingUpdateExpiredEvent`, `V1CustomerSubscriptionResumedEvent`, `V1CustomerSubscriptionTrialWillEndEvent`, `V1CustomerSubscriptionUpdatedEvent` | Added | `Subscription` |
| `V1CustomerTaxIdCreatedEvent`, `V1CustomerTaxIdDeletedEvent`, `V1CustomerTaxIdUpdatedEvent` | Added | `TaxId` |
| `V1CustomerCashBalanceTransactionCreatedEvent` | Added | `CustomerCashBalanceTransaction` |
| `V1FileCreatedEvent` | Added | `File` |
| `V1FinancialConnectionsAccountAccountNumbersUpdatedEvent`, `V1FinancialConnectionsAccountCreatedEvent`, `V1FinancialConnectionsAccountDeactivatedEvent`, `V1FinancialConnectionsAccountDisconnectedEvent`, `V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent`, `V1FinancialConnectionsAccountReactivatedEvent`, `V1FinancialConnectionsAccountRefreshedBalanceEvent`, `V1FinancialConnectionsAccountRefreshedOwnershipEvent`, `V1FinancialConnectionsAccountRefreshedTransactionsEvent`, `V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent`, `V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent`, `V1FinancialConnectionsAccountUpcomingDeactivationEvent` | Added | `FinancialConnections.Account` |
| `V1IdentityVerificationSessionCanceledEvent`, `V1IdentityVerificationSessionCreatedEvent`, `V1IdentityVerificationSessionProcessingEvent`, `V1IdentityVerificationSessionRedactedEvent`, `V1IdentityVerificationSessionRequiresInputEvent`, `V1IdentityVerificationSessionVerifiedEvent` | Added | `Identity.VerificationSession` |
| `V1InvoiceCreatedEvent`, `V1InvoiceDeletedEvent`, `V1InvoiceFinalizationFailedEvent`, `V1InvoiceFinalizedEvent`, `V1InvoiceMarkedUncollectibleEvent`, `V1InvoiceOverdueEvent`, `V1InvoiceOverpaidEvent`, `V1InvoicePaidEvent`, `V1InvoicePaymentActionRequiredEvent`, `V1InvoicePaymentAttemptRequiredEvent`, `V1InvoicePaymentFailedEvent`, `V1InvoicePaymentSucceededEvent`, `V1InvoiceSentEvent`, `V1InvoiceUpcomingEvent`, `V1InvoiceUpdatedEvent`, `V1InvoiceVoidedEvent`, `V1InvoiceWillBeDueEvent` | Added | `Invoice` |
| `V1InvoicePaymentPaidEvent` | Added | `InvoicePayment` |
| `V1InvoiceitemCreatedEvent`, `V1InvoiceitemDeletedEvent` | Added | `InvoiceItem` |
| `V1IssuingAuthorizationCreatedEvent`, `V1IssuingAuthorizationRequestEvent`, `V1IssuingAuthorizationUpdatedEvent` | Added | `Issuing.Authorization` |
| `V1IssuingCardCreatedEvent`, `V1IssuingCardUpdatedEvent` | Added | `Issuing.Card` |
| `V1IssuingCardholderCreatedEvent`, `V1IssuingCardholderUpdatedEvent` | Added | `Issuing.Cardholder` |
| `V1IssuingDisputeClosedEvent`, `V1IssuingDisputeCreatedEvent`, `V1IssuingDisputeFundsReinstatedEvent`, `V1IssuingDisputeFundsRescindedEvent`, `V1IssuingDisputeSubmittedEvent`, `V1IssuingDisputeUpdatedEvent` | Added | `Issuing.Dispute` |
| `V1IssuingPersonalizationDesignActivatedEvent`, `V1IssuingPersonalizationDesignDeactivatedEvent`, `V1IssuingPersonalizationDesignRejectedEvent`, `V1IssuingPersonalizationDesignUpdatedEvent` | Added | `Issuing.PersonalizationDesign` |
| `V1IssuingTokenCreatedEvent`, `V1IssuingTokenUpdatedEvent` | Added | `Issuing.Token` |
| `V1IssuingTransactionCreatedEvent`, `V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent`, `V1IssuingTransactionUpdatedEvent` | Added | `Issuing.Transaction` |
| `V1MandateUpdatedEvent` | Added | `Mandate` |
| `V1PaymentIntentAmountCapturableUpdatedEvent`, `V1PaymentIntentCanceledEvent`, `V1PaymentIntentCreatedEvent`, `V1PaymentIntentPartiallyFundedEvent`, `V1PaymentIntentPaymentFailedEvent`, `V1PaymentIntentProcessingEvent`, `V1PaymentIntentRequiresActionEvent`, `V1PaymentIntentSucceededEvent` | Added | `PaymentIntent` |
| `V1PaymentLinkCreatedEvent`, `V1PaymentLinkUpdatedEvent` | Added | `PaymentLink` |
| `V1PaymentMethodAttachedEvent`, `V1PaymentMethodAutomaticallyUpdatedEvent`, `V1PaymentMethodDetachedEvent`, `V1PaymentMethodUpdatedEvent` | Added | `PaymentMethod` |
| `V1PayoutCanceledEvent`, `V1PayoutCreatedEvent`, `V1PayoutFailedEvent`, `V1PayoutPaidEvent`, `V1PayoutReconciliationCompletedEvent`, `V1PayoutUpdatedEvent` | Added | `Payout` |
| `V1PersonCreatedEvent`, `V1PersonDeletedEvent`, `V1PersonUpdatedEvent` | Added | `Person` |
| `V1PlanCreatedEvent`, `V1PlanDeletedEvent`, `V1PlanUpdatedEvent` | Added | `Plan` |
| `V1PriceCreatedEvent`, `V1PriceDeletedEvent`, `V1PriceUpdatedEvent` | Added | `Price` |
| `V1ProductCreatedEvent`, `V1ProductDeletedEvent`, `V1ProductUpdatedEvent` | Added | `Product` |
| `V1PromotionCodeCreatedEvent`, `V1PromotionCodeUpdatedEvent` | Added | `PromotionCode` |
| `V1QuoteAcceptedEvent`, `V1QuoteCanceledEvent`, `V1QuoteCreatedEvent`, `V1QuoteFinalizedEvent` | Added | `Quote` |
| `V1RadarEarlyFraudWarningCreatedEvent`, `V1RadarEarlyFraudWarningUpdatedEvent` | Added | `Radar.EarlyFraudWarning` |
| `V1ReviewClosedEvent`, `V1ReviewOpenedEvent` | Added | `Review` |
| `V1SetupIntentCanceledEvent`, `V1SetupIntentCreatedEvent`, `V1SetupIntentRequiresActionEvent`, `V1SetupIntentSetupFailedEvent`, `V1SetupIntentSucceededEvent` | Added | `SetupIntent` |
| `V1SigmaScheduledQueryRunCreatedEvent` | Added | `Sigma.ScheduledQueryRun` |
| `V1SourceCanceledEvent`, `V1SourceChargeableEvent`, `V1SourceFailedEvent`, `V1SourceRefundAttributesRequiredEvent` | Added | `Source` |
| `V1SubscriptionScheduleAbortedEvent`, `V1SubscriptionScheduleCanceledEvent`, `V1SubscriptionScheduleCompletedEvent`, `V1SubscriptionScheduleCreatedEvent`, `V1SubscriptionScheduleExpiringEvent`, `V1SubscriptionScheduleReleasedEvent`, `V1SubscriptionScheduleUpdatedEvent` | Added | `SubscriptionSchedule` |
| `V1TaxSettingsUpdatedEvent` | Added | `Tax.Settings` |
| `V1TaxRateCreatedEvent`, `V1TaxRateUpdatedEvent` | Added | `TaxRate` |
| `V1TerminalReaderActionFailedEvent`, `V1TerminalReaderActionSucceededEvent`, `V1TerminalReaderActionUpdatedEvent` | Added | `Terminal.Reader` |
| `V1TestHelpersTestClockAdvancingEvent`, `V1TestHelpersTestClockCreatedEvent`, `V1TestHelpersTestClockDeletedEvent`, `V1TestHelpersTestClockInternalFailureEvent`, `V1TestHelpersTestClockReadyEvent` | Added | `TestHelpers.TestClock` |
| `V1TopupCanceledEvent`, `V1TopupCreatedEvent`, `V1TopupFailedEvent`, `V1TopupReversedEvent`, `V1TopupSucceededEvent` | Added | `Topup` |
| `V1TransferCreatedEvent`, `V1TransferReversedEvent`, `V1TransferUpdatedEvent` | Added | `Transfer` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.endive`
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
