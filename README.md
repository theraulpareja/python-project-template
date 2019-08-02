# python-project-template

This is just a skeleton tree with some templates to use for my python scripts and small projects.

```
|-- README.md
|-- conf
|   |-- config.ini_example
|   `-- config.yaml_example
|-- docs
|   `-- some_docs.txt
|-- logs
|   `-- logs_example.log
|-- requirements.txt
|-- src
|   `-- template_main.py
`-- tests
    `-- test_template.py
```

### conf

Directory to host config files to run an app wether INI or YAML (optional)

### docs

Contain docs of the apps (optional)

### logs

The template_main.py includes a call to customlogger class in order to setup a file and stream handler for logs in the app.

### src

Where the code lives python-project-template.py is a template for the 'main' program but it also includes some custom modules like

* customlogger.py class to set up a custom logger with file and stream handler
* readconfig.py class to read yaml config files 

### tests

To place here the unittests and (optionally) functional tests, the test_template.py has already the skeleton for setUp and tearDown functions for create and destroy logs created by logger by the app.

### requirements.txt

File with all the needed modules and pip packages that a virtualenv needs to have in order to run the app properly

