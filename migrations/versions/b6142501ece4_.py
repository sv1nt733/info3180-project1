"""empty message

Revision ID: b6142501ece4
Revises: 
Create Date: 2022-03-15 22:06:14.866720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6142501ece4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('bedrooms', sa.String(length=30), nullable=True),
    sa.Column('bathrooms', sa.String(length=30), nullable=True),
    sa.Column('location', sa.String(length=300), nullable=True),
    sa.Column('price', sa.String(length=100), nullable=True),
    sa.Column('propertyType', sa.String(length=20), nullable=True),
    sa.Column('photo', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
