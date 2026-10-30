---
title: "Release: Slack CLI v3.6.0"
summary: "Version 3.6.0 of the developer tools for the Slack platform is joining the summer fun!"
url: "https://docs.slack.dev/changelog/2025/08/14/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2025/08/14/slack-cli

# Release: Slack CLI v3.6.0

August 14, 2025

Version `3.6.0` of the developer tools for the Slack platform is joining the summer fun!

*   We added a new `runtime_not_found` error code that will appear when a hook script cannot be found because the runtime for a project wasn't found during execution.
*   We updated the `slack install` command to create and install new Bolt Framework apps that are configured to use app settings as the source of truth (i.e., remote manifest).
*   We updated the Slack CLI output to use the new tools URL at [https://docs.slack.dev/tools](https://docs.slack.dev/tools.md) instead of the previous one at [https://tools.slack.dev](https://tools.slack.dev).
*   We added a [download link](https://downloads.slack-edge.com/slack-cli/slack_cli_latest_windows_64-bit.zip) to the latest version of the Slack CLI for Windows. Manual installations for the latest are now also supported at the following links:
    *   [https://downloads.slack-edge.com/slack-cli/slack\_cli\_latest\_linux\_64-bit.tar.gz](https://downloads.slack-edge.com/slack-cli/slack_cli_latest_linux_64-bit.tar.gz)
    *   [https://downloads.slack-edge.com/slack-cli/slack\_cli\_latest\_macOS\_arm64.tar.gz](https://downloads.slack-edge.com/slack-cli/slack_cli_latest_macOS_arm64.tar.gz)
    *   [https://downloads.slack-edge.com/slack-cli/slack\_cli\_latest\_macOS\_amd64.tar.gz](https://downloads.slack-edge.com/slack-cli/slack_cli_latest_macOS_amd64.tar.gz)
    *   [https://downloads.slack-edge.com/slack-cli/slack\_cli\_latest\_macOS\_64-bit.tar.gz](https://downloads.slack-edge.com/slack-cli/slack_cli_latest_macOS_64-bit.tar.gz)
    *   [https://downloads.slack-edge.com/slack-cli/slack\_cli\_latest\_windows\_64-bit.zip](https://downloads.slack-edge.com/slack-cli/slack_cli_latest_windows_64-bit.zip)
*   We fixed a bug: we now allow new projects to be created more quickly by using a HTTP HEAD request to check whether the template URL exists.
*   We fixed a bug: we now order the outputs of authentication details from the `slack doctor` command according to an alphabetized list of team domains.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
