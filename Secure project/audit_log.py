import logging

class AuditLog:
    def __init__(self, logfile):
        logging.basicConfig(filename=logfile, level=logging.INFO)

    def log_access(self, user, resource):
        logging.info(f"User {user} accessed {resource}")
