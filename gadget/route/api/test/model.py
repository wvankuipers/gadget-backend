from datetime import datetime
from flask import current_app
from slugify import slugify
from sqlalchemy.ext.hybrid import hybrid_property

from gadget import db
from gadget import utils
from gadget.route.api.run import Run


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    browser = db.Column(db.String(250), nullable=False)
    size = db.Column(db.String(250), nullable=False)
    key = db.Column(db.String(250), nullable=False)
    passed = db.Column(db.Boolean, unique=False, default=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    run_id = db.Column(db.Integer, db.ForeignKey('run.id'))

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
        self.slug = slug
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def fixtures():
        if current_app.config['DEBUG'] is False:
            raise Exception('Inserting fixtures not allowed in production')

        return [
            Test(name='test1', browser='browser1', size='size1', key='key1', passed=False, run_id=1),
            Test(name='test2', browser='browser2', size='size2', key='key2', passed=False, run_id=2),
            Test(name='test3', browser='browser3', size='size3', key='key3', passed=True, run_id=3),
        ]

    def serialize(self, recursive=False):
        result = {
            'id': self.id,
            'name': self.name,
            'browser': self.browser,
            'size': self.size,
            'key': self.key,
            'passed': self.passed,
            'created': utils.to_local_js_timestamp(self.created),
            'updated': utils.to_local_js_timestamp(self.updated),
        }

        if recursive:
            result['run'] = Run.query.get(self.run_id).serialize(False)

        return result
