"""empty message

Revision ID: d4b0413fe8b2
Revises: 93c92c0ca6c9
Create Date: 2016-02-12 03:24:23.479432

"""

# revision identifiers, used by Alembic.
revision = 'd4b0413fe8b2'
down_revision = '93c92c0ca6c9'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department_name', sa.String(length=32), nullable=False),
    sa.Column('superior', sa.String(length=32), nullable=False),
    sa.Column('path', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'server', sa.Column('os', sa.String(length=30), nullable=True))
    op.alter_column(u'server', 'last_op_people',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.create_index(op.f('ix_server_os'), 'server', ['os'], unique=False)
    op.drop_index('ix_server_os_type', table_name='server')
    op.drop_index('ix_server_os_version', table_name='server')
    op.drop_column(u'server', 'os_version')
    op.drop_column(u'server', 'os_type')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'server', sa.Column('os_type', mysql.VARCHAR(length=30), nullable=True))
    op.add_column(u'server', sa.Column('os_version', mysql.VARCHAR(length=30), nullable=True))
    op.create_index('ix_server_os_version', 'server', ['os_version'], unique=False)
    op.create_index('ix_server_os_type', 'server', ['os_type'], unique=False)
    op.drop_index(op.f('ix_server_os'), table_name='server')
    op.alter_column(u'server', 'last_op_people',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.drop_column(u'server', 'os')
    op.drop_table('department')
    ### end Alembic commands ###
