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
# To have file and stream custom logger handlers
import customlogger
# To read custom config file in yaml 
import readconfig

if __name__ == "__main__":

    log_file = '../logs/SOME-NAME-HERE'
    custom_log = customlogger.CustomLogger(log_file)
    logger = custom_log.logger

    config_file = '../conf/YOUR-CONF-YAML'
    logger.info('Reading config file {}'.format(config_file))
    params = readconfig.ReadConfigYaml(config_file)

    