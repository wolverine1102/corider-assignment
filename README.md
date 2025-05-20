# CoRider-Flask-Assignment


### To run the app -
1. Clone the repository:
```
git clone https://github.com/wolverine1102/corider-assignment.git
```

2. Create an ```.env``` file in the root directory and add the following environment variables:
```
# Secret key used to sign JWT tokens
JWT_SECRET_KEY=<your_jwt_secret_key>

# Database username for connecting to MongoDB
USERNAME=<your_database_username>

# Database password for authentication
PASSWORD=<your_database_password>

# Name of the MongoDB database
DB=<your_database_name>

# Admin email address for authentication
ADMIN_EMAIL=<your_admin_email>

# Admin password for authentication
ADMIN_PASSWORD=<your_admin_password>

```

3. Build the docker images based on the ```docker-compose.yml``` file:
```
docker-compose build
```

4. To start the services and launch the containers defined in the ```docker-compose.yml``` file.:
```
docker-compose up
```

4. Access the app at:
```
http://127.0.0.1:5000/
```
