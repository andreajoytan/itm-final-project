# itm-final-project

# Instructions on how to run the project (both admin and customer view)

# Admin View

# Log in with the following superuser details to be given access to administrative functions:
## Username: admin
## Password: limongtan

# Manage ‘Groups’ and ‘Users’ under ‘Authentication and Authorization’ in “/admin/” site
## ‘Users’ contains all the information of users who signed up in the website (Ex: staff status)
## ‘Users’ also allows the superuser to add and change users.

# Manage Products in “/admin/” site
## View, add, edit, or delete categories
## View, add, edit, or delete products
### Adding and editing products requires selecting the category of the product from the categories model and inputting product name, description, price, image, availability. Then, it automatically gets the publish date for adding the product, modified date for editing the product, and which superuser created it.

# Manage Products in the website 
## If superuser logs in the website, the navigation bar will have the buttons: “Add Product”, “Manage Products”, and “Log Out” (only for superusers)
## Add products through the “Add Product” button in the navigation bar. Similar inputting in the “/admin/” site
## View all products in the “Manage Products” page and click on the product you want to edit or delete. 
## “Log Out” logs the superuser out, requiring them to log in again if they want to continue using the website

## In the admin site, you can manage orders, customer information, view customer shipping data 

# Manage Orders
## The order number, name of the customer, date the order was placed, and current order status (No, Yes, Unknown) are shown
## Admin can also click on the order number and the customer name and date will be displayed again, and a transaction number will be set by the admin (required)
## In Order Items, the list of items that were ordered will be displayed in this field
# View Customer Information
## Through the admin site, you can view all customer information stored. This information includes: Customer Name, Email, View Shipping Data
## Upon clicking on the address listed, the corresponding customer’s name and order number will be displayed alongside the complete details of the address

 
# Customer View

# Home/Browse Products:
## Navigation bar and footer always contains “Home” and “Browse Products”.
## Only available products are shown to the user.
## “Home” page allows users to view the latest products, along with their names and prices. At the bottom of the page, it has a button (“Shop All Products”) that redirects users to the “Browse Products” page. At the top right hand side of the page, the following are displayed:
### My Form (Button): When clicked, the user will be redirected to a page where they can view the items they added to the form upon shopping
### Dashboard (Button): When clicked, the user will be redirected to a page which allows the user to view his/her order history
### Logout (Button): When clicked, the user will be logged off his/her account 
## “Browse Products” page lists all the products available, along with their names and prices. Users may search for products by inputting what they are looking for. They may also filter products by category, and sort products alphabetically, by price, or latest creation date. Moreover, the user can add products to their quotation form using the ‘add to form’ button found below each listed product. 

## Users may click the displayed products for a more detailed view that shows the product’s description, and date of creation and modification.

## If the user is not logged in, the “Sign-Up” and “Log-In” buttons appear in the navigation bar and footer. Users may do so accordingly.
## After they have been logged in, the navigation bar and footer show “My Dashboard” and “Log Out”
### “My Dashboard” allows users to view their order history
### “Log Out” logs the user out, requiring them to log in again if they want to continue using the website.

# Add to Form and Checkout:
## Using the ‘add to form’ button, the user can add products to their Quotation Form 
## The user can view his/her quotation form by clicking on the ‘My Form’ button located at the top right hand corner of the website page
## When the quotation form is accessed, the user can view the list of products they added to the form.
### The user can add or remove the number of items from the form using the ‘+’ and ‘-’ buttons found beside the quantity number of the item
### In this form, the user can view the total amount of products/items listed in the form, and the total amount due from the list of products
### After reviewing the form, the user can proceed to checkout by clicking on the ‘checkout’ button found at the bottom right hand side of the quotation form 

## After clicking ‘checkout’, the user will be redirected to the checkout page where they will be prompted to input their shipping details
### After reviewing their shipping information, the user can submit the form by clicking on the ‘submit’ button found at the bottom right hand side of the checkout page

## After submitting the shipping details, the customer will be brought to a page which states: ‘The form was successfully submitted.”

# My Dashboard:
## At the top right hand corner, beside the ‘My Form’ button, users can click ‘My Dashboard’
### Upon clicking on ‘My Dashboard’,  the user will be redirected to a page that displays the button ‘Order History’.
## When you click on ‘Order History’, the website will display the following: The Order ID (has a button functionality), The Total Amount/Price of the Order, Order Status, Order Time 

### When the user clicks on the order ID, the user will be shown the order details for that order, the following will be displayed: Type of Product, Quantity of the Ordered Product, Price of the Product, Total Amount Paid, Date Ordered

# END
