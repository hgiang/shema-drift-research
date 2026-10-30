---
title: "Release: Node Slack SDK updates"
summary: "We've released the following Node Slack SDK-related updates:"
url: "https://docs.slack.dev/changelog/2026/09/30/node-sdk"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/09/30/node-sdk

# Release: Node Slack SDK updates

September 30, 2026

We've released the following Node Slack SDK-related updates:

## Socket Mode v3.1.0 {#socket-mode-v310}

*   The default dispatcher now pins the WebSocket connection to HTTP/1.1, since `undici@^8` offers HTTP/2 by default. To do the same with a custom `ProxyAgent` dispatcher, pass `requestTls: { allowH2: false }`.

## Types v3.2.0 {#types-v320}

*   We added the [`ContainerBlock`](https://docs.slack.dev/reference/block-kit/blocks/container-block.md) block interface.
*   We added the [`data_table`](https://docs.slack.dev/reference/block-kit/blocks/data-table-block.md) Block Kit block type (`DataTableBlock`).
*   We now allow `raw_number` cells in [`TableBlock`](https://docs.slack.dev/reference/block-kit/blocks/table-block.md) rows (adds `RawNumberElement`).
*   We added an optional `action_id` property to the [`WorkflowButton`](https://docs.slack.dev/reference/block-kit/block-elements/workflow-button-element.md) block element.

## Web API v8.2.0 {#web-api-v820}

*   We added the `agents.conversations.*` methods for [Slack Code](https://docs.slack.dev/changelog/2026/08/20/slack-code.md):
    *   [`create`](https://docs.slack.dev/reference/methods/agents.conversations.create.md),
    *   [`archive`](https://docs.slack.dev/reference/methods/agents.conversations.archive.md),
    *   [`setProperties`](https://docs.slack.dev/reference/methods/agents.conversations.setproperties.md),
    *   [`setView`](https://docs.slack.dev/reference/methods/agents.conversations.setview.md),
    *   [`setCommands`](https://docs.slack.dev/reference/methods/agents.conversations.setcommands.md),
    *   [`listViews`](https://docs.slack.dev/reference/methods/agents.conversations.listviews.md),
    *   [`removeView`](https://docs.slack.dev/reference/methods/agents.conversations.removeview.md),
    *   [`getCanvas`](https://docs.slack.dev/reference/methods/agents.conversations.getcanvas.md),
    *   [`setCanvasContent`](https://docs.slack.dev/reference/methods/agents.conversations.setcanvascontent.md)

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Node Slack SDK](https://docs.slack.dev/changelog/tags/node-slack-sdk.md)
