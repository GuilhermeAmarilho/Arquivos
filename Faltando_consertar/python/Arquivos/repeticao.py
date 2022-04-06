from time import sleep
def clear():
    try:
        import os
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 50
    print("\n" * lines)
def r(v):
    sleep(v)
    clear()