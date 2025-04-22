import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config['commonInfo']['baseURL']
        return url

    @staticmethod
    def getUseremail():
        username = config['commonInfo']['email']
        return username

    @staticmethod
    def getUserPassword():
        password = config['commonInfo']['password']
        return password