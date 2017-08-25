#coding:utf-8

import sys, logging
from credentials import Credentials
import click

@click.command(name="check")
def check(credentials, verbose):
    """Check project file"""
    FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
    level = logging.DEBUG if verbose else  logging.INFO
    logging.basicConfig(format=FORMAT, level=level)
    credentials = Credentials(path=credentials)




__USAGE = """cump check <options>

"""