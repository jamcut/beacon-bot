# beacon-bot
Python/Aggressor scripts for generating notifications for new beacon connections in MS Teams

*Note: The message card example was based on "shellbot" by Ne0nD0g: https://github.com/Ne0nd0g/shellbot*

### Setup

Configure beacon_bot.py to have valid values for the `TEAM_SERVER_NAME` and `TEAM_HOOK` constants.

### Usage

Run `beacon-bot.cna` using the `agscript` tool in Cobalt Strike.

```./agscript <IP> <port> beacon-bot <password> beacon_bot.cna```

You should now be notified of all new beacons in your MS Teams channel.
