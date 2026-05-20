#!/usr/bin/env python3
"""
Observer pattern - Adding a new subscriber
"""
from typing import Callable, Dict, Protocol, Set


class Observer(Protocol):
    def update(self, topic: str, data: str) -> None:
        ...


class NewsSubject:
    def __init__(self):
        self._observers: Dict[Observer, Set[str] | None] = {}

    def subscribe(self, observer: Observer, topics: Set[str] | None = None) -> None:
        self._observers[observer] = topics

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self._observers:
            del self._observers[observer]

    def notify(self, topic: str, data: str) -> None:
        for observer, topics in list(self._observers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    def update(self, topic: str, data: str) -> None:
        print(f"log:{topic}={data}")


class EmailObserver:
    def update(self, topic: str, data: str) -> None:
        print(f"email:{topic}={data}")


class SmsObserver:
    def update(self, topic: str, data: str) -> None:
        print(f"sms:{topic}={data}")


def main():
    subject = NewsSubject()
    
    log_obs = LogObserver()
    email_obs = EmailObserver()
    sms_obs = SmsObserver()

    subject.subscribe(log_obs, {"sports", "breaking"})
    subject.subscribe(email_obs)
    subject.subscribe(sms_obs, {"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
