# Food-Sharing-Platform
A food-sharing platform connects people to reduce food waste and fight hunger by sharing surplus food. Users can post, browse, and request items via an app or website, with features like geolocation and scheduling. It fosters community, promotes sustainability, and redistributes excess food to those in need, creating a positive social impact.

## Features
- User authentication (Signup/Login/Logout).
- Role-based dashboards (Donors and Recipients).
- Add and view food items for donation.
- Google Maps integration to find nearby donors/recipients.
- Notifications for food requests and status updates.
- Responsive and user-friendly design.

## Setup Instructions

### Clone the Repository
git clone https://github.com/jashwanthbavandlapalli/Food-Sharing-Platform.git
cd Food-Sharing-Platform

### Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate # On Windows: env\Scripts\activate

### Install Dependencies
pip install -r requirements.txt

### Set Up the Database
python manage.py makemigrations
python manage.py migrate

### Run the Development Server
python manage.py runserver

### Access the Application Open your browser and go to 
http://127.0.0.1:8000/

## Usage

- Sign Up as a Donor or Recipient.
- Login to access your dashboard.
- Donors: Add food items with details like name, quantity, and location.
- Recipients: Browse available food and request donations.
- Use the Google Maps feature to locate nearby food-sharing opportunities.

## Contributing
We welcome contributions to improve this platform. Please follow these steps:

- Fork the repository.
- Create a new branch for your feature/bugfix.
- Commit your changes and push them to your branch.
- Open a pull request.

## License
This project is licensed under the MIT License.

## Contact
* Creator: Jashwanth Bavandlapalli
* Email: jashwanthbavandlapalli@gmail.com

