# purge-my-msg

---
> ⚠️ **Disclaimer**: make sure the name of the group is right, otherwise you might lose important information.
---
**purge-my-msg** is a Telegram user bot, which deletes all your messages from a group.

Yes, you can "delete for everyone" even if you were kicked. No, there's no such option, at least not in official clients.

## Usage

```shell
> purge-my-msg.py "Fancy Group Name"
```

And the output, hopefully:

```sh
1337 messages deleted.
```

## Requirements

1. [Telethon](https://github.com/LonamiWebs/Telethon/) v1.17.6+. Currently in master, so:

    ```shell
    pip install https://github.com/LonamiWebs/Telethon/archive/master.zip
    ```

2. `api_id` and `api_hash` of your app, set up in `purge-my-msg.py`.

    You can get those [here](https://my.telegram.org/apps).
