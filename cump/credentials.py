#coding:utf-8

import platform, logging, os, sys, getopt

class S3:
    ACCESS_KEY=""
    PUBLIC_KEY=""
    BUCKET=""


class Credentials:
    log = logging.getLogger('credentials')

    def __init__(self, path, args):
        self._platform = platform.system()
        self.path = path
        if not self.path:
            if self._platform  == "Darwin":
                self.path = "~/.cump/settings.ini"
            elif self._platform == "Windows":
                self.path = ""

        self.log.debug("set credentials path %s" % (self.path,))
        if os.path.isfile(self.path):
            self._read()
        else:
            if path: #выдть ошибку если фаил указан, но не прочтен
                self.log.error("file not exist path %s" % (self.path,))
                sys.exit(2)
            else:
                self.log.debug("file not exist path %s" % (self.path,))

        self._args(args)

    def _read(self):
        self.log.debug("read file path %s" % (self.path,))

