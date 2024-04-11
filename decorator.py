#  Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. 

def shout(func):
    def speakToShout(sent):
        func(sent.upper())
    return speakToShout

def calculateTime(func):
    def func_with_time(*args, **kwargs):
        import time
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Time taken :", end - begin)
    return func_with_time

# Using decorators

@calculateTime
@shout
def speak(sent):
    print(sent)

speak("Hello")
