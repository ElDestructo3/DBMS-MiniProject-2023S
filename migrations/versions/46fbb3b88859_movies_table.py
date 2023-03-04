"""movies table

Revision ID: 46fbb3b88859
Revises: 37584ab88274
Create Date: 2022-03-26 19:28:21.603927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46fbb3b88859'
down_revision = '37584ab88274'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('description', sa.String(length=140), nullable=True),
    sa.Column('genre', sa.String(length=40), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movie_timestamp'), 'movie', ['timestamp'], unique=False)
    op.create_table('renters',
    sa.Column('renter_id', sa.Integer(), nullable=True),
    sa.Column('rented_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rented_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['renter_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('renters')
    op.drop_index(op.f('ix_movie_timestamp'), table_name='movie')
    op.drop_table('movie')
    # ### end Alembic commands ###