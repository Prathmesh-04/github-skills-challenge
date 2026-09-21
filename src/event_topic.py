class EventTopic:
    """Simple in-memory simulation of an event-streaming topic."""

    def __init__(self, name):
        self.name = name
        self.messages = []

    def publish(self, event):
        self.messages.append(event)

    def get_messages(self):
        return list(self.messages)

    def clear(self):
        # Missing from coverage because tests do not clear a topic.
        self.messages.clear()