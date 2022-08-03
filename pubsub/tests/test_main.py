from main import alarm_pubsub


def test_alarm_pubsub(raw_event_alarm_data, capsys):
    alarm_pubsub(raw_event_alarm_data)

    out, _ = capsys.readouterr()
    assert "Alarm Triggered now!" in out


def test_unalarm_pubsub(raw_event_nonalarm_data, capsys):
    alarm_pubsub(raw_event_nonalarm_data)

    out, _ = capsys.readouterr()
    assert "False alarm, ignoring..." in out
