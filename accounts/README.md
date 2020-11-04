The accounts app keeps track of our registered users and who is logged in. This uses the database to perform this task
and is very helpful. Within the accounts we use the views.py to implement a sign up, log in, and logout pages that
are crucial for the webpage. Along with allowing users to login and everything, we have added a password change function
and a password reset function. We use django's builtin email libraries to do the heavy lifting so that an email will be sent
when the password is reset. These are both important features becuase sometimes people need to change there passwords or
they may even forget the passwords so this is a fix to both those issues.