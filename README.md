# Morning Planner By Voltron <img alt="GitHub Actions status" src="https://github.com/cohyunoh/Planner-Project/workflows/Python%20application/badge.svg">

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
