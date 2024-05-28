"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "trems"

_ = MessageFactory("trems")

logger = logging.getLogger("trems")
