# LFB-OVERTIME
There is a need to develop an overtime system for the London Fire Brigade to allow users to sign up for overtime, as well as for system admins (known as RMC) to view who is available. This system has a FF side, and an RMC side.
The file starting with as V followed by a subsequent version number is the users side. This allows users to add themself to the database, as well as edit their account and attach their availability for their four days off.
One issue I have highlighted thus far is the fact any user can edit anyone else as long as they know their pay number. This could be used maliciously. A solution could be to have the edit user on the admin file, and any edits to users will have to be requested.

When you run data.pyw, there will be a database file created in the local directory. When you then go into the Vx.py file, you will be able to populate the database through here. 

There are some syntax issues, mainly regarding closing down child-windows. Other than this, the user side seems to work well. The database is a local file, as if this were to be used as on the LFB system, the idea is it is stored in a global drive, and the database file will be stored somewhere here. Potentially issues for GDPR as users mobile phone numbers are in plain text on the file.

I may create a random .db file with a populated table of random people so you're not guessing what goes in where.

I am starting to develop the admin side of the system where users will be able to see who has done the least amount of overtime, access their details and sort the database by skills, stations etc.
