# from threading import Thread
from servers.server_DAC import DACServer
# from servers.server_GPIB import GPIBServer


def run_dac_server():
    """
    Create a DAC server for the LabJack U6 and run it. This allows for running the function as a process.
    """
    dac_server = DACServer()
    dac_server.run()
    return 1


# def run_gpib_server():
#     """
#     Create a GPIB server for the Prologix controller and run it. This allows for running the function as a process.
#     """
#     gpib_server = GPIBServer()
#     gpib_server.run()
#     return 1


if __name__ == "__main__":
    # t1 = Thread(target=run_dac_server)
    # t2 = Thread(target=run_gpib_server)
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()
    run_dac_server()
