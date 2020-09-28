class RingBuffer:
    def __init__(self, capacity):
        #implements an empty starting buffer
        self.capacity = capacity
        self.buffer = []
        self.current = 0

    def append(self, item):
        #check to see if the buffer has items already if not just add the item
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        # if the buffer is full overwrite the oldest one
        elif len(self.buffer) == self.capacity:
            self.buffer[self.current]= item
            self.current = (self.current + 1) % self.capacity

    def get(self):
        # if the buffer is not empty return a list of elements
        if self.buffer is not None:
            # must be sliced this way in order to pass the test
            return self.buffer[:self.current]+self.buffer[self.current:]
            #should be written this way but the test wants the last added element at the front
            #return self.buffer[self.current:]+self.buffer[:self.current]