# Hand audit of the drift-call labels

Read each item and write the label you would give the model's call at the drifted step.
Judge from the arguments the model actually sent (listed under "What the model did").
The automatic label is not shown here; it is in audit_labels_sample.json.

| label | when |
|---|---|
| V2_CORRECT | the call follows the new API on the drifted parameter and is accepted as correct |
| V2_PARTIAL | the model moved off the old form but got the new one wrong (e.g. a string in the old unit, a wrong new enum value) |
| V1_FORM | the call uses the old contract on the drifted parameter: old name, old enum value, old type, or leaves out the newly required / default-changed parameter |
| V1_SAFE | accepted as correct, but the same pair also succeeded with no change log (September B_strict): the model fills that parameter anyway, so the success says nothing about reading the change (required / default_change only) |
| OTHER_ERROR | the executor rejected the call over a parameter that is not the drifted one |
| OTHER_WRONG | accepted but wrong for a reason other than the drifted parameter's form (another argument is wrong, or a renamed parameter was left out under both names) |
| NO_DRIFT_CALL | the model never called the drifted tool |

Fill in the two lines at the end of each item (the label is case-insensitive; leave the line
empty to skip an item), then run `python3 experiments/audit_sample.py score`:

    human_label: V1_FORM
    note: kept the old name `tags`

## Item 1

- model `gemini-3.6-flash` · condition `Dprime` · drift class `rename` · task `list03`
- **User request:** Update lst_5540 to condition used, 1500 grams shipping weight, headline 'Vintage film camera'; keep it live on the storefront.
- **API change on `update_listing`:** Parameter `headline` has been renamed to `listing_title`; send `listing_title` instead of `headline`.
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"condition": "used", "headline": "Vintage film camera", "listing_id": "lst_5540", "weight_grams": 1500}`
- **Correct call, new API (v2):** `{"condition": "used", "listing_id": "lst_5540", "listing_title": "Vintage film camera", "weight_grams": 1500}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `update_listing`: `{"condition": "used", "listing_id": "lst_5540", "listing_title": "Vintage film camera", "visible": true, "weight_grams": 1500}`
   - result: {"listing_id": "list03", "state": "updated"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 2

- model `gemini-3.6-flash` · condition `Dprime` · drift class `default_change` · task `deal02`
- **User request:** Set deal dl_8813 to proposal stage at $12,000.00.
- **API change on `update_deal`:** The default of parameter `loss_reason` changed from "" to "unspecified".
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"deal_id": "dl_8813", "stage": "proposal", "value_cents": 1200000}`
- **Correct call, new API (v2):** `{"deal_id": "dl_8813", "loss_reason": "", "stage": "proposal", "value_cents": 1200000}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `update_deal`: `{"deal_id": "dl_8813", "stage": "proposal", "value_cents": 1200000}`
   - result: {"deal_id": "deal02", "state": "updated"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 3

- model `gemini-3.1-pro-preview` · condition `Dprime` · drift class `default_change` · task `deal02`
- **User request:** Set deal dl_8813 to proposal stage at $12,000.00.
- **API change on `update_deal`:** The default of parameter `loss_reason` changed from "" to "unspecified".
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"deal_id": "dl_8813", "stage": "proposal", "value_cents": 1200000}`
- **Correct call, new API (v2):** `{"deal_id": "dl_8813", "loss_reason": "", "stage": "proposal", "value_cents": 1200000}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `update_deal`: `{"deal_id": "dl_8813", "stage": "proposal", "value_cents": 1200000}`
   - result: {"deal_id": "deal02", "state": "updated"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 4

- model `gemini-3.1-pro-preview` · condition `CD` · drift class `rename` · task `rem01`
- **User request:** Set a reminder that says 'Submit expense report' for Oct 10 2026 at 17:00 UTC, ping me on my phone half an hour ahead, and attach the note 'Include taxi receipts'. Just the once, not every day.
- **API change on `create_reminder`:** Parameter `note` has been renamed to `annotation`; send `annotation` instead of `note`.
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"channel": "push", "lead_min": 30, "note": "Include taxi receipts", "remind_at": "2026-10-10T17:00:00+00:00", "text": "Submit expense report"}`
- **Correct call, new API (v2):** `{"annotation": "Include taxi receipts", "channel": "push", "lead_min": 30, "remind_at": "2026-10-10T17:00:00+00:00", "text": "Submit expense report"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `create_reminder`: `{"annotation": "Include taxi receipts", "lead_min": 30, "remind_at": "2026-10-10T17:00:00Z", "repeat_daily": false, "text": "Submit expense report"}`
   - result: {"reminder_id": "rem_rem01"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 5

- model `gemini-3.1-pro-preview` · condition `Dprime` · drift class `type_change` · task `job03`
- **User request:** Post a full-time Product Designer opening in the Design department at the NYC office, band up to $140,000.00, visible on the public board as usual.
- **API change on `post_job_opening`:** Parameter `salary_cents` changed type from integer to string. Old meaning: Top of annual salary band in cents. New meaning: Top of annual salary band as decimal string in major units.
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"department": "Design", "employment": "full_time", "location": "NYC office", "salary_cents": 14000000, "title": "Product Designer"}`
- **Correct call, new API (v2):** `{"department": "Design", "employment": "full_time", "location": "NYC office", "salary_cents": "140000.00", "title": "Product Designer"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `post_job_opening`: `{"department": "Design", "employment": "full_time", "location": "NYC", "salary_cents": "140000.00", "title": "Product Designer"}`
   - result: {"job_id": "job_job03", "state": "published"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 6

- model `gemini-3.1-pro-preview` · condition `CD` · drift class `default_change` · task `bmk01`
- **User request:** Bookmark https://arxiv.org/abs/2609.01234 as 'Drift survey', shared with the team, five stars, tagged 'research' — and make sure it syncs to all my devices.
- **API change on `save_bookmark`:** The default of parameter `sync_devices` changed from true to false.
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"privacy": "shared", "rating": 5, "tags": "research", "title": "Drift survey", "url": "https://arxiv.org/abs/2609.01234"}`
- **Correct call, new API (v2):** `{"privacy": "shared", "rating": 5, "sync_devices": true, "tags": "research", "title": "Drift survey", "url": "https://arxiv.org/abs/2609.01234"}`
- **Same model and pair with no change log (September B_strict):** succeeded

What the model did:

1. call `save_bookmark`: `{"privacy": "shared", "rating": 5, "sync_devices": true, "tags": "research", "title": "Drift survey", "url": "https://arxiv.org/abs/2609.01234"}`
   - result: {"bookmark_id": "bm_bmk01"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 7

- model `openai/gpt-5.6-luna` · condition `Dprime` · drift class `type_change` · task `pto03`
- **User request:** Request vacation starting Dec 21 2026 at 09:00 UTC for 2400 minutes, reason 'Year-end trip'; the team should see it on the calendar as usual.
- **API change on `request_time_off`:** Parameter `duration_min` changed type from integer to string. Old meaning: Leave length in minutes. New meaning: Leave length in hours, decimal string.
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"duration_min": 2400, "kind": "vacation", "reason": "Year-end trip", "start": "2026-12-21T09:00:00+00:00"}`
- **Correct call, new API (v2):** `{"duration_min": "40", "kind": "vacation", "reason": "Year-end trip", "start": "2026-12-21T09:00:00+00:00"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `request_time_off`: `{"approver": "direct_manager", "duration_min": "2400", "kind": "vacation", "notify_team": true, "reason": "Year-end trip", "start": "2026-12-21T09:00:00Z"}`
   - result: {"pto_id": "pto_pto03", "state": "pending_approval"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 8

- model `modal-qwen2.5-7b` · condition `C:sys:prose:none` · drift class `default_change` · task `bmk01`
- **User request:** Bookmark https://arxiv.org/abs/2609.01234 as 'Drift survey', shared with the team, five stars, tagged 'research' — and make sure it syncs to all my devices.
- **API change on `save_bookmark`:** The default of parameter `sync_devices` changed from true to false.
- **Shown to the model:** old (v1) declaration; change log in the system prompt, written as prose
- **Correct call, old API (v1):** `{"privacy": "shared", "rating": 5, "tags": "research", "title": "Drift survey", "url": "https://arxiv.org/abs/2609.01234"}`
- **Correct call, new API (v2):** `{"privacy": "shared", "rating": 5, "sync_devices": true, "tags": "research", "title": "Drift survey", "url": "https://arxiv.org/abs/2609.01234"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `save_bookmark`: `{"folder": "", "privacy": "shared", "rating": 5, "sync_devices": true, "tags": "research", "title": "Drift survey", "url": "https://arxiv.org/abs/2609.01234"}`
   - result: {"bookmark_id": "bm_bmk01"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 9

- model `gemini-3.1-pro-preview` · condition `Dprime` · drift class `default_change` · task `deal03`
- **User request:** Mark dl_4407 closed-won at $99,000.00, closed Oct 1 2026.
- **API change on `update_deal`:** The default of parameter `loss_reason` changed from "" to "unspecified".
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"close_date": "2026-10-01", "deal_id": "dl_4407", "stage": "closed_won", "value_cents": 9900000}`
- **Correct call, new API (v2):** `{"close_date": "2026-10-01", "deal_id": "dl_4407", "loss_reason": "", "stage": "closed_won", "value_cents": 9900000}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `update_deal`: `{"close_date": "2026-10-01", "deal_id": "dl_4407", "stage": "closed_won", "value_cents": 9900000}`
   - result: {"deal_id": "deal03", "state": "updated"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 10

- model `gemini-3.1-pro-preview` · condition `Dprime` · drift class `enum_tighten` · task `fly02`
- **User request:** Book a premium economy flight to LIS for Oct 22 2026 with at most a 90-minute layover; a non-refundable ticket is fine.
- **API change on `book_flight`:** Parameter `cabin` no longer accepts the value "premium_economy"; use "premium" instead.
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"cabin": "premium_economy", "depart": "2026-10-22", "destination": "LIS", "max_layover_min": 90}`
- **Correct call, new API (v2):** `{"cabin": "premium", "depart": "2026-10-22", "destination": "LIS", "max_layover_min": 90}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `book_flight`: `{"cabin": "premium", "depart": "2026-10-22", "destination": "LIS", "max_layover_min": 90}`
   - result: {"booking_ref": "fl_fly02", "state": "ticketed"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 11

- model `modal-qwen2.5-7b` · condition `C:tool:json:none` · drift class `type_change` · task `cal01`
- **User request:** Put a design review on my calendar: Oct 6 2026, 14:00 UTC, an hour and a half, in Room 4A. Keep it private, and make sure the attendees get their invites.
- **API change on `create_event`:** Parameter `duration_min` changed type from integer to string. Old meaning: Duration in minutes. New meaning: Duration in hours, decimal string.
- **Shown to the model:** old (v1) declaration; change log in a get_api_changelog result already in the transcript, written as json
- **Correct call, old API (v1):** `{"duration_min": 90, "location": "Room 4A", "start": "2026-10-06T14:00:00+00:00", "title": "Design review", "visibility": "private"}`
- **Correct call, new API (v2):** `{"duration_min": "1.5", "location": "Room 4A", "start": "2026-10-06T14:00:00+00:00", "title": "Design review", "visibility": "private"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `get_api_changelog` (pre-filled, not the model): `{"tool": "create_event"}`
   - result: NOTE: the API behind tool 'create_event' was updated after the tool schema you were given was cached. Machine-readable change log for 'create_event' (apply it when calling): / [ /  { /   "change": "type_changed", /   "new": { /    "desc": "Duration in hours, decimal string", /    "type": "string" /   }, /   "old": { /    "desc": "Duration in minutes", /    "type": "integer" /   }, /   "param": "duration_min" /  } / ]
2. call `create_event`: `{"calendar_id": "primary", "duration_min": 90, "location": "Room 4A", "notify_attendees": true, "start": "2026-10-06T14:00:00Z", "title": "Design review", "visibility": "private"}`
   - result: Error: Invalid type for parameter 'duration_min': expected string, got int.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Invalid type for parameter 'duration_min': expected string, got int.; episode failed.

human_label: 
note: 

## Item 12

- model `openai/gpt-5.6-luna` · condition `C:sys:json:none` · drift class `default_change` · task `log02`
- **User request:** Log that I emailed ct_1188 the pricing deck (summary 'Sent pricing deck'). Don't create a follow-up.
- **API change on `log_interaction`:** The default of parameter `follow_up` changed from false to true.
- **Shown to the model:** old (v1) declaration; change log in the system prompt, written as json
- **Correct call, old API (v1):** `{"contact_id": "ct_1188", "kind": "email", "summary": "Sent pricing deck"}`
- **Correct call, new API (v2):** `{"contact_id": "ct_1188", "follow_up": false, "kind": "email", "summary": "Sent pricing deck"}`
- **Same model and pair with no change log (September B_strict):** succeeded

What the model did:

1. call `log_interaction`: `{"contact_id": "ct_1188", "details": "Emailed the pricing deck.", "duration_min": 0, "follow_up": false, "kind": "email", "pipeline": "sales", "summary": "Sent pricing deck"}`
   - result: {"interaction_id": "ix_log02"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 13

- model `openai/gpt-5.6-luna` · condition `CD` · drift class `required` · task `exp01`
- **User request:** Expense $18.50 at Blue Bottle from Sep 4 2026 as a meal, memo 'Client coffee'.
- **API change on `submit_expense`:** Parameter `cost_center` is now required and has no default. Previously, leaving it out meant "general".
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"amount_cents": 1850, "category": "meals", "incurred_on": "2026-09-04", "memo": "Client coffee", "merchant": "Blue Bottle"}`
- **Correct call, new API (v2):** `{"amount_cents": 1850, "category": "meals", "cost_center": "general", "incurred_on": "2026-09-04", "memo": "Client coffee", "merchant": "Blue Bottle"}`
- **Same model and pair with no change log (September B_strict):** succeeded

What the model did:

(no tool calls)

Final text: What cost center should I charge this expense to?

Executor at the drift step: `None`; episode failed.

human_label: 
note: 

## Item 14

- model `gemini-3.1-pro-preview` · condition `Dprime` · drift class `required` · task `ship03`
- **User request:** Track 9400111899560001234567 and only alert me on exceptions; poll every 720 minutes, call it 'Camera lens', distance remaining in miles.
- **API change on `track_shipment`:** Parameter `carrier` is now required and has no default. Previously, leaving it out meant "auto_detect".
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"alert_on": "exception", "nickname": "Camera lens", "poll_interval_min": 720, "tracking_number": "9400111899560001234567"}`
- **Correct call, new API (v2):** `{"alert_on": "exception", "carrier": "auto_detect", "nickname": "Camera lens", "poll_interval_min": 720, "tracking_number": "9400111899560001234567"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `track_shipment`: `{"alert_on": "exception", "carrier": "USPS", "nickname": "Camera lens", "poll_interval_min": 720, "tracking_number": "9400111899560001234567", "units": "miles"}`
   - result: {"status": "in_transit", "tracker_id": "trk_ship03"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 15

- model `gemini-3.6-flash` · condition `Dprime` · drift class `type_change` · task `ct04`
- **User request:** Add Diego Fuentes (diego@meridian.test) as a prospect scored 80 — newsletter on — then log a call on his new record with summary 'Intro call booked'.
- **API change on `create_contact`:** Parameter `score` changed type from integer to string. Old meaning: Lead score 0-100. New meaning: Lead score 0-100 as string.
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"email": "diego@meridian.test", "full_name": "Diego Fuentes", "score": 80, "stage": "prospect"}`
- **Correct call, new API (v2):** `{"email": "diego@meridian.test", "full_name": "Diego Fuentes", "score": "80", "stage": "prospect"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `create_contact`: `{"email": "diego@meridian.test", "full_name": "Diego Fuentes", "score": "80", "stage": "prospect", "subscribe_newsletter": true}`
   - result: {"contact_id": "ct_ct04"}
2. call `log_interaction`: `{"contact_id": "ct_ct04", "kind": "call", "summary": "Intro call booked"}`
   - result: {"interaction_id": "ix_ct04"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 16

- model `openai/gpt-5.6-luna` · condition `Dprime` · drift class `default_change` · task `deal03`
- **User request:** Mark dl_4407 closed-won at $99,000.00, closed Oct 1 2026.
- **API change on `update_deal`:** The default of parameter `loss_reason` changed from "" to "unspecified".
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"close_date": "2026-10-01", "deal_id": "dl_4407", "stage": "closed_won", "value_cents": 9900000}`
- **Correct call, new API (v2):** `{"close_date": "2026-10-01", "deal_id": "dl_4407", "loss_reason": "", "stage": "closed_won", "value_cents": 9900000}`
- **Same model and pair with no change log (September B_strict):** succeeded

What the model did:

1. call `update_deal`: `{"close_date": "2026-10-01", "currency": "USD", "deal_id": "dl_4407", "loss_reason": "unspecified", "stage": "closed_won", "value_cents": 9900000}`
   - result: {"deal_id": "deal03", "state": "updated"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 17

- model `modal-qwen2.5-7b` · condition `C:user:prose:apply` · drift class `required` · task `ct02`
- **User request:** Add Tom Okafor, tom.o@vantage.test, straight in as a customer. Newsletter as usual.
- **API change on `create_contact`:** Parameter `owner_id` is now required and has no default. Previously, leaving it out meant "auto_assign".
- **Shown to the model:** old (v1) declaration; change log in the user message, written as prose; with the 'apply it step by step' line
- **Correct call, old API (v1):** `{"email": "tom.o@vantage.test", "full_name": "Tom Okafor", "stage": "customer"}`
- **Correct call, new API (v2):** `{"email": "tom.o@vantage.test", "full_name": "Tom Okafor", "owner_id": "auto_assign", "stage": "customer"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `create_contact`: `{"email": "tom.o@vantage.test", "full_name": "Tom Okafor", "owner_id": "user_provided_id", "stage": "customer", "subscribe_newsletter": true}`
   - result: {"contact_id": "ct_ct02"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 18

- model `openai/gpt-5.6-luna` · condition `C_decl` · drift class `type_change` · task `rem03`
- **User request:** Remind me to call the dentist on Oct 12 2026 at 10:00 UTC with two hours' notice; add the note 'Ask about invoice'. Single reminder, no repeat.
- **API change on `create_reminder`:** Parameter `lead_min` changed type from integer to string. Old meaning: Advance notice in minutes. New meaning: Advance notice in hours, decimal string.
- **Shown to the model:** old (v1) declaration, with the change written into the parameter's description
- **Correct call, old API (v1):** `{"lead_min": 120, "note": "Ask about invoice", "remind_at": "2026-10-12T10:00:00+00:00", "text": "Call the dentist"}`
- **Correct call, new API (v2):** `{"lead_min": "2", "note": "Ask about invoice", "remind_at": "2026-10-12T10:00:00+00:00", "text": "Call the dentist"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `create_reminder`: `{"channel": "push", "lead_min": 120, "list_id": "inbox", "note": "Ask about invoice", "remind_at": "2026-10-12T10:00:00Z", "repeat_daily": false, "text": "Call the dentist"}`
   - result: Error: Invalid type for parameter 'lead_min': expected string, got int.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Invalid type for parameter 'lead_min': expected string, got int.; episode failed.

human_label: 
note: 

## Item 19

- model `openai/gpt-5.6-luna` · condition `CD` · drift class `required` · task `rep03`
- **User request:** Run churn_summary as a PDF over the last 4320 minutes filtered to region=emea, with UTC timestamps.
- **API change on `run_report`:** Parameter `workspace` is now required and has no default. Previously, leaving it out meant "default".
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"filters": "region=emea", "format": "pdf", "report_name": "churn_summary", "window_min": 4320}`
- **Correct call, new API (v2):** `{"filters": "region=emea", "format": "pdf", "report_name": "churn_summary", "window_min": 4320, "workspace": "default"}`
- **Same model and pair with no change log (September B_strict):** succeeded

What the model did:

(no tool calls)

Final text: Please provide the analytics workspace to run the report.

Executor at the drift step: `None`; episode failed.

human_label: 
note: 

## Item 20

- model `modal-qwen2.5-7b` · condition `C:user:json:apply` · drift class `rename` · task `pay02`
- **User request:** Pay my landlord's account DE89370400440532013000 $450.00 for October rent (memo 'October rent'), standard speed is fine.
- **API change on `send_payment`:** Parameter `memo` has been renamed to `reference`; send `reference` instead of `memo`.
- **Shown to the model:** old (v1) declaration; change log in the user message, written as json; with the 'apply it step by step' line
- **Correct call, old API (v1):** `{"amount_cents": 45000, "memo": "October rent", "recipient": "DE89370400440532013000"}`
- **Correct call, new API (v2):** `{"amount_cents": 45000, "recipient": "DE89370400440532013000", "reference": "October rent"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `send_payment`: `{"amount_cents": 45000, "currency": "EUR", "funding_source": "default_balance", "recipient": "DE89370400440532013000", "reference": "October rent", "speed": "standard"}`
   - result: {"payment_id": "pay_pay02", "state": "processed"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 21

- model `modal-qwen2.5-7b` · condition `Dprime` · drift class `default_change` · task `sched03`
- **User request:** Schedule a birthday DM to @marco: 'Happy birthday!' for Oct 30 2026 at 9am UTC, confirm delivery like normal.
- **API change on `schedule_message`:** The default of parameter `confirm_receipt` changed from true to false.
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"channel_type": "dm", "send_at": "2026-10-30T09:00:00+00:00", "target": "@marco", "text": "Happy birthday!"}`
- **Correct call, new API (v2):** `{"channel_type": "dm", "confirm_receipt": true, "send_at": "2026-10-30T09:00:00+00:00", "target": "@marco", "text": "Happy birthday!"}`
- **Same model and pair with no change log (September B_strict):** succeeded

What the model did:

1. call `schedule_message`: `{"campaign": "", "channel_type": "dm", "confirm_receipt": true, "retry_count": 1, "send_at": "2026-10-30T09:00:00Z", "target": "@marco", "text": "Happy birthday!", "timezone": "UTC"}`
   - result: {"scheduled_id": "sch_sched03"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 22

- model `gemini-3.1-pro-preview` · condition `CD` · drift class `default_change` · task `hotel03`
- **User request:** Reserve a standard room in Kyoto, check-in Dec 1 2026, 5 nights, and tell the front desk 'Late check-in after 22:00'; email me the confirmation.
- **API change on `reserve_hotel`:** The default of parameter `email_confirmation` changed from true to false.
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"check_in": "2026-12-01", "city": "Kyoto", "nights": 5, "room_type": "standard", "special_requests": "Late check-in after 22:00"}`
- **Correct call, new API (v2):** `{"check_in": "2026-12-01", "city": "Kyoto", "email_confirmation": true, "nights": 5, "room_type": "standard", "special_requests": "Late check-in after 22:00"}`
- **Same model and pair with no change log (September B_strict):** succeeded

What the model did:

1. call `reserve_hotel`: `{"check_in": "2026-12-01", "city": "Kyoto", "email_confirmation": true, "nights": 5, "room_type": "standard", "special_requests": "Late check-in after 22:00"}`
   - result: {"hotel_address": "addr_hotel03", "reservation_id": "htl_hotel03"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 23

- model `modal-qwen2.5-7b` · condition `C:user:prose:apply` · drift class `enum_tighten` · task `pto04`
- **User request:** Request personal leave for Nov 23 2026 starting 09:00 UTC, 480 minutes, reason 'Long weekend' — team calendar updated as usual — then book me a flight to MIA departing 2026-11-23.
- **API change on `request_time_off`:** Parameter `kind` no longer accepts the value "personal"; use "personal_day" instead.
- **Shown to the model:** old (v1) declaration; change log in the user message, written as prose; with the 'apply it step by step' line
- **Correct call, old API (v1):** `{"duration_min": 480, "kind": "personal", "reason": "Long weekend", "start": "2026-11-23T09:00:00+00:00"}`
- **Correct call, new API (v2):** `{"duration_min": 480, "kind": "personal_day", "reason": "Long weekend", "start": "2026-11-23T09:00:00+00:00"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `request_time_off`: `{"duration_min": 480, "kind": "personal_day", "notify_team": true, "reason": "Long weekend", "start": "2026-11-23T09:00:00Z"}`
   - result: {"pto_id": "pto_pto04", "state": "pending_approval"}
2. call `book_flight`: `{"cabin": "economy", "depart": "2026-11-23", "destination": "MIA"}`
   - result: {"booking_ref": "fl_pto04", "state": "ticketed"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 24

- model `modal-qwen2.5-7b` · condition `C:user:prose:apply` · drift class `required` · task `msg04`
- **User request:** Spin up an invite-only channel proj-falcon and post 'Welcome aboard — kickoff Monday.' there at normal priority, link previews as usual.
- **API change on `send_message`:** Parameter `workspace` is now required and has no default. Previously, leaving it out meant "main".
- **Shown to the model:** old (v1) declaration; change log in the user message, written as prose; with the 'apply it step by step' line
- **Correct call, old API (v1):** `{"priority": "normal", "target": "proj-falcon", "text": "Welcome aboard — kickoff Monday."}`
- **Correct call, new API (v2):** `{"priority": "normal", "target": "proj-falcon", "text": "Welcome aboard — kickoff Monday.", "workspace": "main"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `send_message`: `{"priority": "normal", "target": "proj-falcon", "text": "Welcome aboard — kickoff Monday.", "workspace": "main"}`
   - result: {"message_id": "msg_msg04", "state": "delivered"}
2. call `create_channel`: `{"access": "invite_only", "name": "proj-falcon", "topic": "", "workspace": "main"}`
   - result: {"channel_id": "ch_msg04"}

Final text: (none)

Executor at the drift step: `None`; episode failed.

human_label: 
note: 

## Item 25

- model `openai/gpt-5.6-luna` · condition `C:tool:json:none` · drift class `required` · task `copy02`
- **User request:** Copy /data/export.csv to /backup/export.csv with 3 retries if it flakes; keep the metadata as-is.
- **API change on `copy_file`:** Parameter `volume` is now required and has no default. Previously, leaving it out meant "local".
- **Shown to the model:** old (v1) declaration; change log in a get_api_changelog result already in the transcript, written as json
- **Correct call, old API (v1):** `{"dst": "/backup/export.csv", "retries": 3, "src": "/data/export.csv"}`
- **Correct call, new API (v2):** `{"dst": "/backup/export.csv", "retries": 3, "src": "/data/export.csv", "volume": "local"}`
- **Same model and pair with no change log (September B_strict):** succeeded

What the model did:

1. call `get_api_changelog` (pre-filled, not the model): `{"tool": "copy_file"}`
   - result: NOTE: the API behind tool 'copy_file' was updated after the tool schema you were given was cached. Machine-readable change log for 'copy_file' (apply it when calling): / [ /  { /   "change": "now_required", /   "new": "required, no default", /   "old": { /    "default": "local" /   }, /   "param": "volume" /  } / ]
2. call `copy_file`: `{"comment": "Copy requested export file", "conflict": "skip", "dst": "/backup/export.csv", "preserve_meta": true, "retries": 3, "src": "/data/export.csv", "volume": "local"}`
   - result: {"copied_to": "copy02", "state": "ok"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 26

- model `gemini-3.1-pro-preview` · condition `CD` · drift class `required` · task `ship03`
- **User request:** Track 9400111899560001234567 and only alert me on exceptions; poll every 720 minutes, call it 'Camera lens', distance remaining in miles.
- **API change on `track_shipment`:** Parameter `carrier` is now required and has no default. Previously, leaving it out meant "auto_detect".
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"alert_on": "exception", "nickname": "Camera lens", "poll_interval_min": 720, "tracking_number": "9400111899560001234567"}`
- **Correct call, new API (v2):** `{"alert_on": "exception", "carrier": "auto_detect", "nickname": "Camera lens", "poll_interval_min": 720, "tracking_number": "9400111899560001234567"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `track_shipment`: `{"alert_on": "exception", "carrier": "USPS", "nickname": "Camera lens", "poll_interval_min": 720, "tracking_number": "9400111899560001234567", "units": "miles"}`
   - result: {"status": "in_transit", "tracker_id": "trk_ship03"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 27

- model `openai/gpt-5.6-luna` · condition `CD` · drift class `rename` · task `chan03`
- **User request:** Make an open book-club channel, topic 'Monthly reads', and leave auto-archive off.
- **API change on `create_channel`:** Parameter `topic` has been renamed to `channel_purpose`; send `channel_purpose` instead of `topic`.
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"access": "open", "name": "book-club", "topic": "Monthly reads"}`
- **Correct call, new API (v2):** `{"access": "open", "channel_purpose": "Monthly reads", "name": "book-club"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `create_channel`: `{"access": "open", "auto_archive": false, "channel_purpose": "Monthly reads", "history_days": 0, "name": "book-club", "workspace": "main"}`
   - result: {"channel_id": "ch_chan03"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 28

- model `modal-qwen2.5-7b` · condition `C:sys:prose:none` · drift class `rename` · task `perm01`
- **User request:** Give team-accounting write access to /shared/finance just for that folder (not its children), justification 'Month-end close'.
- **API change on `set_permissions`:** Parameter `justification` has been renamed to `audit_reason`; send `audit_reason` instead of `justification`.
- **Shown to the model:** old (v1) declaration; change log in the system prompt, written as prose
- **Correct call, old API (v1):** `{"access": "write", "justification": "Month-end close", "path": "/shared/finance", "principal": "team-accounting"}`
- **Correct call, new API (v2):** `{"access": "write", "audit_reason": "Month-end close", "path": "/shared/finance", "principal": "team-accounting"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `set_permissions`: `{"access": "write", "justification": "Month-end close", "path": "/shared/finance", "principal": "team-accounting", "realm": "corp", "recursive": false}`
   - result: Error: Received unknown parameter: 'justification'.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Received unknown parameter: 'justification'.; episode failed.

human_label: 
note: 

## Item 29

- model `gemini-3.6-flash` · condition `Dprime` · drift class `default_change` · task `rem02`
- **User request:** Set a one-time push reminder to water the plants, Oct 5 2026 at 8am UTC. Definitely not a daily repeat.
- **API change on `create_reminder`:** The default of parameter `repeat_daily` changed from false to true.
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"channel": "push", "remind_at": "2026-10-05T08:00:00+00:00", "text": "Water the plants"}`
- **Correct call, new API (v2):** `{"channel": "push", "remind_at": "2026-10-05T08:00:00+00:00", "repeat_daily": false, "text": "Water the plants"}`
- **Same model and pair with no change log (September B_strict):** succeeded

What the model did:

1. call `create_reminder`: `{"channel": "push", "remind_at": "2026-10-05T08:00:00Z", "repeat_daily": false, "text": "Water the plants"}`
   - result: {"reminder_id": "rem_rem02"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 30

- model `modal-qwen2.5-7b` · condition `C:user:json:apply` · drift class `type_change` · task `pto03`
- **User request:** Request vacation starting Dec 21 2026 at 09:00 UTC for 2400 minutes, reason 'Year-end trip'; the team should see it on the calendar as usual.
- **API change on `request_time_off`:** Parameter `duration_min` changed type from integer to string. Old meaning: Leave length in minutes. New meaning: Leave length in hours, decimal string.
- **Shown to the model:** old (v1) declaration; change log in the user message, written as json; with the 'apply it step by step' line
- **Correct call, old API (v1):** `{"duration_min": 2400, "kind": "vacation", "reason": "Year-end trip", "start": "2026-12-21T09:00:00+00:00"}`
- **Correct call, new API (v2):** `{"duration_min": "40", "kind": "vacation", "reason": "Year-end trip", "start": "2026-12-21T09:00:00+00:00"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `request_time_off`: `{"approver": "direct_manager", "duration": "40", "kind": "vacation", "notify_team": true, "reason": "Year-end trip", "start": "2026-12-21T09:00:00Z"}`
   - result: Error: Received unknown parameter: 'duration'.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Received unknown parameter: 'duration'.; episode failed.

human_label: 
note: 

## Item 31

- model `gemini-3.6-flash` · condition `Dprime` · drift class `required` · task `msg04`
- **User request:** Spin up an invite-only channel proj-falcon and post 'Welcome aboard — kickoff Monday.' there at normal priority, link previews as usual.
- **API change on `send_message`:** Parameter `workspace` is now required and has no default. Previously, leaving it out meant "main".
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"priority": "normal", "target": "proj-falcon", "text": "Welcome aboard — kickoff Monday."}`
- **Correct call, new API (v2):** `{"priority": "normal", "target": "proj-falcon", "text": "Welcome aboard — kickoff Monday.", "workspace": "main"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `create_channel`: `{"access": "invite_only", "name": "proj-falcon"}`
   - result: {"channel_id": "ch_msg04"}
2. call `send_message`: `{"priority": "normal", "target": "#proj-falcon", "text": "Welcome aboard — kickoff Monday.", "unfurl_links": true, "workspace": "main"}`
   - result: {"message_id": "msg_msg04", "state": "delivered"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 32

- model `openai/gpt-5.6-luna` · condition `C:sys:prose:none` · drift class `required` · task `refund03`
- **User request:** Refund the full $250.00 on pay_55710 as fraud; internal note 'Chargeback pre-empt'. Customer should still get the standard refund email.
- **API change on `refund_payment`:** Parameter `ledger` is now required and has no default. Previously, leaving it out meant "main".
- **Shown to the model:** old (v1) declaration; change log in the system prompt, written as prose
- **Correct call, old API (v1):** `{"amount_cents": 25000, "note": "Chargeback pre-empt", "payment_id": "pay_55710", "reason": "fraud"}`
- **Correct call, new API (v2):** `{"amount_cents": 25000, "ledger": "main", "note": "Chargeback pre-empt", "payment_id": "pay_55710", "reason": "fraud"}`
- **Same model and pair with no change log (September B_strict):** succeeded

What the model did:

1. call `refund_payment`: `{"amount_cents": 25000, "ledger": "main", "note": "Chargeback pre-empt", "notify": true, "payment_id": "pay_55710", "reason": "fraud"}`
   - result: {"refund_id": "ref_refund03", "state": "refunded"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 33

- model `gemini-3.6-flash` · condition `Dprime` · drift class `default_change` · task `msg03`
- **User request:** Urgent post to #incidents: 'DB failover complete, all green.' Keep the link previews.
- **API change on `send_message`:** The default of parameter `unfurl_links` changed from true to false.
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"priority": "urgent", "target": "#incidents", "text": "DB failover complete, all green."}`
- **Correct call, new API (v2):** `{"priority": "urgent", "target": "#incidents", "text": "DB failover complete, all green.", "unfurl_links": true}`
- **Same model and pair with no change log (September B_strict):** succeeded

What the model did:

1. call `send_message`: `{"priority": "urgent", "target": "#incidents", "text": "DB failover complete, all green.", "unfurl_links": true}`
   - result: {"message_id": "msg_msg03", "state": "delivered"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 34

- model `gemini-3.6-flash` · condition `CD` · drift class `required` · task `zip02`
- **User request:** Tar up /video/raw as raw-footage.tar, split into 2048 MB parts, unencrypted.
- **API change on `compress_folder`:** Parameter `dest_dir` is now required and has no default. Previously, leaving it out meant "/archives".
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"archive_name": "raw-footage.tar", "folder": "/video/raw", "format": "tar", "split_mb": 2048}`
- **Correct call, new API (v2):** `{"archive_name": "raw-footage.tar", "dest_dir": "/archives", "folder": "/video/raw", "format": "tar", "split_mb": 2048}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `compress_folder`: `{"archive_name": "raw-footage.tar", "dest_dir": "/video", "folder": "/video/raw", "format": "tar", "split_mb": 2048}`
   - result: {"archive_path": "/archives/zip02", "state": "ok"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 35

- model `modal-qwen2.5-7b` · condition `C:tool:json:apply` · drift class `required` · task `zip02`
- **User request:** Tar up /video/raw as raw-footage.tar, split into 2048 MB parts, unencrypted.
- **API change on `compress_folder`:** Parameter `dest_dir` is now required and has no default. Previously, leaving it out meant "/archives".
- **Shown to the model:** old (v1) declaration; change log in a get_api_changelog result already in the transcript, written as json; with the 'apply it step by step' line
- **Correct call, old API (v1):** `{"archive_name": "raw-footage.tar", "folder": "/video/raw", "format": "tar", "split_mb": 2048}`
- **Correct call, new API (v2):** `{"archive_name": "raw-footage.tar", "dest_dir": "/archives", "folder": "/video/raw", "format": "tar", "split_mb": 2048}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `get_api_changelog` (pre-filled, not the model): `{"tool": "compress_folder"}`
   - result: NOTE: the API behind tool 'compress_folder' was updated after the tool schema you were given was cached. Machine-readable change log for 'compress_folder' (apply it when calling): / [ /  { /   "change": "now_required", /   "new": "required, no default", /   "old": { /    "default": "/archives" /   }, /   "param": "dest_dir" /  } / ] / Before calling 'compress_folder', apply this change log step by step: for each change, rewrite the affected argument so the call matches the updated API.
2. call `compress_folder`: `{"archive_name": "raw-footage.tar", "dest_dir": null, "encrypt": false, "folder": "/video/raw", "format": "tar", "label": "", "split_mb": 2048}`
   - result: Error: Invalid type for parameter 'dest_dir': expected string, got NoneType.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Invalid type for parameter 'dest_dir': expected string, got NoneType.; episode failed.

human_label: 
note: 

## Item 36

- model `modal-qwen2.5-7b` · condition `C_decl` · drift class `enum_tighten` · task `pto02`
- **User request:** Put in for personal leave on Nov 6 2026 from 13:00 UTC for 240 minutes, and let the team know via the calendar as usual.
- **API change on `request_time_off`:** Parameter `kind` no longer accepts the value "personal"; use "personal_day" instead.
- **Shown to the model:** old (v1) declaration, with the change written into the parameter's description
- **Correct call, old API (v1):** `{"duration_min": 240, "kind": "personal", "start": "2026-11-06T13:00:00+00:00"}`
- **Correct call, new API (v2):** `{"duration_min": 240, "kind": "personal_day", "start": "2026-11-06T13:00:00+00:00"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `request_time_off`: `{"approver": "direct_manager", "duration_min": 240, "kind": "personal_day", "notify_team": true, "start": "2026-11-06T13:00:00Z"}`
   - result: {"pto_id": "pto_pto02", "state": "pending_approval"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 37

- model `openai/gpt-5.6-luna` · condition `C:tool:json:none` · drift class `default_change` · task `web01`
- **User request:** Search for solid state battery breakthroughs, top 5 results, moderate safe-search, only from nature.com — text results only, no images.
- **API change on `web_search`:** The default of parameter `include_images` changed from false to true.
- **Shown to the model:** old (v1) declaration; change log in a get_api_changelog result already in the transcript, written as json
- **Correct call, old API (v1):** `{"max_results": 5, "query": "solid state battery breakthroughs", "safe_search": "moderate", "site_filter": "nature.com"}`
- **Correct call, new API (v2):** `{"include_images": false, "max_results": 5, "query": "solid state battery breakthroughs", "safe_search": "moderate", "site_filter": "nature.com"}`
- **Same model and pair with no change log (September B_strict):** succeeded

What the model did:

1. call `get_api_changelog` (pre-filled, not the model): `{"tool": "web_search"}`
   - result: NOTE: the API behind tool 'web_search' was updated after the tool schema you were given was cached. Machine-readable change log for 'web_search' (apply it when calling): / [ /  { /   "change": "default_changed", /   "new": true, /   "old": false, /   "param": "include_images" /  } / ]
2. call `web_search`: `{"include_images": false, "max_results": 5, "query": "solid state battery breakthroughs", "region": "us", "safe_search": "moderate", "site_filter": "nature.com"}`
   - result: {"search_id": "srch_web01", "top_url": "https://results.test/web01"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 38

- model `gemini-3.1-pro-preview` · condition `CD` · drift class `type_change` · task `job03`
- **User request:** Post a full-time Product Designer opening in the Design department at the NYC office, band up to $140,000.00, visible on the public board as usual.
- **API change on `post_job_opening`:** Parameter `salary_cents` changed type from integer to string. Old meaning: Top of annual salary band in cents. New meaning: Top of annual salary band as decimal string in major units.
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"department": "Design", "employment": "full_time", "location": "NYC office", "salary_cents": 14000000, "title": "Product Designer"}`
- **Correct call, new API (v2):** `{"department": "Design", "employment": "full_time", "location": "NYC office", "salary_cents": "140000.00", "title": "Product Designer"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `post_job_opening`: `{"department": "Design", "employment": "full_time", "location": "NYC", "salary_cents": "140000.00", "title": "Product Designer"}`
   - result: {"job_id": "job_job03", "state": "published"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 39

- model `openai/gpt-5.6-luna` · condition `C:user:json:apply` · drift class `enum_tighten` · task `fly02`
- **User request:** Book a premium economy flight to LIS for Oct 22 2026 with at most a 90-minute layover; a non-refundable ticket is fine.
- **API change on `book_flight`:** Parameter `cabin` no longer accepts the value "premium_economy"; use "premium" instead.
- **Shown to the model:** old (v1) declaration; change log in the user message, written as json; with the 'apply it step by step' line
- **Correct call, old API (v1):** `{"cabin": "premium_economy", "depart": "2026-10-22", "destination": "LIS", "max_layover_min": 90}`
- **Correct call, new API (v2):** `{"cabin": "premium", "depart": "2026-10-22", "destination": "LIS", "max_layover_min": 90}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `book_flight`: `{"cabin": "premium_economy", "depart": "2026-10-22", "destination": "LIS", "max_layover_min": 90, "refundable": false, "seat_pref": "", "traveler_id": "primary_profile"}`
   - result: Error: Invalid value 'premium_economy' for parameter 'cabin'. Allowed values: economy, premium, business.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Invalid value 'premium_economy' for parameter 'cabin'. Allowed values: economy, premium, business.; episode failed.

human_label: 
note: 

## Item 40

- model `modal-qwen2.5-7b` · condition `C:tool:prose:none` · drift class `enum_tighten` · task `deal04`
- **User request:** Move dl_6120 to negotiation at $27,500.00 and post in #sales: 'dl_6120 moved to negotiation at $27.5k.'
- **API change on `update_deal`:** Parameter `stage` no longer accepts the value "negotiation"; use "in_negotiation" instead.
- **Shown to the model:** old (v1) declaration; change log in a get_api_changelog result already in the transcript, written as prose
- **Correct call, old API (v1):** `{"deal_id": "dl_6120", "stage": "negotiation", "value_cents": 2750000}`
- **Correct call, new API (v2):** `{"deal_id": "dl_6120", "stage": "in_negotiation", "value_cents": 2750000}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `get_api_changelog` (pre-filled, not the model): `{"tool": "update_deal"}`
   - result: NOTE: the API behind tool 'update_deal' was updated after the tool schema you were given was cached. Plain-language change log for 'update_deal' (apply it when calling): / - Parameter `stage` no longer accepts the value "negotiation"; use "in_negotiation" instead.
2. call `update_deal`: `{"deal_id": "dl_6120", "stage": "in_negotiation", "target": "#sales", "text": "dl_6120 moved to negotiation at $27.5k.", "value_cents": 2750000}`
   - result: Error: Received unknown parameter: 'target'.

Final text: (none)

Executor at the drift step: `ERROR_SURFACED`, error: Received unknown parameter: 'target'.; episode failed.

human_label: 
note: 

## Item 41

- model `gemini-3.6-flash` · condition `Dprime` · drift class `type_change` · task `ds03`
- **User request:** Export billing_ledger to s3://viz-archive/billing with zstd compression, 4096 MB chunks, tag 'finance', header row included.
- **API change on `export_dataset`:** Parameter `chunk_mb` changed type from integer to string. Old meaning: Chunk size in megabytes (0 = single file). New meaning: Chunk size in gigabytes, decimal string ("0" = single file).
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"chunk_mb": 4096, "compression": "zstd", "dataset": "billing_ledger", "destination": "s3://viz-archive/billing", "tag": "finance"}`
- **Correct call, new API (v2):** `{"chunk_mb": "4", "compression": "zstd", "dataset": "billing_ledger", "destination": "s3://viz-archive/billing", "tag": "finance"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `export_dataset`: `{"chunk_mb": "4.096", "compression": "zstd", "dataset": "billing_ledger", "destination": "s3://viz-archive/billing", "include_headers": true, "tag": "finance"}`
   - result: {"export_id": "dx_ds03", "state": "queued"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 

## Item 42

- model `modal-qwen2.5-7b` · condition `C:user:json:none` · drift class `default_change` · task `sched03`
- **User request:** Schedule a birthday DM to @marco: 'Happy birthday!' for Oct 30 2026 at 9am UTC, confirm delivery like normal.
- **API change on `schedule_message`:** The default of parameter `confirm_receipt` changed from true to false.
- **Shown to the model:** old (v1) declaration; change log in the user message, written as json
- **Correct call, old API (v1):** `{"channel_type": "dm", "send_at": "2026-10-30T09:00:00+00:00", "target": "@marco", "text": "Happy birthday!"}`
- **Correct call, new API (v2):** `{"channel_type": "dm", "confirm_receipt": true, "send_at": "2026-10-30T09:00:00+00:00", "target": "@marco", "text": "Happy birthday!"}`
- **Same model and pair with no change log (September B_strict):** succeeded

What the model did:

1. call `schedule_message`: `{"campaign": "", "channel_type": "dm", "confirm_receipt": true, "retry_count": 1, "send_at": "2026-10-30T09:00:00Z", "target": "@marco", "text": "Happy birthday!", "timezone": "UTC"}`
   - result: {"scheduled_id": "sch_sched03"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 43

- model `openai/gpt-5.6-luna` · condition `Dprime` · drift class `enum_tighten` · task `hotel02`
- **User request:** Book a deluxe room in Denver for 2 nights from Nov 5 2026, and send the confirmation to my email.
- **API change on `reserve_hotel`:** Parameter `room_type` no longer accepts the value "deluxe"; use "luxury" instead.
- **Shown to the model:** new (v2) declaration; the parameter's description also states the old contract
- **Correct call, old API (v1):** `{"check_in": "2026-11-05", "city": "Denver", "nights": 2, "room_type": "deluxe"}`
- **Correct call, new API (v2):** `{"check_in": "2026-11-05", "city": "Denver", "nights": 2, "room_type": "luxury"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `reserve_hotel`: `{"check_in": "2026-11-05", "city": "Denver", "email_confirmation": true, "guest_profile": "primary", "nights": 2, "room_type": "luxury", "special_requests": ""}`
   - result: {"hotel_address": "addr_hotel02", "reservation_id": "htl_hotel02"}

Final text: (none)

Executor at the drift step: `ACCEPTED_CORRECT`; episode succeeded.

human_label: 
note: 

## Item 44

- model `gemini-3.6-flash` · condition `CD` · drift class `type_change` · task `ds03`
- **User request:** Export billing_ledger to s3://viz-archive/billing with zstd compression, 4096 MB chunks, tag 'finance', header row included.
- **API change on `export_dataset`:** Parameter `chunk_mb` changed type from integer to string. Old meaning: Chunk size in megabytes (0 = single file). New meaning: Chunk size in gigabytes, decimal string ("0" = single file).
- **Shown to the model:** new (v2) declaration, plus the JSON change log in the system prompt
- **Correct call, old API (v1):** `{"chunk_mb": 4096, "compression": "zstd", "dataset": "billing_ledger", "destination": "s3://viz-archive/billing", "tag": "finance"}`
- **Correct call, new API (v2):** `{"chunk_mb": "4", "compression": "zstd", "dataset": "billing_ledger", "destination": "s3://viz-archive/billing", "tag": "finance"}`
- **Same model and pair with no change log (September B_strict):** failed

What the model did:

1. call `export_dataset`: `{"compression": "zstd", "dataset": "billing_ledger", "destination": "s3://viz-archive/billing", "include_headers": true, "tag": "finance"}`
   - result: {"export_id": "dx_ds03", "state": "queued"}

Final text: (none)

Executor at the drift step: `ACCEPTED_WRONG`; episode failed.

human_label: 
note: 
