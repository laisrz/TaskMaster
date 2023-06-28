# TaskMaster

*TaskMaster* is a todo app designed to be used from the command line (terminal).

## Features

### (C)reate

* Allow the user to create a new todo item by providing a task description.
* Store the task in some SQL database with additional information such as the creation date and status (e.g., "incomplete", "completed", "blocked").

### (R)ead

* Display a list of all existing todos, including all their fields.
* Allow the user to filter the list by different filters, such as displaying only completed or incomplete tasks.

### (U)pdate

* Enable the user to update the status of a todo item (e.g., mark it as completed or change it back to incomplete).
* Provide the ability to update the task description if needed.

### (D)elete

* Allow the user to delete a specific todo item by providing its ID.
* Ask for confirmation before deleting to avoid accidental removal of an item.

### How it should work

* Upon starting the app, it should connect to the SQL database (creating it if necessary) and display the main menu.
* The main menu should present options for creating a new task, viewing the task list, updating task status, modifying task description, or deleting a task.
* Depending on the selected option, the app should guide the user through the necessary steps, such as prompting for inputs or displaying the relevant information.
* After performing the requested action, the app should return to the main menu, allowing the user to choose another option or exit the app.


## Development

Create a _virtualenv_

```
python -m venv .venv
```

Activate _virtualenv_

```
source .venv/bin/activate
```
