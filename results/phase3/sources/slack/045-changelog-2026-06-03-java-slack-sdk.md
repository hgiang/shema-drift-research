---
title: "Release: Java Slack SDK v1.49.0"
summary: "* We've added authorship arguments (iconemoji, iconurl, and username) to the assistant.threads.setStatus and chat.startStream API methods."
url: "https://docs.slack.dev/changelog/2026/06/03/java-slack-sdk"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/06/03/java-slack-sdk

# Release: Java Slack SDK v1.49.0

June 3, 2026

*   We've added authorship arguments (`icon_emoji`, `icon_url`, and `username`) to the `assistant.threads.setStatus` and `chat.startStream` API methods.
*   We've added `highlight_type` support to the `files.completeUploadExternal` and `filesUploadV2` API methods. The `highlight_type` parameter allows specifying the file type hint for uploads (e.g., `png`, `jpg`, and `gif` file types), enabling optimistic rendering before the async upload processing job completes.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Java Slack SDK](https://docs.slack.dev/changelog/tags/java-slack-sdk.md)
