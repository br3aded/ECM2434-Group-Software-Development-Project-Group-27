### Group 27 Eco-taskmaster
___

The group members are:

1. Matthew Wood
2. Kelsey Holdgate
3. Isaac Ng
4. Nicholas O’Connor
5. Molly Berridge
6. OPPONG-MENSAH, Kwadwo 


This is a submission for Sprint 2. There are three types of document that you will find the following places.

## PROCESS DOCUMENTS
Our process documents are managed in the trello platform. The link to our project page is below. We (specific username that added) have added mattcollison2 to the board so it is visible.

trello link: [https://trello.com/b/nDIpWRIj/group-software-development-project-group-27]

We have also taken regular snapshots of the kanban board in trello to archive our progress. These are held in the repository below.

[https://drive.google.com/drive/folders/1owaNvxyRhM1L8AAPdHvnkjRPB7oqDzZN?usp=sharing)

Within process documents we have also included the meeting notes, agenda and minutes. These will be found in the repository below.

[https://drive.google.com/drive/folders/1j0YWuejh4w8nyhEPO6uXpL1ITFRKZ2Vb?usp=sharing](./process-documents/meeting-notes/)


## TECHNICAL DOCUMENTS
Our technical documents are primarily managed on the github system. The link to the project is below:

github link: [https://github.com/br3aded/ECM2423-Group-Software-Development-Project-Group-27]

We have also include the versioned source code for archiving.

[https://drive.google.com/drive/folders/1Hs6aQ3uczqaBga1v_cfsOxot4FBWeMr-?usp=sharing](./technical-documents/)

Technical documents are broken down into front end and back end etc.  

## PRODUCT DOCUMENTS
Our product documents are primarily in the form of a product UI. Below is a link to our latest version.

public link: [https://eco-taskmaster.10dletfrab6e.eu-gb.codeengine.appdomain.cloud/home/] (note this cloud version is 1 pull request behind submitted source code)


The UI and design documents for the client have also been archived under the link below:

[https://drive.google.com/drive/folders/1f4gxSqQ7yZP-JuRolXVzUcP13yPViaar?usp=sharing](./product-documents/UI/)

## Onboarding

This is a guide for someone new joining the project or would like to get started extending the project.
The code is split into 3 apps users,home,game. These 3 apps each deal with there own part of the application.

### User

User is the most simple of the apps.

All it contains is the AppUser Model. All this is is the Prebuilt in django User model with a points field added to keep track of the users total points within the game. (See User Manual to see how the points system works).

We use the prebuilt in User model as it comes with authentication features that makes implementing logging and out a user simple.

### Home

The home app is where the user logs in and out takes place and where the user will go to when first accessing the App.

Within the home/static folder can be found all the javascript , css and image files used within the home App.

Here is a list of all files:

button-dim.js

default.css

favicon-large.png

favicon.png

forum-background.jpeg

main.js

page-logic.js

piazza-aerial.jpg

sidebar.css

style1.css

Within the home/templates folder are all the html files related to the home app.

Here is a list of all the files within that folder:

index.html

login.html

template.html

The first page the user sees is rendered in the Members View(home/) which uses the index.html file found in the templates file and styled in the static folder.

When first accessing the page you will see a sidebar that is being used through out all the pages this is a resuable and can be found in most html files.

The other views used within home are:

login_view(login/) - used to render the login.html template , the user can create a new account or login from this page.

add_user(login/add_user) - creates a new User and AppUser model and adds to the database ,returns a HttpRedirect to login.

login_user(login/user_login) - called when attempting to login. Uses django Authetication Features to verify is the details the person is trying to login with exist if so they are logged in and sent the game page if not they are sent back to login page.

logout_user(logout/) - Called when the logout button is pressed on the side bar at anytime and Uses Django logout feature to log the userout and returns them back to home.

The only model in home/models.py is the group model which is mainly used in the game app to store that users that are playing each game. The group model contains the fields group_leader which is just an AppUser and is the person who created the lobby. Max_players which is just an integer and is value stored when the player creates a game to decide they number of players in a game and group_members which store multiple GroupMembers fields which come from the GroupMembers Model. The group members model contains the fields user_id which is just an AppUser , group_id which is just a group and points_earned which is used to track the points earned in a single game.

### Game 

The game app is where most of the functionality of the game is. The user is first taken to a page where they can enter a game code , create a new game or view there lobbys.

Game lobbys are created through Game model this contains the fields game_name which is the lobby name the player submits , game_code which is a randomly generated 5 letter that is used to access game data, start_datetime which is just the time when the lobby is created , game_state which is at what point the game is (all the game states are defined inside of game model) , max_rounds which is also submitted by the user when the game is created and is how many tasks will be played through out the game, Current_round_number is used to track what round of the game is being played , current_round_name is where we store the task name for each round, hosting_group is a Group model and submissions is part of the submissions model.

The submissions model also contained in game app and is used for submitting images for task. It contains 3 fields user_id which stores the the AppUser for the submission , game_id which stores what game the submission is used for and submission which is a Binary Field that is used to store the actual image.

Inside of game/static can found found all the javascript , css , file images and a text file called tasks.txt that is used to store already made task suggestions. All these files are used within the game app.

Here are all the files within this folder:

create1.css

create2.js

default1.css

display-results.js

favicon.png

forum-background.jpeg

gamelobby.css

icon-placeholder.jpg

playerlobby.css

populate-lobby.js

populate-tasks-demo.js

ranking.js

setting-task.css

sidebar1.css

sidebar2.css

submit-task.css

take-photo.js

tasks.txt

verify-lobby-code.js

waiting-players.css

waiting.css

Within the game/templates are all the html files used within the folder.

Here are all the files within this folder:

createlobby.html

gamelobby-client.html

join_lobby.html

player_lobbys.html

results-demo.html

setting-task-demo.html

setting-task.html

submit_task.html

take_picture.html

temp.html

test.html

waiting_for_players.html

waiting_for_task.html

waiting_ranking.html

waiting_reponse.html

The views used within game app are:

create_lobby(/create_lobby) - this view is used to render the createlobby.html template

add_lobby(/add_lobby) -  this is called from within createlobby.html and creates a new Game model for the details the user has entered it then renders the lobby view

add_player(/add_player) -  this is used when joining a lobby through game code and retrevies all the data related to a game lobby and returns a JsonResponse

lobby_view(/lobby/<str:game_code>) - this is where all the correct view and pages are rendered based on the game state and is where the main functionality of game code is contained

set_task_view(/setting_task/<str:game_code>) -  this randomly gets 3 tasks from task.txt file and then renders setting-task.html passing these 3 tasks to it

set_task(/set_task/<str:game_code>) - this takes the POST from setting-task.html and saves a task under game.current_round_name and then goes back to the lobby view

members(/game) - this renders the join_lobby.html page which is the page the user goes to after logging in

player_lobbys(/player_lobbys) - this filters through all the games that the current user is logged into and then renders the player_lobbys.html page passing this list of games. On this page the user can load into any lobby they are a part of

submit_task(/submit_task/<str:game_code>) - renders player_lobbys.html page

take_picture(/take_picture/<str:game_code>) -  this renders the take_picture.html page
