from imapclient import IMAPClient
from src.libs.logger import logger


def new_imap_client(host, port=143, ssl=False):
    """Connect to imap server.

    Return imapclient instance or None if any exception occurs

    """
    try:
        client = IMAPClient(host, port=port, ssl=ssl)
        if not ssl:
            client.starttls()
        return client
    except Exception as e:
        logger.error(
            "Failed to connect to imap server: %s:%s, reason: %r",
            host,
            port,
            e,
        )


def login(client, username, password):
    """Login client using username and password

    client is IMAPClient instance

    """
    try:
        client.login(username, password)
        return True
    except Exception as e:
        logger.error("Could not login: %r", e)
        return False