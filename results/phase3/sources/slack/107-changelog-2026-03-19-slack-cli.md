---
title: "Release: Slack CLI v3.15.0"
summary: "Version 3.15.0 of the developer tools for the Slack platform has arrived!"
url: "https://docs.slack.dev/changelog/2026/03/19/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/03/19/slack-cli

# Release: Slack CLI v3.15.0

March 19, 2026

Version `3.15.0` of the developer tools for the Slack platform has arrived!

*   The `slack create` command now normalizes project directory names to kebab-case (lowercase, dash-delimited, no whitespace or special characters). For example: `slack create "My App"` now creates a `my-app` directory instead of a `My-App` directory.
*   We've updated the the `slack create` command's app name prompt to show the randomly generated app name as placeholder text. You can press `Enter` to accept the default name, or type in a new name.
*   Bolt JavaScript and Bolt Python projects now default to using the local `manifest.json` as the app manifest (previously, it was a remote manifest from [app settings](https://api.slack.com/apps)). Changes to the app manifest via app settings will now be detected by the Slack CLI, and a prompt will be displayed before any manifest update action occurs (e.g., when using the `slack run` command). The manifest source is set after creating a new project with the `slack create` command or by initializing an existing project using the `slack init` command, and the setting is stored as `"manifest.source": "local"` in the `.slack/config.json` file.
*   We've updated the `slack app link` command to support projects that use a manifest file as the manifest source (`manifest.json`). As part of this:
    *   A warning message will not be displayed when the manifest source is local (project file).
    *   The manifest source is not changed; it now uses the project's current manifest source.
    *   The current manifest source is displayed for your reference.
    *   A tip on where to change the manifest source (`.slack/config.json`) is displayed.
*   We've also updated the app manifest overwrite warning prompt wording and appearance:
    *   It now clarifies that the app settings manifest will be overwritten by the project's app manifest file.
    *   It now displays a warning that changes were detected on the app settings manifest that are not in the project's app manifest file.
*   We fixed a bug: we now output a warning instead of an error if activating the Python virtual environment (`.venv/`) fails.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
