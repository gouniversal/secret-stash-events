from secret_stash_events import __version__
import pytest
from secret_stash_events.domain import model


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.parametrize("class_name, field_name, expected_value",
    [
        ("PageView", "event_id", "page_view_0_1"),
    ]
)
def test_model_event_id(class_name, field_name, expected_value):
    EventClass = getattr(model, class_name)
    event_class = EventClass()
    assert getattr(event_class, field_name) == expected_value


@pytest.mark.parametrize("class_name, field_name, expected_value",
    [
        ("PageView", "schema", {'version_id': 'str', 'session_id': 'str', 'user_agent': 'str', 'path': 'str', 'ip_address': 'str',}),
    ]
)
def test_model_schema(class_name, field_name, expected_value):
    EventClass = getattr(model, class_name)
    event_class = EventClass()
    assert getattr(event_class, field_name) == expected_value


@pytest.mark.parametrize("class_name, field_name, expected_value",
    [
        ("PageView", "dataflow_bigquery_schema",
         'version_id:STRING,session_id:STRING,user_agent:STRING,path:STRING,ip_address:STRING'),
    ]
)
def test_model_dataflow_bigquery_schema(class_name, field_name, expected_value):
    EventClass = getattr(model, class_name)
    event_class = EventClass()
    assert getattr(event_class, field_name) == expected_value


@pytest.mark.parametrize("class_name, input_type, expected_type",
    [
        ("PageView", "string", "STRING"),
        ("PageView", "str", "STRING"),
        ]
)
def test_model_to_bigquery_type(class_name: str, input_type: str, expected_type: str):
    EventClass = getattr(model, class_name)
    event_class = EventClass()
    assert event_class.to_bigquery_type(input_type) == expected_type


@pytest.mark.parametrize("class_name, version_id, expected_event_id",
    [
        ("PageView", "01", "page_view_0_1"),
        ("PageView", "10", "page_view_1_0"),
        ]
)
def test_event_id(class_name, version_id, expected_event_id):
    EventClass = getattr(model, class_name)
    event_class = EventClass(version_id=version_id)
    assert event_class.event_id == expected_event_id
