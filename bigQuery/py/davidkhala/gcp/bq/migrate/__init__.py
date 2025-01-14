from enum import auto

from davidkhala.syntax import NameEnum


class SourceDialect(NameEnum):
    Teradata = auto()
    Redshift = auto()
    Bteq = auto()
    Oracle = auto()
    HiveQL = auto()
    SparkSQL = auto()
    Snowflake = auto()
    Netezza = auto()
    AzureSynapse = auto()
    Vertica = auto()
    SQLServer = auto()
    Presto = auto()
    MySQL = auto()
    Postgresql = auto()
