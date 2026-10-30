---
title: "Release: Slack CLI v3.0.1"
summary: "Slack CLI v3.0.1 delivers a handful of small improvements thanks to our developer community feedback."
url: "https://docs.slack.dev/changelog/2025/03/19/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2025/03/19/slack-cli

# Release: Slack CLI v3.0.1

March 19, 2025

Slack CLI `v3.0.1` delivers a handful of small improvements thanks to our developer community feedback.

*   We've fixed the `--token` flag and it'll work when combined with the `--app` and `--team` flags.
*   We've fixed the `--app` flag to use the specified app and it'll work when combined with the `--team` flag.
*   We've disabled app manifest caching and overwrite protection for Deno Slack SDK apps that run on Slack because it's not required.
*   We've fixed a bug to support large manifest files by allowing the hooks to parse multi-line boundaries.
*   We've fixed a bug to prevent creating a new app that would overwrite an existing app for a specified team.
*   We've fixed a bug to show an app's team name and team ID, when the app's auth is missing.
*   We've fixed a bug to reset terminal text formatting after prompts, which conflicts with tools such as Python virtual environments.
*   We've improved the performance of resolving the authentication for local, dev apps by reducing the reading of your credentials file.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
