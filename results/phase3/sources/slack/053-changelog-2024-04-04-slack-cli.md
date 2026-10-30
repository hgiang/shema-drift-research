---
title: "Release: Slack CLI v2.21.0"
summary: "Version 2.21.0 of the developer tools for the Slack automations platform has sprung!"
url: "https://docs.slack.dev/changelog/2024/04/04/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2024/04/04/slack-cli

# Release: Slack CLI v2.21.0

April 4, 2024

Version `2.21.0` of the developer tools for the Slack automations platform has sprung!

*   You can now display runtime versions for your application's execution environment using the `doctor` hook. To enjoy the improved `slack doctor` command experience, existing Deno Slack SDK-based apps must have their `deno-slack-hooks` dependency upgraded to the latest version (`v1.3.0`).
*   By relying only on the `get-manifest` hook when attempting to get a manifest rather than checking for a `slack.yaml` file, we now surface any errors that are returned when getting the manifest.
*   We removed the possibility of an error when generating the message boundary hook protocol, and now preserve spacing in logged outputs.
*   We corrected a few typos behind the scenes.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
