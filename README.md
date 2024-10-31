# Futurama Hall of Fame

## Project Description

The **Futurama Hall of Fame** is a web application designed to showcase the beloved characters from the animated television series **Futurama**. This project extracts and displays comprehensive information about each character, providing fans and newcomers alike with a deeper insight into their favorite personalities from the show.

### Features

- **Character Profiles**: Each character is presented with essential information, including:
  - Name
  - Gender
  - Species
  - Occupation
  - Iconic quotes and catchphrases
  
- **User-Friendly Interface**: The application employs Bootstrap for a responsive and visually appealing layout, ensuring an enjoyable browsing experience across devices.

- **Custom Error Handling**: The application incorporates custom error pages for improved user experience, providing friendly messages in the event of server errors or not found pages.

- **Robust Testing**: The codebase includes thorough unit tests using both `pytest` and `django.test`, ensuring the reliability and stability of the application.
- **Logging Capability**: The application implements logging to capture important events and errors. This feature aids in monitoring application performance and debugging issues, providing valuable insights into the application's behavior in production.

### Purpose

This project serves as both a tribute to the iconic characters of **Futurama** and an opportunity to demonstrate my skills in web development, data handling, and testing. It showcases my ability to create an engaging user experience while adhering to best practices in software development.

### Technologies Used

- **Python** and **Django** for backend development
- **HTML**, **CSS**, **Javascript** and **Bootstrap** for frontend design
- **Faker** library for generating mock data
- **pytest** for testing

## Getting Started

These instructions will help you set up a copy of the **Futurama Hall of Fame** project on your local machine for development and testing purposes. Refer to the **Deployment** section for instructions on how to deploy the project in a live environment.

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python** (version 3.10.12 or higher)
- **pip** (Python package installer)

To install the required packages for production deployment, you can run:

```bash
pip install -r requirements.txt
```

For development and testing purposes, install the required packages from the `requirements-dev.txt` file:
```bash
pip install -r requirements-dev.txt
```

## Deployment

To get the application up and running:

1. Adjust the `settings.py` file according to your setup (e.g., allowed hosts, logging). 
2. Start the development server by running the following command in your terminal:
    ```bash
    python manage.py runserver
    ```
   This will run the application locally for development and testing purposes.
3. For deploying the project on a live system, follow the official Django deployment documentation: [Django Deployment Documentation](https://docs.djangoproject.com/en/5.1/howto/deployment/)

## Built With

* [Python 3.10.12](http://www.python.org/) - Developing with the best programming language.
* [Django 5.1.2](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.

## Authors
* **Vlasios Dimitriadis** - [Futurama: Hall of Fame - Github](https://github.com/bdimitriadis/futurama/)
