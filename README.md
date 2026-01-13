Task 1: Set up Laravel project locally with database

Download & extract the Laravel project

Link: Laravel project zip

Extract to a folder inside C:\xampp\htdocs\your_project_name.

Set up database

Open phpMyAdmin (http://localhost/phpmyadmin)

Create a new database, e.g., laravel_db

Import the SQL file:

project_folder/db/db.sql


Configure Laravel to use the database

Open .env file in Laravel project folder

Update these lines with your database info:

DB_DATABASE=laravel_db
DB_USERNAME=root
DB_PASSWORD=


Save the file.

Install dependencies

Open CMD in the project folder

Run:

composer install


Generate application key

php artisan key:generate


Serve the Laravel project

php artisan serve


This will give a URL like http://127.0.0.1:8000

Open it in a browser → you should see the login page

Take a screenshot (closure of Task 1)

Task 2: Selenium script to automate login

Here’s a Python Selenium script that opens the login page, fills random values, and exits:

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

# Generate random email and password
def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

email = f"{random_string()}@example.com"
password = random_string()

# Path to your ChromeDriver
driver_path = "C:/path/to/chromedriver.exe"  # update this

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("http://127.0.0.1:8000")  # Laravel login page URL

time.sleep(2)

# Fill email and password fields (update selectors if needed)
driver.find_element(By.NAME, "email").send_keys(email)
driver.find_element(By.NAME, "password").send_keys(password)

time.sleep(2)
driver.quit()


✅ This script does exactly what you requested: fills random credentials and exits.

Task 3: Integrate HTML calendar template into Laravel

Download & extract HTML template

Link: HTML template zip

Extract to a folder.

Move calendar HTML into Laravel

Copy:

html/vertical-menu-template/app-calendar.html


Paste as:

resources/views/html-page.blade.php


Move assets to public folder

Create folder: public/calendar-assets

Copy:

assets/css → public/calendar-assets/css
assets/js → public/calendar-assets/js
assets/images → public/calendar-assets/images


Update all <link> and <script> paths in html-page.blade.php to use Laravel asset():

<link rel="stylesheet" href="{{ asset('calendar-assets/css/style.css') }}">
<script src="{{ asset('calendar-assets/js/app.js') }}"></script>


Add Laravel route

In routes/web.php:

Route::get('/html-page', function() {
    return view('html-page');
});


Access in browser:

http://127.0.0.1:8000/html-page


You should see the calendar page live in Laravel
