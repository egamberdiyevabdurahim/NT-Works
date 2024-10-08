"""empty message

Revision ID: a5aae066ff08
Revises: 83f0b96143d7
Create Date: 2024-09-11 17:36:57.655178

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5aae066ff08'
down_revision: Union[str, None] = '83f0b96143d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('to_do',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task', sa.String(), nullable=True),
    sa.Column('is_completed', sa.Boolean(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('to_do')
    # ### end Alembic commands ###
