from subprocess import Popen
from os import kill
import signal


class Process:

    def __init__(self):
        pass

    @classmethod
    def new_process(cls):
        proceso = Popen(['start', 'chrome'], shell=True)
        id_p = proceso.pid
        print("Proceso {} Creado:".format(id_p))
        return int(id_p)

    @classmethod
    def kill_process(cls, id_proc):
        kill(id_proc, signal.SIGTERM)
        print("proceso {} terminado ...".format(id_proc))


if __name__ == "__main__":
    cod = Process.new_process()
    # Process.kill_process(5860)

