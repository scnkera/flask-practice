from flask_sqlalchemy impor SQLAlchemy
from flask_migrate import Migrate
from .models.base import Base

db = SQLAlchemy(model_class=Base)
migrate = Migrate()