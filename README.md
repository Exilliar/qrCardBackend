# qrCardsBackend

Django app for the backend of the qr-cards webapp

## endpoints

`/qrCards/account` - GET - get all account data, including all cards
`/qrCards/account` - POST - add a new card
`/qrCards/account` - PATCH - add a card to the account

## Django stuff

## Running

To serve:
`python3 manage.py runserver`

## Creating app

`python3 manage.py startapp exampleapp`

## Database stuff

### Migrating

Create migration files:

`python3 manage.py makemigrations exampleapp`

Then do the migrations:

`python3 manage.py migrate`
