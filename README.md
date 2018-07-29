# FirebaseUtils
A set of administrative tools to make working with firebase easier.

To use, do the following:
1. Clone the repo
2. `cd /path/to/clone`
3. `mkdir -p res/keys`
4. `cd res/keys`
5. Create a file named `client-data.json`. It should contain the following content:
 {
    "apiKey": "apiKey",
    
    "authDomain": "projectId.firebaseapp.com",
    
    "databaseURL": "https://databaseName.firebaseio.com",
    
    "storageBucket": "projectId.appspot.com",
    
   
    "serviceAccount": "path/to/serviceAccountCredentials.json",
    
    "messagingSenderId": "senderid"
  }
  
 6. Create a file named 'service-account-credentials.json`. You can download this file from your firebase app console under Project settings > Service accounts
 7. Use pip to install the requirements listed in requirements.txt
 
 At the moment, this only supports generating a firebase auth token for a user by email address. 
