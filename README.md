# CoRider Flask Assignment


### To run the app -
1. Clone the repository:
```
git clone https://github.com/wolverine1102/corider-assignment.git
```

2. Create an ```.env``` file in the root directory and add the following environment variables:
```
JWT_SECRET_KEY
USERNAME
PASSWORD
DB
ADMIN_EMAIL
ADMIN_PASSWORD
```

3. Create the Docker image:
```
docker build -t <image_name> .
```

4. Build the services using Docker Compose:
```
docker-compose build
```

5. Access the app at:
```
http://127.0.0.1:5000/
```
