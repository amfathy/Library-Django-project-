# Library System

## Overview

The Library System is a Django-based web application designed to manage book inventory, user accounts, and borrowing activities. It provides a user-friendly interface for both administrators and students, with different levels of access and functionality.

## Features

- **User Authentication**: Sign up, log in, and manage user profiles.
- **Role-Based Access**: Differentiates between admin and student roles with appropriate permissions.
- **Book Management**: Admins can add, update, and view books.
- **Search Functionality**: Users can search for books by various criteria.
- **User Dashboard**: Personalized views for logged-in users and admins.

## URL Configuration

The application uses the following URL patterns:

- **Home**: `/` - Login page for users.
- **Logout**: `/logout` - Logout the current user.
- **Add Book**: `/addBook` - Admin interface to add new books.
- **Admin Home**: `/adminhome` - Admin dashboard.
- **Admin Login**: `/adminn` - Login page for admin users.
- **Borrow**: `/borrow` - Page for borrowing books.
- **Period**: `/period` - Page for borrowing periods.
- **Profile**: `/profile` - User profile page.
- **Show Books**: `/showbooks` - View and search books.
- **Signup**: `/signup` - Signup page with options.
- **Student Signup**: `/studentsignup` - Signup page for students.
- **Admin Signup**: `/adminsignup` - Signup page for admins.
- **Update Profile**: `/updateform` - Update user profile and password.
- **Update Book**: `/<int:id>` - Update book details by ID.
- **Search**: `/search` - Search functionality for books.

## Views

The following views handle the respective functionalities:

- **`admin`**: Authenticates and logs in an admin user.
- **`borrow`**: Displays the borrowing page (for logged-in users).
- **`user_login`**: Handles user login.
- **`period`**: Displays borrowing periods.
- **`profile`**: Displays user profile (restricted to logged-in users).
- **`showbooks`**: Displays and searches books.
- **`signup`**: Provides signup options.
- **`updateform`**: Handles profile and password updates.
- **`addBook`**: Allows admins to add new books.
- **`adminhome`**: Displays the admin home page.
- **`updateBook`**: Updates book details.
- **`logout_user`**: Logs out the current user.
- **`studentsignup`**: Handles student signup.
- **`adminsignup`**: Handles admin signup.
- **`search`**: Displays the search page.

## Usage

1. **Login**:
    - Navigate to `/` to log in.

2. **Manage Books**:
    - Admins can manage books through `/addBook` and update them using `/<int:id>`.

3. **Search for Books**:
    - Use `/showbooks` and the search bar to find books by author, ISBN, or publication year.

4. **User and Admin Signup**:
    - Access signup options at `/signup`, and choose between student or admin signup.

5. **Profile Management**:
    - Update user profile and password at `/updateform`.

