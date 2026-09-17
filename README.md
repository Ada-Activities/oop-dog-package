# Dog Class
This Repository is an example for the Intro to OOP roundtable. 

## One-Time Setup

Follow these directions once when you start working on this activity **during roundtables**:

1. Navigate to your projects folder named `projects`

```bash
$ cd ~/Developer/projects
```

2. In Github click on the green "Code" button in Github and then copy the URL. This will allow you to download a copy of this project into your projects folder. 

After copying the URL, run the following command in your terminal:

```
$ git clone <paste your copied URL here>
```
This command makes a new folder called `oop-dog-package`, and then puts the project into this new folder. Use `ls` to confirm there's a new project folder

1. Move your location into this project folder

```bash
$ cd oop-dog-package
```

4. Create a virtual environment named `venv` for this project:

```bash
$ python3 -m venv venv
```

5. Activate this environment:

```bash
$ source venv/bin/activate
```

6. Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

 7. Install dependencies once at the beginning of this project while your virtual environment is activated. Note that `(venv)` is not part of the command below that you need to run.

```bash
$ (venv) pip install -r requirements.txt
```

## Running the activity

1. Run the main file and observe the results.

```bash
$ python main.py
```

## Testing the activity

1. Run the tests with pytest

```bash
$ pytest
```

or configure them to run in the VS Code Test Explorer.