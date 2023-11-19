Certainly! Below is a README.md file for your simple web application:

markdown

# Simple Web Application

This is a simple web application that serves a Bootstrap-themed HTML page using a Python HTTP server.

## Usage

1. Clone the repository:

   ```bash
   git clone "https://github.com/gvriil/hw_19.1.git"

    Navigate to the project directory:

    bash

cd cw_19.1

Run the Python server:

bash

    python server-file.py

    Open your web browser and go to http://localhost:8090 to view the web page.

Project Structure

    static/: Contains static files (e.g., HTML templates, CSS files).
    main.py: Python script to run the HTTP server.

HTML Page Structure

The HTML page served by the application consists of the following sections:

    Product Card and Form Section:
        Product card with a "Buy" button.
        Form with fields for "Name" and "Email" and a "Send" button.

    FAQ Section:
        Three buttons with common questions:
            How to buy?
            How to deliver?
            What is the warranty?
        Collapsible blocks with answers for each question.

    Additional Task: Table Section:
        Table displaying product information with columns:
            Number
            Product Name
            Price per Unit
            Quantity
            Total Amount
            Order Status
        Statuses are color-coded:
            New: Blue
            Processing: Yellow
            Processed: Green
            Canceled: Red

Dependencies

    Bootstrap CSS: https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css
    Bootstrap JS (optional): https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js

License

This project is licensed under the MIT License - see the LICENSE file for details.

