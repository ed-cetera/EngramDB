import os

import engramdb.engramdb as engramdb


def test_load_config():
    config_1 = engramdb.load_config()
    expected_config_1 = {"host": "localhost", "port": 8042}
    assert config_1 == expected_config_1

    configfile_2 = (
        os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + "/../../etc")
        + "/engramdb.conf.sample"
    )
    config_2 = engramdb.load_config(configfile_2)
    expected_config_2 = {"host": "localhost", "port": 8042}
    assert config_2 == expected_config_2

    configfile_3 = (
        os.path.dirname(os.path.realpath(__file__))
        + "/test_engramdb_fixtures/test_load_config.conf"
    )
    config_3 = engramdb.load_config(configfile_3)
    expected_config_3 = {"host": "1.2.3.4", "port": 1234}
    assert config_3 == expected_config_3
