from distutils.version import StrictVersion
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Index,
    Integer,
    String,
    Text,
)

if StrictVersion(db.__version__) >= StrictVersion('1.3.4'):
    from sqlalchemy.dialects.postgresql.json import JSONB
else:
    from sqlalchemy.dialects.postgresql import JSONB


Base = declarative_base()


class FileReport(Base):
    __tablename__ = 'filereport'
    id = Column('id', Integer, primary_key=True)
    node_id = Column('node_id', Text, index=True)
    ip = Column('ip', String)
    country_code = Column('country_code', String, index=True)
    timestamp = Column('timestamp', DateTime, server_default="now()")
    streamed_bytes = Column('streamed_bytes', BigInteger)
    username = Column('username', String, index=True)
    requested_bytes = Column('requested_bytes', BigInteger)

    report_data = Column(JSONB, nullable=True)

    __table_args__ = (
        Index("filereport_report_data_idx", "report_data", postgresql_using="gin",),
    )