import uuid
from sqlalchemy.dialects.postgresql import UUID

from compat import basestring
from extensions import db

# Alias common SQLAlchemy names
Column = db.Column
relationship = db.relationship


class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()


class Model(CRUDMixin, db.Model):
    """Base model class that includes CRUD convenience methods."""

    __abstract__ = True

    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self, **kwargs)
        # ..
        self.set_id()

    def set_id(self):
        pass        

# # From Mike Bayer's "Building the app" talk
# # https://speakerdeck.com/zzzeek/building-the-app
# class SurrogatePK(object):
#     """A mixin that adds a surrogate integer 'primary key' column named ``id`` to any declarative-mapped class."""

#     __table_args__ = {'extend_existing': True}

#     id = db.Column(db.Integer, primary_key=True)

#     @classmethod
#     def get_by_id(cls, record_id):
#         """Get record by ID."""
#         if any(
#                 (isinstance(record_id, basestring) and record_id.isdigit(),
#                  isinstance(record_id, (int, float))),
#         ):
#             return cls.query.get(int(record_id))
#         # ..
#         return None

class SurrogatePK(object):
    """A mixin that adds a surrogate integer 'primary key' column named ``id`` to any declarative-mapped class."""

    __table_args__ = {'extend_existing': True}

    id = Column(UUID(as_uuid=True), primary_key=True)

    @classmethod
    def get_by_id(cls, record_id):
        return cls.query.get(str(record_id))

    def set_id(self):
        self.id = uuid.uuid4()

def reference_col(tablename, nullable=False, pk_name='id', **kwargs):
    """Column that adds primary key foreign key reference.

    Usage: ::

        category_id = reference_col('category')
        category = relationship('Category', backref='categories')
    """
    return db.Column(
        db.ForeignKey('{0}.{1}'.format(tablename, pk_name)),
        nullable=nullable, **kwargs)




class Proxy(object):

    class Meta:
        model = None
        fields = []

    @classmethod
    def record(cls, row):
        # ..
        ret = {}
        for id, item in enumerate(cls.Meta.fields):
            ret[item] = row[id]
        # ...
        return ret 

    @classmethod  
    def rs(cls):
        # ...
        args = [ getattr(cls.Meta.model, field ) for field in cls.Meta.fields]
        qs = db.session.query(*args)
        # ..
        return qs


    @classmethod
    def all(cls, filterum=None, orderum=None):
        # ..
        qs = cls.rs()
        # ..
        if filterum:
            qs = qs.filter(filterum())
        # ..
        if orderum:
            qs = qs.order_by(orderum())
        # ..
        return [cls.record(row) for row in qs.all()]


    @classmethod
    def records(cls):
        return cls.all()