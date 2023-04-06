## Auction Listing Web Application

#### Video Demo:  <https://youtu.be/oL2Mli-JqRI>

This web application is built using Django and allows users to create and bid on auction listings, as well as comment on listings and add them to a watchlist. Here are some key features of the application:

### Models
- User: built-in Django user model
- Listing: contains fields for the title, description, starting bid, image URL, and category of a listing
- Bid: contains fields for the amount of the bid and the user who made the bid
- Comment: contains fields for the text of the comment and the user who made the comment

### Create Listing
- Users can create a new listing with a title, description, starting bid, image URL, and category.

### Active Listings Page
- Users can view all currently active auction listings on the default route of the web application.
- For each active listing, the title, description, current price, and photo (if one exists for the listing) are displayed.

### Listing Page
- Clicking on a listing takes users to a page specific to that listing, where they can view all details about the listing, including the current price.
- Signed-in users can add the item to their watchlist, remove it from the watchlist if it is already on there, and bid on the item.
- The bid must be at least as large as the starting bid and greater than any other bids that have been placed.
- If the user who created the listing is signed in, they can close the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.
- If a user who has won an auction is signed in on a closed listing page, the page will display that they have won the auction.
- Signed-in users can also add comments to the listing page.

### Watchlist
- Signed-in users can view all of the listings they have added to their watchlist on a Watchlist page.
- Clicking on any of those listings takes the user to that listing’s page.

### Categories
- Users can visit a page that displays a list of all listing categories.
- Clicking on the name of any category takes the user to a page that displays all of the active listings in that category.

### Django Admin Interface
- A site administrator can view, add, edit, and delete any listings, comments, and bids made on the site via the Django admin interface.
