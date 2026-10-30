---
title: "Release: Slack CLI v4.5.0"
summary: "Version 4.5.0 of the developer tools for the Slack platform has landed!"
url: "https://docs.slack.dev/changelog/2026/07/21/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/07/21/slack-cli

# Release: Slack CLI v4.5.0

July 21, 2026

Version `4.5.0` of the developer tools for the Slack platform has landed!

*   The Slack CLI now recommends the official [Slack plugin](https://claude.com/plugins/slack) to Claude Code users.
*   We've reduced the verbose output when using `create --app` to link an existing app during project creation.
*   We've added a `--category` flag to `slack docs search` command.
*   When the CLI errors because a prompt must be shown while in a non-TTY environment (AI agents, devops scripts, etc.), the error message now displays the prompt and, for app and team selection, the matching flags to select an option.
*   We've fixed a recurring `unable_to_parse_json` error caused by empty JSON files (credentials, config, or app state) left behind by an interrupted write; the CLI now treats them as empty state and recovers automatically.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
