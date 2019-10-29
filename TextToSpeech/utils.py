import time
from playsound import playsound

def play_audio(file_name):
    """
    Play audio file.
    :param str file_name: name of file that will be played.
    :rtype: None
    :return: void method
    """
    assert (isinstance(file_name, str))
    playsound(file_name)


def get_current_timestamp():
    """
    Returns current timestamp as str.
    :rtype: str
    :return: current timestamp (Return the current time in seconds since the Epoch)
    """
    return time.time()
