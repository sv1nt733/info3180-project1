from . import db 

class Properties(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(1000))
    bedrooms = db.Column(db.String(30))
    bathrooms = db.Column(db.String(30))    
    location = db.Column(db.String(300))
    price = db.Column(db.String(100))
    propertyType = db.Column(db.String(20))
    photo = db.Column(db.String(200))

    def __init__(self, title, description, bedrooms, bathrooms, location, price, propertyType, photo):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price  
        self.propertyType = propertyType  
        self.photo = photo 