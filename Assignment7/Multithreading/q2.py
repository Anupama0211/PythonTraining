"""
2.	For below given functions, create a normal thread for function ‘non_deamon’ and create a daemon thread for function ‘test_daemon’.
"""
import time
from threading import Thread


def non_daemon():
    print('Starting non daemon')
    print('Exiting non daemon')


def daemon_test():
    print('Starting deamon')
    time.sleep(5)
    print('Exiting deamon')


daemon_thread = Thread(target=daemon_test, daemon=True)
non_daemon_thread = Thread(target=non_daemon)
daemon_thread.start()
non_daemon_thread.start()
