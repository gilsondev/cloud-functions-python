import base64
import pytest


@pytest.fixture
def raw_event_alarm_data():
    message = b"ALARM"
    return {"data": base64.b64encode(message)}


@pytest.fixture
def raw_event_nonalarm_data():
    message = b"NONALARM"
    return {"data": base64.b64encode(message)}
