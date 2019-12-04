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

## APIs Used:
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
7. Set the following environment variables. Be sure to use the following format for the correct operating systems. Replace "your_client_id" with the correct OAuth client ID, and replace "your_client_secret" with the corresponding client secret.
```
For POSIX
---------
export GOOGLE_CLIENT_ID="your_client_id"
export GOOGLE_CLIENT_SECRET="your_client_secret"

For Windows
-----------
set GOOGLE_CLIENT_ID="your_client_id"
set GOOGLE_CLIENT_SECRET="your_client_secret"
```
8. Navigate to the Credentials section. Create an API key. Restrict the API key to only work on Maps Embed API. Set Website Restriction to `http://localhost:5000/home`. Set the following environment variable using this API key.
```
For POSIX
---------
export MAPS_EMBED_API_KEY="your_maps_embed_api_key"

For Windows
-----------
set MAPS_EMBED_API_KEY="your_maps_embed_api_key"
```


### 0. Make sure python3 and pip3 are installed.

### 1. Clone
```
git clone https://github.com/cohyunoh/Planner-Project.git
```

### 2. Navigate into Planner-Project
```
cd Planner-Project
```

### 3. Pull from GitHub Submodule dependency
```
git submodule update --init --recursive
```

### 4. Make a virtual environment
```
python3 -m venv venv
```

### 5. Activate your virtual environment
```
python3 -m venv venv
. venv/bin/activate
```

### 6. Install the necessary packages outlined in requirements.txt
```
pip3 install -r requirements.txt
```

### 7. Run the Flask app
```
python3 run.py
```

### (8?). Update from GitHub Submodule if needed
```
git submodule update --recursive --remote
```
