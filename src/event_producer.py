from event_topic import EventTopic


class EventProducer:
    """Publishes anomaly events to an in-memory topic."""

    def __init__(self, topic: EventTopic):
        self.topic = topic

    def publish(self, event):
        # Missing from coverage because tests only publish non-empty events.
        if not event:
            return False

        self.topic.publish(event)
        return True