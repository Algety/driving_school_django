# GoDrive Driving school in Wales

This website is designed for an imaginery GoDrive Driving School, based in West Wales. It aims to attract new learners and support current learners by providing clear, accessible information about the school's driving lessons and instructors, and convinient functionality for lessons managing. The site features:
- A Home page introducing the various types of driving lessons available, including beginner sessions, refresher courses, and intensive driving programs.
- An Our Team page showcasing GoDrive’s certified instructors, their qualifications, and their unique approach to learner success.
- A Booking page where new users can easily schedule lessons online.
- A User`s Bookings page where registered learners can view, update, or cancel their existing lessons.
- An Authorisation section for users to register or log in to their personal accounts.

This website has been created as the third Milestone project for Code Institute's Web Application Development Course. 

![image]![Laptop](https://github.com/Algety/driving_school_django/blob/main/static/images/image-2.png)
![image]![Phone screen](https://github.com/Algety/driving_school_django/blob/main/static/images/image-1.png)

### View the live website [here](https://driving-school-django-4592c5b6512c.herokuapp.com/)
***  

## Site Goals
The primary goals of the GoDrive Driving School website are to:
- Attract more learners and increase lesson bookings.
- Establish credibility and trust with both prospective and existing learners.
- Strengthen brand recognition across Wales and beyond.
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
- As a nnew customer, I want a smooth booking process so I can reserve a lesson with minimal hassle.
#### Learner
- As a learner, I want to log in and view my upcoming driving lessons so I can keep track of my schedule.
- As a learner, I’d like to edit or cancel bookings if my availability changes.
#### Team mamber
- As a GoTeam member, I want to log in securely and manage lesson bookings to stay on top of scheduling.
- As a GoTeam member, I want to view, add, update, or delete lessons to reflect current availability.
- As a GoTeam member, I want the ability to update site content (like lesson types or instructor bios) without needing technical support.


## Design
### Website Structure
The GoDrive Driving School website consists of four primary pages: Home Page, Our Team, Booking a Lesson Page, and User's Bookings. The default landing page is the Home Page, which includes a navigation bar and a consistent footer across all pages for easy access and site-wide cohesion.
The Home Page welcomes visitors with an engaging banner and an overview of the different lesson types offered, such as manual and automatic driving lessons, motorway driving lessons, Pass Plus course, intensive training, and refresher courses. It also links to instructor profiles and the booking system via the top navigation menu.
The Our Team page introduces GoDrive’s certified driving instructors, offering insight into their experience, teaching approach, helping visitors feel confident in their choice of instructor.
The Booking Page allows new users to select a location (Cardigan, Carmarthen, Aberystwyth), lesson date, and time slot through a dynamic booking form. Prefilled values and validation features enhance usability and reduce friction in the booking process.
After a booking is submitted, users are redirected to the User`s Bookings page, where they can view, edit, or delete upcoming lessons. The site also displays real-time success messages after actions like booking or cancellation, further improving the experience.
Additionally, the site includes an admin panel, empowering GoDrive team members to manage content without external technical support. This panel allows:
- Easy content updates across different site sections, the ability to post new content blocks with or without images, depending on the context.
- Rich-text editing with Summernote, enabling styled formatting for text-based updates.
- An intuitive database of students and bookings, giving administrators direct oversight of lesson schedules.

### Database Design
![Alt text](https://github.com/Algety/driving_school_django/blob/main/static/images/tables scheme.png)


## Credits
### Content
1. The icons - [Font Awesome](https://fontawesome.com/)
2. The logo and favicon created with help [Logo Design](https://logodesign.ai/)
3. Favicon sized with [Favicon Io](https://favicon.io/favicon-converter/)
4. Free images and AI generating - [Freepik](https://www.freepik.com/)
5. Image resizer - [Imageresizer](https://imageresizer.com/)
### Code
1. Code samples have been adapted specifically for the site - [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/), Code Institute lectures code.