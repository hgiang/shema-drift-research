---
title: "Rate limit changes for non-Marketplace apps"
summary: "You can view this page in Japanese: 非 Marketplace アプリのレート制限の変更."
url: "https://docs.slack.dev/changelog/2025/05/29/rate-limit-changes-for-non-marketplace-apps"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2025/05/29/rate-limit-changes-for-non-marketplace-apps

# Rate limit changes for non-Marketplace apps

May 29, 2025

_This page has been updated to clarify the rate limits for existing internal customer-built apps._

Japanese version available / 日本語版

You can view this page in Japanese: [非 Marketplace アプリのレート制限の変更](https://docs.slack.dev/ja-jp/2025-05-terms-rate-limit-update-and-faq.md).

We're updating the rate limits for the `conversations.history` and `conversations.replies` Web API methods methods for non-Marketplace apps. This rate limit reduction will apply only to applications that are commercially distributed outside of the Marketplace (also called “unlisted” apps). It will immediately impact affect new unlisted applications and new installations of existing unlisted non-Marketplace applications. The new rate limits will be updated to allow 1 request per minute and will return a maximum of 15 objects per request.

The new rate limits will not be applied to existing installations of unlisted, distributed applications published outside the Marketplace.

Slack is updating the [Slack API Terms of Service](https://slack.com/terms-of-service/api). The updated terms are effective immediately for applications created on or after May 29, 2025. They will go into effect on June 30, 2025 for apps created before May 29, 2025.

In addition, Slack is updating the rate limits for the [`conversations.history`](https://docs.slack.dev/reference/methods/conversations.history.md) and [`conversations.replies`](https://docs.slack.dev/reference/methods/conversations.replies.md) API methods. This change will not impact Marketplace apps. New non-Marketplace applications and new installations of existing non-Marketplace applications will be subject to the updated rate limits immediately, as of May 29, 2025.

Existing installations of apps distributed outside the Marketplace (excluding internal customer-built apps) will not be impacted.

## What's changing? {#what}

The rate limits for both the [`conversations.history`](https://docs.slack.dev/reference/methods/conversations.history.md) and [`conversations.replies`](https://docs.slack.dev/reference/methods/conversations.replies.md) API methods are changing from `Tier 3` to `Tier 1` for commercially distributed apps that are not approved for the Slack Marketplace:

*   [`conversations.history`](https://docs.slack.dev/reference/methods/conversations.history.md) - The `conversations.history` API method rate limit for commercially distributed apps created after **May 29, 2025**, and for net new installations of existing apps, will be limited to 1 request per minute, unless they are approved for the Slack Marketplace. The maximum and default for the `limit` parameter has been reduced to 15 objects.
    
*   [`conversations.replies`](https://docs.slack.dev/reference/methods/conversations.replies.md) - The `conversations.replies` API method rate limit for commercially distributed apps created after **May 29, 2025**, and for net new installations of existing apps, will be limited to 1 request per minute, unless they are approved for the Slack Marketplace. The maximum and default for the `limit` parameter has been reduced to 15 objects.
    

Internal customer-built applications are not impacted by these changes. For Custom apps, the [`conversations.history`](https://docs.slack.dev/reference/methods/conversations.history.md) and [`conversations.replies`](https://docs.slack.dev/reference/methods/conversations.replies.md) API methods are limited to 50+ requests per minute. The maximum and default values for the limit parameter are 1,000 objects.

[Read on](#faq) for more answers to the questions you have. And of course, let us know if you have any additional questions, concerns, or suggestions about these changes. Thank you!

## Frequently asked questions {#faq}

### What changes are being made to the API Terms of Service? {#what-tos}

You can read the full terms [here](https://slack.com/terms-of-service/api) but below is a summary of what's changing:

**Commercial Distribution**: The updated terms confirm that the [Slack Marketplace](https://slack.com/marketplace) is the only appropriate channel for commercially distributing apps built with Slack APIs, whether those apps are "unlisted" (published outside of the Marketplace) or provide a customer instructions for a templated custom app that connects to your product.

**Data Usage**: We’re reinforcing safeguards around how third-party applications can store, use, and share data accessed via Slack APIs.

**API-Specific Terms**: We're providing clearer guidance on how to use certain APIs, such as the Discovery API and the Real-time Search API, responsibly.

### What changes are being made to the Slack APIs? {#what-api}

The majority of developers will not see any changes to Slack APIs. We're making targeted rate limit changes to two specific [Web API](https://docs.slack.dev/apis/web-api.md) methods: the [`conversations.history`](https://docs.slack.dev/reference/methods/conversations.history.md) and [`conversations.replies`](https://docs.slack.dev/reference/methods/conversations.replies.md) methods, _only_ for apps distributed outside of the [Slack App Marketplace](https://my.slack.com/marketplace). These methods are designed to facilitate an app reading a comment or a thread, but in the hands of unvetted applications have the potential to exfiltrate large amounts of sensitive conversational data. To help keep workspace data secure and prevent bulk data exfiltration by unvetted applications, these methods will have a new rate limit of 15 messages per request at one request per minute. Marketplace apps will not see a rate limit change. Internal customer-built apps will not notice any changes.

We're also announcing new, off-platform capabilities for our Real-time Search API, currently available to select partners.

### Why are you making these changes? {#why}

As AI systems become more powerful, so do the risks associated with how customer data is accessed and used. Slack is strengthening and clarifying our policies so we can better safeguard customers and support innovation while preventing unsanctioned data scraping and abuse.

As noted in the [Slack Developer Policy](https://docs.slack.dev/developer-policy.md), the Slack Marketplace has always been the intended home for secure, high-quality apps. Slack does not charge for Marketplace inclusion, so it is open to developers who meet [Marketplace guidelines](https://docs.slack.dev/slack-marketplace/slack-marketplace-app-guidelines-and-requirements.md) and submit for review. While Slack does not certify or endorse apps, before an app can be published on the Marketplace, we perform a security review and analyze the scopes that an application requests in light of its functionality. This process bolsters customer confidence in their tools and helps ensure the security of the Slack ecosystem. Unlisted apps, by contrast, are for development and testing—not large-scale or commercial distribution. With these updates to the API Terms of Service, we're now making that distinction even clearer.

Along with these policy changes, we are implementing targeted rate limits to two conversations methods to focus on the applications that may be putting customer data most at risk—unvetted applications potentially pulling large amounts of customer data.

Finally, we recognize that customers and developers are eager to _safely_ capitalize on the valuable business knowledge stored in Slack conversations. We're announcing new, off-platform capabilities in our Real-time Search API that will unlock possibilities for Marketplace applications to facilitate exciting new AI use cases.

### Will my Marketplace app be impacted? {#marketplace-impacts}

These terms updates apply to all development with Slack APIs, but Marketplace apps that abide by the [Slack Marketplace guidelines](https://docs.slack.dev/slack-marketplace/slack-marketplace-app-guidelines-and-requirements.md) should not see any changes.

### Will my non-Marketplace app be impacted? {#non-marketplace-impacts}

While these terms changes apply to all development using Slack APIs, the majority of developers will not notice any changes for the time being.

If you don't call the [`conversations.history`](https://docs.slack.dev/reference/methods/conversations.history.md) or [`conversations.replies`](https://docs.slack.dev/reference/methods/conversations.replies.md) Web API methods, you will likely not see any rate limit changes for the time being. But the Marketplace is ultimately the right destination for all commercially distributed apps, so if you commercially distribute your application, you should explore the [listing process](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide.md) and review the [Slack Marketplace guidelines](https://docs.slack.dev/slack-marketplace/slack-marketplace-app-guidelines-and-requirements.md) to understand how to make your app suitable for the Marketplace.

Developers who are affected by rate limit changes or enforcement will receive notice with more detailed information about how their app is affected and what to do next. Most notably, starting today, new installs of non-Marketplace commercially distributed apps will see lower rate limits for the [`conversations.history`](https://docs.slack.dev/reference/methods/conversations.history.md) and the [`conversations.replies`](https://docs.slack.dev/reference/methods/conversations.replies.md) Web API methods. To help keep workspace data secure and prevent bulk data exfiltration by unvetted applications, these methods will have a new rate limit of 15 messages per request at one request per minute. Internal customer-built applications are not impacted by these changes and continue to have a rate limit of 1,000 messages per request at 50+ requests per minute.

### Will my internal app be impacted? {#internal}

No, internal customer-built apps are not impacted and retain their current, higher rate limits. The new rate limits only apply to commercially distributed applications outside the Marketplace.

### What is the Real-time Search API and how can it help me access channel data after these changes? {#real-time-search-api}

While we understand customers and developers want to enhance their applications with data from Slack, bulk downloads of customers' conversational data for indexing and querying pose risks of exposing sensitive information and undermining Slack access controls, such as private channel membership.

Our Real-time Search API helps meet this need, giving you a better, safer way to access Slack channel data after these changes. It allows for real-time querying of Slack data without storing it, allowing customers and developers to take advantage of the wealth of knowledge in Slack with a more targeted approach that doesn't necessitate storing sensitive conversational data. It's currently in a limited beta with select partners. Stay tuned for announcements on the general availability of this API.

### How can I update my app to meet Marketplace requirements? {#meet-marketplace-requirements}

Please review the [Marketplace guidelines](https://docs.slack.dev/slack-marketplace/slack-marketplace-app-guidelines-and-requirements.md) for a detailed look at the types of applications suitable for the Marketplace and guidance on how best to use methods and scopes for your use cases.

Note the Real-time Search API, which facilitates real-time search and data access, may unlock use cases that previously would not have been approved for the Marketplace.

### How can I update my app to avoid rate limit errors? {#avoid-errors}

If you see an increase in rate limit errors, please refer to our [guide](https://docs.slack.dev/apis/web-api/rate-limits.md) on how to respond to rate limit conditions. Most apps do not need the ability to read the full content of a channel, so if you're running into rate limit errors, consider the other ways the platform may provide to get the kind of focused, contextual information an app typically requires, such as the [Events API](https://docs.slack.dev/apis/events-api.md) or the forthcoming Real-time Search API.

### What if I do nothing? {#nothing}

Most apps are unaffected by these changes. Apps already using the [`conversations.history`](https://docs.slack.dev/reference/methods/conversations.history.md) and [`conversations.replies`](https://docs.slack.dev/reference/methods/conversations.replies.md) Web API methods will continue to function, but new installations may encounter additional rate limit errors unless they are approved for the Slack Marketplace. These rate limits will not impact existing installations of these apps. Any new apps created and commercially distributed you create may encounter additional rate limit errors unless they are submitted to the Slack Marketplace.

**Tags:**

*   [Announcement](https://docs.slack.dev/changelog/tags/announcement.md)
