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
    - `get:drinks`
    - `get:drinks-detail`
    - `post:drinks`
    - `patch:drinks`
    - `delete:drinks`
6. Create new roles for:
    - Barista
        - can ` get:drinks, get:drinks-detail`
        - account ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNkYmVUN091QkFYWjM5cEEyOExSdSJ9.eyJpc3MiOiJodHRwczovL2Rldi1wcm9qZWN0LXVkYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAzNTc0NDU3Y2JhZDMwMDY5ODk5NWIwIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNjE0MTc3MjYwLCJleHAiOjE2MTQyNjM2NjAsImF6cCI6IlZVMkxLNTNjSlpvelg2MzY0VmtPaGptYjZ2UGlEa2dtIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.3ts6xecPiB1wSkBiEpLvuCzxsfB2p9xf_VJ1NQoIpICazHMgzKjL8FuERBuRU8Rz39_2R67Wswvl1vZDdYnC4uz2rvXrVdYh2eYzZQbLKXJSyTZRUTtcDN-xMyayaEUkm5Z6BtAw9L1I5i5GfSiLd5DjWe_wG0mbBQuI49BQfyK1-1eHKgREw8iZdHkmNze_Lh4xXFW6xQQrDaB1gYlkOHydsY2M-tC9D1TkLnvWVq7MWIWxvoEwODe5twWJs98UoYy34UnShrj6dlnBeMUZ38e7dm_H3IyFV547_rJbaMhxMKHszWFodlj2EGWWCSUEAkffWm2YVp_9_6LgjWf-cw```
        
        - Manager
        - can perform all actions
        - account
        ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNkYmVUN091QkFYWjM5cEEyOExSdSJ9.eyJpc3MiOiJodHRwczovL2Rldi1wcm9qZWN0LXVkYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAzNTczZjc3Y2JhZDMwMDY5ODk5NWEzIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNjE0MTc2MDA2LCJleHAiOjE2MTQyNjI0MDYsImF6cCI6IlZVMkxLNTNjSlpvelg2MzY0VmtPaGptYjZ2UGlEa2dtIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.VpAJbkPhwJHlIUcGLJR8-5m0ylG5fPz0FIrd3I4wQNwUZYkyuO12_CTQFqRunen939uHCM9vTztaWaZX0hfG6LfmZaUUyNosXeiDYJt7fD6ahszbjcD5moDh6Xm7nRwiNWglTbfPdOo7E9INhCJBocuu2O5V1oc9CvMUIPIAN8JcgcfPLafVle1KQgj8bwnwJIMYzOnnXhUzRT6d85uUNGrmKCFGyG7sEeuEXPooYNULGHRENsK7UABDt4uX-12APQkvb-gSQhTb4oyOLGziitldCcufDazgQj8D3eihcJga6YS0oNPjc0dNUPUSpTKp-tYVPg_PTN-DSoines4img```


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
