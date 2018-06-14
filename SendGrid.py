# Code taken from here: https://github.com/sendgrid/sendgrid-python/blob/master/USE_CASES.md#transactional-templates

import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Substitution, Mail
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

# DO NOT FORGET TO gitignore workspace.xml
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

from_email = Email("test@example.com")
subject = "I'm replacing the subject tag"
to_email = Email("lagousis@gmail.com")
content = Content("text/html", "I'm replacing the <strong>body tag</strong>")
mail = Mail(from_email, subject, to_email, content)
mail.personalizations[0].add_substitution(Substitution("-contact_name-", "Stavros L"))
mail.template_id = "3c23b0f6-3ff4-4fe8-840d-8f61593c314d"
try:
    response = sg.client.mail.send.post(request_body=mail.get())
except urllib.HTTPError as e:
    print (e.read())
    exit()
print(response.status_code)
print(response.body)
print(response.headers)