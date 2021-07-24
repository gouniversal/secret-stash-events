from secret_stash_events.domain.base import EventClass
from dataclasses import dataclass


@dataclass
class PageView(EventClass):
    version_id: str = "01"
    session_id: str = None
    user_agent: str = None
    path: str = None
    ip_address: str = None
