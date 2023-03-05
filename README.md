
# Deimos Backend

"Backend for Las Deimos 🚀✨"

![App Screenshot](https://github.com/Zoronium/Deimos/blob/main/LdBackend.png?raw=true)



## Description



The backend for Las Deimos is a server-side application that manages the restaurant's data and provides an API for accessing and manipulating that data. It is typically built using Django-rest,Django-cors a database like SQLlite and Deployed on Replit. The purpose of the restaurant backend is to provide a centralized system for managing the restaurant's menu, orders, and reservations.

The backend typically provides endpoints for creating, reading, updating, and deleting menu items, orders, and reservations. These endpoints can be accessed through HTTP requests, and they usually return JSON data. The backend also includes a security mechanism to ensure that only authorized users can access the data.

The restaurant backend is an essential component of a modern restaurant management system. It enables the restaurant to manage its data more efficiently, reduce errors, and provide better service to its customers. With a well-designed backend, a restaurant can streamline its operations and provide a more personalized and efficient experience to its customers.
## Installations

1. For Django-Backend API server

   1. Firstly Add a .env file as its needed by the Docker use [.env.sample](./restaurant-api/.env.sample)

   ```bash
   cd restaurant-api/
   touch .env
   cat .env.sample >> .env
   ```

   2. You can use the docker compose command to fire up a container
      below cmd 👇🏻

   ```bash
   docker compose -f "restaurant-api\docker-compose.yaml" up -d --build
   ```

   3. Standalone test server for testing or small production
      for virtual enviorment

   ```bash
   cd restaurant-api/
   python3 -m venv .venv
   source ./venv/bin/activate
   ```

   install and runing server

   ```bash
   pip install --upgrade pip
   pip install --no-cache-dir -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py runserver
   ```

2. For Front end Devlopment

   1. use Docker to get the best and error free install

   ```bash
   docker compose -f "restaurant-menu-front\docker-compose.yaml" up -d --build
   ```

   1. for testing and small props.

   ```bash
   npm i
   npm start
   ```
## Workflow

![App Screenshot](https://github.com/Zoronium/Deimos/blob/main/BackendWorkflow.png?raw=true)

## Deployment

https://Deimos-backend.zoronium.repl.co

![App Screenshot](https://blog.replit.com/images/new_logo/existing_logo.jpg?v=1664916455431
)


## API Reference

#### Get all items

```http
  GET /api/menu/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `product` | `string` | **Required**. Your all menu items |

#### Get item

```http
  GET /api/menu/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `number` | **Required**. Your menu product Id of item to fetch |

#### Get all categories

```http
  GET /api/cat/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `product` | `string` | **Required**. Your all categories |


## Frontend

Repo : https://github.com/Zoronium/Deimos

Deployment : https://deimos-cupdv0cej-zoronium.vercel.app/
