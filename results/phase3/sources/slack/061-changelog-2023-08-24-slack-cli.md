---
title: "Release: Slack CLI v2.8.0"
summary: "Version 2.8.0 of the developer tools for the Slack automations platform has arrived!"
url: "https://docs.slack.dev/changelog/2023/08/24/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2023/08/24/slack-cli

# Release: Slack CLI v2.8.0

August 24, 2023

Version `2.8.0` of the developer tools for the Slack automations platform has arrived!

*   We've improved Deno dependency caching.
*   The `app list` command no longer requires authentication, and will instead display an `unknown` app status in cases where no authentication is found.
*   The `run`, `deploy`, and `delete` commands will now resolve organization-level authentication in cases where workspace-level authentication is missing.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
