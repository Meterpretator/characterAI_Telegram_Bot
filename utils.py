from characterai import PyCAI
import config


def char_response(prompt):
    client = PyCAI(config.TOKEN_VALUE) #Token: Copy value
    char = config.CHAR_TOKEN #Character ID, found in the url of the character
    chat = client.chat.get_chat(char)
    participants = chat['participants']

    if not participants[0]['is_human']:
        tgt = participants[0]['user']['username']
    else:
        tgt = participants[1]['user']['username']

    message = prompt
    data = client.chat.send_message(
        chat['external_id'], tgt, message
    )
    name = data['src_char']['participant']['name']
    text = data['replies'][0]['text']
    return text
