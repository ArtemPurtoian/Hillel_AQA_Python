import subprocess
import sys


def my_print(string_to_print: str):
    """
    Implement your own print function. It should work on all operating systems.
    You can't use build-in print function
    """
    if sys.platform.startswith('win'):
        subprocess.run(['echo', string_to_print], shell=True)
    else:
        subprocess.run(['echo', string_to_print], shell=False)
