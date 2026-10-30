---
title: "Announcing the Slack MCP server and Real-time Search API"
summary: "We're excited to announce the release of not one, but two, major components designed to significantly enhance how Large Language Models (LLMs) and AI agents interact with your workspace data: the Slack Model Context Protocol (MCP) server and the Real-time Search (RTS) API!"
url: "https://docs.slack.dev/changelog/2026/02/17/slack-mcp"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/02/17/slack-mcp

# Announcing the Slack MCP server and Real-time Search API

February 17, 2026

We're excited to announce the release of not one, but _two_, major components designed to significantly enhance how Large Language Models (LLMs) and AI agents interact with your workspace data: the Slack Model Context Protocol (MCP) server and the Real-time Search (RTS) API!

## Slack MCP Server {#slack-mcp-server}

The MCP server enables AI agents to interact with Slack content through tools designed for LLM-driven discovery, configuration, and execution. Unlike APIs, the MCP server is built specifically for LLM consumption with robust descriptions and examples that return natural language responses. Refer to our documentation to learn more about the [Slack MCP server](https://docs.slack.dev/ai/slack-mcp-server.md).

## Real-time Search API {#real-time-search-api}

The Data Access API has evolved into the [Real-time Search API](https://docs.slack.dev/apis/web-api/real-time-search-api.md)! This API allows users to access Slack data through a secure search interface, enabling third-party applications to retrieve relevant Slack data without storing customer information on external servers. Get started using the Real-time Search API with [this guide](https://docs.slack.dev/apis/web-api/real-time-search-api.md) or get straight to business with the [method reference](https://docs.slack.dev/reference/methods/assistant.search.context.md).

### Scope updates to assistant.search.context {#scope-updates-to-assistantsearchcontext}

Along with these changes, the [`assistant.search.context`](https://docs.slack.dev/reference/methods/assistant.search.context.md) API method has undergone a scope change. The `assistant.search.context` API method moved away from the single `search:read` scope to a set of granular `search:read.*` scopes:

*   [`search:read.public`](https://docs.slack.dev/reference/scopes/search.read.public.md) (required) - for public channel access
*   [`search:read.private`](https://docs.slack.dev/reference/scopes/search.read.private.md) - for private channels (with user consent)
*   [`search:read.im`](https://docs.slack.dev/reference/scopes/search.read.im.md) - for direct messages (with user consent)
*   [`search:read.mpim`](https://docs.slack.dev/reference/scopes/search.read.mpim.md) - for multi-party direct messages (with user consent)

This change allows for more granular control over what data AI-enabled apps can access.

**Tags:**

*   [Announcement](https://docs.slack.dev/changelog/tags/announcement.md)
*   [New Feature](https://docs.slack.dev/changelog/tags/new-feature.md)
