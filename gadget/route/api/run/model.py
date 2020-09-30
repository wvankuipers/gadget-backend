from datetime import datetime
from flask import current_app
from slugify import slugify
from sqlalchemy.ext.hybrid import hybrid_property

from gadget import db
from gadget import utils
from gadget.route.api.suite import Suite


class Run(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _nr = db.Column('nr', db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    suite_id = db.Column(db.Integer, db.ForeignKey('suite.id'))
    tests = db.relationship('Test', backref='run', cascade='all, delete-orphan')

    @hybrid_property
    def nr(self):
        return self._nr

    @nr.setter
    def slug(self, nr):
        next_available_number = 1  # @todo fetch from db
        self._nr = next_available_number

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self, nr, suite_id):
        self.updated = datetime.utcnow()
        self._nr = nr
        self.suite_id = suite_id
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def fixtures():
        if current_app.config['DEBUG'] is False:
            raise Exception('Inserting fixtures not allowed in production')

        return [
            Run(_nr=1, suite_id=1),
            Run(_nr=2, suite_id=2),
            Run(_nr=3, suite_id=3),
        ]

    def serialize(self, recursive=True):
        result = {
            'id': self.id,
            'nr': self.nr,
            'created': utils.to_local_js_timestamp(self.created),
            'updated': utils.to_local_js_timestamp(self.updated),
            'suite': Suite.query.get(self.suite_id).serialize(False),
        }

        if recursive:
            result['tests'] = utils.serialize_list(self.tests)

        return result
