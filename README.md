# ChoreListParser
Reads my student house chore list. When complete will link with Tasker AutoNotifications to remind individuals to perform their weekly chores. 
May also link with Google Calendar.

#### client_secret.json file withheld for privacy reasons. Users will need to generate their own JSON file through the following steps:
*Go to the Google APIs Console.  
*Create a new project.  
*Click Enable API. Search for and enable the [Google Drive API.](https://console.developers.google.com/apis/dashboard?project=chores-196516&duration=PT1H)  
*Create credentials for a Web Server to access Application Data.  
*Name the service account and grant it a Project Role of Editor.  
*Download the JSON file.  
(Copy the JSON file to your code directory and rename it to client_secret.json))  
  

(instructions taken from: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html?utm_source=youtube&utm_medium=video&utm_campaign=youtube_python_google_sheets)
