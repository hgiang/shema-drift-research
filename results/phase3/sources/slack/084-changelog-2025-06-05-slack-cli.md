---
title: "Release: Slack CLI v3.3.0"
summary: "Version 3.3.0 of the developer tools for the Slack platform has arrived!"
url: "https://docs.slack.dev/changelog/2025/06/05/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2025/06/05/slack-cli

# Release: Slack CLI v3.3.0

June 5, 2025

Version `3.3.0` of the developer tools for the Slack platform has arrived!

*   We've added native support for Apple silicon; the install script will use the matching `arm64` build for developers upgrading.
*   We fixed a bug when creating a project using a git repo template. Previously, if the template included `.git` within the URL, the template would fail to be cloned (for example, when running the `slack create --template https://github.com/slack-samples/example.git.project.git` command).
*   We fixed a bug: setting the `source` using the flag for the `slack manifest info` command now takes precedence to project configurations, which are used to determine the default source.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
