import base64


def alarm_pubsub(event: dict):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
    """
    message = base64.b64decode(event['data']).decode('utf-8')

    if message != "ALARM":
        print("False alarm, ignoring...")
        return

    print("Alarm Triggered now!")
