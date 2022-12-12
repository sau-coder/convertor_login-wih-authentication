"""v0.0 initial commit

Revision ID: 81d1857f7c18
Revises: 
Create Date: 2022-12-08 12:41:09.186846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81d1857f7c18'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email_id', sa.String(), nullable=True),
    sa.Column('mobile_no', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('retype_password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('username'),
    sa.UniqueConstraint('email_id'),
    sa.UniqueConstraint('mobile_no')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
