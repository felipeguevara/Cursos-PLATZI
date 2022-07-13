import time

class FiboIter():
    
    def __init__(self, max_number: int = None):
        self.max = max_number

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
        
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        
        elif self.counter ==1:
            self.counter += 1
            return self.n2
        
        else:
            self.aux = self.n1 + self.n2
            self.counter += 1
            self.n1, self.n2 = self.n2, self.aux
        
            if not self.max:
                return self.aux
            if self.max:
                if self.counter > self.max:
                    raise StopIteration
                else:
                    return self.aux

if __name__ == '__main__':
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(.05)