from datetime import datetime
from flask import current_app
from slugify import slugify
from sqlalchemy.ext.hybrid import hybrid_property

from gadget import db
from gadget import utils


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    _slug = db.Column('slug', db.String(250), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    suites = db.relationship('Suite', backref='project', cascade='all, delete-orphan')

    @hybrid_property
    def slug(self):
        return self._slug

    @slug.setter
    def slug(self, slug):
        self._slug = slugify(slug)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self, name, slug):
        self.updated = datetime.utcnow()
        self.name = name
        self. slug = slug
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def fixtures():
        if current_app.config['DEBUG'] is False:
            raise Exception('Inserting fixtures not allowed in production')

        return [
            Project(name='project1', slug='project1'),
            Project(name='project2', slug='project2'),
            Project(name='project3', slug='project3'),
        ]

    def serialize(self, recursive=True):
        result = {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'created': utils.to_local_js_timestamp(self.created),
            'updated': utils.to_local_js_timestamp(self.updated)
        }

        if recursive:
            result['suites'] = utils.serialize_list(self.suites)

        return result
