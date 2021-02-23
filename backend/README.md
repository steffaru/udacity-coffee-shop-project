# Coffee Shop Backend ☕🤎

## Getting Started 🚄

### Installing Dependencies ⚙⚙🔩🔩

#### Python 3.7 🐍

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment 🦾🦿

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies 🧩🧩

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies 🔑🔑

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server 🧗‍♀️

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.
 
## Tasks ⛏⛏

### Setup Auth0  🧰🧰

1. Create two new Auth0 Account 👩‍💻
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:drinks-detail`
    - `post:drinks`
    - `patch:drinks`
    - `delete:drinks`
6. Create new roles for:
    - Barista
        - can `get:drinks-detail`
        - account ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN1cEdUbE5XSTlsZzhWazhOQnR0RSJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktZGV2LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMzNkNzcwMjkxOGM2MDA2OWU4ODQ1ZSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImlhdCI6MTYxNDAzNjE3OCwiZXhwIjoxNjE0MDQzMzc4LCJhenAiOiJjNXdlOTlQeWRIeUtzczNGVjBXendhR0oySktaVHFUbSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.fDi5z70acbg6kd58v6Ce4dWi9veAlET85u5z5JouDkRkLovEPqyySKJb1Vc7MNksRevfGCkvF6xapd_NN_PPUwsW689hDnT-fRUO1B94DfaJ9NFeYe6es6BFft6g8x30iQCxlQWjKPZhCeAB_ZAA04QXz-uQibBucVyQYYraCnDxndSKK7ckp_qDyA5xr6DjXr9CU59-hM1fKkAGZONukQ5WSYCGjhr3S5GChcU5utgd4-oj30eW_LLdS7EzqUxRNbfHiCFxi-EFhgyqjZ1N-0AjQEjk61vXmea8mpRhgzlZXNQeA7ZhqIZgMBhmL1wuWm8nf6AdGFCr3eMQtqXAFQ```
        
        - Manager
        - can perform all actions
        - account
        ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN1cEdUbE5XSTlsZzhWazhOQnR0RSJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktZGV2LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMzNkODAyYWY1MDQ2MDA2OTYyYmE5OSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImlhdCI6MTYxNDAzNTQ3NiwiZXhwIjoxNjE0MDQyNjc2LCJhenAiOiJjNXdlOTlQeWRIeUtzczNGVjBXendhR0oySktaVHFUbSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.dR2ZEyJfgo11PtdRAcrDDrvkAJQ9J-flJZV1h5giuNnjTwRuRcm5OquRwIL_b6LONvrTKGnLH3TRMmFp43YzFN7P1GnAFn_-uvmpHxv556A2IJPeC54hW_hZnxITSArtGQRku5tHqM2qzAV0WcHC8V9-wXSCUM20FbflWViVDa8FUHfHci-4d8igaey--Hi6Tq9pBcs7fDkTStNjDXfM2uqM4gn4Uvo6qnMuHkzpAc1ON9upn85AQjGHpyY__7SJfpVrzJ9Emgd2roSTVP6bwDET81agbIF7ZtCR6WxRdyqpw-oMvMykQ1uGQ71psoeHEC5YclPKdNsNbUSxUggBpA```


7. Test your endpoints with [Postman](https://getpostman.com).🧫🧫
    - Register 2 users - assign the Barista role to one and Manager role to the other.
    - Sign into each account and make note of the JWT.
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.
    - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server ♀️🤹‍

1. `./src/auth/auth.py`
2. `./src/api.py`
