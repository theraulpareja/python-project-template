#!/usr/env python

import logging
import sys
import os

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red


class CustomLogger:
    def __init__(self, log_full_path, file_level='DEBUG', stream_level='INFO'):
        """Create logger, with file and console handlers"""
        if log_full_path is None:
            print(R + "[-] ERROR: CustomLogger(log_full_path, file_level='DEBUG', stream_level='INFO') needs an argument" + W)
            sys.exit(1)
        try:
            self.logger = logging.getLogger(log_full_path)
            self.logger.setLevel(logging.DEBUG)

            file_handler = logging.FileHandler(log_full_path, mode='w')
            if file_level is 'INFO':
                file_handler.setLevel(logging.INFO)
            elif file_level is 'DEBUG':
                file_handler.setLevel(logging.DEBUG)
            elif file_level is 'WARNING':
                file_handler.setLevel(logging.WARNING)
            elif file_level is 'ERROR':
                file_handler.setLevel(logging.ERROR)
            else:
                print(R + "[-] ERROR: file handler logger level not accepted, only ['ERROR', 'WARNING', 'INFO', 'DEBUG'] are accepted" + W)
                sys.exit(1)

            stream_handler = logging.StreamHandler(stream=sys.stdout)
            if stream_level is 'INFO':
                stream_handler.setLevel(logging.INFO)
            elif stream_level is 'DEBUG':
                stream_handler.setLevel(logging.DEBUG)
            elif stream_level is 'WARNING':
                stream_handler.setLevel(logging.WARNING)
            elif stream_level is 'ERROR':
                stream_handler.setLevel(logging.ERROR)
            else:
                print(R + "[-] ERROR: strean handler logger level not accepted, only ['ERROR', 'WARNING', 'INFO', 'DEBUG'] are accepted" + W)
                sys.exit(1)

            formatter_log = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s', "%d-%m-%Y %H:%M:%S")
            formatter_stream = logging.Formatter('%(levelname)s:%(message)s', "%d-%m-%Y %H:%M:%S")

            file_handler.setFormatter(formatter_log)
            stream_handler.setFormatter(formatter_stream)

            self.logger.addHandler(file_handler)
            self.logger.addHandler(stream_handler)

        except Exception as msg:
            print(R + '[-] ERROR: Could not create logger and handlers, pelase review {}'.format(msg) + W)
            sys.exit(2)
