class ChangeQueueItem(object):
    def __init__(self, type_of_change="", relative_path=""):
        self.type_of_change = type_of_change
        self.relative_path = relative_path


class ChangeQueue(object):
    queue = []

    def pushChange(self, type_of_change, relative_path):
        self.queue.append(ChangeQueueItem(type_of_change, relative_path))
        return self

    def popChange(self):
        return self.queue.pop(0)

    def hasChange(self):
        return len(self.queue) > 0
