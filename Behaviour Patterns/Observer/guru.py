from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    """
    Subject interface: methods to manage subscribers.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notifiy(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    Subject owns:
        - state (important to all subscribers)
        - notifies a list of observers when state changes
    """

    _state: int = None
    """
    Subjects state - imperative to observers.
    """

    _observers: List[Observer] = []
    """
    List of subscribers, in real life this would be more complex.
    """

    def attach(self, observer: Observer) -> None:
        print('Observer ATTACHED.')
        self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Subscripton management methods.
    """
    def notifiy(self) -> None:
        # Notify all observers about an event.
        print('Subject: Notifying observers...')
        for observer in self._observers:
            observer.update(self)
        
    def business_logic(self) -> None:
        print('Subject: I\'m doing something important.')
        self._state = randrange(0,10)
        print(f'Subject new state: {self._state}')
        self.notifiy()
        

class Observer(ABC):
    """
    The Oberserver interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        # Receive update from subject.
        pass


"""
Concrete observers: react to the updates issued by the Subject (if attached).
"""

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print('ConcreteObserver AAA: Reacted to the event.')

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print('ConcreteObserver BBB: Reacted to the event.')

if __name__ == '__main__':
    # The client code.
    subject     = ConcreteSubject()
    observer_a  = ConcreteObserverA()
    observer_b  = ConcreteObserverB()
    subject.attach(observer_a)
    subject.attach(observer_b)
    subject.business_logic()
    subject.business_logic()
    subject.detach(observer_a)
    subject.business_logic()
