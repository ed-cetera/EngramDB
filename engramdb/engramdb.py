import configparser

import flask


def load_config(configfile=None):
    configfile_parser = configparser.ConfigParser()
    if configfile is not None:
        configfile_parser.read(configfile)
    config = {}
    config["host"] = configfile_parser.get("EngramDB", "host", fallback="localhost")
    config["port"] = configfile_parser.getint("EngramDB", "port", fallback=8042)
    return config


def create_app(config):
    app = flask.Flask("engramdb")

    @app.route("/")
    def root():
        return "Hello World!"

    return app
