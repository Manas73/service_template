class LoggerSettings:
    """A configuration class for setting up logging in the application.

    This class provides a method to retrieve a dictionary containing
    logging configuration settings.

    """

    @classmethod
    def get_config(cls) -> dict:
        """Retrieves the logging configuration dictionary.

        This method returns a dictionary containing the configuration
        for logging, including formatters, handlers, and loggers.

        Returns:
            dict: A dictionary with the following structure:
                {
                    "version": int,
                    "disable_existing_loggers": bool,
                    "formatters": dict,
                    "handlers": dict,
                    "loggers": dict
                }

        Example:
            config = LoggerSettings.get_config()
            logging.config.dictConfig(config)

        """
        return {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s - %(name)s - %(levelname)s :: %(message)s",
                    "datefmt": "%m-%d-%Y %H:%M:%S",
                }
            },
            "handlers": {
                "standard": {
                    "class": "logging.StreamHandler",
                    "level": "DEBUG",
                    "formatter": "standard",
                    "stream": "ext://sys.stdout",
                }
            },
            "loggers": {
                "": {  # root logger
                    "handlers": ["standard"],
                    "level": "INFO",
                    "propagate": False,
                },
                "debug_logger": {
                    "handlers": ["standard"],
                    "level": "DEBUG",
                    "propagate": False,
                },
            },
        }
