---
title: "Release: Python Slack SDK v3.43.0"
summary: "* We've added a public, read-only ts property to ChatStream and AsyncChatStream, enabling users to call the chat.update API method as a fallback when the server closes a stream due to undocumented timeouts."
url: "https://docs.slack.dev/changelog/2026/06/30/py-slack-sdk"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/06/30/py-slack-sdk

# Release: Python Slack SDK v3.43.0

June 30, 2026

*   We've added a public, read-only `ts` property to `ChatStream` and `AsyncChatStream`, enabling users to call the [`chat.update`](https://docs.slack.dev/reference/methods/chat.update.md) API method as a fallback when the server closes a stream due to undocumented timeouts.
*   We made the `thread_ts` argument of the [`assistant.threads.setSuggestedPrompts`](https://docs.slack.dev/reference/methods/assistant.threads.setsuggestedprompts.md) API method optional.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Python Slack SDK](https://docs.slack.dev/changelog/tags/python-slack-sdk.md)
