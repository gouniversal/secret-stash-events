from typing import Any, Dict, Union
from json import dumps as json_dumps
from dataclasses import dataclass


@dataclass
class EventClass:
    version_id: str
    timestamp: str = None
    visitor_id: str = None

    @property
    def event_id(self) -> str:
        event_version = f"{self.__class__.__name__}{self.version_id}"
        return "".join(
            ["_" + i.lower() if (i.isupper() or i.isnumeric()) else i for i in event_version]
        ).lstrip("_")

    @property
    def dataflow_bigquery_schema(self) -> str:
        dataflow_bigquery_schema_ = [
            f"{k}:{self.to_bigquery_type(value=v)}" for k, v in self.schema.items()
        ]
        return ",".join(dataflow_bigquery_schema_)

    @property
    def schema(self) -> Dict[str, Any]:
        return {k: v.__name__ for k, v in self.__annotations__.items()}

    @staticmethod
    def to_bigquery_type(value: str) -> Union[Dict[str, str], None]:
        types_ = {
            "string": "STRING",
            "str": "STRING",
        }
        return types_.get(value, None)

    def to_dict(self) -> Dict[str, Any]:
        _dict = {k: v for k, v in self.__dict__.items()}
        _dict["event_id"] = self.event_id
        return _dict

    def to_bytes(self) -> bytes:
        return json_dumps(self.to_dict()).encode('utf-8')

