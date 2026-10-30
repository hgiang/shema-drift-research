---
title: "Agent context has landed"
summary: "Agent apps can now receive context about what a user is currently viewing when they send a message. When a user has a channel, DM, thread, canvas, or list open and messages your app, Slack will pass that context automatically."
url: "https://docs.slack.dev/changelog/2026/07/02/app-context"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/07/02/app-context

# Agent context has landed

July 2, 2026

Agent apps can now receive context about what a user is currently viewing when they send a message. When a user has a channel, DM, thread, canvas, or list open and messages your app, Slack will pass that context automatically.

Here's what developers need to know:

*   **New event: [`app_context_changed`](https://docs.slack.dev/reference/events/app_context_changed.md)**: Slack will send an `app_context_changed` event to your app whenever the user's active context changes. The event payload includes an ordered list of entities the user is currently viewing.
*   **The `app_context` is now sent to [`message.im`](https://docs.slack.dev/reference/events/message.im.md) and [`app_home_opened`](https://docs.slack.dev/reference/events/app_home_opened.md) events**: Slack will also send the `app_context` to these events if the app is subscribed to the `app_context_changed` event.

Learn more in the guide to [Developing agents](https://docs.slack.dev/ai/developing-agents.md#app-context).

**Tags:**

*   [Announcement](https://docs.slack.dev/changelog/tags/announcement.md)
