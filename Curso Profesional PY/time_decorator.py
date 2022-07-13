from datetime import datetime
import numpy as np

def execution_time(func):
    def run_function(*args, **kwargs): #run_function(lista) #multiples args & multiples key words args
        now = datetime.now()
        func(*args, **kwargs) #func(lista) #multiples args & multiples key words args
        end = datetime.now()
        total_time = end-now
        print(f'the total time was: {total_time.total_seconds()}')
        #return now-end
    return run_function

@execution_time
def suma(lista: list) -> int:
    total = 0
    for i in lista:
        total += i
    return total

if __name__ == "__main__":
    print(suma([*range(10, 10000000, 1)]))
        