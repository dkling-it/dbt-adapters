from dbt.adapters.postgres.impl import PostgresIndexConfig


def test_index_config_render_uses_configured_name():
    config = PostgresIndexConfig(columns=["id"], name="custom_index")

    assert config.render(None) == "custom_index"


def test_index_config_render_generates_name_when_unconfigured():
    config = PostgresIndexConfig(columns=["id"])

    class Relation:
        def render(self):
            return "relation"

    assert len(config.render(Relation())) == 32
