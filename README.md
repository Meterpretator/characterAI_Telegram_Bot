# characterAI_Telegram_Bot
Simple telegram bot for Character.AI using an unofficial API for Character AI for Python (https://github.com/kramcat/CharacterAI)
# Installation
```shell
pip install -r requirements.txt
```
# Configure
In `config.py` change variables:

| PARAMETR      | DESCRIPTION                                                                                                                                   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `TOKEN_VALUE` | 1. Open DevTools in your browser (I used Firefox)<br/>2. Go to Storage -> Local Storage -> char_token<br/>3. Copy `value`                       |
| `CHAR_TOKEN`  | Character token from URL<br/>(e.g. https://beta.character.ai/chat?source=recent-chats&char=XXXXXXXXXXX where `XXXXXXXXXXX` is Character token |
| `BOT_TOKEN`   | Your telegram bot token                                                                                                                       |

# Engage
`python main.py`
