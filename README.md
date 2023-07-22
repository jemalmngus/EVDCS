# EVDCs: Electronic Vehicle Deployment and Control System for Addis Ababa Taxi Services

EVDCs (Electronic Vehicle Deployment and Control System) is an innovative solution developed using Django, HTML, CSS, JavaScript, Django Rest Framework, and Arduino. It aims to optimize the deployment and control of electronic vehicles for Addis Ababa taxi services, with a focus on ensuring fair distribution of taxis and efficient fare management.

## Key Features:

1. **Electronic Vehicle Deployment:** The system facilitates the deployment of electronic vehicles for taxi services in Addis Ababa. It automates the process of assigning available electronic taxis to strategically located taxi stands throughout the city.

2. **Taxi Waiting Time Management:** EVDCs calculates and manages the waiting time for taxis at each taxi stand. It considers factors such as taxi availability, demand, and location proximity to ensure efficient and fair distribution of taxis among different areas of the city.

3. **Fare Distribution:** The system incorporates a fair fare distribution algorithm to calculate and manage taxi fares based on distance traveled, time taken, and other relevant factors. This ensures a transparent and equitable fare structure for both taxi drivers and passengers.

4. **Real-time Monitoring:** EVDCs provides real-time monitoring of the taxi fleet, allowing administrators to track the location, status, and performance of each electronic vehicle. This monitoring capability enables better fleet management and timely response to any issues or emergencies.

5. **Integration with Arduino:** The system integrates with Arduino-based hardware devices installed in each electronic taxi. This allows for remote control and monitoring of various taxi functionalities, such as locking/unlocking doors, managing charging, and collecting data for performance analysis.

6. **User-Friendly Interface:** EVDCs features a user-friendly web interface that enables taxi drivers, administrators, and passengers to access relevant information and perform necessary actions easily. The interface provides dashboards, maps, and intuitive controls for efficient navigation and management.

## Purpose and Goals:

EVDCs aims to promote the adoption of electronic vehicles in Addis Ababa's taxi services while ensuring fair distribution of taxis and efficient fare management. By leveraging Django, HTML, CSS, JavaScript, Django Rest Framework, and Arduino technology, this system revolutionizes the way electronic taxis are deployed, controlled, and monitored for the benefit of both drivers and passengers.

## Installation and Setup:

1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required packages from the `requirements.txt` file using `pip install -r requirements.txt`.
4. Configure the database settings in `settings.py`.
5. Run migrations with `python manage.py migrate`.
6. Start the development server with `python manage.py runserver`.

## How to Use:

1. Access the web application through a web browser using the provided URL.
2. Taxi drivers can log in to view their assigned taxis and manage their availability.
3. Administrators can access the dashboard to monitor the taxi fleet and manage taxi stands.
4. Passengers can use the system to find available taxis and estimate fares for their journeys.

## Contributing:

We welcome contributions from the community to enhance and improve EVDCs. If you find any issues or have new feature ideas, please open a GitHub issue or submit a pull request.



## Acknowledgments:

We extend our gratitude to the Django, HTML, CSS, JavaScript, Django Rest Framework, and Arduino communities for their valuable contributions, which made this project possible.

Thank you for your interest in EVDCs. Let's together revolutionize the taxi services with electronic vehicles and smart control systems!
