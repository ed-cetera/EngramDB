import os

import bjoern

import engramdb.engramdb as engramdb


# Load config
for filepath in (
    os.environ.get("ENGRAMDB_CONF"),
    "~/.engramdb/engramdb.conf",
    "~/.config/engramdb/engramdb.conf",
    os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + "/../etc")
    + "/engramdb.conf",
):
    if filepath is None:
        continue
    configfile = os.path.expanduser(filepath)
    if os.path.isfile(configfile):
        config = engramdb.load_config(configfile)
        break
else:
    config = engramdb.load_config()

# Run WSGI server with app
app = engramdb.create_app(config)
print(
    "Starting EngramDB, ",
    "listening on ",
    config["host"],
    ":",
    config["port"],
    ".",
    sep="",
)
bjoern.run(app, config["host"], config["port"])
