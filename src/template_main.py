#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Common python modules
import logging
#import pdb
#import sys
#import yaml
#import os
#import shutil
#import paramiko
#import time


#Classes 
class ReadConfigYaml:
        """Parese yaml config file to get necessary data to run open_github_enterprise.py"""

        def __init__(self, yaml_file_name):

            if not os.path.exists(yaml_file_name):
                logger.error('Missing main configuration file {}'.format(yaml_file_name))
                sys.exit(3)
            logger.debug('reading file {}'.format(yaml_file_name))

            try:
                with open(yaml_file_name) as yaml_file:
                    logger.debug('loading config file {}'.format(yaml_file_name))
                    output = yaml.load(yaml_file)
            except Exception as msg:
                logger.exception('Can not load the YAML file {}, please review syntax with any online yaml pareser: {}'.format(yaml_file_name, msg))
                sys.exit(3)

            if output['XXXX']['XXXX'] is None:
                logger.error('Can not find XXXX value in {}'.format(yaml_file_name))
                sys.exit(3)
            else:
                self.XXXX = output['XXXX']['XXXX']
                logger.debug('XXXX param loaded = {} '.format(self.XXXXX))


#Functions
def create_logger(log_name):
    """Create logger  with file and console handlers"""

    if log_name is None:
        print R + '[-] ERROR: create_logger(log_name) needs an argument' + W
        sys.exit(1)

    try:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_name, mode='w')
        file_handler.setLevel(logging.DEBUG)

        stream_handler = logging.StreamHandler(stream=sys.stdout)
        stream_handler.setLevel(logging.INFO)

        formatter_log = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s', "%d-%m-%Y %H:%M:%S")
        formatter_stream = logging.Formatter('%(levelname)s:%(message)s', "%d-%m-%Y %H:%M:%S")
        file_handler.setFormatter(formatter_log)
        stream_handler.setFormatter(formatter_stream)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    except Exception as msg:
        print R + '[-] ERROR: Could not create logger and handlers, pelase review {}'.format(msg) + W
        sys.exit(2)

    return logger


#Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[36m'  # blue-cyan

#Create logger
log_dir = '../logs/'
log_name = 'XXXXXXXXX.log'
full_path_log = log_dir + log_name
logger = create_logger(full_path_log)

#Configuration file
config_dir         = '../conf/'
config_file_name   = 'XXXXXXX.yaml'
full_path_config   = config_dir + config_file_name


if __name__ == "__main__":

