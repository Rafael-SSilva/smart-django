# Backend

In the root folder (**smart-django**) simply run the command bellow to create the container. images, services and set them running.

```sh
docker componse up --build
```
If everything was ok, the backend service will be available at http://127.0.0.1
Also you can access the django admin painel with the credentials from the **.env ** file:

```
DJANGO_ADMIN_EMAIL=someuser@email.com
DJANGO_ADMIN_PASSWORD=some@password
```

# Frontend

Access the frontend folder and run the command bellow:

```sh
npm install 
npm run dev
```

Now the frontend server should be running on http://127.0.0.1:5173/.
You can login with the django admin credentials and also create new users to authenticate.

