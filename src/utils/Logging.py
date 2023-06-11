import logging
import os
import inspect


class Logging:
    logger = logging.getLogger("Vision system")
    level = logging.DEBUG

    src_folder_path = None

    old_log_record_factory = logging.getLogRecordFactory()

    @classmethod
    def get_src_path(cls, file) -> None:
        cls.src_folder_path = os.path.dirname(os.path.abspath(file))

    @classmethod
    def get_new_log_record(cls, filename, lineno) -> logging.LogRecord:
        def record_factory(*args, **kwargs):
            record = cls.old_log_record_factory(*args, **kwargs)
            record.filename = filename[len(cls.src_folder_path) + 1 :]
            record.lineno = lineno
            return record

        logging.setLogRecordFactory(record_factory)

    @classmethod
    def setup(cls) -> None:
        formatter = logging.Formatter(
            "[%(levelname)s]: %(asctime)s - %(filename)s:%(lineno)d : %(message)s"
        )
        cls.logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)

        cls.logger.addHandler(console_handler)

    @classmethod
    def get_debug_level(cls) -> None:
        cls.logger.setLevel(logging.DEBUG)

    @classmethod
    def get_warning_level(cls) -> None:
        cls.logger.setLevel(logging.WARNING)

    @classmethod
    def get_info_level(cls) -> None:
        cls.logger.setLevel(logging.INFO)

    @classmethod
    def debug(cls, msg: str) -> None:
        frame = inspect.currentframe().f_back
        filename = inspect.getfile(frame)
        lineno = frame.f_lineno
        cls.get_new_log_record(filename, lineno)

        cls.logger.log(level=logging.DEBUG, msg=msg)

    @classmethod
    def warning(cls, msg: str) -> None:
        frame = inspect.currentframe().f_back
        filename = inspect.getfile(frame)
        lineno = frame.f_lineno
        cls.get_new_log_record(filename, lineno)

        cls.logger.log(level=logging.WARNING, msg=msg)

    @classmethod
    def info(cls, msg: str) -> None:
        frame = inspect.currentframe().f_back
        filename = inspect.getfile(frame)
        lineno = frame.f_lineno
        cls.get_new_log_record(filename, lineno)

        cls.logger.log(level=logging.INFO, msg=msg)

    @classmethod
    def error(cls, msg: str) -> None:
        frame = inspect.currentframe().f_back
        filename = inspect.getfile(frame)
        lineno = frame.f_lineno
        cls.get_new_log_record(filename, lineno)

        cls.logger.log(level=logging.ERROR, msg=msg)
