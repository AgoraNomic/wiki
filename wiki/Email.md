# General

* Double-check you're sending to the correct list
* Add an empty space between quoted content and your response, to make it easier to read

# Gmail

The gmail webclient is not friendly to Agora. Please consider composing and reading emails on a desktop client.

## Filtering

[Gmail's filters](https://support.google.com/mail/answer/6579?hl=en) should be configured to ensure no emails go to spam.

The following filter will capture ALL agora emails:

    list:(agora-business.agoranomic.org) OR list:(agora-discussion.agoranomic.org) OR list:(agora-official.agoranomic.org) OR list(agora@listserver.tue.nl)
    
Apply this filter and mark 'never send to spam'. You can also apply a label and skip inbox if you want all Agora emails to go to a different folder.

If you're fulfilling an office it can be useful to create filters to find emails related to it. Here's an example filter to catch votes:

    (list:(agora-business.agoranomic.org OR list:(agora-business.agoranomic.org)) AND (assessor OR promotor OR for OR against OR present OR endorse)
    
