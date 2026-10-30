---
title: "Release: Python Slack SDK v3.42.0"
summary: "* We've added authorship arguments (iconemoji, iconurl, and username) to the assistant.threads.setStatus and chat.startStream API methods."
url: "https://docs.slack.dev/changelog/2026/05/18/py-slack-sdk"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/05/18/py-slack-sdk

# Release: Python Slack SDK v3.42.0

May 18, 2026

*   We've added authorship arguments (`icon_emoji`, `icon_url`, and `username`) to the `assistant.threads.setStatus` and `chat.startStream` API methods.
*   We've added `highlight_type` support to the `files.completeUploadExternal` and `filesUploadV2` API methods. The `highlight_type` parameter allows specifying the file type hint for uploads (e.g., `png`, `jpg`, and `gif` file types), enabling optimistic rendering before the async upload processing job completes.
*   We've added support for the following new Block Kit blocks: [card block](https://docs.slack.dev/reference/block-kit/blocks/card-block.md), [carousel block](https://docs.slack.dev/reference/block-kit/blocks/carousel-block.md), and [alert block](https://docs.slack.dev/reference/block-kit/blocks/alert-block.md). All three include deserialization support via `Block.parse()`, exports in `__init__.py`, and round-trip tests.
*   We've added a new `BlocksChunk` model class to support the new `blocks` chunk type for streaming API methods (`chat.startStream`, `chat.appendStream`, and `chat.stopStream`). Refer to [New Block Kit blocks and Streaming API method updates](https://docs.slack.dev/changelog/2026/04/16/block-kit-new-blocks.md) for more details.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Python Slack SDK](https://docs.slack.dev/changelog/tags/python-slack-sdk.md)
