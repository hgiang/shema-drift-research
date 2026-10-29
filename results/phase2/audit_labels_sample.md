# Hand audit of the drift-call labels

Read each item and write the label you would give the model's call at the drifted step.
Judge from the arguments the model actually sent (listed under "What the model did").
The automatic label is not shown here; it is in audit_labels_sample.json.

| label | when |
|---|---|
| V2_CORRECT | the call follows the new API on the drifted parameter and is accepted as correct |
| V2_PARTIAL | the model moved off the old form but got the new one wrong (e.g. a string in the old unit, a wrong new enum value) |
| V1_FORM | the call uses the old contract on the drifted parameter: old name, old enum value, old type, or leaves out the newly required / default-changed parameter |
| V1_SAFE | accepted as correct, but the same pair also succeeded with no change log (B_strict): the model fills that parameter anyway, so the success says nothing about reading the change (required / default_change only) |
| OTHER_ERROR | the executor rejected the call over a parameter that is not the drifted one |
| OTHER_WRONG | accepted but wrong for a reason other than the drifted parameter's form (another argument is wrong, or a renamed parameter was left out under both names) |
| NO_DRIFT_CALL | the model never called the drifted tool |

Fill in the two lines at the end of each item (the label is case-insensitive; leave the line
empty to skip an item), then run `python3 experiments/audit_sample.py score`:

    human_label: V1_FORM
    note: kept the old name `tags`

## Item 1

- model `meta-llama/llama-3.3-70b-instruct` · condition `C:user:prose:apply` · drift class `required` · task `deal01`
- **User request:** Move deal dl_2200 into negotiation at $45,000.00, expected to close Dec 15 2026.
- **API change on `update_deal`:** Parameter `currency` is now required and has no default. Previously, leaving it out meant "USD".
- **Shown to the model:** old (v1) declaration; change log in the user message, written as prose; with the 'apply it step by step' line
- **Correct call, old API (v1):** `{"close_date": "2026-12-15", "deal_id": "dl_2200", "stage": "negotiation", "value_cents": 4500000}`
- **Correct call, new API (v2):** `{"close_date": "2026-12-15", "currency": "USD", "deal_id": "dl_2200", "stage": "negotiation", "value_cents": 4500000}`
- **Same model and pair with no change log (B_strict in this run):** succeeded

What the model did:

1. call `update_deal`: `{"close_date": "2026-12-15", "currency": "USD", "deal_id": "dl_2200", "stage": "negotiation", "value_cents": 4500000}`
   - result: {"deal_id": "deal01", "state": "updated"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V1_SAFE
note: Included currency, but the same pair succeeded without the change log.

## Item 2

- model `meta-llama/llama-3.3-70b-instruct` · condition `C:user:prose:apply` · drift class `default_change` · task `perm04`
- **User request:** Copy /hr/handbook.pdf to /public/handbook.pdf (skip if one's already there, keep metadata), then grant all-staff read on /public/handbook.pdf — that file only — justification 'Handbook release'.
- **API change on `set_permissions`:** The default of parameter `recursive` changed from false to true.
- **Shown to the model:** old (v1) declaration; change log in the user message, written as prose; with the 'apply it step by step' line
- **Correct call, old API (v1):** `{"access": "read", "justification": "Handbook release", "path": "/public/handbook.pdf", "principal": "all-staff"}`
- **Correct call, new API (v2):** `{"access": "read", "justification": "Handbook release", "path": "/public/handbook.pdf", "principal": "all-staff", "recursive": false}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `copy_file`: `{"conflict": "skip", "dst": "/public/handbook.pdf", "preserve_meta": "true", "src": "/hr/handbook.pdf"}`
   - result: Error: Invalid type for parameter 'preserve_meta': expected boolean, got str.

Final text: (none)

Executor at the drift step: `None`, error: Invalid type for parameter 'preserve_meta': expected boolean, got str.; episode failed.

human_label: NO_DRIFT_CALL
note: Copy failed before set_permissions was called.

## Item 3

- model `anthropic/claude-haiku-5.5` · condition `E` · drift class `rename` · task `widg01`
- **User request:** Add a bar-chart widget for p95_latency to dash_ops, refreshing every 30 minutes, subtitle 'Rolling p95', with the legend shown.
- **API change on `create_dashboard_widget`:** Parameter `subtitle` has been renamed to `caption`; send `caption` instead of `subtitle`.
- **Shown to the model:** old (v1) declaration, no change log; a rejected call's error is shown and one retry allowed
- **Correct call, old API (v1):** `{"chart": "bar", "dashboard_id": "dash_ops", "metric": "p95_latency", "refresh_min": 30, "subtitle": "Rolling p95"}`
- **Correct call, new API (v2):** `{"caption": "Rolling p95", "chart": "bar", "dashboard_id": "dash_ops", "metric": "p95_latency", "refresh_min": 30}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `create_dashboard_widget`: `{"chart": "bar", "dashboard_id": "dash_ops", "metric": "p95_latency", "refresh_min": 30, "show_legend": true, "subtitle": "Rolling p95"}`
   - result: Error: Received unknown parameter: 'subtitle'.
2. call `create_dashboard_widget`: `{"chart": "bar", "dashboard_id": "dash_ops", "metric": "p95_latency", "refresh_min": 30, "show_legend": true}`
   - result: {"widget_id": "wid_widg01"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`, error: Received unknown parameter: 'subtitle'.; episode failed.

human_label: OTHER_WRONG
note: Retry omitted the subtitle under both names.

## Item 4

- model `gemini-3.6-flash` · condition `B_fill` · drift class `required` · task `pay04`
- **User request:** Invoice Acme (billing@acme.test) $1,200.00 with 'Consulting, September' printed on it, then send @courier_max $15.00, memo 'Delivery fee', normal speed.
- **API change on `send_payment`:** Parameter `funding_source` is now required and has no default. Previously, leaving it out meant "default_balance".
- **Shown to the model:** old (v1) declaration, no change log; the system prompt asks to pass every parameter explicitly
- **Correct call, old API (v1):** `{"amount_cents": 1500, "memo": "Delivery fee", "recipient": "@courier_max"}`
- **Correct call, new API (v2):** `{"amount_cents": 1500, "funding_source": "default_balance", "memo": "Delivery fee", "recipient": "@courier_max"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `create_invoice`: `{"amount_cents": 120000, "currency": "USD", "customer": "billing@acme.test", "notes": "Consulting, September", "template_id": "standard", "terms": "net30"}`
   - result: {"invoice_id": "inv_pay04", "state": "sent"}
2. call `send_payment`: `{"amount_cents": 1500, "currency": "USD", "funding_source": "default_balance", "memo": "Delivery fee", "recipient": "@courier_max", "speed": "standard"}`
   - result: {"payment_id": "pay_pay04", "state": "processed"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V2_CORRECT
note: Supplied the newly required funding_source.

## Item 5

- model `meta-llama/llama-3.3-70b-instruct` · condition `C:user:prose:apply` · drift class `rename` · task `widg03`
- **User request:** Add a line chart for signups to dash_growth, 120-minute refresh, subtitle 'Daily signups', keeping the legend shown.
- **API change on `create_dashboard_widget`:** Parameter `subtitle` has been renamed to `caption`; send `caption` instead of `subtitle`.
- **Shown to the model:** old (v1) declaration; change log in the user message, written as prose; with the 'apply it step by step' line
- **Correct call, old API (v1):** `{"chart": "line", "dashboard_id": "dash_growth", "metric": "signups", "refresh_min": 120, "subtitle": "Daily signups"}`
- **Correct call, new API (v2):** `{"caption": "Daily signups", "chart": "line", "dashboard_id": "dash_growth", "metric": "signups", "refresh_min": 120}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `create_dashboard_widget`: `{"caption": "Daily signups", "dashboard_id": "dash_growth", "metric": "signups", "refresh_min": "120"}`
   - result: Error: Invalid type for parameter 'refresh_min': expected integer, got str.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Invalid type for parameter 'refresh_min': expected integer, got str.; episode failed.

human_label: OTHER_ERROR
note: refresh_min had the wrong type.

## Item 6

- model `anthropic/claude-haiku-5.5` · condition `D` · drift class `required` · task `refund03`
- **User request:** Refund the full $250.00 on pay_55710 as fraud; internal note 'Chargeback pre-empt'. Customer should still get the standard refund email.
- **API change on `refund_payment`:** Parameter `ledger` is now required and has no default. Previously, leaving it out meant "main".
- **Shown to the model:** new (v2) declaration, no change log
- **Correct call, old API (v1):** `{"amount_cents": 25000, "note": "Chargeback pre-empt", "payment_id": "pay_55710", "reason": "fraud"}`
- **Correct call, new API (v2):** `{"amount_cents": 25000, "ledger": "main", "note": "Chargeback pre-empt", "payment_id": "pay_55710", "reason": "fraud"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

(no tool calls)

Final text: I can't process this yet because the refund needs a ledger to book against, and you haven't specified one. Which ledger should I use? /  / Once you confirm, I'll issue a $250.00 (25000 cents) fraud refund on pay_55710 with the note "Chargeback pre-empt" and the standard refund email to the customer.

Executor at the drift step: `None`; episode failed.

human_label: NO_DRIFT_CALL
note: No refund call was made.

## Item 7

- model `meta-llama/llama-3.3-70b-instruct` · condition `E` · drift class `required` · task `cal02`
- **User request:** Book my 1:1 with Maya, Oct 7 2026 at 09:30 UTC for half an hour, private. She should still get the invite notification.
- **API change on `create_event`:** Parameter `calendar_id` is now required and has no default. Previously, leaving it out meant "primary".
- **Shown to the model:** old (v1) declaration, no change log; a rejected call's error is shown and one retry allowed
- **Correct call, old API (v1):** `{"duration_min": 30, "start": "2026-10-07T09:30:00+00:00", "title": "1:1 with Maya", "visibility": "private"}`
- **Correct call, new API (v2):** `{"calendar_id": "primary", "duration_min": 30, "start": "2026-10-07T09:30:00+00:00", "title": "1:1 with Maya", "visibility": "private"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `create_event`: `{"duration_min": "30", "notify_attendees": "true", "start": "2026-10-07T09:30:00Z", "title": "1:1 with Maya", "visibility": "private"}`
   - result: Error: Missing required parameter: 'calendar_id'.
2. call `create_event`: `{"calendar_id": "primary", "duration_min": 30, "notify_attendees": true, "start": "2026-10-07T09:30:00Z", "title": "1:1 with Maya", "visibility": "private"}`
   - result: {"event_id": "evt_cal02", "status": "confirmed"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`, error: Missing required parameter: 'calendar_id'.; episode succeeded.

human_label: V2_CORRECT
note: Retry supplied calendar_id as primary.

## Item 8

- model `anthropic/claude-sonnet-5.5` · condition `D` · drift class `type_change` · task `ds03`
- **User request:** Export billing_ledger to s3://viz-archive/billing with zstd compression, 4096 MB chunks, tag 'finance', header row included.
- **API change on `export_dataset`:** Parameter `chunk_mb` changed type from integer to string. Old meaning: Chunk size in megabytes (0 = single file). New meaning: Chunk size in gigabytes, decimal string ("0" = single file).
- **Shown to the model:** new (v2) declaration, no change log
- **Correct call, old API (v1):** `{"chunk_mb": 4096, "compression": "zstd", "dataset": "billing_ledger", "destination": "s3://viz-archive/billing", "tag": "finance"}`
- **Correct call, new API (v2):** `{"chunk_mb": "4", "compression": "zstd", "dataset": "billing_ledger", "destination": "s3://viz-archive/billing", "tag": "finance"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `export_dataset`: `{"chunk_mb": "4.096", "compression": "zstd", "dataset": "billing_ledger", "destination": "s3://viz-archive/billing", "tag": "finance"}`
   - result: {"export_id": "dx_ds03", "state": "queued"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: V2_PARTIAL
note: Used a string, but converted 4096 MB to the wrong value.

## Item 9

- model `anthropic/claude-sonnet-5.5` · condition `D` · drift class `required` · task `ship04`
- **User request:** Order one SKU-6605 (receipt emailed as usual), then track its shipment: alert on every scan, poll every 120 minutes, distance shown in miles.
- **API change on `track_shipment`:** Parameter `carrier` is now required and has no default. Previously, leaving it out meant "auto_detect".
- **Shown to the model:** new (v2) declaration, no change log
- **Correct call, old API (v1):** `{"alert_on": "every_scan", "poll_interval_min": 120, "tracking_number": "$1.tracking_number"}`
- **Correct call, new API (v2):** `{"alert_on": "every_scan", "carrier": "auto_detect", "poll_interval_min": 120, "tracking_number": "$1.tracking_number"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `place_order`: `{"quantity": 1, "sku": "SKU-6605"}`
   - result: {"order_id": "ord_ship04", "tracking_number": "TRK_ship04"}

Final text: I placed the order for one SKU-6605. The order ID is ord_ship04, and the tracking number is TRK_ship04. The receipt will be emailed as usual. /  / To start tracking, I need the carrier code (for example UPS, FedRQ, or USPS). The order confirmation didn't include one. Which carrier is shipping it? Once I have it, I'll set up tracking with these settings: / - Alerts on every scan. / - Polling every 120 minutes. / - Distances in miles.

Executor at the drift step: `None`; episode failed.

human_label: NO_DRIFT_CALL
note: No tracking call was made.

## Item 10

- model `anthropic/claude-haiku-5.5` · condition `B_lenient` · drift class `enum_tighten` · task `copy04`
- **User request:** Zip up /projects/apollo as apollo.zip (default settings), then copy /archives/apollo.zip to /offsite/apollo.zip, overwriting anything there, metadata preserved.
- **API change on `copy_file`:** Parameter `conflict` no longer accepts the value "overwrite"; use "replace" instead.
- **Shown to the model:** old (v1) declaration, no change log; the executor drops unknown parameters and coerces types
- **Correct call, old API (v1):** `{"conflict": "overwrite", "dst": "/offsite/apollo.zip", "src": "/archives/apollo.zip"}`
- **Correct call, new API (v2):** `{"conflict": "replace", "dst": "/offsite/apollo.zip", "src": "/archives/apollo.zip"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `compress_folder`: `{"archive_name": "apollo.zip", "folder": "/projects/apollo"}`
   - result: {"archive_path": "/archives/copy04", "state": "ok"}
2. call `copy_file`: `{}`
   - result: Error: Missing required parameter: 'dst'.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Missing required parameter: 'dst'.; episode failed.

human_label: OTHER_ERROR
note: Copy call was rejected for missing dst.

## Item 11

- model `anthropic/claude-sonnet-5.5` · condition `CD` · drift class `default_change` · task `hotel03`
- **User request:** Reserve a standard room in Kyoto, check-in Dec 1 2026, 5 nights, and tell the front desk 'Late check-in after 22:00'; email me the confirmation.
- **API change on `reserve_hotel`:** The default of parameter `email_confirmation` changed from true to false.
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"check_in": "2026-12-01", "city": "Kyoto", "nights": 5, "room_type": "standard", "special_requests": "Late check-in after 22:00"}`
- **Correct call, new API (v2):** `{"check_in": "2026-12-01", "city": "Kyoto", "email_confirmation": true, "nights": 5, "room_type": "standard", "special_requests": "Late check-in after 22:00"}`
- **Same model and pair with no change log (B_strict in this run):** succeeded

What the model did:

1. call `reserve_hotel`: `{"check_in": "2026-12-01", "city": "Kyoto", "email_confirmation": true, "nights": 5, "room_type": "standard", "special_requests": "Late check-in after 22:00"}`
   - result: {"hotel_address": "addr_hotel03", "reservation_id": "htl_hotel03"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V1_SAFE
note: Explicit confirmation also succeeded without the change log.

## Item 12

- model `anthropic/claude-sonnet-5.5` · condition `Dprime` · drift class `enum_tighten` · task `pto01`
- **User request:** Request personal time off starting Oct 19 2026 at 09:00 UTC for 480 minutes, reason 'Family visit', and post the absence so the team knows.
- **API change on `request_time_off`:** Parameter `kind` no longer accepts the value "personal"; use "personal_day" instead.
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"duration_min": 480, "kind": "personal", "reason": "Family visit", "start": "2026-10-19T09:00:00+00:00"}`
- **Correct call, new API (v2):** `{"duration_min": 480, "kind": "personal_day", "reason": "Family visit", "start": "2026-10-19T09:00:00+00:00"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `request_time_off`: `{"duration_min": 480, "kind": "personal_day", "reason": "Family visit", "start": "2026-10-19T09:00:00Z"}`
   - result: {"pto_id": "pto_pto01", "state": "pending_approval"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V2_CORRECT
note: Used personal_day.

## Item 13

- model `anthropic/claude-haiku-5.5` · condition `E` · drift class `type_change` · task `bmk04`
- **User request:** Bookmark https://shop.lumen.test/desk-lamp as 'Lumen desk lamp' — shared, 2 stars, synced to all my devices — then set a keyword monitor on 'Lumen desk lamp discount'.
- **API change on `save_bookmark`:** Parameter `rating` changed type from integer to string. Old meaning: Star rating 0-5. New meaning: Star rating 0-5 as string.
- **Shown to the model:** old (v1) declaration, no change log; a rejected call's error is shown and one retry allowed
- **Correct call, old API (v1):** `{"privacy": "shared", "rating": 2, "title": "Lumen desk lamp", "url": "https://shop.lumen.test/desk-lamp"}`
- **Correct call, new API (v2):** `{"privacy": "shared", "rating": "2", "title": "Lumen desk lamp", "url": "https://shop.lumen.test/desk-lamp"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `save_bookmark`: `{"privacy": "shared", "rating": 2, "sync_devices": true, "title": "Lumen desk lamp", "url": "https://shop.lumen.test/desk-lamp"}`
   - result: Error: Invalid type for parameter 'rating': expected string, got int.
2. call `save_bookmark`: `{"privacy": "shared", "rating": "\"2\"", "sync_devices": true, "title": "Lumen desk lamp", "url": "https://shop.lumen.test/desk-lamp"}`
   - result: {"bookmark_id": "bm_bmk04"}
3. call `monitor_keyword`: `{"keyword": "Lumen desk lamp discount"}`
   - result: {"monitor_id": "mon_bmk04"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`, error: Invalid type for parameter 'rating': expected string, got int.; episode failed.

human_label: V2_PARTIAL
note: Retry sent quotation marks inside the rating string.

## Item 14

- model `anthropic/claude-haiku-5.5` · condition `E` · drift class `type_change` · task `ct04`
- **User request:** Add Diego Fuentes (diego@meridian.test) as a prospect scored 80 — newsletter on — then log a call on his new record with summary 'Intro call booked'.
- **API change on `create_contact`:** Parameter `score` changed type from integer to string. Old meaning: Lead score 0-100. New meaning: Lead score 0-100 as string.
- **Shown to the model:** old (v1) declaration, no change log; a rejected call's error is shown and one retry allowed
- **Correct call, old API (v1):** `{"email": "diego@meridian.test", "full_name": "Diego Fuentes", "score": 80, "stage": "prospect"}`
- **Correct call, new API (v2):** `{"email": "diego@meridian.test", "full_name": "Diego Fuentes", "score": "80", "stage": "prospect"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `create_contact`: `{"email": "diego@meridian.test", "full_name": "Diego Fuentes", "score": 80, "stage": "prospect", "subscribe_newsletter": true}`
   - result: Error: Invalid type for parameter 'score': expected string, got int.
2. call `create_contact`: `{"email": "diego@meridian.test", "full_name": "Diego Fuentes", "score": "\"80\"", "stage": "prospect", "subscribe_newsletter": true}`
   - result: {"contact_id": "ct_ct04"}
3. call `log_interaction`: `{"contact_id": "ct_ct04", "kind": "call", "summary": "Intro call booked"}`
   - result: {"interaction_id": "ix_ct04"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`, error: Invalid type for parameter 'score': expected string, got int.; episode failed.

human_label: V2_PARTIAL
note: Retry sent quotation marks inside the score string.

## Item 15

- model `gemini-3.6-flash` · condition `B_strict` · drift class `rename` · task `sched04`
- **User request:** Schedule 'Office closed for maintenance Friday.' to #eu-office for Oct 15 2026 07:00 UTC under campaign 'facilities' (delivery confirmation on), then DM @facilities-lead: 'Scheduled the Friday closure notice.'
- **API change on `schedule_message`:** Parameter `campaign` has been renamed to `campaign_tag`; send `campaign_tag` instead of `campaign`.
- **Shown to the model:** old (v1) declaration, no change log
- **Correct call, old API (v1):** `{"campaign": "facilities", "send_at": "2026-10-15T07:00:00+00:00", "target": "#eu-office", "text": "Office closed for maintenance Friday."}`
- **Correct call, new API (v2):** `{"campaign_tag": "facilities", "send_at": "2026-10-15T07:00:00+00:00", "target": "#eu-office", "text": "Office closed for maintenance Friday."}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `schedule_message`: `{"campaign": "facilities", "confirm_receipt": true, "send_at": "2026-10-15T07:00:00Z", "target": "#eu-office", "text": "Office closed for maintenance Friday."}`
   - result: Error: Received unknown parameter: 'campaign'.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Received unknown parameter: 'campaign'.; episode failed.

human_label: V1_FORM
note: Used the old campaign parameter.

## Item 16

- model `anthropic/claude-sonnet-5.5` · condition `C` · drift class `required` · task `room04`
- **User request:** Book Echo for board prep on Oct 21 2026, 13:30 UTC, 90 minutes, boardroom layout, panel text 'Board prep', no catering — then tell #leadership: 'Echo is booked for board prep, Oct 21 13:30 UTC.'
- **API change on `book_meeting_room`:** Parameter `building` is now required and has no default. Previously, leaving it out meant "HQ".
- **Shown to the model:** old (v1) declaration; JSON change log in the system prompt
- **Correct call, old API (v1):** `{"duration_min": 90, "layout": "boardroom", "purpose": "Board prep", "room": "Echo", "start": "2026-10-21T13:30:00+00:00"}`
- **Correct call, new API (v2):** `{"building": "HQ", "duration_min": 90, "layout": "boardroom", "purpose": "Board prep", "room": "Echo", "start": "2026-10-21T13:30:00+00:00"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

(no tool calls)

Final text: Which building is Echo in? The booking tool now requires a building code, and I don't have one for this request. Once you tell me, I'll book the room and then post the message to #leadership.

Executor at the drift step: `None`; episode failed.

human_label: NO_DRIFT_CALL
note: No booking call was made.

## Item 17

- model `meta-llama/llama-3.3-70b-instruct` · condition `Dprime` · drift class `enum_tighten` · task `kw02`
- **User request:** Monitor 'schema drift' every 30 minutes with email alerts, and tell me as soon as a mention appears.
- **API change on `monitor_keyword`:** Parameter `alert_channel` no longer accepts the value "email"; use "mail" instead.
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"alert_channel": "email", "check_interval_min": 30, "keyword": "schema drift"}`
- **Correct call, new API (v2):** `{"alert_channel": "mail", "check_interval_min": 30, "keyword": "schema drift"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `monitor_keyword`: `{"alert_channel": "mail", "check_interval_min": "30", "keyword": "schema drift", "notify_immediately": "true"}`
   - result: Error: Invalid type for parameter 'check_interval_min': expected integer, got str.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Invalid type for parameter 'check_interval_min': expected integer, got str.; episode failed.

human_label: OTHER_ERROR
note: check_interval_min had the wrong type.

## Item 18

- model `meta-llama/llama-3.3-70b-instruct` · condition `E` · drift class `enum_tighten` · task `kw04`
- **User request:** Pull the top 3 web results for 'acme recall', then keep watching that phrase hourly (every 60 minutes) with email alerts, labeled 'recall watch' — alert me the instant a new mention appears.
- **API change on `monitor_keyword`:** Parameter `alert_channel` no longer accepts the value "email"; use "mail" instead.
- **Shown to the model:** old (v1) declaration, no change log; a rejected call's error is shown and one retry allowed
- **Correct call, old API (v1):** `{"alert_channel": "email", "check_interval_min": 60, "keyword": "acme recall", "label": "recall watch"}`
- **Correct call, new API (v2):** `{"alert_channel": "mail", "check_interval_min": 60, "keyword": "acme recall", "label": "recall watch"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `web_search`: `{"max_results": "3", "query": "acme recall"}`
   - result: Error: Invalid type for parameter 'max_results': expected integer, got str.
2. call `web_search`: `{"max_results": "3", "query": "acme recall"}`
   - result: Error: Invalid type for parameter 'max_results': expected integer, got str.

Final text: (none)

Executor at the drift step: `None`, error: Invalid type for parameter 'max_results': expected integer, got str.; episode failed.

human_label: NO_DRIFT_CALL
note: Web search failed before monitoring was called.

## Item 19

- model `meta-llama/llama-3.3-70b-instruct` · condition `Dprime` · drift class `type_change` · task `cart04`
- **User request:** Order 4 of SKU-3321 with express shipping (receipt emailed to me as usual), then start tracking that order's shipment.
- **API change on `place_order`:** Parameter `quantity` changed type from integer to string. Old meaning: Number of units. New meaning: Number of units as string.
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"quantity": 4, "shipping_speed": "express", "sku": "SKU-3321"}`
- **Correct call, new API (v2):** `{"quantity": "4", "shipping_speed": "express", "sku": "SKU-3321"}`
- **Same model and pair with no change log (B_strict in this run):** succeeded

What the model did:

1. call `place_order`: `{"quantity": "4", "shipping_speed": "express", "sku": "SKU-3321"}`
   - result: {"order_id": "ord_cart04", "tracking_number": "TRK_cart04"}
2. call `track_shipment`: `{"tracking_number": "TRK_cart04"}`
   - result: {"status": "in_transit", "tracker_id": "trk_cart04"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V2_CORRECT
note: Sent quantity as the correct string.

## Item 20

- model `anthropic/claude-sonnet-5.5` · condition `CD` · drift class `default_change` · task `perm02`
- **User request:** Give jsmith write access to /repos/atlas for the next 8 hours (480 minutes), only on that path itself.
- **API change on `set_permissions`:** The default of parameter `recursive` changed from false to true.
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"access": "write", "expiry_min": 480, "path": "/repos/atlas", "principal": "jsmith"}`
- **Correct call, new API (v2):** `{"access": "write", "expiry_min": 480, "path": "/repos/atlas", "principal": "jsmith", "recursive": false}`
- **Same model and pair with no change log (B_strict in this run):** succeeded

What the model did:

1. call `set_permissions`: `{"access": "write", "expiry_min": 480, "path": "/repos/atlas", "principal": "jsmith", "recursive": false}`
   - result: {"grant_id": "gr_perm02", "state": "applied"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V1_SAFE
note: Explicit recursive setting also succeeded without the change log.

## Item 21

- model `anthropic/claude-haiku-5.5` · condition `C:user:prose:apply` · drift class `enum_tighten` · task `copy04`
- **User request:** Zip up /projects/apollo as apollo.zip (default settings), then copy /archives/apollo.zip to /offsite/apollo.zip, overwriting anything there, metadata preserved.
- **API change on `copy_file`:** Parameter `conflict` no longer accepts the value "overwrite"; use "replace" instead.
- **Shown to the model:** old (v1) declaration; change log in the user message, written as prose; with the 'apply it step by step' line
- **Correct call, old API (v1):** `{"conflict": "overwrite", "dst": "/offsite/apollo.zip", "src": "/archives/apollo.zip"}`
- **Correct call, new API (v2):** `{"conflict": "replace", "dst": "/offsite/apollo.zip", "src": "/archives/apollo.zip"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `compress_folder`: `{"archive_name": "apollo.zip", "folder": "/projects/apollo"}`
   - result: {"archive_path": "/archives/copy04", "state": "ok"}
2. call `copy_file`: `{}`
   - result: Error: Missing required parameter: 'dst'.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Missing required parameter: 'dst'.; episode failed.

human_label: OTHER_ERROR
note: Copy call was rejected for missing dst.

## Item 22

- model `meta-llama/llama-3.3-70b-instruct` · condition `B_lenient` · drift class `default_change` · task `perm02`
- **User request:** Give jsmith write access to /repos/atlas for the next 8 hours (480 minutes), only on that path itself.
- **API change on `set_permissions`:** The default of parameter `recursive` changed from false to true.
- **Shown to the model:** old (v1) declaration, no change log; the executor drops unknown parameters and coerces types
- **Correct call, old API (v1):** `{"access": "write", "expiry_min": 480, "path": "/repos/atlas", "principal": "jsmith"}`
- **Correct call, new API (v2):** `{"access": "write", "expiry_min": 480, "path": "/repos/atlas", "principal": "jsmith", "recursive": false}`
- **Same model and pair with no change log (B_strict in this run):** succeeded

What the model did:

1. call `set_permissions`: `{"access": "write", "expiry_min": 480, "path": "/repos/atlas", "principal": "jsmith", "recursive": false}`
   - result: {"grant_id": "gr_perm02", "state": "applied"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V1_SAFE
note: Explicit recursive setting also succeeded without the change log.

## Item 23

- model `anthropic/claude-sonnet-5.5` · condition `C:user:prose:apply` · drift class `default_change` · task `deal03`
- **User request:** Mark dl_4407 closed-won at $99,000.00, closed Oct 1 2026.
- **API change on `update_deal`:** The default of parameter `loss_reason` changed from "" to "unspecified".
- **Shown to the model:** old (v1) declaration; change log in the user message, written as prose; with the 'apply it step by step' line
- **Correct call, old API (v1):** `{"close_date": "2026-10-01", "deal_id": "dl_4407", "stage": "closed_won", "value_cents": 9900000}`
- **Correct call, new API (v2):** `{"close_date": "2026-10-01", "deal_id": "dl_4407", "loss_reason": "", "stage": "closed_won", "value_cents": 9900000}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `update_deal`: `{}`
   - result: Error: Missing required parameter: 'deal_id'.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Missing required parameter: 'deal_id'.; episode failed.

human_label: OTHER_ERROR
note: Update call was rejected for missing deal_id.

## Item 24

- model `anthropic/claude-haiku-5.5` · condition `B_lenient` · drift class `default_change` · task `room02`
- **User request:** Get me the Baltic room for Oct 14 2026, 9:00 UTC, two hours, theater seating. We don't need food.
- **API change on `book_meeting_room`:** The default of parameter `catering` changed from false to true.
- **Shown to the model:** old (v1) declaration, no change log; the executor drops unknown parameters and coerces types
- **Correct call, old API (v1):** `{"duration_min": 120, "layout": "theater", "room": "Baltic", "start": "2026-10-14T09:00:00+00:00"}`
- **Correct call, new API (v2):** `{"catering": false, "duration_min": 120, "layout": "theater", "room": "Baltic", "start": "2026-10-14T09:00:00+00:00"}`
- **Same model and pair with no change log (B_strict in this run):** succeeded

What the model did:

1. call `book_meeting_room`: `{"catering": false, "duration_min": 120, "layout": "theater", "room": "Baltic", "start": "2026-10-14T09:00:00Z"}`
   - result: {"booking_id": "bk_room02"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V1_SAFE
note: Explicit catering setting also succeeded without the change log.

## Item 25

- model `gemini-3.6-flash` · condition `B_strict` · drift class `default_change` · task `msg01`
- **User request:** Reply in thread th_4451 in #eng with 'Deploy window opens at 18:00 UTC.' — normal priority, link previews on.
- **API change on `send_message`:** The default of parameter `unfurl_links` changed from true to false.
- **Shown to the model:** old (v1) declaration, no change log
- **Correct call, old API (v1):** `{"priority": "normal", "target": "#eng", "text": "Deploy window opens at 18:00 UTC.", "thread_id": "th_4451"}`
- **Correct call, new API (v2):** `{"priority": "normal", "target": "#eng", "text": "Deploy window opens at 18:00 UTC.", "thread_id": "th_4451", "unfurl_links": true}`
- **Same model and pair with no change log (B_strict in this run):** succeeded

What the model did:

1. call `send_message`: `{"priority": "normal", "target": "#eng", "text": "Deploy window opens at 18:00 UTC.", "thread_id": "th_4451", "unfurl_links": true}`
   - result: {"message_id": "msg_msg01", "state": "delivered"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V1_SAFE
note: Explicit link previews also succeeded without the change log.

## Item 26

- model `anthropic/claude-sonnet-5.5` · condition `B_strict` · drift class `rename` · task `widg03`
- **User request:** Add a line chart for signups to dash_growth, 120-minute refresh, subtitle 'Daily signups', keeping the legend shown.
- **API change on `create_dashboard_widget`:** Parameter `subtitle` has been renamed to `caption`; send `caption` instead of `subtitle`.
- **Shown to the model:** old (v1) declaration, no change log
- **Correct call, old API (v1):** `{"chart": "line", "dashboard_id": "dash_growth", "metric": "signups", "refresh_min": 120, "subtitle": "Daily signups"}`
- **Correct call, new API (v2):** `{"caption": "Daily signups", "chart": "line", "dashboard_id": "dash_growth", "metric": "signups", "refresh_min": 120}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `create_dashboard_widget`: `{"chart": "line", "dashboard_id": "dash_growth", "metric": "signups", "refresh_min": 120, "subtitle": "Daily signups"}`
   - result: Error: Received unknown parameter: 'subtitle'.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Received unknown parameter: 'subtitle'.; episode failed.

human_label: V1_FORM
note: Used the old subtitle parameter.

## Item 27

- model `anthropic/claude-haiku-5.5` · condition `B_strict` · drift class `required` · task `msg04`
- **User request:** Spin up an invite-only channel proj-falcon and post 'Welcome aboard — kickoff Monday.' there at normal priority, link previews as usual.
- **API change on `send_message`:** Parameter `workspace` is now required and has no default. Previously, leaving it out meant "main".
- **Shown to the model:** old (v1) declaration, no change log
- **Correct call, old API (v1):** `{"priority": "normal", "target": "proj-falcon", "text": "Welcome aboard — kickoff Monday."}`
- **Correct call, new API (v2):** `{"priority": "normal", "target": "proj-falcon", "text": "Welcome aboard — kickoff Monday.", "workspace": "main"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `create_channel`: `{"access": "invite_only", "name": "proj-falcon"}`
   - result: {"channel_id": "ch_msg04"}
2. call `send_message`: `{"priority": "normal", "target": "proj-falcon", "text": "Welcome aboard — kickoff Monday.", "unfurl_links": true}`
   - result: Error: Missing required parameter: 'workspace'.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Missing required parameter: 'workspace'.; episode failed.

human_label: V1_FORM
note: Omitted the newly required workspace.

## Item 28

- model `meta-llama/llama-3.3-70b-instruct` · condition `CD` · drift class `default_change` · task `msg03`
- **User request:** Urgent post to #incidents: 'DB failover complete, all green.' Keep the link previews.
- **API change on `send_message`:** The default of parameter `unfurl_links` changed from true to false.
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"priority": "urgent", "target": "#incidents", "text": "DB failover complete, all green."}`
- **Correct call, new API (v2):** `{"priority": "urgent", "target": "#incidents", "text": "DB failover complete, all green.", "unfurl_links": true}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `send_message`: `{"priority": "urgent", "target": "#incidents", "text": "DB failover complete, all green.", "unfurl_links": "true"}`
   - result: Error: Invalid type for parameter 'unfurl_links': expected boolean, got str.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Invalid type for parameter 'unfurl_links': expected boolean, got str.; episode failed.

human_label: V2_PARTIAL
note: Supplied unfurl_links as a string, not a boolean.

## Item 29

- model `anthropic/claude-haiku-5.5` · condition `E` · drift class `rename` · task `cal03`
- **User request:** Set up the quarterly town hall: Nov 2 2026, 16:00 UTC, one hour, in the Main auditorium. Everyone invited should be notified.
- **API change on `create_event`:** Parameter `location` has been renamed to `venue`; send `venue` instead of `location`.
- **Shown to the model:** old (v1) declaration, no change log; a rejected call's error is shown and one retry allowed
- **Correct call, old API (v1):** `{"duration_min": 60, "location": "Main auditorium", "start": "2026-11-02T16:00:00+00:00", "title": "Quarterly town hall"}`
- **Correct call, new API (v2):** `{"duration_min": 60, "start": "2026-11-02T16:00:00+00:00", "title": "Quarterly town hall", "venue": "Main auditorium"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `create_event`: `{"duration_min": 60, "location": "Main auditorium", "notify_attendees": true, "start": "2026-11-02T16:00:00+00:00", "title": "Quarterly Town Hall"}`
   - result: Error: Received unknown parameter: 'location'.
2. call `create_event`: `{"duration_min": 60, "notify_attendees": true, "start": "2026-11-02T16:00:00+00:00", "title": "Quarterly Town Hall"}`
   - result: {"event_id": "evt_cal03", "status": "confirmed"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`, error: Received unknown parameter: 'location'.; episode failed.

human_label: OTHER_WRONG
note: Retry omitted the venue under both names.

## Item 30

- model `meta-llama/llama-3.3-70b-instruct` · condition `B_strict` · drift class `rename` · task `fly03`
- **User request:** Book an economy flight to AUS on Dec 3 2026, window seat, layovers no more than 180 minutes; don't pay extra for refundable.
- **API change on `book_flight`:** Parameter `seat_pref` has been renamed to `seat_preference`; send `seat_preference` instead of `seat_pref`.
- **Shown to the model:** old (v1) declaration, no change log
- **Correct call, old API (v1):** `{"cabin": "economy", "depart": "2026-12-03", "destination": "AUS", "max_layover_min": 180, "seat_pref": "window"}`
- **Correct call, new API (v2):** `{"cabin": "economy", "depart": "2026-12-03", "destination": "AUS", "max_layover_min": 180, "seat_preference": "window"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `book_flight`: `{"cabin": "economy", "depart": "2026-12-03", "destination": "AUS", "max_layover_min": "180", "refundable": "false", "seat_pref": "window"}`
   - result: Error: Received unknown parameter: 'seat_pref'.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Received unknown parameter: 'seat_pref'.; episode failed.

human_label: V1_FORM
note: Used the old seat_pref parameter.

## Item 31

- model `meta-llama/llama-3.3-70b-instruct` · condition `E` · drift class `default_change` · task `hotel03`
- **User request:** Reserve a standard room in Kyoto, check-in Dec 1 2026, 5 nights, and tell the front desk 'Late check-in after 22:00'; email me the confirmation.
- **API change on `reserve_hotel`:** The default of parameter `email_confirmation` changed from true to false.
- **Shown to the model:** old (v1) declaration, no change log; a rejected call's error is shown and one retry allowed
- **Correct call, old API (v1):** `{"check_in": "2026-12-01", "city": "Kyoto", "nights": 5, "room_type": "standard", "special_requests": "Late check-in after 22:00"}`
- **Correct call, new API (v2):** `{"check_in": "2026-12-01", "city": "Kyoto", "email_confirmation": true, "nights": 5, "room_type": "standard", "special_requests": "Late check-in after 22:00"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `reserve_hotel`: `{"check_in": "2026-12-01", "city": "Kyoto", "email_confirmation": "true", "nights": "5", "special_requests": "Late check-in after 22:00"}`
   - result: Error: Invalid type for parameter 'nights': expected integer, got str.
2. call `reserve_hotel`: `{"check_in": "2026-12-01", "city": "Kyoto", "nights": 5, "special_requests": "Late check-in after 22:00"}`
   - result: {"hotel_address": "addr_hotel03", "reservation_id": "htl_hotel03"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`, error: Invalid type for parameter 'nights': expected integer, got str.; episode failed.

human_label: V1_FORM
note: Accepted retry omitted email_confirmation.

## Item 32

- model `anthropic/claude-sonnet-5.5` · condition `Dprime` · drift class `rename` · task `sched04`
- **User request:** Schedule 'Office closed for maintenance Friday.' to #eu-office for Oct 15 2026 07:00 UTC under campaign 'facilities' (delivery confirmation on), then DM @facilities-lead: 'Scheduled the Friday closure notice.'
- **API change on `schedule_message`:** Parameter `campaign` has been renamed to `campaign_tag`; send `campaign_tag` instead of `campaign`.
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"campaign": "facilities", "send_at": "2026-10-15T07:00:00+00:00", "target": "#eu-office", "text": "Office closed for maintenance Friday."}`
- **Correct call, new API (v2):** `{"campaign_tag": "facilities", "send_at": "2026-10-15T07:00:00+00:00", "target": "#eu-office", "text": "Office closed for maintenance Friday."}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `schedule_message`: `{"campaign_tag": "facilities", "channel_type": "group", "send_at": "2026-10-15T07:00:00Z", "target": "#eu-office", "text": "Office closed for maintenance Friday."}`
   - result: {"scheduled_id": "sch_sched04"}
2. call `send_message`: `{"target": "@facilities-lead", "text": "Scheduled the Friday closure notice."}`
   - result: {"message_id": "msg_sched04", "state": "delivered"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: OTHER_WRONG
note: Used campaign_tag, but another argument made the accepted call wrong.

## Item 33

- model `gemini-3.6-flash` · condition `B_strict` · drift class `default_change` · task `hotel03`
- **User request:** Reserve a standard room in Kyoto, check-in Dec 1 2026, 5 nights, and tell the front desk 'Late check-in after 22:00'; email me the confirmation.
- **API change on `reserve_hotel`:** The default of parameter `email_confirmation` changed from true to false.
- **Shown to the model:** old (v1) declaration, no change log
- **Correct call, old API (v1):** `{"check_in": "2026-12-01", "city": "Kyoto", "nights": 5, "room_type": "standard", "special_requests": "Late check-in after 22:00"}`
- **Correct call, new API (v2):** `{"check_in": "2026-12-01", "city": "Kyoto", "email_confirmation": true, "nights": 5, "room_type": "standard", "special_requests": "Late check-in after 22:00"}`
- **Same model and pair with no change log (B_strict in this run):** succeeded

What the model did:

1. call `reserve_hotel`: `{"check_in": "2026-12-01", "city": "Kyoto", "email_confirmation": true, "nights": 5, "room_type": "standard", "special_requests": "Late check-in after 22:00"}`
   - result: {"hotel_address": "addr_hotel03", "reservation_id": "htl_hotel03"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V1_SAFE
note: Explicit confirmation also succeeded without the change log.

## Item 34

- model `anthropic/claude-sonnet-5.5` · condition `CD` · drift class `type_change` · task `job03`
- **User request:** Post a full-time Product Designer opening in the Design department at the NYC office, band up to $140,000.00, visible on the public board as usual.
- **API change on `post_job_opening`:** Parameter `salary_cents` changed type from integer to string. Old meaning: Top of annual salary band in cents. New meaning: Top of annual salary band as decimal string in major units.
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"department": "Design", "employment": "full_time", "location": "NYC office", "salary_cents": 14000000, "title": "Product Designer"}`
- **Correct call, new API (v2):** `{"department": "Design", "employment": "full_time", "location": "NYC office", "salary_cents": "140000.00", "title": "Product Designer"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `post_job_opening`: `{"department": "Design", "employment": "full_time", "internal_only": false, "location": "NYC", "salary_cents": "140000.00", "title": "Product Designer"}`
   - result: {"job_id": "job_job03", "state": "published"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: OTHER_WRONG
note: Salary conversion was correct, but location differed.

## Item 35

- model `anthropic/claude-haiku-5.5` · condition `D` · drift class `type_change` · task `fly04`
- **User request:** Book a premium economy flight to CDG on Nov 18 2026 (aisle seat, layovers under 240 minutes, non-refundable fare is fine), then reserve a hotel in Paris checking in 2026-11-18 for 3 nights.
- **API change on `book_flight`:** Parameter `max_layover_min` changed type from integer to string. Old meaning: Max layover in minutes (0 = no limit). New meaning: Max layover in hours, decimal string ("0" = no limit).
- **Shown to the model:** new (v2) declaration, no change log
- **Correct call, old API (v1):** `{"cabin": "premium_economy", "depart": "2026-11-18", "destination": "CDG", "max_layover_min": 240, "seat_pref": "aisle"}`
- **Correct call, new API (v2):** `{"cabin": "premium_economy", "depart": "2026-11-18", "destination": "CDG", "max_layover_min": "4", "seat_pref": "aisle"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `book_flight`: `{"cabin": "premium_economy", "depart": "2026-11-18", "destination": "CDG", "max_layover_min": "4", "refundable": false, "seat_pref": "aisle"}`
   - result: {"booking_ref": "fl_fly04", "state": "ticketed"}
2. call `reserve_hotel`: `{"check_in": "2026-11-18", "city": "Paris", "nights": 3}`
   - result: {"hotel_address": "addr_fly04", "reservation_id": "htl_fly04"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V2_CORRECT
note: Converted 240 minutes to the string "4".

## Item 36

- model `meta-llama/llama-3.3-70b-instruct` · condition `CD` · drift class `default_change` · task `rem02`
- **User request:** Set a one-time push reminder to water the plants, Oct 5 2026 at 8am UTC. Definitely not a daily repeat.
- **API change on `create_reminder`:** The default of parameter `repeat_daily` changed from false to true.
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"channel": "push", "remind_at": "2026-10-05T08:00:00+00:00", "text": "Water the plants"}`
- **Correct call, new API (v2):** `{"channel": "push", "remind_at": "2026-10-05T08:00:00+00:00", "repeat_daily": false, "text": "Water the plants"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `create_reminder`: `{"remind_at": "2026-10-05T08:00:00Z", "repeat_daily": "false", "text": "water the plants"}`
   - result: Error: Invalid type for parameter 'repeat_daily': expected boolean, got str.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Invalid type for parameter 'repeat_daily': expected boolean, got str.; episode failed.

human_label: V2_PARTIAL
note: Supplied repeat_daily as a string, not a boolean.

## Item 37

- model `anthropic/claude-sonnet-5.5` · condition `Dprime` · drift class `required` · task `msg04`
- **User request:** Spin up an invite-only channel proj-falcon and post 'Welcome aboard — kickoff Monday.' there at normal priority, link previews as usual.
- **API change on `send_message`:** Parameter `workspace` is now required and has no default. Previously, leaving it out meant "main".
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"priority": "normal", "target": "proj-falcon", "text": "Welcome aboard — kickoff Monday."}`
- **Correct call, new API (v2):** `{"priority": "normal", "target": "proj-falcon", "text": "Welcome aboard — kickoff Monday.", "workspace": "main"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `create_channel`: `{"access": "invite_only", "name": "proj-falcon"}`
   - result: {"channel_id": "ch_msg04"}
2. call `send_message`: `{"target": "proj-falcon", "text": "Welcome aboard — kickoff Monday.", "workspace": "main"}`
   - result: {"message_id": "msg_msg04", "state": "delivered"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V2_CORRECT
note: Supplied workspace as main.

## Item 38

- model `anthropic/claude-haiku-5.5` · condition `D` · drift class `type_change` · task `room03`
- **User request:** Book Delta on Nov 3 2026 at 10:00 UTC for half an hour; label it 'Standup overflow' on the panel. No food.
- **API change on `book_meeting_room`:** Parameter `duration_min` changed type from integer to string. Old meaning: Booking length in minutes. New meaning: Booking length in hours, decimal string.
- **Shown to the model:** new (v2) declaration, no change log
- **Correct call, old API (v1):** `{"duration_min": 30, "purpose": "Standup overflow", "room": "Delta", "start": "2026-11-03T10:00:00+00:00"}`
- **Correct call, new API (v2):** `{"duration_min": "0.5", "purpose": "Standup overflow", "room": "Delta", "start": "2026-11-03T10:00:00+00:00"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `book_meeting_room`: `{"catering": false, "duration_min": "0.5", "purpose": "Standup overflow", "room": "Delta", "start": "2026-11-03T10:00:00Z"}`
   - result: {"booking_id": "bk_room03"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V2_CORRECT
note: Converted half an hour to the string "0.5".

## Item 39

- model `anthropic/claude-haiku-5.5` · condition `C:user:prose:apply` · drift class `default_change` · task `msg03`
- **User request:** Urgent post to #incidents: 'DB failover complete, all green.' Keep the link previews.
- **API change on `send_message`:** The default of parameter `unfurl_links` changed from true to false.
- **Shown to the model:** old (v1) declaration; change log in the user message, written as prose; with the 'apply it step by step' line
- **Correct call, old API (v1):** `{"priority": "urgent", "target": "#incidents", "text": "DB failover complete, all green."}`
- **Correct call, new API (v2):** `{"priority": "urgent", "target": "#incidents", "text": "DB failover complete, all green.", "unfurl_links": true}`
- **Same model and pair with no change log (B_strict in this run):** succeeded

What the model did:

1. call `send_message`: `{"priority": "urgent", "target": "#incidents", "text": "DB failover complete, all green.", "unfurl_links": true}`
   - result: {"message_id": "msg_msg03", "state": "delivered"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V1_SAFE
note: Explicit link previews also succeeded without the change log.

## Item 40

- model `anthropic/claude-haiku-5.5` · condition `E` · drift class `rename` · task `cart01`
- **User request:** Order 2 units of SKU-8842 with express shipping and the gift message 'Happy birthday, Lena!' — email me the receipt as usual.
- **API change on `place_order`:** Parameter `gift_message` has been renamed to `gift_note`; send `gift_note` instead of `gift_message`.
- **Shown to the model:** old (v1) declaration, no change log; a rejected call's error is shown and one retry allowed
- **Correct call, old API (v1):** `{"gift_message": "Happy birthday, Lena!", "quantity": 2, "shipping_speed": "express", "sku": "SKU-8842"}`
- **Correct call, new API (v2):** `{"gift_note": "Happy birthday, Lena!", "quantity": 2, "shipping_speed": "express", "sku": "SKU-8842"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `place_order`: `{"gift_message": "Happy birthday, Lena!", "quantity": 2, "send_receipt": true, "shipping_speed": "express", "sku": "SKU-8842"}`
   - result: Error: Received unknown parameter: 'gift_message'.
2. call `place_order`: `{"gift_message": "Happy birthday, Lena!", "quantity": 2, "send_receipt": true, "shipping_speed": "express", "sku": "SKU-8842"}`
   - result: Error: Received unknown parameter: 'gift_message'.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Received unknown parameter: 'gift_message'.; episode failed.

human_label: V1_FORM
note: Repeated the old gift_message parameter.

## Item 41

- model `anthropic/claude-haiku-5.5` · condition `D` · drift class `required` · task `rem04`
- **User request:** Add a 30-minute 'Flu shot' event on Oct 20 2026 at 11:00 UTC (attendees notified as normal), and set a one-off push reminder 'Leave for flu shot' at 10:30 that day with 15 minutes lead.
- **API change on `create_reminder`:** Parameter `list_id` is now required and has no default. Previously, leaving it out meant "inbox".
- **Shown to the model:** new (v2) declaration, no change log
- **Correct call, old API (v1):** `{"channel": "push", "lead_min": 15, "remind_at": "2026-10-20T10:30:00+00:00", "text": "Leave for flu shot"}`
- **Correct call, new API (v2):** `{"channel": "push", "lead_min": 15, "list_id": "inbox", "remind_at": "2026-10-20T10:30:00+00:00", "text": "Leave for flu shot"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `create_event`: `{"duration_min": 30, "start": "2026-10-20T11:00:00Z", "title": "Flu shot"}`
   - result: {"event_id": "evt_rem04", "status": "confirmed"}

Final text: The flu shot event is on your calendar for Oct 20, 2026 at 11:00 UTC for 30 minutes, with attendees notified as normal. /  / I haven't set the reminder yet because I need two details: /  / 1. **Which reminder list should it go in?** The reminder tool requires a list ID, and I don't have one for you. / 2. **How should the 15-minute lead work?** I can read it two ways: /    - Set the reminder for 10:30 UTC with a 15-minute lead, so it fires at 10:15 UTC. /    - Fire at 10:30 UTC with no lead time, and treat the 15 minutes as something else.

Executor at the drift step: `None`; episode failed.

human_label: NO_DRIFT_CALL
note: No reminder call was made.

## Item 42

- model `anthropic/claude-sonnet-5.5` · condition `Dprime` · drift class `type_change` · task `ds03`
- **User request:** Export billing_ledger to s3://viz-archive/billing with zstd compression, 4096 MB chunks, tag 'finance', header row included.
- **API change on `export_dataset`:** Parameter `chunk_mb` changed type from integer to string. Old meaning: Chunk size in megabytes (0 = single file). New meaning: Chunk size in gigabytes, decimal string ("0" = single file).
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"chunk_mb": 4096, "compression": "zstd", "dataset": "billing_ledger", "destination": "s3://viz-archive/billing", "tag": "finance"}`
- **Correct call, new API (v2):** `{"chunk_mb": "4", "compression": "zstd", "dataset": "billing_ledger", "destination": "s3://viz-archive/billing", "tag": "finance"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `export_dataset`: `{"chunk_mb": "4.096", "compression": "zstd", "dataset": "billing_ledger", "destination": "s3://viz-archive/billing", "tag": "finance"}`
   - result: {"export_id": "dx_ds03", "state": "queued"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: V2_PARTIAL
note: Used a string, but converted 4096 MB to the wrong value.

## Item 43

- model `gemini-3.6-flash` · condition `B_fill` · drift class `required` · task `zip02`
- **User request:** Tar up /video/raw as raw-footage.tar, split into 2048 MB parts, unencrypted.
- **API change on `compress_folder`:** Parameter `dest_dir` is now required and has no default. Previously, leaving it out meant "/archives".
- **Shown to the model:** old (v1) declaration, no change log; the system prompt asks to pass every parameter explicitly
- **Correct call, old API (v1):** `{"archive_name": "raw-footage.tar", "folder": "/video/raw", "format": "tar", "split_mb": 2048}`
- **Correct call, new API (v2):** `{"archive_name": "raw-footage.tar", "dest_dir": "/archives", "folder": "/video/raw", "format": "tar", "split_mb": 2048}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `compress_folder`: `{"archive_name": "raw-footage.tar", "dest_dir": "/archives", "encrypt": false, "folder": "/video/raw", "format": "tar", "label": "", "split_mb": 2048}`
   - result: {"archive_path": "/archives/zip02", "state": "ok"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: V2_CORRECT
note: Supplied the newly required dest_dir.

## Item 44

- model `anthropic/claude-sonnet-5.5` · condition `Dprime` · drift class `default_change` · task `deal02`
- **User request:** Set deal dl_8813 to proposal stage at $12,000.00.
- **API change on `update_deal`:** The default of parameter `loss_reason` changed from "" to "unspecified".
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"deal_id": "dl_8813", "stage": "proposal", "value_cents": 1200000}`
- **Correct call, new API (v2):** `{"deal_id": "dl_8813", "loss_reason": "", "stage": "proposal", "value_cents": 1200000}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `update_deal`: `{"deal_id": "dl_8813", "stage": "proposal", "value_cents": 1200000}`
   - result: {"deal_id": "deal02", "state": "updated"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: V1_FORM
note: Omitted loss_reason despite its changed default.

## Item 45

- model `gemini-3.6-flash` · condition `B_fill` · drift class `type_change` · task `inv01`
- **User request:** Bill Globex (ap@globex.test) $2,500.00 on net-30 terms; the invoice should carry the note 'Milestone 2'.
- **API change on `create_invoice`:** Parameter `amount_cents` changed type from integer to string. Old meaning: Invoice total in cents. New meaning: Invoice total as decimal string in major units.
- **Shown to the model:** old (v1) declaration, no change log; the system prompt asks to pass every parameter explicitly
- **Correct call, old API (v1):** `{"amount_cents": 250000, "customer": "ap@globex.test", "notes": "Milestone 2", "terms": "net30"}`
- **Correct call, new API (v2):** `{"amount_cents": "2500.00", "customer": "ap@globex.test", "notes": "Milestone 2", "terms": "net30"}`
- **Same model and pair with no change log (B_strict in this run):** failed

What the model did:

1. call `create_invoice`: `{"amount_cents": 250000, "currency": "USD", "customer": "ap@globex.test", "notes": "Milestone 2", "template_id": "standard", "terms": "net30"}`
   - result: Error: Invalid type for parameter 'amount_cents': expected string, got int.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Invalid type for parameter 'amount_cents': expected string, got int.; episode failed.

human_label: V1_FORM
note: Sent amount_cents as the old integer type.
