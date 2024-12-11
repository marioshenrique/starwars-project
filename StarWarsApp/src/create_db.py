from config import engine, Base
from models.user_model import User

Base.metadata.create_all(bind=engine)
