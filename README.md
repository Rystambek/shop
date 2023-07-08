# e-shop-api

this is simple rest api project for drf practice

## Features

1. non-authenticated users can get product
2. authenticated users (only superuser) can crud product 
3. authenticated users can buy product
4. authenticated users can comment
5. authenticated users can like

## Tables

1. User
2. Product
3. Order
4. Comment
5. Like

### Schema

User:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| username | str  | unique username |
| password | str  | password |

Product:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| name | str  | name        |
| description | str  | description   |
| price | float  | price   |
| image | str  | url for image   |
| ram | int  | ram   |
| color | str  | color   |
| memory | int  | memory   |

Order:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| user | fk  | user_id   |
| product | fk  | product_id   |

Comment:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| text | str  | text        |
| user | fk  | user_id   |
| product | fk  | product_id   |

Like:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| like | bool  | bool        |
| user | fk  | user_id   |
| product | fk  | product_id   |
# shop
