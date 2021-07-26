from secret_stash_events.domain.base import EventClass
from dataclasses import dataclass


@dataclass
class PageView(EventClass):
    event_id: str = None
    event_version_id: str = "01"
    ip_address: str = None
    path: str = None
    session_id: str = None
    timestamp: str = None
    user_agent: str = None
    visitor_id: str = None

    def __post_init__(self):
        self.event_id = self._event_id
