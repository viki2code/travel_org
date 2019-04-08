"""change name column

Revision ID: b872791db685
Revises: e7514901d107
Create Date: 2019-04-03 13:30:06.545745

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b872791db685'
down_revision = 'e7514901d107'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('travel_plan', sa.Column('date_end', sa.DateTime(), nullable=True))
    op.add_column('travel_plan', sa.Column('date_start', sa.DateTime(), nullable=False))
    op.create_index(op.f('ix_travel_plan_date_end'), 'travel_plan', ['date_end'], unique=False)
    op.create_index(op.f('ix_travel_plan_date_start'), 'travel_plan', ['date_start'], unique=False)
    op.drop_index('ix_travel_plan_date_in', table_name='travel_plan')
    op.drop_index('ix_travel_plan_date_out', table_name='travel_plan')
    op.drop_column('travel_plan', 'date_out')
    op.drop_column('travel_plan', 'date_in')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('travel_plan', sa.Column('date_in', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('travel_plan', sa.Column('date_out', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.create_index('ix_travel_plan_date_out', 'travel_plan', ['date_out'], unique=False)
    op.create_index('ix_travel_plan_date_in', 'travel_plan', ['date_in'], unique=False)
    op.drop_index(op.f('ix_travel_plan_date_start'), table_name='travel_plan')
    op.drop_index(op.f('ix_travel_plan_date_end'), table_name='travel_plan')
    op.drop_column('travel_plan', 'date_start')
    op.drop_column('travel_plan', 'date_end')
    # ### end Alembic commands ###