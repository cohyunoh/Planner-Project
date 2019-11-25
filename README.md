# Morning Planner By Voltron
<img alt="GitHub Actions status" src="https://github.com/cohyunoh/Planner-Project/workflows/Python%20application/badge.svg">

## Roster and Roles
* CONNOR OH: project manager, bootstrap designer, reddit API implementor
* LEIA PARK: bootstrap designer, database handler
* JUN TAO LEI: Google API master and OAuth2 master

## What Is It?
We are making a website that acts as a planner you look at every morning to get your day started
* Shows the date
* Shows tasks and reminders, which can be modified
* Shows top posts on from a Reddit subreddit, default to a news related subreddit
* Shows your commute and what traffic lies ahead

## APIS Used:
* Google Calender API: https://docs.google.com/document/d/1atMCAui86AwBSWEz8lCIJFaNkUL4V5fwVecNcnxSpP0/edit
* Google Tasks API: https://docs.google.com/document/d/1AxGWZziRmWGfXmMuuxaUzVqP4-9Cn9GkN3X8Qn-0888/edit#
* Google Maps Embedded API: https://docs.google.com/document/d/1BrK8KIi1jxdETaGoEcuEB_UDiGwZhFFeWxZ_dlwiFww/edit#heading=h.gkfplvc4i8hr
* Reddit API: https://docs.google.com/document/d/1YvhzlfshJvUZ_7GWKKUiI0KUppHE-Ee_l4Xp3jMJuFc/edit

## How To Run:

### -1. This Flask application requires credentials in order to run properly.
> Since this Flask application uses OAuth2.0 to access Google APIs, the application needs to have a client ID and a client secret issued by Google. This is necessary as the credentials allow Google to identify the application and lets end users authenticate the application. If you want to test this application, please refer to the following directions.

1. Obtain a Google account if you do not have one.
2. Go to your Google Cloud Console.
3. Create a project.
4. Navigate to the session named "APIs & Services".
5. Navigate to the OAuth consent screen section. Configure the OAuth consent screen. Be sure to include the following scopes are enabled: email, profile, openid.
```
  1. In order to enable the Calendar and Tasks API, navigate to "Library". Search for Calendar and Tasks, and enable them.
  2. While you are at "Library", enable the Maps Embed API and retrieve an API key for later use.
  3. Navigate back to the OAuth consent section and add the following scopes: ../auth/calendar, and ../auth/tasks.
```
6. Navigate to the Credentials section. Create credentials for the test application. Be sure to add the associated redirect URI for this application.
```
  1. When you create an OAuth client ID or click on an existing OAuth client ID, you should see a section labelled "Authorized redirect URIs".
  2. Enter the following redirect URI if you are testing on a local computer using localhost: http://localhost:5000/google/oauth2.
```
7. Create a creds.json file or rename the creds_example.json file to creds.json and place it in the project main/root directory. Be sure to use the following format. Replace "your_client_id" with the correct OAuth client ID, and replace "your_client_secret" with the corresponding client secret.
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
cd Planner-Project
git submodule update --init --recursive
```

### 3. Activate your virtual environment
```
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
