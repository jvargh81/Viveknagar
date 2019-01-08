from login import db
from models import BlogPost

# create the database and the db tables
db.create_all()

# insert
db.session.add(BlogPost("Good","I\'m good."))
db.session.add(BlogPost("well","I\'m well."))

# commit changes
db.session.commit()