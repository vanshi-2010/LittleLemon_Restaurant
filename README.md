# LittleLemon_Capstone
Capstone Project for Little Lemon 

You will need to update the DB credentials as required to use your local DB

NOTE: Please enter your own database details, create users and tokens manually or through apis. 

## Endpoints to test 
### Users

* GET http://127.0.0.1:8000/auth/users/ - Lists User (only returns authenticated user)
* POST http://127.0.0.1:8000/auth/users/ - Creates User 
    * Example Body:
    ```json
        {
            "email": "test@test.com",
            "username": "test",
            "password": "testpassword"
        }
    ```

### Token

* POST http://127.0.0.1:8000/restaurant/api-token-auth
    * Example Body:
    ```json
        {
            "username": "test",
            "password": "testpassword"
        }
    ```

### Menu
* GET http://127.0.0.1:8000/restaurant/menu - Lists all menu items
* GET http://127.0.0.1:8000/restaurant/menu/1 - Get specfic menu item
* POST http://127.0.0.1:8000/restaurant/menu - Creates menu item
    * Example Body:
    ```json
        {
                "title": "Test Item",
                "price": 5.45,
                "inventory": 1000
        }
    ```
* PUT http://127.0.0.1:8000/restaurant/menu/1 - Updates menu item
    * Example Body:
    ```json
        {
                "title": "Updated Test Item",
                "price": 1.45,
                "inventory": 10
        }
    ```
* DELETE http://127.0.0.1:8000/restaurant/menu/1 - Deletes menu item

### Bookings
* GET http://127.0.0.1:8000/restaurant/booking/tables - Lists bookings
* POST http://127.0.0.1:8000/restaurant/booking/tables - Creates Booking
    * Example Body:
    ```json
        {
            "name": "Test",
            "no_of_guests": 1,
            "booking_date": "2024-06-14T12:00:00Z"
        }
    ```
* GET http://127.0.0.1:8000/restaurant/booking/tables/1 - Gets booking by ID
* PUT http://127.0.0.1:8000/restaurant/booking/tables/1 - Updates Booking
    Example Body:
    ```json
        {
            "name": "Lennys",
            "no_of_guests": 5,
            "booking_date": "2024-06-18T12:00:00Z"
        }
    ```
* DELETE http://127.0.0.1:8000/restaurant/booking/tables/1 - Deletes Booking

## Run Unit tests

```python manage.py test```
