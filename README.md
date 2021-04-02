# Example Angular-on-Flask Starter

This repository contains a quickstart angular + flask application that can be
deployed to AppEngine on the Google Cloud Platform.

You will need to install python3, node, and the gcloud sdk to use it.
Additionally you will need a [Google Cloud](https://console.cloud.google.com/freetrial) account.

##Server setup
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

##GCP setup
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
