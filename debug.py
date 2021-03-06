import codecs
import logging
import os


class Debug(object):
    DEBUG        = False
    READFROMFILE = False  # Read from file for debugging
    SAVELASTFILE = False  # Write to file upon each request

    @staticmethod
    def readFromFile(file_name):
        """
        readFromFile(): Read the debug information from file if READFROMFILE is enabled
        """
        if Debug.READFROMFILE and os.path.exists(file_name):
            with open(file_name, 'rb') as debug_file:
                return debug_file.read()
        else:
            return ''
    # END: def readFromFile():

    @staticmethod
    def writeToFile(file_name, debug, encoding):
        """
        writeToFile(): Write the debug information to file if SAVELASTFILE is enabled
        """
        if Debug.SAVELASTFILE:
            try:
                with codecs.open(file_name, 'w', encoding) as debug_file:
                    debug_file.write(str(debug))
            except TypeError:
                with open(file_name, 'ab') as debug_file:
                    debug_file.write(str(debug))
    # END: def writeToFile():

    @staticmethod
    def printDictionary(d):
        """
        printDictionary(d): Prints well spaced key value pairs
        """
        maxKeyFmt = '{0: <' + str(len(max(d, key=len))) + '}'
        for k in sorted(d.keys()):
            logging.debug(maxKeyFmt.format(k) + ' - ' + str(d[k]))
    # END: def printDictionary(d):
# END: class Debug
