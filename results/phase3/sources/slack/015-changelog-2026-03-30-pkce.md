---
title: "PKCE is now generally available!"
summary: "We are excited to announce support for Proof Key for Code Exchange (PKCE). PKCE is an OAuth security extension that enables developers to build more secure Slack applications on public clients, such as desktop apps and mobile apps, without the need to embed a vulnerable client_secret."
url: "https://docs.slack.dev/changelog/2026/03/30/pkce"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/03/30/pkce

# PKCE is now generally available!

March 30, 2026

We are excited to announce support for Proof Key for Code Exchange (PKCE). PKCE is an OAuth security extension that enables developers to build more secure Slack applications on public clients, such as desktop apps and mobile apps, without the need to embed a vulnerable `client_secret`.

Previously available in early access by request only, PKCE can now be enabled directly in your app settings without contacting Slack support.

### Key things to know {#key-things-to-know}

*   Enabling PKCE marks your app as a public client. This is a one-way operation; it cannot be undone without contacting Slack support.
*   OAuth installations which redirect to a custom URI scheme (e.g. `myApp://auth`) will always receive [rotating tokens](https://docs.slack.dev/authentication/using-token-rotation.md), even if token rotation is turned off. OAuth installations issued to a standard web URL (e.g. `myWebshite.com/auth`) will only receive rotating tokens if the 'token rotation' setting is enabled. All refresh tokens issued to PKCE-enabled apps expire after 30 days.
*   Once enabled, PKCE arguments (`code_challenge`, `code_challenge_method`, `code_verifier`) are optional for standard OAuth flows, but required when redirecting to a custom URI scheme.
*   Desktop redirects (custom URI schemes and `localhost` redirects for PKCE-enabled apps) cannot request bot scopes.

### Getting started {#getting-started}

Check out the [PKCE documentation](https://docs.slack.dev/authentication/using-pkce.md) to learn how to implement the full PKCE flow, including how to generate a `code_verifier`, construct the authorization URL, and exchange the code using the [`oauth.v2.access`](https://docs.slack.dev/reference/methods/oauth.v2.access.md) API method without a client secret.

**Tags:**

*   [New Feature](https://docs.slack.dev/changelog/tags/new-feature.md)
*   [Announcement](https://docs.slack.dev/changelog/tags/announcement.md)
