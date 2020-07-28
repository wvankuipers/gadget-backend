"""create project table

Revision ID: 9a2fcc1d5fa4
Revises:
Create Date: 2020-07-27 21:19:54.879995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a2fcc1d5fa4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'project',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('slug', sa.String(50), nullable=False),
        sa.Column(
            'created',
            sa.DateTime,
            server_default=sa.func.current_timestamp()
        ),
        sa.Column(
                    'updated',
                    sa.DateTime,
                    server_default=sa.func.current_timestamp()
        ),
    )
    pass


def downgrade():
    op.drop_table('project')
    pass
