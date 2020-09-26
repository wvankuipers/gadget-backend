from datetime import datetime
from flask import current_app
from slugify import slugify
from sqlalchemy.ext.hybrid import hybrid_property

from gadget import db
from gadget import utils
from gadget.route.api.project import Project


class Suite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    _slug = db.Column('slug', db.String(250), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    runs = db.relationship('Run', backref='suite', cascade='all, delete-orphan')

    @hybrid_property
    def slug(self):
        return self._slug

    @slug.setter
    def slug(self, slug):
        self._slug = slugify(slug)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self, name, slug, project_id):
        self.updated = datetime.utcnow()
        self.name = name
        self.slug = slug
        self.project_id = project_id
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def fixtures():
        if current_app.config['DEBUG'] is False:
            raise Exception('Inserting fixtures not allowed in production')

        return [
            Suite(name='suite1', slug='suite1', project_id=1),
            Suite(name='suite2', slug='suite2', project_id=2),
            Suite(name='suite3', slug='suite3', project_id=3),
        ]

    def serialize(self, recursive=True):
        result = {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'created': utils.to_local_js_timestamp(self.created),
            'updated': utils.to_local_js_timestamp(self.updated),
            'project': Project.query.get(self.project_id).serialize(False),
        }

        if recursive:
            result['runs'] = utils.serialize_list(self.runs)

        return result
