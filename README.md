## This template is good for

- 


## Python virtual env setup

Even though ROS runs against python2, we want to setup the virtual environment with python3 so that we can use black and flake8 formatters and linters.

```
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
