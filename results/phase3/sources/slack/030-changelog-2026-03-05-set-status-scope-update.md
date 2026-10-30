---
title: "Set status method scope update"
summary: "The assistant.threads.setStatus API method now accepts either the assistantwrite scope. This allows channel-based apps to use AI loading states in channels, without having to request assistantwrite scope in favor of the chat:write scope exclusively, so update your app soon!"
url: "https://docs.slack.dev/changelog/2026/03/05/set-status-scope-update"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/03/05/set-status-scope-update

# Set status method scope update

March 5, 2026

The [`assistant.threads.setStatus`](https://docs.slack.dev/reference/methods/assistant.threads.setstatus.md) API method now accepts either the [`assistant:write`](https://docs.slack.dev/reference/scopes/assistant.write.md) or [`chat:write`](https://docs.slack.dev/reference/scopes/chat.write.md) scope. This allows channel-based apps to use [AI loading states](https://docs.slack.dev/ai/developing-agents.md#loading-state) in channels, without having to request `assistant:write` or use the AI assistant split view. The `assistant.threads.setStatus` API method will eventually no longer accept the `assistant:write` scope in favor of the `chat:write` scope exclusively, so update your app soon!

**Tags:**

*   [Announcement](https://docs.slack.dev/changelog/tags/announcement.md)
