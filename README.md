T H E C H A LL E N G E

Build an online service for generating CSV files with fake (dummy) data using
Python and Django:

Any user can log in to the system with a username and password. You can
use generic views provided by Django to implement these features.
Registering new users via the admin interface is enough. Note, that you
do not need to implement a user profile interface to support password
change or similar functionality.
Any logged-in user can create any number of data schemas to create
datasets with fake data.
Each such data schema has a name and a list of columns with names and
specified data types.
You need to implement different types of data (at least 5 different types):
Full name (a combination of first name and last name)
Job
Email
Domain name
Phone number
Company name
Text (with a specified range for a number of sentences)
Integer (with specified range)
Address
Date
Users can build the data schema with any number of columns of any type
described above. Some types support extra arguments (like a range),
while others do not.
Each column also has its own name (which will be a column header in the
CSV file) and order (just a number to manage column order).
After creating the schema, the user should be able to input the number of
records he/she needs to generate and press the “Generate data” button.
After pressing the button, the frontend should send an AJAX request to
the server to generate the data. When the CSV file of the specified
structure is ready, the file can be saved to the “media” directory.
The interface should show a colored label of generation status for each
dataset (processing/ready).
Add a “Download” button for datasets available for download.
The completed application should be deployed to PythonAnywhere
(https://www.pythonanywhere.com/) and be available online. Please,
create a test user and provide us with the credentials.
The source code should be committed to the repository on GitHub,
Bitbucket, or GitLab. Please, send us the link to the repo as well.

T E C H N O L O G Y S T A C K

Python 3
Django
Bootstrap, Bulma, UIKit, or any other similar framework for UI
Use PEP8 for your Python code.
T E C H N O L O G Y S T A C K

The page structure can be seen here:

https://www.figma.com/file/GLah5wCMHIyw7hJI4Gekns/CSV-fake-data-
generator?node-id=24278%3A2