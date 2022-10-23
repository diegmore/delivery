# delivery-backend

## Develop environment setup

To deploy the backend project on a local environment, please follow these instructions:

### Requirements

- Git
- Python3
- PostgreSQL >= 10

### Clone project

Clone the project from GitHub:

`git clone https://github.com/diegmore/delivery.git`

Go to root folder:

`cd delivery`

### Virtual environment

Create a python virtual environment for this project:

`python3 -m virtualenv env`

If you don't have virtualenv, install it:

`python3 -m pip install virtualenv`

After installation is complete, activate the virtual environment:

| Linux                     | Windows 10               |
| ------------------------- | ------------------------ |
| `source env/bin/activate` | `.\env\Scripts\activate` |

### Environment variables

Make a copy of `.env.example`, rename it to `.env`, and change it according to you local configuration.

#### Linux

Import the variables in your `.env` file to your virtual environment:

`source .env`

#### Windows

Delete the `export` keyword from all the enviroment variables in your `.env` file.

> e.g. `export DB_DATABASE=delivery` &#8594; `DB_DATABASE=delivery`

### Database

If you haven't done so already, create an empty database on PostgreSQL.

Its name needs to match the one on the `DB_DATABASE` environment variable.

### Dependencies

Download project dependencies using pip:

`python -m pip install -r requirements.txt`

### Server configuration

After installing dependencies, run the following commands to set up the database and superuser:

`python manage.py migrate`

`python manage.py update_deliveryman_position`

### Start server

Finally, run the Django local server:

`python manage.py runserver`



# Consuming all endpoints 

To schedule a delivery order u need to make a POST request to the URL `http://localhost:8000/order/` with the next body

```json
{
    "delivery_man": 2,
    "delivery_date": "2022-10-22T20:05:00.000Z",
    "delivery_lat": 1,
    "delivery_long": 1,
    "destination_lat": 50,
    "destination_long": 50
}
```
If the delivery man has another scheduled order in the next hour it will return error

To list all orders requested in one specific day u need to make a GET request to the URL and with the next params `http://localhost:8000/order?orderedDate=YYYY-MM-DD`

To list the orders of a delivery man in a specific date u need to make a GET request to the URL and with the next params `http://localhost:8000/order/get-orders-by-deliveryman?orderedDate=YYYY-MM-DD&deliveryMan={deliverId}`


To get the nearest delivery man in a specific hour and coordinates u need to make a GET request to the URL and with the next params `http://localhost:8000/order/get-near-deliveryman?queryDate=YYYY-MM-DDTHH:mm:ssZ&queryLat={latitude}&queryLng={longitude}`

If you have any doubts please let me know in my email damc@hotmail.es

thanks

