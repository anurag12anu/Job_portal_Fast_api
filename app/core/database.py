from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base


DATABASE_URL="postgresql://postgres:Rewa%40123@localhost/jobportalDB"
engine=create_engine(declarative_base)
sessionLocal=sessionmaker(bind=engine)

Base=declarative_base