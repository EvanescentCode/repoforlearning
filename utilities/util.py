import logging
import inspect
import softest


class Utils(softest.TestCase):
    """
    W tej klasie odnajdziemy soft custom_logger'a który przyjmuje za argument log_level:

    DEBUG - Detailed information, typically of interest only when diagnosing problems.

    INFO - Confirmation that things are working as expected.

    WARNING - An indication that something unexpected happened, or indicative of some problem in the near future
    (e.g. ‘disk space low’). The software is still working as expected.

    ERROR - Due to a more serious problem, the software has not been able to perform some function.

    CRITICAL - A serious error, indicating that the program itself may be unable to continue running.
    ____________________________________________________________________________________________________________________
    Znajdziemy tutaj także soft_assert_list_item() i soft_assert_item() które wykonują assert, który nie przerywa
    skryptu
    """

    def custom_logger(self, log_level=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        handler = logging.FileHandler(filename='..\\reports\log.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                                      datefmt='%d-%m-%Y %H:%M:%S %p')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def assert_list_item(self, list_name, ass_value):
        log = self.custom_logger()
        for ass in list_name:
            log.info('Text is:'+ ass.text)
            self.assertEqual(ass, ass_value)
            log.info('Assert Pass')

    def soft_assert_list_item(self, list_name, ass_value):
        log = self.custom_logger()
        for ass in list_name:
            log.info('Text is: ' + ass.text)
            self.soft_assert(self.assertEqual, ass, ass_value)
            log.info('Assert Pass')

    def soft_assert_item(self, item, ass_value):
        log = self.custom_logger()
        log.info('Text is' + ass_value.text)
        self.soft_assert(self.assertEqual, item, ass_value)
        log.info('Assert Pass')

