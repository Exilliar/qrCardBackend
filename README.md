# qrCardsBackend

Django app for the backend of the qr-cards webapp

## endpoints

`/qrCards/account/<string:email>`

- GET
- get the account id (or maybe some auth sometime in the future) when given an email. If the email has not already been logged then a new account will be created in the db and the new accountid will be returned

`/qrCards/account/<int:accountid>/card`

- GET
- get all accounts cards

`/qrCards/card`

- POST
- add a new card to the db

`/qrCards/account/<int:accountid>/card/<int:cardid>`

- PATCH
- add a card to the account

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
