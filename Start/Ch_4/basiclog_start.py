# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging

# TODO: Use basicConfig to configure logging
logging.basicConfig(filename="basiclog.log",
                    level= logging.DEBUG)
# TODO: Try out each of the log levels
logging.debug("logging.debug message")
logging.info("logging.info message")
logging.warning("logging.warning message")
logging.error("logging.error message")
logging.critical("logging.critical message")
# TODO: Output formatted strings to the log
fmtstr= f"%(timedate)s  %(function)s"


