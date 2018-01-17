# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from priqueues.heap_priority_queue import HeapPriorityQueue
import time
import threading
import re
import signal
import logging

LOG_FILENAME = 'scheduler.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

IDLE_TASK_PRIORITY = 20

class CommandHandler(threading.Thread):
    """ The thread for parsing the commmands."""

    def __init__(self, priority_queue, lock):
        threading.Thread.__init__(self)
        self.shutdown_flag = threading.Event()
        self._pq = priority_queue
        self._lock = lock

    def run(self):
        while not self.shutdown_flag.is_set():
            cmd = raw_input('Enter job adding cmd: ')
            # cmd example: add job hello with length 3 and priority 2
            if 'add job' in cmd:
                mo = re.search(
                    "add job (\w*) with length (\d*) and priority (-*\d*)", cmd)
                name = mo.group(1)
                tlen = mo.group(2)
                prt = mo.group(3)
                try:
                    tlen = int(tlen)
                    prt = int(prt)
                except ValueError:
                    print(
                    "add job name with length n(1-100) and priority p(-20-19)."
                    )
                    continue
                if 1 <= tlen <= 100 and -20 <= prt <= 19:
                    self._lock.acquire()
                    self._pq.add(prt, [name, tlen])
                    self._lock.release()
                else:
                    print(
                    "length range: 1-100, priority range: -20-19, inclusive."
                    )
        # print('command handler thread is stopped!')


class Simulator(threading.Thread):
    """ The thread for execute every job."""

    def __init__(self, priority_queue, lock):
        threading.Thread.__init__(self)
        self.shutdown_flag = threading.Event()
        self._pq = priority_queue
        self._lock = lock

    def run(self):
        while not self.shutdown_flag.is_set():
            self._lock.acquire()
            k, v = self._pq.remove_min()
            self._lock.release()
            # always keep idle task in queue
            if k == IDLE_TASK_PRIORITY:
                self._lock.acquire()
                self._pq.add(k, v)
                self._lock.release()
                continue
            # not idle tasks
            logging.info(v[0])
            tlen = v[1]
            time.sleep(1)  # sleep some time
            v[1] = tlen - 1
            if v[1] > 0:
                self._lock.acquire()
                self._pq.add(k, v)  # not done, add again
                self._lock.release()
        # print('simulator thread is stopped!')


def service_shutdown(signum, frame):
    raise ServiceExit


class ServiceExit(Exception):
    """ Custom exception which is used to trigger the clean exit
    of all running threads and the main program."""
    pass


class JobScheduler(object):
    """ Job scheduler."""

    def __init__(self):
        self._pq = HeapPriorityQueue()
        self._pq.add(IDLE_TASK_PRIORITY, ('task_idle', 0))  # idle task
        self._lock = threading.Lock()
        self._cmd_handler = CommandHandler(self._pq, self._lock)
        self._simulator = Simulator(self._pq, self._lock)
        self._predefine_tasks()
        # register signal handlers
        signal.signal(signal.SIGTERM, service_shutdown)
        signal.signal(signal.SIGINT, service_shutdown)

    def _predefine_tasks(self):
        self._pq.add(-19, ['Bitcoin', 6])
        self._pq.add(-18, ['Ethereum', 5])
        self._pq.add(0, ['Ripple', 2])
        self._pq.add(2, ['Power', 1])

    def action(self):
        try:
            self._cmd_handler.start()
            self._simulator.start()
            # Keep the main thread running, otherwise signals are ignored.
            while(True):
                time.sleep(0.5)
        except ServiceExit:
            self._cmd_handler.shutdown_flag.set()
            self._simulator.shutdown_flag.set()
            self._cmd_handler.join()
            self._simulator.join()
        print('Exit scheduler!\n')


if __name__ == '__main__':
    scheduler = JobScheduler()
    scheduler.action()

