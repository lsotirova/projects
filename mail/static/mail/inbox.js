document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // Call the send_email function when the compose-form has been submitted
  document.querySelector('#compose-form').addEventListener('submit', send_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#single-email').style.display = 'none';


  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#single-email').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Load mailbox content
  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
      // Print emails
      console.log(emails);

      // Loop through emails and add to the emails-view
      emails.forEach(email => {
        const singleEmail = document.createElement('div');
        singleEmail.classList.add('card', 'email', 'mb-3');
        singleEmail.classList.add(email.read ? 'read-email' : 'unread-email');

        // Set the innerHTML to display email information
        if (mailbox === 'sent') {
          singleEmail.innerHTML = `
            <div class="card-body">
              <div class="row">
                <div class="col-3 font-weight-bold">${email.recipients.join(', ')}</div>
                <div class="col-6">
                  <span><strong>Subject:</strong> ${email.subject}</span>
                  <span class="text-muted">${email.body.replace(/(\r\n|\n|\r)/gm, " ").replace(/<br>/g, " ").slice(0, 40)}${email.body.length > 50 ? '...' : ''}</span>
                </div>
                <div class="col-3 text-right">${email.timestamp ? email.timestamp : ''}</div>
              </div>
            </div>
          `;
        } else {
          singleEmail.innerHTML = `
            <div class="card-body">
              <div class="row">
                <div class="col-3 font-weight-bold">${email.sender}</div>
                <div class="col-6">
                  <span><strong>Subject:</strong> ${email.subject}</span>
                  <span class="text-muted">${email.body.replace(/(\r\n|\n|\r)/gm, " ").replace(/<br>/g, " ").slice(0, 40)}${email.body.length > 50 ? '...' : ''}</span>
                </div>
                <div class="col-3 text-right">${email.timestamp}</div>
              </div>
            </div>
          `;        
        }
      
        document.querySelector('#emails-view').appendChild(singleEmail);
        
        singleEmail.addEventListener('click', function() {
          view_email(email.id);
          // Mark email as read when clicked
          if (!email.read) {
            mark_email_as_read(email.id);
            singleEmail.classList.remove('unread-email');
            singleEmail.classList.add('read-email');
          }
        });
      });
    });
}

function mark_email_as_read(email_id) {
  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: true
    })
  });
}

function send_email(event) {
  event.preventDefault();

  // Save information in variables 
  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;

  // Replace new lines with HTML line breaks
  const formattedBody = body.replace(/\n/g, "<br>");

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: formattedBody
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
      load_mailbox('sent');

      // Show success message
      const successMessage = document.createElement('div');
      successMessage.classList.add('alert', 'alert-success', 'fade', 'show');
      successMessage.setAttribute('role', 'alert');
      successMessage.style.backgroundColor = 'rgba(255, 255, 255, 0.7)';
      successMessage.innerHTML = 'Email successfully sent.';
      document.querySelector('#emails-view').insertAdjacentElement('afterbegin', successMessage);

      // Fade out after 3 seconds
      setTimeout(() => {
        successMessage.classList.remove('show');
        successMessage.remove();
      }, 2500);
  });
}


function view_email(id) {

  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#single-email').style.display = 'block';

  // Get the single email information
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);


      const emailDetails = document.querySelector('#single-email');

      emailDetails.innerHTML = `
          <div class="card email" id="email-card">
          <div class="card-header d-flex justify-content-between align-items-center">
            <h5 class="mb-0 text-left">${email.subject}</h5>
            <span class="text-muted text-right">${email.timestamp}</span>
          </div>
          <div class="card-body">
            <div class="row mb-3">
              <div class="col-sm-1 font-weight-bold">From:</div>
              <div class="col-sm-10">${email.sender}</div>
            </div>
            <div class="row mb-3">
              <div class="col-sm-1 font-weight-bold">To:</div>
              <div class="col-sm-10">${email.recipients.join(', ')}</div>
            </div>
            <br>
            <div class="row mb-3">
              <div class="col-sm-1"></div>
              <div class="col-sm-10" style="text-align:justify;">${email.body}</div>
            </div>
            <br>
            <div class="row float-right" id="actions">
              <div class="col-sm-10" id="action-buttons"></div>
            </div>
          </div>
        </div>
      `;


      if(!email.read) {
        fetch(`/emails/${email.id}`, {
          method: 'PUT',
          body: JSON.stringify({
              read: true
          })
        })
      }

      const archiveBtn = document.createElement('button');
      archiveBtn.setAttribute('id', 'archive-btn');
      archiveBtn.innerHTML = email.archived ? 'Unarchive' : 'Archive';
      archiveBtn.className = email.archived ? 'btn btn-light' : 'btn btn-secondary';
      archiveBtn.addEventListener('click', function() {
        fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({
              archived: !email.archived
          })
        })
        .then(() => {
            // If the email was previously archived, redirect to the archived inbox
            load_mailbox('inbox');
            // Show archive message
            const archiveMessage = document.createElement('div');
            archiveMessage.classList.add('alert', 'alert-success', 'fade', 'show');
            archiveMessage.setAttribute('role', 'alert');
            archiveMessage.innerHTML = email.archived ? 'Email successfully unarchived.': 'Email successfully archived';
            archiveMessage.style.backgroundColor = 'rgba(255, 255, 255, 0.7)';
            document.querySelector('#emails-view').insertAdjacentElement('afterbegin', archiveMessage);

            // Fade out after 3 seconds
            setTimeout(() => {
              archiveMessage.classList.remove('show');
              archiveMessage.remove();
            }, 2500);
          
        })
      });

      
      document.querySelector('#actions').appendChild(archiveBtn);
      
      const replyBtn = document.createElement('button');
      replyBtn.className = 'btn btn-info';
      replyBtn.innerHTML = 'Reply';
      replyBtn.addEventListener('click', function() {
        compose_email();
        reSubject = email.subject;

        if (!reSubject.startsWith('Re:')) {
          reSubject = 'Re:' + reSubject;
        } else {
          reSubject = reSubject;
        };
        emailBody = email.body
        emailBody = emailBody.replace(/<br>/g, '\n');
        document.querySelector("#compose-recipients").value = email.sender;
        document.querySelector("#compose-subject").value = reSubject;
        document.querySelector("#compose-body").value = `\n\nOn ${email.timestamp} ${email.sender} wrote: \n \n ${emailBody}`;
      });
      document.querySelector('#actions').appendChild(replyBtn);
      


      const actionButtons = document.querySelector('#action-buttons');
      actionButtons.appendChild(archiveBtn);
      actionButtons.appendChild(replyBtn);
      actionButtons.style.display = 'flex';
      actionButtons.style.flexDirection = 'row';
      actionButtons.style.gap = '10px';
  });
}