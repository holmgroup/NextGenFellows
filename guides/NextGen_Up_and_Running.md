# NextGen: Up and Running with Python
Andrew Kitahara
Last edited: June 4, 2020

## Objectives:
In this first exercise, we'll focus on getting up and running with Python 3.X by using Jupyter notebooks. If you're already familiar with Python, great! If you're not, don't worry; we'll get you up to speed soon enough. Our objectives are detailed here:
1. Install Python and Make a Virtual Environment
2. Install additional libraries
3. Launch Jupyter from Terminal/ Command Line


## 0. If You're Already Familiar
If you're already familiar with Python and Jupyter, feel free to skip this read. Just be sure you've downloaded the data from Box.


## 1. Install Python and Make a Virtual Environment
### 1.1 Installing Python
One of the biggest hurdles for newcomers to Python is getting up and running with a working environment. Let's start by making sure that we have Python 3 installed on our machines. I'm starting from scratch to hopefully emulate the steps that anyone who is completely new might need to step through. It's easy enough to download Python from the official website [here](https://www.python.org/downloads/) and install on your computer. As of June 3, 2020, the most recent version released is Python 3.8.3 which is what I've downloaded. I'm running macOS and the installation was simple enough with the default conditions; I can see Python 3.8 successfully installed in my Applications folder. The process should be similarly simple for Windows users. If you use Linux, then I hope you're already comfortable with the package manager for your system. Specifically for Ubuntu users, you can install with `sudo apt-get -y install python3.8`.

Verify that you have successfully installed Python. If you already have Python installed, you might have multiple versions that you can check, but for the sake of continuity I will be referring to Python 3.8.3. In your Terminal or Command Line, execute the following (the `$` marks the end of what my console writes, and the beginning of where I will write):
```Shell
$ python3.8 -v
```
This should return the following line:
```
Python 3.8.3
```

### 1.2 Make a Virtual Environment
Great! That was easy! Now let's do something neat; let's set up a virtual environment for us to develop our projects. Sure, you could get up and running right away with your newly installed Python, but it's good practice to set up a virtual environment for your projects. One of the most common frustrations that I've encountered is to make this awesome package of code, then come back months later to find out that it doesn't work anymore because I've changed dependencies by upgrading certain libraries in my main environment.

Setting up a virtual environment is easy. This is how I am making a virtual environment called `nextgen` using my new installation of Python 3.8. Do note, you'll want to make sure your current working directory is somewhere convenient for making a virtual environment. Executing the following command will make a directory for the virtual environment in your current working directory. You might be inclined to put everything in your default home directory, or if you think you'll have multiple projects, you might consider making a dedicated directory to manage this and future virtual environments.

---
**NOTE**

This guide was made and tested on macOS and Linux machines. Windows users might want to follow this guide [(link)](https://realpython.com/python-virtual-environments-a-primer/) to set up their virtual environment.

---

Make a root directory to manage virtual environments.

```Shell
$ mkdir python_venvs
$ cd python_venvs
```


```Shell
$ python3.8 -m venv nextgen
```

Now we can activate our environment with the following:
```Shell
$ source nextgen/bin/activate
```

And similarly, you can deactivate with:
```Shell
(nextgen)$ deactivate
```

Go ahead and **keep your virtual environment activated** for the rest of this tutorial. Once you've activated your virtual environment, you can change directories within your Terminal as you please.

### 1.3 Other Options
I made this with the idea that I would try to keep things as simple as possible to help you get up and running with minimal frustration. But do know that there are several options in managing your virtual environments. `Anaconda` is one of the most popular distribution platforms because it has a simple wrapper for managing libraries. It's worth checking out if you're really interested in this kind of thing. Perhaps the biggest benefit of Anaconda is that by default it includes many commonly used Python libraries, which means users spend less time manually installing libraries.

## 2. Install Additional Libraries
### The quick way: install from `requirements.txt`.
```Shell
(nextgen)$ pip install -r requirements.txt
```

### The slower way: piece by piece.
Now we'll install additonal libraries using the Python package installer, `pip`. Go ahead and navigate to your project folder.

```Shell
# go to your default/ home directory
(nextgen)$ cd ~
# navigate to the project directory
(nextgen)$ cd Documents/NextGen2020
```

We can check the list of currently installed libraries with the following command:
```Shell
(nextgen)$ pip list
```

If everything has gone well, you should see the following list (versions may vary):
```
Package    Version
---------- -------
pip        19.2.3
setuptools 41.2.0
```
You might even see a warning message urging you to upgrade `pip` if there's a more recent version available. If so, you can upgrade `pip` with the following:
```Shell
(nextgen)$ pip install --upgrade pip
```

Now let's install a few extra libraries that we'll use today. Namely: `numpy`, `pandas`, and `matplotlib`. We can do these three in one line, separating each name by a space.

```Shell
(nextgen)$ pip install numpy pandas matplotlib
```

At this point `pip list` should return this:
```Shell
Package         Version
--------------- -------
cycler          0.10.0
kiwisolver      1.2.0
matplotlib      3.2.1
numpy           1.18.5
pandas          1.0.4
pip             20.1.1
pyparsing       2.4.7
python-dateutil 2.8.1
pytz            2020.1
setuptools      41.2.0
six             1.15.0
```

And while we're at it, let's install a couple extra nice libraries, `scikit-image` and `scikit-learn`:
```Shell
(nextgen)$ pip install scikit-image scikit-learn
```

Let's install one more thing that will help us as we embark on some data exploration: `jupyterlab`. Read up on Project Jupyter here [(link)](https://jupyterlab.readthedocs.io/en/stable/index.html). You know the drill:

```Shell
(nextgen)$ pip install jupyterlab
```

## 3. Launch Jupyter Lab
From within the project directory, run the following to launch an interactive Python environment in your web browser with Jupyter:
```Shell
(nextgen)$ jupyter lab
```

This should launch the Jupyter Lab client in your web browser at `localhost:8888`. Inside you should see the project folder that contains the following:

```
data/
notebooks/
LICENSE
README.md
requirements.txt
```

If you haven't downloaded the data from Box yet, this is the time to do it. Ryan uploaded a folder to the Box called `NEU-CLS`. Download that and save it under the `data/` directory.
