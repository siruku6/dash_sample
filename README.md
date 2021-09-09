# App Name

## Overview

## Description

## Requirement

You need to install the following packages on your Host OS.

- docker
- docker-compose

## Build Environment

1. Prepare .env
    ```bash
    $ cp .env.example .env
    ```

2. Prepare docker image and container
    ```bash
    $ docker-compose build

    # NOTE: Please don't run docker-compose up, but exec this shell to raise container.
    $ ./container_raiser.sh
    ```

And then, you can access [localhost:8050](http://localhost:8050) with your browser.
