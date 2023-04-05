# Email Client Single Page App

This is a single-page application email client built using JavaScript, HTML, and CSS. The app is implemented inside of `inbox.js` file, and all the requirements listed below are fulfilled:

## Send Mail
When a user submits the email composition form, JavaScript code is added to send the email by making a POST request to `/emails`, passing in values for recipients, subject, and body. After the email has been sent, the user's sent mailbox is loaded.

## Mailbox
When a user visits their Inbox, Sent mailbox, or Archive, the appropriate mailbox is loaded by making a GET request to `/emails/<mailbox>` to request the emails for a particular mailbox. When a mailbox is visited, the application first queries the API for the latest emails in that mailbox. The name of the mailbox appears at the top of the page. Each email is then rendered in its own box, with a border, displaying who the email is from, what the subject line is, and the timestamp of the email. If the email is unread, it appears with a white background, and if the email has been read, it appears with a gray background.

## View Email
When a user clicks on an email, they are taken to a view where they can see the content of that email. A GET request to `/emails/<email_id>` is made to request the email. The application shows the email's sender, recipients, subject, timestamp, and body. An additional div is added to `inbox.html` for displaying the email. The code is updated to hide and show the right views when navigation options are clicked. Once the email is clicked on, it is marked as read by sending a PUT request to `/emails/<email_id>`.

## Archive and Unarchive
Users can archive and unarchive emails that they have received. When viewing an Inbox email, the user is presented with a button that lets them archive the email. When viewing an Archive email, the user is presented with a button that lets them unarchive the email. This requirement does not apply to emails in the Sent mailbox. A PUT request is sent to `/emails/<email_id>` to mark an email as archived or unarchived. Once an email has been archived or unarchived, the user's inbox is loaded.

## Reply
Users can reply to an email. When viewing an email, the user is presented with a "Reply" button that lets them reply to the email. When the user clicks the "Reply" button, they are taken to the email composition form. The composition form is pre-filled with the recipient field set to whoever sent the original email. The subject line is also pre-filled with "Re: <original subject>" (if the subject line already begins with "Re:", it is not added again). The body of the email is pre-filled with a line like "On Jan 1 2020, 12:00 AM foo@example.com wrote:" followed by the original text of the email.
