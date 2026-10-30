---
title: "Optional scopes have landed"
summary: "You can now mark individual OAuth scopes as optional when configuring your Slack app! Optional scopes give users more control over what data your app can access during installation, without blocking them from installing your app entirely."
url: "https://docs.slack.dev/changelog/2026/03/16/optional-scopes"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/03/16/optional-scopes

# Optional scopes have landed

March 16, 2026

You can now mark individual OAuth scopes as optional when configuring your Slack app! Optional scopes give users more control over what data your app can access during installation, without blocking them from installing your app entirely.

What's changed:

*   **App configuration**: Mark scopes as optional directly from the [app settings](https://api.slack.com/apps) page or via your app manifest using the new `bot_optional` and `user_optional` fields.
*   **OAuth flow**: Users now see optional scopes presented separately during installation and can choose which ones to grant.
*   **Admin controls**: Workspace admins can pre-approve which optional scopes are available to their users when approving apps.
*   **App manifest**: Two new fields—`bot_optional` and `user_optional`—are now supported under `oauth_config.scopes`. See [App manifest](https://docs.slack.dev/reference/app-manifest.md#oauth) fields for details.

If your app uses scopes that aren't strictly required for core functionality, consider marking them as optional to improve installation rates. Read more on the [Installing with OAuth](https://docs.slack.dev/authentication/installing-with-oauth.md#optional-scopes) page.

**Tags:**

*   [Announcement](https://docs.slack.dev/changelog/tags/announcement.md)
*   [New Feature](https://docs.slack.dev/changelog/tags/new-feature.md)
