---
title: "Release: Slack CLI v3.0.0"
summary: "Version 3.0.0 of the developer tools for the Slack automations platform is here, with lots of goodies for you!"
url: "https://docs.slack.dev/changelog/2025/02/27/slack-cli-release"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2025/02/27/slack-cli-release

# Release: Slack CLI v3.0.0

February 27, 2025

Version `3.0.0` of the developer tools for the Slack automations platform is here, with lots of goodies for you!

*   We renamed the `slack.json` file to `.slack/hooks.json`, and continue to support `slack.json` for existing projects. There is now a warning shown in `--verbose` output to encourage projects to migrate their `slack.json` to `.slack/hooks.json.`
*   We've removed the `invalid_app_directory` error from any commands run in nested project directories, and now search for the required `slack.json` file in the project's configuration. We also now also check for this file at `.slack/hooks.json`.
*   We now cache the last known manifest export; the cache is used to avoid overwriting changes on app settings. If the manifest is changed on app settings since the last update, a confirmation prompt will appear before making another update via the Slack CLI.
*   We've moved the top-level commands you know and love, `slack create` and `slack samples`, to be sub-commands of the `slack project` command (they remain aliased as top-level commands though, so there is no change to the user experience).
*   We've updated the `slack doctor` command to display the `manifest.source` value, which will be either `local` or `remote`.
*   We now officially support Bolt for JavaScript and Bolt for Python in the Slack CLI! 🎉
*   As such, we've updated the `slack create` command with a new create journey that allows you to choose between different types of apps for Bolt for JavaScript, Bolt for Python, and Deno.
*   We've also added the `slack init` command, which will initialize an existing Bolt for JavaScript, Bolt for Python, or Deno project with Slack CLI support.
*   We fixed a bug to avoid confusion with regular outputs, and now prefix all separate debug logs with a timestamp.
*   We fixed a bug to avoid spinning the spinner when outputting with debug logs, or if styles are removed with the `--no-color` flag.
*   We fixed a bug to now display uninstalled apps in selections when using the `slack collaborators` and `slack manifest` commands.
*   We fixed a bug with confirming trusted templates that are from a Slack GitHub organization.
*   We fixed a bug regarding writing console outputs to activity logs during local runs.
*   We fixed a bug where the Slack CLI would get stuck if one of the goroutines of the `slack run` command encountered an error; we now exit the `slack run` command if this happens.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
