from src.libs.arguments import args
from src.libs.client.imap import new_imap_client, login
from src.configuration.imap import ImapConfig
from src.libs.logger import logger
import time

def connect(user, password):
    client = new_imap_client(ImapConfig.host, ImapConfig.port)
    login(client, user, password)
    return client


def get_number_of_messages(user, password, folder):
    client = connect(user, password)
    total_message = client.select_folder(folder).get(b"EXISTS")
    return total_message


def count_mail(folder: str, messages: int=0):
    user_message_info = {}
    for user in ImapConfig.imap_users:
        email = user.get("email")
        password = user.get("password")
        total = get_number_of_messages(email, password, folder)
        after = total + messages
        user_message_info.update({email:{"total": total, "after": after}})

    while 1:
        time.sleep(1)
        result = []
        for user in ImapConfig.imap_users:
            email = user.get("email")
            password = user.get("password")
            current = get_number_of_messages(email, password, folder)
            total = user_message_info.get(email).get("total")
            after = user_message_info.get(email).get("after")
            if current == after:
                result.append(email)
        logger.info(f"DONE: {result}")
        if len(result) == len(ImapConfig.imap_users):
            break


def get_status_message(folder):
    for user in ImapConfig.imap_users:
        email = user.get("email")
        password = user.get("password")
        client = connect(email, password)
        client.select_folder(folder)
        unseen = len(client.search("UNSEEN"))
        seen = len(client.search("SEEN"))
        logger.info({
            "EMAIL": email,
            "UNSEEN ": unseen,
            "SEEN": seen
        })



if __name__ == '__main__':
    arg = args.__dict__

    count = arg.get("count")
    status = arg.get("status")

    if count:
        count_mail(folder=count[0], messages=int(count[1]))
    elif status:
        get_status_message(status)