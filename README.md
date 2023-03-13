Python-JabberBot
===
A framework for writing IM/chat robots for the Jabber / XMPP protocol.

This is a fork of [python-jabberbot](http://thp.io/2007/python-jabberbot/) to python 3

## TODO
1. fix acceptownmsgs
    - based on bareJID/fullJID
    - based on Nickname in MUC

2. Admin-only-commands

3. React on MUC-invitations
- Parameter in constructor (invitable=False)

4. Respect MUC statuscodes

5. Behavior of prefix
- Different behavior for direct/groupchat messages
    - no prefix for direct messages
- (none/default-prefix) in constructor / muc-specific-prefix (in muc_join_room)

6. React on error-stanzas
- Nickname already chosen
- Kick/Ban/Invite/etc. not allowed

7. Clean up code
- sort functions related to XEPs

8. Using transports
- icq msn irc

9. Documentation
- First steps
- PyDocs

## Authors
Thomas Perl <m@thp.io>  
John Martinez <jvm@axiometric.com>  
Dan Sanders <dan@ified.ca>  
Pat Notz <patnotz@gmail.com>  
Justin Forest <justin.forest@gmail.com>  
Hernan Grecco <hernan.grecco@gmail.com>  
Arthur Furlan <afurlan@afurlan.org>  
Andrew Williams <andy@tensixtyone.com>  
Josh Aune <luken@omner.org>  
Malte Kuhn <git@monkz.de>  
Matthew Kemp <mattkemp@gmail.com>  
David O'Rourke <david.orourke@gmail.com>  
René Mayrhofer <rene@mayrhofer.eu.org>  
Andreas Zwinkau <beza1e1@web.de>  
Fabian Deutsch <fabian.deutsch@gmx.de>  
Richard Marko <rissko@gmail.com>  
Tomasz Woźniak <tomlee@szluug.org>  
Josh Panter <joshu@unfettered.net>  
