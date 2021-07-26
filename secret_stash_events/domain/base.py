from typing import Any, Dict, Union
from json import dumps as json_dumps
from dataclasses import dataclass


@dataclass
class EventClass:

    @property
    def _event_id(self) -> str:
        return self.__class__.__name__

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
        return {k: v for k, v in self.__dict__.items()}

    def to_bytes(self) -> bytes:
        return json_dumps(self.to_dict()).encode('utf-8')

