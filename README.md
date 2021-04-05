# Example Angular-on-Flask Starter

This repository contains a quickstart angular + flask application that can be
deployed to AppEngine on the Google Cloud Platform.

You will need to install python3, node, and the gcloud sdk to use it.
Additionally you will need a [Google Cloud](https://console.cloud.google.com/freetrial) account.

## Server setup

I recommend you use a [venv](https://docs.python.org/3/library/venv.html) while developing with this repo.
One way to do this is in the command listing below.

```
cd server
virtualenv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Now you can run the server locally:

```
flask run
```

configure flask and your backend variables in .flaskenv (see example.flaskenv)
.flaskenv is BOTH

- where you put your super secret flask backend stuff
- where you configure

## Client setup

you are probably going to want @angular/fire and firebase
in my project i changed angular.json's
client/architecht/build/configurations/[prod|dev]/filereplacements['environment.ts']
to have a separate dev and prod env file for different firebase creds

from the top

```
cd client
npm install
ng serve -c dev
```

if that makes it so http://localhost:4200 serves you 'example works!' and http://localhost:4200/api/ serves you 'hello', everything is set up right
if you get error occured while trying to proxy, probably you don't have flask running do `flask run` in another terminal from the server dir
now we are going to make it so you can deploy to gcp, by creating a production client build with

```
ng build
```

files in server/dist/client should be created

## GCP setup

Once you have the [Cloud SDK](https://cloud.google.com/sdk/docs/install)
installed and your GCP account created, run `gcloud init` to create a default
configuration. In this process you will log in to your GCP account and create
a new GCP project.

To get started:

- Follow instructions in example.env
- Run `npm install` from this folder
- Run `python -m pip install -r requirements.txt`
  - Use python3
  - You may use a [venv](https://docs.python.org/3/library/venv.html).

To run in development mode:

- Set FLASK_ENV to development in .env
- `python -m flask run`
- `ng serve`
- navigate to http://localhost:5000 (or whatever your flask instance is)

To run in production mode:

- Set FLASK_ENV to production in .env
- `ng build --prod`
- `npm start`
- navigate to http://localhost:8000 (or whatever your flask instance is)
