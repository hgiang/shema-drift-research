---
title: "Introducing Work Objects"
summary: "As you may have spied in the Slack CLI v3.9.0 release yesterday, support for Work Objects is now generally available! 🎉"
url: "https://docs.slack.dev/changelog/2025/10/22/work-objects"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2025/10/22/work-objects

# Introducing Work Objects

October 22, 2025

As you may have spied in the [Slack CLI v3.9.0 release](https://docs.slack.dev/changelog/2025/10/21/slack-cli.md) yesterday, support for Work Objects is now generally available! 🎉

[Work Objects](https://docs.slack.dev/messaging/work-objects-overview.md) allow you to represent and collaborate on data from third-party services where the work is already happening, right in Slack. They have two primary components: an [unfurl component](https://docs.slack.dev/messaging/work-objects-overview.md#unfurl), and a [flexpane component](https://docs.slack.dev/messaging/work-objects-overview.md#flexpane).

We've also introduced a new [`entity_details_requested`](https://docs.slack.dev/reference/events/entity_details_requested.md) event and the [`entity.presentDetails`](https://docs.slack.dev/reference/methods/entity.presentdetails.md) API method, and have added support for Work Objects to the [`chat.unfurl`](https://docs.slack.dev/reference/methods/chat.unfurl.md) API method. SDK support for these API updates is coming soon.

To learn how it all comes together to create a seamless experience for your users, check out the [full documentation](https://docs.slack.dev/messaging/work-objects-overview.md)!

**Tags:**

*   [Announcement](https://docs.slack.dev/changelog/tags/announcement.md)
*   [New Feature](https://docs.slack.dev/changelog/tags/new-feature.md)
