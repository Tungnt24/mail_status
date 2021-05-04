from src.configuration import config


class ImapConfig:
    host = config.get("IMAP_HOST", "")
    port = config.get("IMAP_PORT", 143)
    ssl = config.get("IMAP_SSL", False)
    imap_users = config.get("IMAP_USERS", [])
