---
title: "Release: Slack CLI v3.12.0"
summary: "Version 3.12.0 of the developer tools for the Slack platform has landed!"
url: "https://docs.slack.dev/changelog/2026/02/05/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/02/05/slack-cli

# Release: Slack CLI v3.12.0

February 5, 2026

Version `3.12.0` of the developer tools for the Slack platform has landed!

*   We've updated the `slack create` command to display "AI Agent app" instead of "AI app" to align with Slack's new Agent app features.
*   We've added `pyproject.toml` support to Bolt for Python projects. The `slack create` and `slack init commands` will now detect `pyproject.toml` files, add the `slack-cli-hooks<1.0.0` to the dependency section (when missing), and display instructions on how to install the dependencies. Python projects now support either or both of the `requirements.txt` and `pyproject.toml` files.
*   We've updated the `slack run` command to support file watching and live reloading for Bolt for JavaScript and Bolt for Python projects. When a file is changed, the Slack CLI will automatically restart the app development server. When the `manifest.json` file is changed, the manifest update API is called (`.slack/config.json` must have `manifest.source: "local"`).
*   We fixed a bug: we removed support for the `.slackignore` file in the project root, as this file was unused. For posterity, during the Slack CLI Beta, this allowed Deno SDK projects to ignore files during deployment, but the feature was removed before Slack CLI v1.0.0.
*   We fixed a bug: the `slack app settings` command now opens the App Settings home page ([https://api.slack.com/apps](https://api.slack.com/apps)) when the command is run outside of a project. This allows you to see your complete list of apps.
*   We fixed a bug: we now print a debug log if the manifest file was changed but not reinstalled if the `manifest.source` was set to `"remote"`.

Hooks minimum versions

You should be prompted to update both the Slack CLI and hooks together, but note the following minimum versions are required for file watching to support server restarts:

*   `v0.3.0` for Python Slack Hooks
*   `v1.3.0` for Node Slack Hooks

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
