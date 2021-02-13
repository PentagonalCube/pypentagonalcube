# pypentagonalcube
A public repository to hold a python toolkit.


# Overview

- [Installation](#Installation)
  - [Versions](#Versions)
- [Logging](#Logging)
- [Requests](#Requests)
- [Quickstart](#Quickstart)


  

# Installation

You can add a line containing the information to your `requirements.txt` for your project:
`git+ssh://git@github.com/PentagonalCube/pypentagonalcube.git@v0.3.8` 
`git+https://git@github.com/PentagonalCube/pypentagonalcube.git@v0.3.8`

It is also possible to install it directly via pip:
`python -m pip install git+ssh://git@github.com/PentagonalCube/pypentagonalcube.git@v0.3.8`
`python -m pip install git+https://git@github.com/PentagonalCube/pypentagonalcube.git@v0.3.8`

## Versions

The repository is versioned using github tags that align with the pip installation version: `vx.x.x`, not every version of the code will be a github release.

Installation without and `@<version>` tag will install from the base branch `main`, this is always the latest version of the code.



# Logging

The logger here is just the default logger but with the logging level set by the environment.

**Usage**

```
from pypentagonalcube import logging
logging.info(f"message here")
```

**Environment Variable**

```
#   Defaults to "error".
PYPENTAGONALCUBE_DEBUG=info  #  Valid options: debug, info, warning, error, critical
```


# Requests

Needing to make an HTTP(s) request is pretty common, the function within this package allows you to make a request though through a basic cache mechanism.


**Environment Variable**

```
#   Defaults to 15 minutes.
PYPENTAGONALCUBE_CACHE_SECONDS=60  # Any positive number is valid here.  
```


## Examples

**JSON GET Request**

```
from pypentagonalcube import get_web_request_via_cache
response = get_web_request_via_cache(url=EXAMPLE_GET_URL)
```


# Quickstart

A CLI tool to get a definition containing most of the configuration options for a given service/technology.

Rather than just copy/paste pieces from existing projects when starting new ones, it makes sense to centralise the information into a single template and then use that.

Quickstart will create a copy of the definition file stored within its package version for various files.

**Running the tool**

TODO: At the moment the script `quickstart.py` can be run.
