import yaml
import os
import sys
import customlogger 


custom_log = customlogger.CustomLogger(log_file)
logger = custom_log.logger


class ReadConfigYaml:
        """Parse yaml config file to get necessary data to run git-cacher"""
        def __init__(self, yaml_file_name):
            if not os.path.exists(yaml_file_name):
                logger.error('Missing main configuration file {}'.format(yaml_file_name))
                sys.exit(10)
            try:
                with open(yaml_file_name) as yaml_file:
                    logger.info('loading config file {}'.format(yaml_file_name))
                    params = yaml.load(yaml_file)
            except Exception as msg:
                logger.error('Can not load the YAML file {}, please review syntax with any online yaml pareser: {}'.format(yaml_file_name, msg))
            try:
                self.github_url = params['GITHUB']['url']
                self.token = params['GITHUB']['token']
                self.user = params['GITHUB']['user']
            except Exception as msg:
                logger.error('{}: Missing GITHUB PARAMS in {}'.format(msg, yaml_file_name))

            try:
                self.cacher_basepath = params['CACHER']['basepath']
                self.workers = params['CACHER']['workers']
                self.repos = params['CACHER']['repos']
            except Exception as msg:
                logger.error('{}: Missing  CACHER PARAMS in {}'.format(msg, yaml_file_name))
            logger.info('Config params loaded')
