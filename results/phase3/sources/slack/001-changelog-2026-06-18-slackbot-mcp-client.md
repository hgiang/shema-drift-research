---
title: "Announcing the Slackbot MCP Client"
summary: "We're excited to introduce you to the Slackbot MCP Client, which gives you the ability to superpower Slackbot with your desired tools."
url: "https://docs.slack.dev/changelog/2026/06/18/slackbot-mcp-client"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/06/18/slackbot-mcp-client

# Announcing the Slackbot MCP Client

June 18, 2026

We're excited to introduce you to the Slackbot MCP Client, which gives you the ability to superpower Slackbot with your desired tools.

The Slackbot MCP Client allows developers to connect [MCP servers](https://modelcontextprotocol.io/) to Slack. Once connected, Slackbot will automatically discover your MCP server's tools and invoke them based on user prompts in conversation.

Four authentication methods are available for connecting to MCP servers:

*   **Slack identity auth**: for MCP servers that map Slack user and team IDs to available features, with no separate OAuth flow required for end users.
*   **No auth**: for MCP servers that serve standard responses regardless of requestor.
*   **Dynamic Client Registration**: for MCP servers that support standard OAuth discovery. Slack handles client registration automatically.
*   **Manual OAuth**: for MCP servers where you manually register OAuth credentials with the provider.

Read the [Slackbot MCP Client docs](https://docs.slack.dev/ai/slackbot-mcp-client.md) to get started.

**Tags:**

*   [Announcement](https://docs.slack.dev/changelog/tags/announcement.md)
*   [New Feature](https://docs.slack.dev/changelog/tags/new-feature.md)
