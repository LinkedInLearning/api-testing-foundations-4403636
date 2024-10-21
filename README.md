# API Testing Foundations
This is the repository for the LinkedIn Learning course API Testing Foundations. The full course is available from [LinkedIn Learning][lil-course-url].

![API Testing Foundations][lil-thumbnail-url] 

The ability to quickly and effectively test APIs is a critical skill for software testers and QA engineers. In this intermediate-level course, instructor Dave Westerveld covers the basics of API testing, sharing how to work with several industry-standard tools for testing APIs at scale in an organization. After providing a primer on web services and important API terminology, Dave shows how to use Postman for some basic API exploration. He then goes over some basic approaches and methodologies used in testing GET, POST, PUT, and DELETE requests; discusses some of the details of performance and security testing; and more.

## Installing
1. To use these exercise files, you must have the following installed:
	- python 3.11
    - poetry
2. Clone this repository into your local machine using the terminal (Mac), CMD (Windows), or a GUI tool like SourceTree.

If you don't have the necessary prerequisites, see the sections below on how to install them

### Installing python
You will need python 3.11 to run this application. You can check what version of python you have by going to the command shell (search for "terminal" in your applications) and calling 
```bash
python -V
```
Note that on older Macs you that come with python 2 installed the `python` command will point to python 2. You should also try running `python3 -V` to see if you have python 3 installed.

If you do not have version 3.11, you will need to install it.

#### Mac OS
You can install python on a Mac using the `homebrew` package manager. If you do not yet have homebrew installed (you can check by running `which homebrew`), run the following command

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

To install python run this command:
```bash
brew install python@3.11
```

#### Windows
To install the latest version of python on Windows, go to the [Windows downloads](https://www.python.org/downloads/windows/) page on python.org. Download the latest release and run the installer.

### Installing Poetry
This application uses [poetry](https://python-poetry.org/docs/) for dependency management. You can install poetry with the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Once you have it installed, you can use it to install all the other package dependencies.

## Setup

### Environment setup
You need to set the `DATABASE_URL` environment variable to point to a database server.
This application will run off of an in-memory database so you can set it like this at the command line:

`export DATABASE_URL="sqlite+pysqlite:///./sql_db.db"` 

or on Windows:

`set DATABASE_URL="sqlite+pysqlite:///./sql_db.db"`

### Installing
With python 3.11 and poetry installed, you are ready to setup this application. Use poetry to install all the dependencies:

```bash
poetry install
```

## Running the app locally
In order to run this app locally call this command:

```bash
poetry run uvicorn main:app --reload
```

Alternatively, you can run it with the make command:

```bash
make run-dev
```

You can then access the application at http://127.0.0.1:8000

You can see documentation for the API at http://127.0.0.1:8000/docs


### Instructor

Dave Westerveld            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/dave-westerveld).

[lil-course-url]: https://www.linkedin.com/learning/api-testing-foundations-22763217?dApp=59033956&leis=LAA
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D4E0DAQGYSZSvOzrO-Q/learning-public-crop_675_1200/0/1697137417352?e=2147483647&v=beta&t=hR5AnoqA0zfb0uh7CP0_qCKanLmq2F6mIYE2z3KTCVs

