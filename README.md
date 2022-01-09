# Importing Your Previous Project
Unfortunately, I haven't figured out a way to allow you to fork your previous project as your submission to the next project and retain the original submission, so you'll have to do some manual moving of files - but I want to make sure that all of your versions of your project are here throughout development.

# Copying Text Files and Folders
* Download your previous project as a zip (Files list, click the three-dots, download as zip)
* Expand the zip file
* Drag & drop the files and folder onto the new project's Files list on the left-hand side
* When asked if you want to overwrite files, select yes
 
# Dumping Your Database
Unfortunately, Replit doesn't copy the database over (the downloaded file is 0kb), so you have to dump the database, copy the file manually, and then read the database.
* In the Repl Shell of your previous project, enter the following command (assuming you didn't rename your database file), this will open the database in the sqlite3 editor (the $ is the prompt, don't enter this):
```
$ sqlite3 db.sqlite3
```
* When the sqlite3 prompt comes up, enter the following (sqlite> is the prompt, don't enter this):
```
sqlite> .output db.sql
sqlite> .dump
sqlite> .exit
```
* You should now see a db.sql file in your list of Files

# Reading Your Database
* In your new project, create a db.sql file at the same level as the db.sqlite3 file
* Open the db on the new project:
```
$ sqlite3 db.sqlite3
```
* Read in the sql file to this database:
```
sqlite3> .read db.sql
```

# Verifying Your New Site

* Double check that all of the files and folders came across
* Run your new server
* Make sure everything still works as it did before
  * Access your various apps
  * Access your automatic admin app and ensure your data is all there
