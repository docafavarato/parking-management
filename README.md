# Parking management

# About
A complete functional parking management system built with Java (Spring) and Python (Flask).<br><br>
The API repository is <a href="https://github.com/docafavarato/parking-management-api">here</a>

# Functions
## Dashboard
![image](https://github.com/docafavarato/parking-management/assets/98183878/aaaa58dd-581d-4e1b-91e7-814f83afc63a)
The dashboard section show some status of the establishment, such as:
- Registered cars
- Active parkings
- Available parking lots
- Today total earnings
- Pending payments
## Parkings
![image](https://github.com/docafavarato/parking-management/assets/98183878/5911eeed-3119-4dd5-bfa8-221fb22242b7)
The "Add a parking" section contains a form that creates a new parking based on the following attributes:
- Start time
- Car
- Parking lot
- Rate

![image](https://github.com/docafavarato/parking-management/assets/98183878/8c9b2909-de8c-4309-8af9-592c0fad74d7)
The "Manage parkings" section contains a table with the attributes of all the registered parkings and two buttons, one to erase the parking and one to end it. It also has a "filter by" option with the following params:
- Going
- Ended
- All
## Lots
![image](https://github.com/docafavarato/parking-management/assets/98183878/8b46bbf3-4f3b-483f-b169-fc3ea2e30f91)
The "Add a parking lot" section contains a form that creates a new parking lot based on the following attribute:
- Tag

![image](https://github.com/docafavarato/parking-management/assets/98183878/8e68e53a-5bdd-45ba-996c-037619b2b203)
The "Manage parking lots" section contains a table with the attributes of all the registered parking lots and two buttons, one to erase the parking lot and one to edit it. It also has a "filter by" option with the following params:
- Occupied
- Unoccupied
- All
## Cars
![image](https://github.com/docafavarato/parking-management/assets/98183878/8899cda4-3410-495e-9757-7271964ba764)
The "Add a car" section contains a form that creates a new car based on the following attributes:
- License plate
- Brand
- Model
- Color

![image](https://github.com/docafavarato/parking-management/assets/98183878/4802dbab-97c0-483a-9233-1d30afc52f39)
The "Manage cars" section contains a table with the attributes of all the registered cars and three buttons, one to erase the parking lot, one to edit it and one to check all the parkings related to it.
## Payments
![image](https://github.com/docafavarato/parking-management/assets/98183878/ebd64311-24e4-4814-a73b-f7b48d1cd3c3)
The "Manage payments" section contains a table with the attributes of all the registered payments and two buttons, one to erase the payment and one to complete the payment if it's pending.
