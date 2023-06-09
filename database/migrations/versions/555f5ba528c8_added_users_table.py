"""Added users table

Revision ID: 555f5ba528c8
Revises: 
Create Date: 2023-02-01 16:06:44.946091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '555f5ba528c8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.String(length=10), nullable=True),
    sa.Column('won', sa.Integer(), nullable=True),
    sa.Column('loss', sa.Integer(), nullable=True),
    sa.Column('win_ratio', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_account')
    # ### end Alembic commands ###
