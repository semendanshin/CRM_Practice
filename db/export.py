from models import Base

from sqlalchemy.schema import CreateTable
from sqlalchemy.dialects import postgresql, registry
from sqlalchemy import create_mock_engine, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from ydb.sqlalchemy import register_dialect, YqlDialect
from ydb import dbapi

import grpc


def export_models(filename: str) -> None:
    def metadata_dump(sql, *multiparams, **params):
        with open(filename, "a") as file:
            file.write(str(sql.compile(dialect=postgresql.dialect())) + ";\n")

    with open(filename, "w") as file:
        file.write("")

    engine = create_mock_engine("postgresql://", metadata_dump)
    Base.metadata.create_all(engine, checkfirst=False)


def test_ydb():
    # uri = "ydb://localhost:2136/test"
    uri = "yql://localhost:2136?database=/local"

    registry.register("yql", "ydb.sqlalchemy", "YqlDialect")

    # register_dialect()

    engine = create_engine(
        "yql://",
        connect_args={
            "database": "/local",
            "endpoint": "localhost:2136",
        },
        echo=True,
        module=dbapi,
    )
    #
    # engine = create_engine(
    #     "yql://",
    #     connect_args={
    #         "database": "database=/local",
    #         "endpoint": "grpc://localhost:2136",
    #     },
    #     echo=True,
    # )

    session = sessionmaker(engine)()

    print(session.execute(text('SELECT 1')).fetchall())


if __name__ == "__main__":
    export_models("models.sql")
    # test_ydb()
