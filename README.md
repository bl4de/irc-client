### irc-client

Simple IRC (Internet Relay Chat) Client written in Python 2

### usage

To join any channel on Freenode, with selected username, simply run irc_client.py and put desired username as a first argument, followed by channel name (with following # or without):

```
./irc_client.py myusername channeltojoin
```

or

```
./irc_client.py myusername #channeltojoin   // actually not working :)
```

__Seems that passing channel name with following # break script, as Python treats # as the begining of the comment?__


#### References

https://en.wikipedia.org/wiki/Internet_Relay_Chat

RFC 1459 (Internet Relay Chat Protocol)

https://tools.ietf.org/html/rfc1459


RFC 2812 (Internet Relay Chat: Client Protocol):

https://tools.ietf.org/html/rfc2812


http://chi.cs.uchicago.edu/chirc/irc_examples.html

http://books.msspace.net/mirrorbooks/irchacks/059600687X/irchks-CHP-13-SECT-2.html



