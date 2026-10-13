# Django Master Course — Cars Project

A learning project developed while following the Django Master course. Built with Python, Django, and PostgreSQL, this application provides car inventory management functionality, including CRUD operations, authentication, inventory statistics, and AI-powered car descriptions using the OpenAI API.

The project was deployed to AWS EC2, covering Linux server configuration, production application serving, web server integration, and infrastructure backup.

## Technologies

- Python
- Django
- PostgreSQL
- Django ORM
- HTML and CSS
- OpenAI API (GPT-4.1 nano)
- AWS EC2
- Ubuntu Server
- Nginx
- uWSGI
- Unix sockets
- systemd
- Git and GitHub

## Topics Covered

- Django project and app structure
- Models and Django Admin
- Database migrations
- URLs, Views, and Templates
- Django ORM and database queries
- Forms and ModelForms
- File and image uploads
- Class-Based Views (CBVs)
- CRUD operations
- User authentication and authorization
- Django signals
- Database aggregation with `Sum`
- Reusable functions and code refactoring
- OpenAI API integration
- Environment variables for API key management
- Automated car description generation
- Git branching, commits, and pull requests
- AWS EC2 instance configuration
- Ubuntu Server administration
- PostgreSQL production configuration
- Nginx and uWSGI integration
- Application serving through a Unix socket
- systemd service configuration
- Static public IP configuration
- EC2 image backup using Amazon Machine Images (AMI)

## Progress

### Project Setup

- [x] Django project created
- [x] Cars app created
- [x] Database migrations applied
- [x] Django superuser created
- [x] PostgreSQL database configured

### Models and Admin

- [x] Car model implemented
- [x] Admin configuration
- [x] Car data validation
- [x] Car photo upload support
- [x] Car description/bio fields

### Views, Templates, and Forms

- [x] URL routing configured
- [x] Template-based views implemented
- [x] Cars listing page
- [x] Car details page
- [x] Car registration page
- [x] Car photo registration
- [x] ModelForm implementation
- [x] Class-Based Views refactoring
- [x] Car creation
- [x] Car details
- [x] Car update
- [x] Car deletion
- [x] Car photo display and fallback handling
- [x] Form and field validation

### Authentication and Authorization

- [x] User authentication requirements
- [x] Restricted car creation to authenticated users
- [x] Restricted car updates to authenticated users
- [x] Restricted car deletion to authenticated users
- [x] Access control for car management pages

### Database and Business Logic

- [x] Django ORM queries
- [x] Inventory statistics
- [x] Aggregate calculations using `Sum`
- [x] Total number of cars calculation
- [x] Total inventory value calculation
- [x] Reusable functions for business logic
- [x] Django signals: `pre_save`, `post_save`, `pre_delete`, and `post_delete`

### OpenAI Integration

- [x] OpenAI API client created
- [x] GPT-4.1 nano integration
- [x] Automated car description generation
- [x] Description length limited to 250 characters
- [x] API key loaded through environment variables

### Development Workflow

- [x] Git version control
- [x] Feature branches
- [x] Conventional commits
- [x] Pull requests
- [x] Feature development and refactoring through pull requests

### AWS Deployment

- [x] AWS EC2 instance created
- [x] Ubuntu Server configured
- [x] SSH access configured
- [x] Git access configured on the server
- [x] Python application environment configured
- [x] PostgreSQL configured on the server
- [x] Django application deployed
- [x] uWSGI configured as the application server
- [x] Unix socket configured for Nginx and uWSGI communication
- [x] Nginx installed and configured
- [x] Static file serving configured
- [x] systemd service configured for application management
- [x] Static public IP configured
- [x] EC2 image backup created

## Project Goals

- Practice Django development through a practical project.
- Build a complete car inventory management application.
- Apply authentication, authorization, and database operations.
- Integrate external APIs into a Django application.
- Develop good software engineering practices using Git and GitHub.
- Gain practical experience deploying Django applications to AWS.
- Strengthen backend development, Linux, database, and cloud infrastructure skills.
- Progress toward building and maintaining production-ready web applications.
