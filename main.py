#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import time
from sensor import main_sensor
from server import Server
import sys


def main():
    parameter_list = sys.argv
    node_number = int(parameter_list[1])
    basic_port = 33335
    # node_number = 0
    server_name = "r"+str(node_number)
    server = Server(node_number, server_name, basic_port)
    server.start()
    time.sleep(50)
    main_sensor(node_number, basic_port)
    server.join()


if __name__ == '__main__':
    main()
