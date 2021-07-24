from secret_stash_events.domain.base import EventClass
from dataclasses import dataclass


@dataclass
class PageView(EventClass):

    ip_address: str = None
    path: str = None
    session_id: str = None
    user_agent: str = None
    version_id: str = "01"
