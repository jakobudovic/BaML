# Python environment setup

This file is meant to help you with setting up your Python installation. If you are already familiar with Python, you might not need to read all steps thoroughly.

> This file is a MARKDOWN file. These allow for simple text formatting. Although not strictly necessary, we recommend to use a text viewer/editor which can display MARKDOWN files in their formatted version for improved readability.

## Install Python

Go to the [Python website](https://www.python.org/downloads/) and install Python for your OS.

- Feel free to get the latest version of Python 3. We recommend a minimum version of 3.10.
- Python usually offers an installation manager which guides you through the setup.
- We suggest that you also install pip and the documentation files.
- Also, don't forget to add Python to your system PATH. See, e.g., [here](https://realpython.com/add-python-to-path/) for additional information.

Verify your installation by opening a terminal (search for `cmd` on Windows) and executing
```bash
python --version
```
If the installation was successful, you should see the installed version of Python as a response.

> **Note**: On Linux, Python is already pre-installed. We strongly discourage uninstalling Python in this case since it is part of the operating system. In case you need a newer version of Python, please make sure that you install it *additionally* and not as a replacement.


## Create a virtual environment

In this step, we will create a virtual environment for development. 

- Virtual environments are separate "installations" of Python which are mostly decoupled from your main installation of Python.
- In particular, they allow to install additional packages without affecting the main or other virtual environments. 
- This usually helps to keep development requirements clean and simple.

In this manual, we introduce the use of `python venv` for environment management. 

- It is a simple and pre-installed (with Python) tool. See [here](https://docs.python.org/3/library/venv.html) for additional information. 
- Alternative environment management tools include [`virtualenv`](https://pypi.org/project/virtualenv/) or [Anaconda](https://www.anaconda.com/) / [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/). They are usually more feature-rich but need more work to be set up. 

If you already have experience with virtual environments or are certain that you don't need this feature, you may skip this step. We will now proceed with `python venv`.

First, start by **creating a folder** in which you would like to put all your BAML-related code. We want to call this directory `BAML/`, but your path may differ, of course. 

Open a terminal / command window and **navigate inside this directory**. 

Next, check that your Python installation supports `venv`. To this end, run
```bash
python -m venv -h
```
This command should print the help text for `venv`.

Finally, **create the environment** by running
```bash
python -m venv baml-venv
```
This creates an environment in the subdirectory *baml-venv*. In this directory, the equally named **environment `baml-venv`** is located.

> If you have multiple Python installations on your system (e.g. on Linux), please make sure to specify the correct one. Note that aliases for Python might not work correctly when using this command.


## Activate the virtual environment

Until now, the environment is created but not active. This means that packages will still be installed to your main Python installation. 

To **activate the environment**, you need to run an OS-specific command (from `BAML/`) which executes a script in the environment's folder:

| Platform | Shell | Command to activate virtual environment | 
| -------- | ----- | --------------------------------------- |
| POSIX (Linux/Mac) | bash/zsh | `source baml-venv/bin/activate` |
|          | fish | `source baml-venv/bin/activate.fish` |
|          | csh/tcsh | `source baml-venv/bin/activate.csh` |
|          | PowerShell | `baml-venv/bin/Activate.ps1` |
| Windows  | cmd.exe | `baml-venv\Scripts\activate.bat` |
|          | PowerShell | `baml-venv\Scripts\Activate.ps1` |

(Table adapted from [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html))

If the command runs sucessfully, you should see an indication that the environment is active on the left side of the current terminal line, similar to this:
```bash
(baml-venv) C:\<...>\BAML>
```

> Note: You can deactivate the environment later by typing `deactivate` in your shell.


## Installing packages

For package installation, you can use the `pip` command. Check that it is set up by typing
```bash
pip --version
```

After having verfied that your environment is active, **install the required packages for this course**. First, copy the *requirements.txt* file from the Moodle course to your `BAML/` directory. Then, you can easily install the packages by calling
```bash
pip install -r requirements.txt
```

You can view and verify the installed packages by executing
```bash
pip list
```

## Test environment

Copy the script `test-installation.py` to your `BAML/` folder and run
```bash
python test-installation.py
```

## Development in an IDE

Many IDEs support selection of a Python environment for execution. We cannot give a complete tutorial for this purpose here. For some popular editors, we provide helpful links below:

- [Visual Studio Code](https://code.visualstudio.com/docs/python/environments)
- [Pycharm](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#widget)


## Starting Jupyter notebooks

Jupyter notebooks are files which

- mix Python code with formatted text
- can interactively execute Python code (actually, a Python instance is running in the background)

> If you are already familiar with Jupyter notebooks, feel free to use any of your preferred options. For example, Visual Studio Code has great support for Jupyter notebooks.

> If you are new to Jupyter, we recommend to use the solution below since it should be functional with the setup described until here.

Within a shell with active virtual environment, run 
```bash
jupyter notebook <path to BAML/>
```

This should bring up a new site in your browser. Don't worry - this site is running locally on your system without connecting to the internet (see address line).

On this site, you can navigate your local directories and open files. 
In particular, you can open, modify and execute `.ipynb` files. 

Next, we suggest that you try this feature by continuing with our Python basics tutorial.