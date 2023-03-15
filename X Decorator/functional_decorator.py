import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start   = time.time()
        result  = func(*args, **kwargs)
        end     = time.time()
        print(f'{func.__name__} took {int((end-start)*1000)}ms')
    return wrapper

@time_it
def function(*args, **kwargs):
    print('Launching function....')
    time.sleep(1)
    print('Function executed successfully.')
    return

if __name__ == '__main__':
    function()