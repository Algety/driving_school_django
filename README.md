# GoDrive Driving school in Wales

This website is designed for an imaginary GoDrive Driving School, based in West Wales. It aims to attract new learners and support current learners by providing clear, accessible information about the school's driving lessons and instructors, and convenient functionality for managing lessons. The site features:
- A Home page introducing the various types of driving lessons available, including beginner sessions, refresher courses, and intensive driving programs.
- An Our Instructors page showcasing GoDrive’s certified instructors, their qualifications, and their unique approach to learner success.
- A Booking page where new users can easily schedule lessons online.
- A User's Bookings page where registered learners can view, update, or cancel their existing lessons.
- An Authorisation section for users to register or log in to their personal accounts.

This website has been created as the third Milestone project for Code Institute's Web Application Development Course. 

![Laptop](https://github.com/Algety/driving_school_django/blob/main/static/images/image-2.png)
![Phone screen](https://github.com/Algety/driving_school_django/blob/main/static/images/image-1.png)

### View the live website [here](https://driving-school-django-4592c5b6512c.herokuapp.com/)
***  

## Site Goals
The primary goals of the GoDrive Driving School website are to:
- Attract more learners and increase lesson bookings.
- Establish credibility and trust with both prospective and existing learners.
- Strengthen brand recognition across local area and Wales (with perspective of opening new branches across the UK).
- Provide the GoDrive team with a convenient tool for maintaining content, tracking learners, and organizing bookings.

To achieve these goals, the site should:
- Engage visitors with clear, inviting content and eye-catching visuals that showcase lesson types and instructor expertise.
- Foster confidence by offering transparent, detailed information about driving lessons, pricing, and scheduling.
- Make it easy for users to register, log in, and reserve or manage bookings through an intuitive and responsive interface.
- Empower administrators with tools to easily update the site’s content, maintain a database of learners, and efficiently manage scheduling and reservations without technical support.


## User Experience - UX
### User stories
#### Potential Customer
- As a new customer, I want to easily explore the different types of driving lessons offered so I can find one that suits my level and needs.
- As a new customer, I want to learn about the driving instructors so I can feel confident in their experience and teaching style.
- As a new customer, I want a smooth booking process so I can reserve a lesson with minimal hassle.
#### Learner
- As a learner, I want to log in and view my upcoming driving lessons so I can keep track of my schedule.
- As a learner, I’d like to edit or cancel bookings if my availability changes.
#### Team member
- As a GoDrive team member, I want to log in securely and manage lesson bookings to stay on top of scheduling.
- As a GoDrive team member, I want to view, add, update, or delete lessons to reflect current availability.
- As a GoDrive team member, I want the ability to update site content (like lesson types or instructor bios) without needing technical support.


## Design
### Website Structure
The GoDrive Driving School website consists of four primary pages: Home Page, Our Instructors, Book Your Lesson Page, and User's Bookings. The default landing page is the Home Page, which includes a navigation bar and a consistent footer across all pages for easy access and site-wide cohesion. The navbar is fixed at the top, so when a user is scrolling down a page, the navbar and the book a lesson button stay visible and available all the time.
The Home Page welcomes visitors with an engaging banner and an overview of the different lesson types offered, such as manual and automatic driving lessons, motorway driving lessons, Pass Plus course, intensive training, and refresher courses. It also links to instructor profiles and the booking system via the top navigation menu.
The Our Instructors page introduces GoDrive’s certified driving instructors, offering insight into their experience, teaching approach, helping visitors feel confident in their choice of instructor.
The Booking Page allows new users to select a location (Cardigan, Carmarthen, Aberystwyth), lesson date, and time slot through a dynamic booking form. Prefilled values and validation features enhance usability and reduce friction in the booking process.
After a booking is submitted, users are redirected to the User's Bookings page, where they can view, edit, or delete upcoming lessons.
The site also displays real-time success messages after actions like booking or cancellation, further improving the experience.
Additionally, the site includes an admin panel, empowering GoDrive team members to manage content without external technical support. This panel allows:
- Easy content updates across different site sections, the ability to post new content blocks with or without images, depending on the context.
- Rich-text editing with Summernote, enabling styled formatting for text-based updates.
- An intuitive database of students and bookings, giving administrators direct oversight of lesson schedules.

### Database Design
![ERD](https://github.com/Algety/driving_school_django/blob/main/static/images/ERD_driving_school.jpeg)

## Planned Scope of Work for future implementation
The project will be expanded to include instructor-specific lesson bookings, with the option to choose a lesson type:

### 1. Instructor Integration
- A new **Instructors app** will be created to manage a list of instructors.  
- The app will store and manage details for each instructor (first and last name, contact info, photo, availability, specialization, and experience).
- Instructor’s blocks on the *Our Instructors* page will display the details stored in the Instructors app.
- A **“Book a Lesson”** button will be added at the end of each instructor’s block on the *Our Instructors* page, allowing users to book a lesson with a specific instructor.   

### 2. Booking System Extension
- The **LessonBooking** model will be extended with an instructor field - a foreign Key to **Instructor** model to create a **one-to-many relationship**: one instructor can have many bookings.  
- Users will be able to select a specific instructor when booking a lesson.  
- Validation Logic will be added to prevent booking of more than one lesson with the same instructor in the same time slot. 

### 3. Lesson Type Selection
- A new field **lesson type** (e.g., theory, practical, refresher) will be added to the **LessonBooking** model and the booking form, with a list of lesson types. Booking a lesson, a user will be able to choose a type of a lesson (optionally). 

### 4. Time Slot Availability
- On the *Book a Lesson* page, the booking form will show only available time slots for the user to select.

## Testing
### Responsiveness
The project was tested using the Chrome Developer Tools and Amiresponsive site to verify responsiveness of the site.

Devices tested using the Google Developer Tools emulator:
iPhone XR
iPhone 12 Pro
iPhone 14 Pro Max
Pixel 7
Samsung Galaxy S8+
Samsung Galaxy S20 Ultra
iPad Mini
iPad Air
iPad Pro
Surface Pro 7
Surface Duo
Galaxy Z Fold 5
Asus Zenbook Fold
Samsung Galaxy A51/71
Nest Hub
Nest Hub Max


![Responsiveness](https://github.com/Algety/driving_school_django/blob/main/static/images/responsive_check.jpg)
![Responsiveness](https://github.com/Algety/driving_school_django/blob/main/static/images/responsive_check_2.jpg)
![Responsiveness](https://github.com/Algety/driving_school_django/blob/main/static/images/responsive_check_3.jpg)

All the pages of the site are displayed correctly on different devices.

### HTML, CSS and JS Validation
The W3C Markup Validator and W3C CSS Validator services were used to validate the project's pages for syntax errors. The screenshots below provide the results of testing.

### Performance Accessibility and SEO
Google Lighthouse was used to test Performance, Best Practices, Accessibility and SEO.

### 

## Deployment

### Local Setup
For this project a PostgreSQL database is used.

**Prerequisites:**
- Python 3.x, Git, and PostgreSQL installed and running  
- Recommended: create a virtual environment for the project  

1. Clone or fork this repository to create a local copy on your machine.  
2. Create and activate a virtual environment:  
   - Windows: python -m venv .venv then .\.venv\Scripts\activate  
   - macOS/Linux: python3 -m venv .venv then source .venv/bin/activate  
3. Install the Python dependencies listed in requirements.txt with the command: pip install -r requirements.txt  
4. In PostgreSQL, create a database and user.  
5. Create a new file env.py at the root level and add environment variables:  
import os
    os.environ['SECRET_KEY'] = '<your-secret-key>'
    os.environ['DATABASE_URL'] = 'postgresql://user:pass@localhost:5432/dbname'
    os.environ['CLOUDINARY_URL'] = 'cloudinary://API_KEY:API_SECRET@CLOUD_NAME'  
6. Install the packages required to connect to PostgreSQL and update requirements.txt: pip install dj-database-url~=0.5 psycopg2~=2.9 then pip freeze --local > requirements.txt  
7. In settings.py, connect to env.py:  
   import dj_database_url  
   if os.path.isfile('env.py'): import env  
8. Remove or comment out the default SQLite configuration.  
9. Configure the database to use the DATABASE_URL environment variable: DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}  
10. Add env.py to .gitignore.  
11. Ensure env.py is loaded before Django settings by importing it at the top of manage.py, wsgi.py, and asgi.py.  
12. Run migrations: python manage.py makemigrations and python manage.py migrate  
13. Create a superuser: python manage.py createsuperuser  
14. Start the Django app: python manage.py runserver  
    - Stop the app with CTRL+C (⌘+C on Mac).  
    - To run it again, use the same command: python manage.py runserver  

### Heroku Deployment
1. Sign in to Heroku, click New → Create New App, choose a region, and click Create.  
2. In the Settings tab, reveal Config Vars. Add a key DISABLE_COLLECTSTATIC with value 1.  
3. Install a production webserver: pip install gunicorn~=20.1  
4. Update requirements.txt: pip freeze --local > requirements.txt  
5. Create a file named Procfile (no extension) in the project root. Add: web: gunicorn driving_school.wsgi 
6. In settings.py, add the Heroku app hostname to ALLOWED_HOSTS: ALLOWED_HOSTS = ['app-name.herokuapp.com']  
7. Set DEBUG = False in settings.py.  
8. Push changes to GitHub: git add . , git commit -m "Prepare for Heroku deployment" , git push  
9. On Heroku, go to Deploy → Deployment Method and select GitHub.  
10. Connect your GitHub repository in the Connect to GitHub section.  
11. Under Manual Deploy, select the main branch and click Deploy Branch.  
12. In the Resources tab, enable an Eco Dyno (free tier).  
13. Verify there is no conflicting Postgres add-on if you are using your own database.  
14. Click Open App to view your deployed project.  


## Credits
### Content
1. The icons - [Font Awesome](https://fontawesome.com/)
2. The logo and favicon created with help [Logo Design](https://logodesign.ai/)
3. Favicon sized with [Favicon Io](https://favicon.io/favicon-converter/)
4. Free images and AI generating - [Freepik](https://www.freepik.com/)
5. Image resizer - [Imageresizer](https://imageresizer.com/)
6. ERD (Entity Relationship Diagram) of the models created with help [Lucid.app](https://lucid.app/)

### Code
1. Code samples have been adapted specifically for the site - [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/), Code Institute lectures code.