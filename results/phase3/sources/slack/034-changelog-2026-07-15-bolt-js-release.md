---
title: "Release: Bolt for JS v5"
summary: "Version 5.0.0 of Bolt for JS is here! This release follows the Node Slack SDK's shift from axios to the native Fetch API, removes the deprecated Workflow Steps from Apps feature, and raises the minimum Node.js version to 20."
url: "https://docs.slack.dev/changelog/2026/07/15/bolt-js-release"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/07/15/bolt-js-release

# Release: Bolt for JS v5

July 15, 2026

Version `5.0.0` of Bolt for JS is here! This release follows the Node Slack SDK's shift from axios to the native Fetch API, removes the deprecated Workflow Steps from Apps feature, and raises the minimum Node.js version to 20.

If your app doesn't use proxy/TLS configuration or inspect `respond()` return values, this upgrade is possibly only a version bump.

## New features {#new-features}

*   We've added a `dispatcher` option to the `SocketModeReceiver` class.
*   We've added `instanceof` operator support to error classes.

## Breaking changes {#breaking-changes}

*   We've raised the minimum Node.js version to 20.
*   We've removed the `agent` and `clientTls` options from the `AppOptions` interface.
*   We've updated the `SocketModeReceiver` class to accept a `dispatcher` option instead of proxy agents.
*   We've removed Workflow Steps from Apps.
*   We've updated the `respond()` utility function to return a native `Response` object.
*   We've upgraded the Node Slack SDK dependencies.
*   We've improved error handling throughout.

For full migration details, see the [Bolt for JS v4 to v5 migration guide](https://docs.slack.dev/tools/bolt-js/migration/migration-v5.md).

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Bolt JS](https://docs.slack.dev/changelog/tags/bolt-js.md)
