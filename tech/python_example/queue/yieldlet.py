# -*- coding: utf-8 -*-
from greenlet import greenlet, getcurrent
from time import sleep


class Event(object):
    def __init__(self, name):
        self.name = name
        self.listeners = set()

    def listen(self, listener):
        self.listeners.add(listener)

    def fire(self):
        for listener in self.listeners:
            listener()


class EventManager(object):
    def __init__(self):
        self.events = {}

    def register(self, name):
        self.events[name] = Event(name)

    def fire(self, name):
        self.events[name].fire()

    def await(self, event_name):
        self.events[event_name].listen(getcurrent().switch)
        getcurrent().parent.switch()

    def use(self, func):
        return greenlet(func).switch


event = EventManager()
event.register("click")


@event.use
def test(name):
    print "=" * 50
    print "%s waiting click" % name
    event.await("click")
    print "clicked !!"


test("micro-thread")
print "do many other works..."
sleep(3)  # do many other works
print "done... now trigger click event."
event.fire("click")

