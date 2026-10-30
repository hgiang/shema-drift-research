---
title: "Release: Slack CLI v2.11.0"
summary: "Version 2.11.0 of the developer tools for the Slack automations platform has spookily appeared!"
url: "https://docs.slack.dev/changelog/2023/10/26/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2023/10/26/slack-cli

# Release: Slack CLI v2.11.0

October 26, 2023

Version `2.11.0` of the developer tools for the Slack automations platform has spookily appeared!

*   We've updated commands requiring validation (e.g. `manifest`, `deploy`, `install`, `triggers create`, and `triggers run`) to catch errors if a connector is not installed, attempt to install any certified apps related to connectors mentioned in the manifest, and then re-validate the manifest.
*   We added new error codes for connectors to aid you in troubleshooting.
*   We added a `--file` flag to the `function distribute` command (renamed to `function access`) so that you can manage access and distributions with a configuration file instead of multiple commands.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
