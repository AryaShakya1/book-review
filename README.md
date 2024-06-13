
# Book Review Platform Project

Create a platform where users can add books, write reviews for books, and rate them. The platform will include features for user roles, where admin users have additional privileges compared to normal users. Additionally, all reviews should be displayed under the respective book they are related to.

## Prerequisites

- Python 3.x
- Django 3.x or later
- pip (Python package installer)
- Node.js (v14.18.0 or later)
- npm (v6.14.15 or later) or yarn (v1.22.0 or later)

## Installation

Clone the repository

```bash
    git clone https://github.com/AryaShakya1/book-review.git
    cd book-review
```


### Backend Installation

Create a virtual environment

```bash
    python -m venv env
```

Activate the virtual environment

```bash
  .\env\Scripts\activate  # On Linux use source env/bin/activate
```

Install the required packages
```bash
    pip install -r requirements.txt
```
#### Environment Variables

To run this project, you will need to add the following environment variables to your .env file

Create a .env file in the root directory of the project and add the following environment variables:

```
JWT_SIGNING_KEY=your-signing-key
```

Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the Development Server:
```bash
python manage.py runserver
```

The application can be accessed at http://localhost:8000/
