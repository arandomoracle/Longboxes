# -*- coding: utf-8 -*-

# Define database tables

## Users
db.define_table('users',
    Field('username', type='string'),
    Field('display_name', type='string'),
    Field('password', type='password')
)

## Boxes
db.define_table('boxes',
    Field('user_id', type='reference users'),
    Field('name', type='string'),
    Field('creation_date', type='date', default=request.now),
    Field('visible', type='boolean')
)

## Comics
db.define_table('comics',
    Field('box_id', type='reference boxes'),
    Field('title', type='string'),
    Field('issue_no', type='integer'),
    Field('writers', type='list:string'),
    Field('artists', type='list:string'),
    Field('publisher', type='string'),
    Field('description', type='string'),
    Field('image', type='upload')
)