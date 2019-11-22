# Morning Planner By Voltron
<img alt="GitHub Actions status" src="https://github.com/cohyunoh/Planner-Project/workflows/Python%20application/badge.svg">

## Roster and Roles
* CONNOR OH: project manager, bootstrap designer, reddit API implementor
* LEIA PARK: bootstrap designer, database handler
* JUN TAO LEI: Google API master and OAuth2 master

## What Is It?
We are making a website that acts as a planner you look at every morning to get your day started
* shows the date
* shows tasks and reminders, which can be added on to
* shows top posts on Reddit News
* shows your commute and what traffic lies ahead

## How To Run:

### -1. This Flask application requires credentials in order to run properly
> Since this Flask application uses OAuth2.0 to access Google APIs, the application needs to have a client ID and a client secret issued by Google. This is necessary as the credentials allow Google to identify the application and lets end users authenticate the application. If you want to test this application, please refer to the following directions.
    
    1. Obtain a Google account if you do not have one.
    2. Go to your Google Cloud Console.
    3. Create a project.
    4. Navigate to the session named "APIs & Services".
    5. Navigate to the OAuth consent screen section. Configure the OAuth consent screen. Be sure to include the scopes: email, profile, openid, ../auth/calendar, ../auth/tasks. Note that you may need to enable the Calendar API and the Tasks API.
    6. Navigate to the Credentials section. Create credentials for the test application. Be sure to add the associated redirect URI for this application. Note that the URI will be <http://localhost:5000/google/oauth2> if you run this application on localhost.
    7. Create a file name creds.json and place it in the project main/root directory. Be sure to use the following format.
    ```
    {
      "google_client_id": "your_client_id",
      "google_client_secret": "your_client_secret"
    }
    ```
    

### 0. Make sure python3 and pip3 are installed.

### 1. Clone
```
git clone https://github.com/cohyunoh/Planner-Project.git
```

### 2. Pull from GitHub Submodule
```
git submodule update --init --recursive
```

### 3. Activate your virtual environment
```
cd Planner-Project
python3 -m venv venv
. venv/bin/activate
```

### 4. Install the necessary packages outlined in requirements.txt
```
pip3 install -r requirements.txt
```

### 5. Run the Flask app
```
python3 run.py 
```

### 6. Update from GitHub Submodule if needed
```
git submodule update --recursive --remote
```
