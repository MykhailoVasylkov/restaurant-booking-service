# Napoli Restaurant

## Overview
Napoli Restaurant is a web site designed to streamline the reservation process for users at Napoli Restaurant. The system allows users to explore the menu, view contact information, check working hours, and find the restaurant’s location on the map. Customers have the ability to register, make reservations, view, edit, and delete their bookings and reviews. It aims to provide a smooth and convenient user experience.

## Responsive Mockup
![Responsive Mockup](/static/images/readme/am_i_responsive.jpg)

## Features
### Existing Features
#### Features overview
- **User Registration and Authentication**: Users can create an account and log in to manage their reservations and reviews.
- **Online Table Reservation**: Users can choose a date, time, and the number of guests to make a reservation.
- **Menu View**: Users can browse the current restaurant menu.
- **Reviews and Ratings**: Customers can leave reviews and ratings for their dining experience.

#### Main Page

- **Navigation Bar**:
Featured on all four pages, the fully responsive navigation bar includes links to the Logo, Home page, Menu, Booking, and Contact Us page. It is identical across all pages, ensuring consistent and easy navigation. This section enables users to smoothly move from one page to another across all devices, without the need to use the ‘back’ button to return to previous pages. Additionally, it displays the user's current status, such as whether they are logged in or logged out, allowing for seamless interaction with the site.
##### Navigation Bar (Desktop)
![Nav Bar Desktop](/static/images/readme/main/nav_bar_d.jpg)
##### Navigation Bar (Mobile)
![Nav Bar Mobile](/static/images/readme/main/nav_bar.jpg)

- **Hero Section**: Contains a background video, shor description, with two buttons: "View Menu" and "Book a Table".
##### Hero Section (Desktop)
![Hero Section Desktop](/static/images/readme/main/hero_section_d.jpg)
##### Hero Section (Mobile)
![Hero Section Mobile](/static/images/readme/main/hero_section.jpg)

- **About Section**: Includes description of Napoli Restaurant and a photo carousel displaying images related to the restaurant.
##### About Section (Desktop)
![About Section Desktop](/static/images/readme/main/about_section_d.jpg)
##### About Section (Mobile)
![About Section Mobile](/static/images/readme/main/about_section.jpg)

- **CTA Section**: Features call to action text and a parallax background image with a "Book a Table" button.
##### CTA Section (Desktop)
![CTA Section Desktop](/static/images/readme/main/cta_d.jpg)
##### CTA Section (Mobile)
![CTA Section Mobile](/static/images/readme/main/cta.jpg)

- **Footer**: Includes the Logo (which is a link to the main page), contact info, working hours, social links, and navigation to the menu, booking, and contact us sections.
##### Footer Section (Desktop)
![CTA Footer Desktop](/static/images/readme/main/footer_d.jpg)
##### Footer Section (Mobile)
![CTA Footer Mobile](/static/images/readme/main/footer.jpg)

#### Menu Page
- **Menu Nav Bar**: A fixed navigation bar that moves down with scrolling. Each category links to the corresponding section of the menu.
##### Menu Nav Bar (Desktop)
![Menu Nav Bar Desktop](/static/images/readme/menu/menu_nav_d.jpg)
##### Menu Nav Bar (Mobile)
![Menu Nav Bar Mobile](/static/images/readme/menu/menu_nav.jpg)

- **Menu Section**: Displays separated categories of the menu, each containing dish cards.
##### Menu Section (Desktop)
![Menu Section Desktop](/static/images/readme/menu/menu_section_d.jpg)
##### Menu Section (Mobile)
![Menu Section Mobile](/static/images/readme/menu/menu_section.jpg)

- **Dish Cards**: Each card includes a photo, dish name, price, and description. A "View Details" button opens a modal, which can be closed.
##### Dish Cards (Desktop)
![Dish Cards Desktop](/static/images/readme/menu/dish_modal_d.jpg)
##### Dish Cards (Mobile)
![Dish Cards Mobile](/static/images/readme/menu/dish_modal.jpg)

#### Booking Page
- **CTA Section**: Includes information why client should reserv a table and a button to "Reserve", which takes users to the booking form. The section has a parallax background image.
##### CTA Section (Desktop)
![CTA Section Desktop](/static/images/readme/booking/cta_booking_d.jpg)
##### CTA Section (Mobile)
![CTA Section Mobile](/static/images/readme/booking/cta_booking.jpg)

- **Your Reservations Section**: Displays the logged-in user's reservation cards, with options to edit or delete. When deleting, a confirmation modal appears. The reservation card shows the date and time of booking, reservation details, and booking status (Pending, Confirmed, Cancelled, Expired).
##### Your Reservations Section(Desktop)
![Your Reservations Section Desktop](/static/images/readme/booking/your_reservtion_section_d.jpg)
##### Your Reservations Section (Mobile)
![Your Reservations Section Mobile](/static/images/readme/booking/your_reservtion_section.jpg)
##### Your Reservations Section Delete Modal
![Your Reservations Section Delete Modal](/static/images/readme/booking/your_reservtion_delete_modal.jpg)

- **Table Reservation Form**: Includes fields such as Client (auto-populated based on login info), Phone Number, Date (min date: today), Time (restricted by working hours), Number of People, Number of Tables (calculated automatically), and a Comment field. Users can submit the reservation form.
##### Table Reservation Form(Desktop)
![Table Reservation Form Desktop](/static/images/readme/booking/reservation_form_d.jpg)
##### Table Reservation Form (Mobile)
![Table Reservation Form Mobile](/static/images/readme/booking/reservation_form.jpg)

#### Contact Us Page
- **Contact Section**: 
  1) Embedded Google Map with a shop label marker. Clicking the label opens a modal with contact info and a popup asking users if they want to be redirected to Google Maps for directions.
  2) "Get in Touch" section with contact details.
  3) "Open Hours" section displaying the restaurant’s working hours.
##### Contact Section (Desktop)
![Contact Section](/static/images/readme/contact/contact_section_d.jpg)
##### Contact Section (Mobile)
![Contact Section](/static/images/readme/contact/contact_section.jpg)

- **Review Form**: Only logged-in users can leave reviews. The form includes a rating field (stars) and a review body with a submit button.
##### Review Form (Desktop)
![Review Form](/static/images/readme/contact/review_form-d.jpg)
##### Review Form (Mobile)
![Review Form](/static/images/readme/contact/review_form.jpg)

- **Star Rating Functionality**
The review form includes a star rating field where users can rate their experience with the restaurant. The rating is displayed as five stars. 

1) Hover Effect: When the user hovers over a star, it turns yellow to indicate which star they are about to select.
2) Selection Effect: Once the user clicks on a star, it turns gold to indicate their final selection. The stars that the user selects will remain gold, representing the rating they have chosen.
##### Star Rating Functionality (Desktop)
![Star Rating Functionality](/static/images/readme/contact/stars-function.jpg)

- **Your Reviews Section**: Displays the user’s reviews with options to edit and delete. Deleting a review prompts a confirmation modal.
##### Your Reviews Section (Desktop)
![Your Reviews Section](/static/images/readme/contact/user_reviews_d.jpg)
##### Your Reviews Section (Mobile)
![Your Reviews Section](/static/images/readme/contact/user_reviews.jpg)
##### Your Reviews Delete Modal (Mobile)
![Your Reviews Delete Modal](/static/images/readme/contact/user_reviews_delete_modal.jpg)

- **Recent Reviews Section**: Displays reviews left by all users.
##### Recent Reviews Section (Desktop)
![Recent Reviews Section](/static/images/readme/contact/all_reviews_d.jpg)
##### Recent Reviews Section (Mobile)
![Recent Reviews Section](/static/images/readme/contact/all_reviews.jpg)

#### Logout Page
- **Sign Out Button**: A button to log out the user from the site.
##### Sign Out Button (Desktop)
![Sign Out Button](/static/images/readme/log/logout_d.jpg)
##### Sign Out Button (Mobile)
![Sign Out Button](/static/images/readme/log/logout.jpg)

#### Login Page
- **Sign In Form**: Includes fields for username and password, a "Remember Me" option, and a sign-in button.
##### Sign In Form (Desktop)
![Sign In Form](/static/images/readme/log/login_page_d.jpg)
##### Sign In Form (Mobile)
![Sign In Form](/static/images/readme/log/login_page.jpg)

#### Register Page
- **Sign Up Form**: Includes fields for Username, Email (optional), Password, and a "Sign Up" button.
##### Sign Up Form (Desktop)
![Sign Up Form](/static/images/readme/log/restration_page_d.jpg)
##### Sign Up Form (Mobile)
![Sign Up Form](/static/images/readme/log/restration_page.jpg)

#### Restrictions for Unregistered Users
- **Booking a Table**: Unregistered users cannot make reservations. They must log in to book a table.

![Booking a Table](/static/images/readme/logout_permissions/booking_page_log_out.jpg)

- **Leaving a Review**: Only registered and logged-in users are allowed to leave reviews. Unregistered users cannot submit reviews for dishes or the restaurant.

![Leaving a Review](/static/images/readme/logout_permissions/contact_page_log_out.jpg)

#### Notifications
- **Action Confirmation Modals**: After creating, editing, or deleting a reservation or review, a modal notification appears on the screen to confirm the action.
![Action Confirmation Modals](/static/images/readme/notiffications/booking_create.jpg)
- **Login/Logout Notifications**: When a user logs in or logs out, a modal notification appears confirming the action.
![Login/Logout Notifications](/static/images/readme/notiffications/login_not.jpg)

### Features Left to Implement
- Email registration confirmation
- Social media and Google registration integration
- Online ordering with a shopping cart and online payment
- Implementing a reward system where customers earn points for discounts.


## Models

#### Models Explanation
Initially, during the planning phase, I did not intend to create a Category Model and Dish Model. Instead, I had a Menu Model that contained category choices directly within it. However, during the implementation process, I realized that it would be much more convenient for both development and for administrators and users of the admin panel to have a separate model for categories. This would allow categories to be created and managed directly through the admin panel.

As a result, I renamed the existing Menu Model to Dish Model and changed the category field to a ForeignKey, linking each dish to a category.

### Reservation Model
The **Reservation** model stores client bookings. It includes fields for the client's phone number, booking date, time, people count, table count, comment, and status. The status of the reservation can be "Pending", "Confirmed", or "Cancelled". Additionally, it includes validation for phone numbers, people count, and table count, along with timestamp fields for creation and updates.

- `client`: Foreign key linking to the **User** model (client making the reservation).
- `phone_number`: A character field for the client's phone number.
- `date`: The date of the reservation.
- `time`: The time of the reservation.
- `people_count`: The number of people for the reservation.
- `table_count`: The number of tables reserved.
- `comment`: A text field for additional comments or requests.
- `created_at`: Automatically populated timestamp for when the reservation is created.
- `updated_at`: Automatically populated timestamp for when the reservation is updated.
- `status`: The current status of the reservation (Pending, Confirmed, Cancelled).

##### Reservation Model Scheme
![Reservation Model](/static/images/readme/models/reservation_model.jpg)

### Review Model
The **Review** model stores user reviews for dishes or services. It includes:

- `author`: Foreign key to the **User** model representing the author of the review.
- `rating`: A positive integer representing the review rating (1-5).
- `body`: The content of the review.
- `created_on`: Timestamp for when the review was created.
- `updated_at`: Timestamp for when the review was last updated.
- `approved`: A boolean field indicating whether the review is approved for display.

##### Review Model Scheme
![Review Model](/static/images/readme/models/review_model.jpg)

### Category Model
The **Category** model helps organize dishes into categories with:

- `name`: A string field for the category's name.
- `order`: A positive integer for the category's order in the list, helping to sort categories.

### Dish Model
The **Dish** model represents a menu item with the following fields:

- `name`: The name of the dish.
- `description`: A detailed description of the dish.
- `price`: The price of the dish.
- `currency`: A choice field for the currency (EUR, USD, GBP).
- `category`: Foreign key to the **Category** model, categorizing the dish.
- `image`: An optional field for the dish’s image, stored in Cloudinary.
- `status`: A choice field indicating if the dish is available or unavailable.
- `publishing_status`: A choice field indicating whether the dish is in draft or published status.
- `order`: A positive integer that helps order the dishes in the menu.

##### Dish Model Scheme
![Dish Model](/static/images/readme/models/menu_model.jpg)

## Design

The design uses a vibrant and modern color palette to create a visually engaging and user-friendly experience:

### Color Scheme:
The main sections and navbar are highlighted with a bright yellow color for high contrast, while the footer is designed with a dark gray for a sleek, professional look. This combination provides balance and visual appeal.

### Hero Section:
A full-screen background video is used in the hero section to capture attention and set the tone for the site, creating a dynamic and immersive experience.

### CTA Sections:
For the call-to-action sections, a parallax image effect is implemented, providing depth and interactivity as users scroll through the page.

### About Section:
A carousel of images is used to showcase key information in a visually engaging way, allowing for easy browsing of multiple images.

### Typography:
The primary font is **Jura**, chosen for its clean, modern, and easy-to-read style. The font is displayed in dark blue, contributing to a sophisticated and clear look. For the footer and CTA sections, white text is used for high contrast against darker backgrounds.

### Navigation & Interactivity:
The navigation menu and links in the footer feature a hover effect, offering interactive feedback to users and enhancing the overall usability.

### Consistent & Responsive Design:
The website is designed to be fully responsive, ensuring a consistent user experience on both desktop and mobile devices. Every page adapts seamlessly to different screen sizes, maintaining usability and visual harmony.

### Wireframes:
Before development, wireframes for each page were sketched out to plan the layout and functionality, ensuring a smooth development process and a clear vision of the final product.
![Wireframe 1](/static/images/readme/design/sitemap1.jpg)
![Wireframe 2](/static/images/readme/design/sitemap2.jpg)
![Wireframe 3](/static/images/readme/design/sitemap3.jpg)
![Wireframe 4](/static/images/readme/design/sitemap4.jpg)

This design focuses on simplicity, accessibility, and a modern aesthetic, delivering a visually appealing and user-friendly experience for all visitors.

# Testing

## Django testing

### Tests for Booking app

#### Tests for Forms
- **Valid Data**: The form is tested with correct data to ensure that it is valid and can be processed.
- **Invalid Phone Number**: The form is tested with an invalid phone number to check that it raises an error in the phone number field.
- **Empty Fields**: The form is tested with empty fields to ensure that required fields (like client, phone number, date, time, etc.) trigger appropriate error messages.

#### Tests for Models
- **Reservation Creation**: Ensures that a reservation can be created correctly with the provided fields, including client, phone number, date, time, etc.
- **Default Status**: Tests that the default status of a new reservation is set to "Pending" (0).
- **Phone Number Length**: Verifies that the phone number cannot exceed the maximum allowed length of 15 characters.
- **Positive People Count**: Ensures that the number of people cannot be negative or zero.
- **Positive Table Count**: Ensures that the table count cannot be negative or zero.
- **Cascade Deletion**: Tests that when a user is deleted, their reservations are also deleted.
- **String Representation**: Verifies that the string representation of a reservation is formatted correctly.

#### Tests for URLs
- **Booking Page URL**: Verifies that the URL for the booking page resolves correctly to the `booking_page` view.
- **Edit Booking URL**: Checks that the URL for editing a booking resolves to the `edit_booking` view.
- **Delete Booking URL**: Ensures that the URL for deleting a booking resolves to the `delete_booking` view.

#### Tests for Views
- **Booking Page Accessibility**: Tests that the booking page is accessible with a GET request and that the correct template is used.
- **Create Booking**: Verifies that a reservation is successfully created when submitting the form with valid data via a POST request.
- **Delete Booking**: Tests the deletion of an existing reservation by sending a POST request to the delete view and confirming that the reservation no longer exists.
- **Edit Booking**: Verifies that an existing reservation can be edited by sending a POST request with updated details, and checks that the changes are reflected in the database.

### Tests for Сontact app

#### Tests for Forms
- **Valid Data**: The form is tested with valid data to ensure it processes correctly without errors.
- **Invalid Rating**: The form is tested with an invalid rating (greater than 5) to verify that it fails validation.
- **Missing Rating**: The form is tested with a missing rating to ensure it triggers an error as the rating is a required field.
- **Empty Body**: The form is tested with an empty review body to check if it triggers an error, as the body field is mandatory.

#### Tests for Models
- **Review Creation**: The test ensures that a review is created correctly, with accurate author, rating, body, and default approval status.
- **Rating Validation**: This test checks that ratings outside the allowed range (1–5) raise validation errors.
- **String Representation**: The test ensures the `__str__` method of the review model returns the correct string format.
- **Default Values**: The test verifies that default values, like the approval status and timestamps, are properly set upon creating a review.
- **Review Ordering**: The test checks if reviews are correctly ordered by their creation date, with the latest review coming first.

#### Tests for Views
- **Review Create View (GET)**: This test checks if the review creation page is accessible and returns the correct template.
- **Review Create View (POST)**: This test verifies that submitting a valid review creates a new review and redirects the user properly.
- **Edit Review View**: The test ensures that an existing review can be edited, and the changes are saved in the database.
- **Delete Review View**: This test checks if submitting a delete request for a review successfully removes it from the database.
- **Review Saved Correctly**: The test ensures that valid reviews are saved correctly with the right data in the database, and the approval status is set to false by default.

#### Tests for URLs
- **Review Create URL**: This test checks if the URL for creating a review (`contact/`) resolves to the `review_create` view.
- **Edit Review URL**: The test ensures that the URL for editing a review (`edit/<pk>`) correctly resolves to the `edit_review` view.
- **Delete Review URL**: The test verifies that the URL for deleting a review (`delete/<pk>`) resolves to the `delete_review` view.

### Tests for Menu app

#### Tests for Models
- **Category Creation**: Tests that a category is created with the expected name and order.
- **Category String Representation**: Verifies that the `__str__` method returns the correct category name.
- **Category Ordering**: Ensures that categories are ordered according to the `order` field.
- **Default Category Order**: Checks that a category has the default order value when no explicit order is provided.
- **Category Order Update**: Tests that updating the order field of a category is properly saved.
- **Category Ordering After Update**: Confirms that the ordering of categories remains correct after an update to the order field.
- **Dish Creation**: Verifies that a dish is created correctly with all required attributes such as name, description, price, currency, category, status, publishing status, and order.
- **Price with Currency**: Ensures that the method displaying the dish’s price with the corresponding currency symbol returns the expected result.
- **Dish String Representation**: Tests that the dish's string representation correctly returns its name.

#### Tests for Views
- **Menu by Category Status Code**: Tests that the menu view returns an HTTP 200 status code.
- **Menu by Category Template**: Verifies that the correct template is used to render the menu page.
- **Menu by Category Context**: Ensures that the view context includes only published dishes grouped by category.
- **Menu by Category Ordering**: Confirms that both categories and the dishes within each category are ordered correctly according to their respective order fields.

#### Tests for URLs
- **Menu URL Resolution**: Tests that the URL for the menu page correctly resolves to the intended view function.

### Tests for Home app

#### Tests for Views
- **Home Page View**: The home page view is tested to ensure that it returns an HTTP 200 status code and renders the correct template.

#### Tests for URLs
- **Home URL Resolution**: The URL for the home page is tested to verify that it resolves to the correct view function.

## Manual Testing
## Home Page - Manual Testing

| Feature                   | Test Action                                       | Expected Outcome                                      | Result (✔/❌) | Fix (if needed) |
|---------------------------|---------------------------------------------------|-------------------------------------------------------|---------------|-----------------|
| **Nav Bar**               | Press nav sections                                | Navigates to respective pages                         | ✔             | N/A             |
| **Nav Bar**               | Hover over links                                  | Hover effect is visible                               | ✔             | N/A             |
| **Hero Section**          | Press buttons                                     | Navigates to menu or booking pages                    | ✔             | N/A             |
| **Hero Section**          | Hover over buttons                                | Hover effect is visible                               | ✔             | N/A             |
| **Hero Section**          | Check background video playback                   | Background video plays                                | ✔             | N/A             |
| **About Section Carousel**| Press left/right arrows                           | Photos change accordingly                             | ✔             | N/A             |
| **About Section Carousel**| Observe automatic photo changes                   | Photos change automatically                           | ✔             | N/A             |
| **CTA Section**           | Press button                                      | Navigates to the booking page                         | ✔             | N/A             |
| **CTA Section**           | Verify parallax effect on background image        | Parallax effect is visible                            | ✔             | N/A             |
| **CTA Section**           | Hover over buttons                                | Hover effect is visible                               | ✔             | N/A             |
| **Footer**                | Press footer links                                | Navigates to respective pages                         | ✔             | N/A             |
| **Footer**                | Hover over footer links                           | Hover effect is visible                               | ✔             | N/A             |

---

## Menu Page - Manual Testing

| Feature           | Test Action                                     | Expected Outcome                                   | Result (✔/❌) | Fix (if needed) |
|-------------------|-------------------------------------------------|----------------------------------------------------|---------------|-----------------|
| **Menu Nav Bar**  | Press menu section button                       | Navigates to the specific menu section             | ✔             | N/A             |
| **Menu Nav Bar**  | Hover over nav bar buttons                      | Hover effect is visible                            | ✔             | N/A             |
| **Menu Nav Bar**  | Scroll down                                     | Navigation bar becomes fixed                       | ✔             | N/A             |
| **Dish Card**     | Press button on a dish card                     | Opens modal displaying dish details                | ✔             | N/A             |
| **Dish Card**     | Press the "X" in the modal                      | Modal closes                                       | ✔             | N/A             |

---

## Booking Page - Manual Testing

| Feature                   | Test Action                                               | Expected Outcome                                                         | Result (✔/❌) | Fix (if needed) |
|---------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------|---------------|-----------------|
| **CTA Section**           | Press button                                              | Navigates to the booking form                                            | ✔             | N/A             |
| **CTA Section**           | Check parallax effect on background image                 | Parallax effect is visible                                               | ✔             | N/A             |
| **CTA Section**           | Hover over buttons                                        | Hover effect is visible                                                  | ✔             | N/A             |
| **Your Reservations**     | Press Edit button                                         | Navigates to the reservation form                                        | ✔             | N/A             |
| **Your Reservations**     | Edit reservation and press Update button                  | Reservation is updated with a confirmed status message                   | ✔             | N/A             |
| **Your Reservations**     | Press Delete button                                       | Opens modal with options to cancel or confirm                            | ✔             | N/A             |
| **Your Reservations**     | Press cancel in delete modal                              | Modal closes                                                             | ✔             | N/A             |
| **Your Reservations**     | Press delete in delete modal                              | Reservation is deleted with a confirmed status message                   | ✔             | N/A             |
| **Reservation Form**      | Submit form with all fields correctly filled              | Reservation is created with a confirmed status message                   | ✔             | N/A             |
| **Reservation Form**      | Submit form with an invalid phone number                   | Form displays error: "Please provide a valid phone number."              | ✔             | N/A             |
| **Reservation Form**      | Check starting date field                                  | Starting date is set to today's date                                     | ✔             | N/A             |
| **Reservation Form**      | Verify time range based on chosen date                     | Time range adjusts correctly according to the selected date              | ✔             | N/A             |
| **Reservation Form**      | Choose number of people                                    | Form calculates the required number of tables                            | ✔             | N/A             |
| **Reservation Form**      | Submit form with an empty comment (optional)             | Form submits successfully                     | ✔             | N/A             |
| **Reservation Form**      | Submit form with empty required fields                     | Form prompts to fill in the missing fields                               | ✔             | N/A             |
| **Booking for occupied time slots**                     | Attempt to book a time slot that is already reserved          | Display message: "You already have a reservation for this time. Please edit the existing reservation to make changes."                | ✔             | N/A             |
|**Booking without authentication**                    | Try to book a reservation without being logged in              | Display message: "Please select a client."                                                                                           | ✔             | N/A             |

---

## Contact Page - Manual Testing

| Feature         | Test Action                                           | Expected Outcome                                                  | Result (✔/❌) | Fix (if needed) |
|-----------------|-------------------------------------------------------|-------------------------------------------------------------------|---------------|-----------------|
| **Google Map**  | Press label to open contact information modal         | Modal with contact information opens                              | ✔             | N/A             |
| **Google Map**  | Press label to open redirection modal for Google Map   | Modal prompts for redirection to Google Maps                      | ✔             | N/A             |
| **Review Form** | Click on stars to select a rating                      | Stars are colored in gold indicating the selected rating          | ✔             | N/A             |
| **Review Form** | Hover over stars                                      | Hover effect is visible on stars                                  | ✔             | N/A             |
| **Review Form** | Submit form with empty fields                         | Form prompts to fill in the missing fields                          | ✔             | N/A             |
| **Your Reviews**| Submit valid review via the form                       | Review is created with a confirmed status message                  | ✔             | N/A             |
| **Your Reviews**| Press Edit button                                     | Navigates to the review editing form                               | ✔             | N/A             |
| **Your Reviews**| Edit review and press Update button                   | Review is updated with a confirmed status message                  | ✔             | N/A             |
| **Your Reviews**| Press Delete button                                   | Opens modal with options to cancel or confirm                        | ✔             | N/A             |
| **Your Reviews**| Press cancel in delete modal                          | Modal closes                                                       | ✔             | N/A             |
| **Your Reviews**| Press delete in delete modal                          | Review is deleted with a confirmed status message                  | ✔             | N/A             |
| **Leaving review without authentication**                 | Try to submit a review without being logged in                   | Display message: "Please select a client."                                                                                           | ✔             | N/A             |
---

## Logout Page - Manual Testing

| Feature   | Test Action                  | Expected Outcome                                           | Result (✔/❌) | Fix (if needed) |
|-----------|------------------------------|------------------------------------------------------------|---------------|-----------------|
| **Sign Out** | Press the Sign Out button      | User is signed out with a confirmed status message          | ✔             | N/A             |

---

## Register Page - Manual Testing

| Feature         | Test Action                                           | Expected Outcome                                                       | Result (✔/❌) | Fix (if needed) |
|-----------------|-------------------------------------------------------|------------------------------------------------------------------------|---------------|-----------------|
| **Sign Up Form**| Submit form with all fields correctly filled          | User is created with a confirmed status message                         | ✔             | N/A             |
| **Sign Up Form**| Submit form with mismatched password confirmation      | Form displays error: "You must type the same password each time."         | ✔             | N/A             |
| **Sign Up Form**| Submit form with an empty username field               | Form prompts to fill in the username field                              | ✔             | N/A             |
| **Sign Up Form**| Submit form with password too similar to personal info   | Form displays error regarding password similarity (if applicable)         | ✔             | N/A             |
| **Sign Up Form**| Submit form with a password shorter than 8 characters    | Form displays error about minimum length requirement                     | ✔             | N/A             |
| **Sign Up Form**| Submit form with a commonly used password               | Form displays error about the password being too common                  | ✔             | N/A             |
| **Sign Up Form**| Submit form with an entirely numeric password           | Form displays error regarding numeric-only password                      | ✔             | N/A             |

---

## Log In Page - Manual Testing

| Feature         | Test Action                                           | Expected Outcome                                                       | Result (✔/❌) | Fix (if needed) |
|-----------------|-------------------------------------------------------|------------------------------------------------------------------------|---------------|-----------------|
| **Sign In Form**| Submit form with an empty username field               | Form prompts to fill in the username field                              | ✔             | N/A             |
| **Sign In Form**| Submit form with an incorrect password                 | Displays error: "The username and/or password you specified are not correct" | ✔             | N/A             |
| **Sign In Form**| Submit form with all fields correctly filled            | User is logged in with a confirmed status message                        | ✔             | N/A             |

## Admin panel - Manual Testing
| Feature                                      | Test Action                                                                              | Expected Outcome                                                                                                                                              | Result (✔/❌) | Fix (if needed) |
|----------------------------------------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|-----------------|
| **Menu App - Category**                      |                                                                                          |                                                                                                                                                               |               |                 |
| Category Creation                            | Create a new category via the admin panel                                                | Category is successfully created and becomes visible in the admin panel and on the website                                                                    | ✔             | N/A             |
| Category Order Change                        | Change the order value of an existing category                                           | The display order of categories on the website updates accordingly                                                                                            | ✔             | N/A             |
| Category Deletion                            | Delete a category via the admin panel                                                    | The category is removed from both the admin panel and the website                                                                                             | ✔             | N/A             |
| **Menu App - Dish**                          |                                                                                          |                                                                                                                                                               |               |                 |
| Dish Creation                                | Create a new dish with all required fields for a specific category                       | Dish is successfully created and assigned to the selected category                                                                                            | ✔             | N/A             |
| Dish Order Change                            | Update the order value of a dish within its category                                      | The new dish order is reflected on the website                                                                                                                | ✔             | N/A             |
| Dish Filtering                               | Apply filters by category, status, publishing status, and price in the admin panel         | The dish list is correctly filtered based on the selected criteria                                                                                            | ✔             | N/A             |
| Dish Deletion                                | Select and delete one or multiple dishes                                                 | The selected dishes are removed from the system                                                                                                               | ✔             | N/A             |
| Dish Required Fields Validation              | Attempt to create a dish without filling in all required fields                           | The dish is not saved and an error message is displayed                                                                                                       | ✔             | N/A             |
| Dish Status Selection                        | Create a dish and choose a status (available/unavailable)                                  | Dish is saved with the chosen status; if marked as "unavailable," the status is shown in the modal on the Menu page                                               | ✔             | N/A             |
| Dish Publishing Status Selection             | Create a dish with the publishing status set to "draft"                                    | The dish is not published on the website when its publishing status is set to "draft"                                                                           | ✔             | N/A             |
| **Booking App - Reservations**               |                                                                                          |                                                                                                                                                               |               |                 |
| Reservation Status Assignment                | Assign a status (pending, confirmed, canceled) to a reservation via the admin panel         | The reservation's status is updated accordingly                                                                                                               | ✔             | N/A             |
| Reservation Creation                         | Create a reservation with all required fields (comment is optional)                        | Reservation is successfully created with the assigned status                                                                                                  | ✔             | N/A             |
| Reservation Filtering                        | Filter reservations by date and status in the admin panel                                  | The reservations list is correctly filtered according to the selected criteria                                                                                | ✔             | N/A             |
| Reservation Deletion                         | Select and delete one or more reservations                                               | The selected reservations are removed from the system                                                                                                         | ✔             | N/A             |
| **Contact App - Reviews**                    |                                                                                          |                                                                                                                                                               |               |                 |
| Review Approval                              | Toggle the approval status for a client review                                             | The review's approval status is updated accordingly                                                                                                           | ✔             | N/A             |
| Review Creation                              | Create a review with all required fields and select the desired approval status             | The review is successfully created and saved with the chosen approval status                                                                                    | ✔             | N/A             |
| Review Filtering                             | Filter reviews by rating and approval status in the admin panel                             | The reviews list is correctly filtered based on the selected criteria                                                                                           | ✔             | N/A             |
| Review Deletion                              | Select and delete a review via the admin panel                                              | The review is removed from the system                                                                                                                         | ✔             | N/A             |

| **Authentication and Authorization- Users** 
| Feature                      | Test Action                                                        | Expected Outcome                                                                    | Result (✔/❌) | Fix (if needed) |
|------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------|---------------|-----------------|
| **User Deletion**            | Delete a user from the admin panel                                 | The user is successfully removed from the database                                  | ✔             | N/A             |
| **User Filtering (Staff)**   | Apply filter by staff status in the admin panel                    | The list of users is filtered to show only staff members                            | ✔             | N/A             |
| **User Filtering (Superuser)**| Apply filter by superuser status in the admin panel                 | The list of users is filtered to show only superusers                               | ✔             | N/A             |
| **User Filtering (Active)**  | Apply filter by active status in the admin panel                   | The list of users is filtered to show only active users                             | ✔             | N/A             |
| **User Creation**            | Add a new user by providing username, password, and confirm password | The user is successfully created and appears in the users list                      | ✔             | N/A             |
### Bugs
- On mobile devices, Flatpickr does not work, causing the functionality that restricts date selection to the current day and time selection to business hours to fail.


### Validator Testing
- **HTML**: No errors were returned when passing through the official W3C validator.
- **CSS**: No errors were found when passing through the official (Jigsaw) validator.
- **JS**: No errors were found when passing through JSHint.
- **Python**: No errors were found when passing through CI Python Linter.
- **Accessibility**: I confirmed that the colors and fonts chosen are easy to read and accessible by running it through Lighthouse in devtools.
##### Lighthouse Desktope
![Lighthouse Desktope](/static/images/readme/lighthouse/lighthouse_d.jpg)
##### Lighthouse Mobile
![Lighthouse Mobile](/static/images/readme/lighthouse/lighthouse.jpg)

## Deployment

I deployed the site to **Heroku**. The deployment process was as follows:

### 1. Preparing for Deployment
Before deploying, I ensured that my GitHub repository contained all the necessary files, including:
- `requirements.txt`
- `Procfile`
- `env` file with environment variables (excluded from Git using .gitignore)
- did collectstatic 

### 2. Connecting the GitHub Repository to Heroku
1. I logged into **Heroku Admin Panel**.
2. Created a new app by selecting **New** > **Create new app**.
3. Chose a unique app name and selected my region.
4. Navigated to the **Deploy** tab.
5. In the **Deployment method** section, selected **GitHub**.
6. Connected my GitHub account and linked the repository.

### 3. Deploying the Application
1. In the **Manual Deploy** section, I clicked **Deploy Branch** (with `main` selected).
2. I waited for the build process to complete and confirmed the successful deployment.

### 4. Configuring Environment Variables
1. I went to the **Settings** tab in Heroku.
2. Clicked **Reveal Config Vars**.
3. Added all required environment variables (`CLOUDINARY_URL`, `DATABASE_URL`, `GOOGLE_MAPS_API_KEY`, `SECRET_KEY`,).
4. Saved the changes.

The live link can be found here: [Napoli](https://napoli-restaurant-1ab96f563776.herokuapp.com/)

## Clone this Repository

To clone this repository, use the following command:

- git clone https://github.com/MykhailoVasylkov/restaurant-booking-service

##  Forking the Project
To fork the repository and work on your own version:

- Go to the [repository](https://github.com/MykhailoVasylkov/restaurant-booking-service) on GitHub.
- Click the Fork button in the upper right corner.
- Choose "Create a new fork"

## Credits

### Content

- **Text**: All text content was generated using Chat-GPT.
- **Favicon**: Created using [favicon.io](https://favicon.io/).
- **Font Awesome Kit**: Sourced from [cdnjs.com](https://cdnjs.com/libraries/font-awesome).
- **Django-Blog Reference**: I used the **Django-blog** project as a reference to understand how to configure settings, work with Django Template Language (DTL), models, views, forms, URLs, and the admin panel.
- **Chat-GPT Assistance**: I used Chat-GPT to help implement specific functionality according to my needs, including:
  1. Implementing **Flatpickr** and extending its functionality to limit date selection and working hours.
  2. Hiding the **navbar menu** when opening a dish modal.
  3. Automating **table calculation** in the booking form based on the number of guests.
  4. Integrating **Google Maps API** with custom marker settings.
  5. Implementing an **interactive star rating system** for reviews.
  6. Adding functionality for **editing and deleting reservations and reviews**.
- **Bootstrap & Chat-GPT**: I used Bootstrap documentation and Chat-GPT to implement:
  - A **carousel** for the "About Us" section.
  - A **parallax effect** for the CTA sections.

### Media
- **Images and video**: All images and video are sourced from [Pexels stock](https://www.pexels.com/).
- **Icons**: Icons sourced from [Fond awesome](https://fontawesome.com/).

