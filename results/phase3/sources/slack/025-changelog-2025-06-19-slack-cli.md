---
title: "Release: Slack CLI v3.4.0"
summary: "Version 3.4.0 of the developer tools for the Slack platform is here!"
url: "https://docs.slack.dev/changelog/2025/06/19/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2025/06/19/slack-cli

# Release: Slack CLI v3.4.0

June 19, 2025

Version `3.4.0` of the developer tools for the Slack platform is here!

*   The install script and the `slack upgrade` command will now automatically detect your macOS architecture and install an Intel or an Apple Silicon binary.
*   Outputs from erroring hook scripts, such as those found when gathering an abnormal app manifest, are no longer hidden in verbose outputs but are instead shown with invocation errors.
*   In preparation for apps using the [Run on Slack infrastructure](https://docs.slack.dev/workflows/run-on-slack-infrastructure.md) to work with [Deno 2](https://deno.com/blog/v2.0), the following Deno ecosystem releases have gone out:
    *   `v2.15.1` of the [Deno Slack SDK](https://github.com/slackapi/deno-slack-sdk/releases/tag/2.15.1)
    *   `v1.4.0` of the [Deno Slack Hooks](https://github.com/slackapi/deno-slack-hooks/releases/tag/1.4.0)
    *   `v1.1.3` of the [Deno Slack Runtime](https://github.com/slackapi/deno-slack-runtime/releases/tag/1.1.3)

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
