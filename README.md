# 📈 Data Viz Activity

This repository contains the specification for the _**Data Visualization Activity 7 Stack**_. Currently, the services are organized as a [Docker swarm](https://docs.docker.com/engine/swarm/key-concepts/) stack in compose-like files (located in the `cs-data-viz/docker` directory).

## Contents

- [Activity](#activity)
- [Development](#development)
- [Deploying the Stack](#deploying-the-stack)
- [Contributing](#contributing)
- [LICENSE](#license)

## Activity

1. Export the [Brazilian eCommerce dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce) to one of the DBMS (Database Management Systems) below:
    - [Mongo](https://www.mongodb.com)
    - [Postgres](https://www.postgresql.org)
2. Connect the chosen DBMS to [Metabase](https://www.metabase.com);
3. Create data exploration visualizations in Metabase;

## Development

To install the **development pre-requisites**, please follow the instructions in the links below:

- [Python 3.8](https://www.python.org/downloads/)
- [Poetry](https://github.com/python-poetry/poetry#installation)

### Installing development dependencies

First, change your current working directory to the project's root directory and bootstrap the project:

```bash
# change current working directory
$ cd <path/to/cs-data-viz>

# bootstraps development and project dependencies
$ make bootstrap
```

>_**NOTE**: By default, [poetry creates and manages virtual environments to install project dependencies](https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment) -- meaning that it will work isolated from your global Python installation. This avoids conflicts with other packages installed in your system._

## Deploying the Stack

### Requirements

Considering that the stack is organized as a [Docker swarm](https://docs.docker.com/engine/swarm/key-concepts/) stack in compose-like files (located in the `cs-data-viz/docker` directory), the following dependencies must be installed:

- [Docker](https://docs.docker.com/get-docker/)

> **_note_**: if you're using a Linux system, please take a look at [Docker's post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)!

### Setup

Firstly, make sure to build the **database** Docker image. From the project's root directory:

```bash
# change current working directory
$ cd docker/database

# build the docker image
$ docker build . -f Dockerfile -t postgres:cs-data-viz
```

Now, pull the remaining docker images used by the stack:

```bash
# fetches services' docker images
$ make docker-pull
```

Finally, update the `docker/env.d` files for each service with the appropriate configurations, credentials, and any other necessary information.

### Initialize Swarm mode

In your deployment machine, initialize Docker Swarm mode:

```bash
# joins the swarm
$ docker swarm init
```

>**_NOTE:_**  For more information on what is Swarm and its key concepts, please refer to [Docker's documentation](https://docs.docker.com/engine/swarm/key-concepts/).

### Deploying services

After following the previous steps, ensure you are in the `docker` stack directory and then deploy the stack:

```bash
# change current working directory
$ cd docker

# deploys/updates the stack from the specified file
$ docker stack deploy -c compose.yml cs-data-viz
```

### Verifying the Stack's Status

Check if all the services are running and have **exactly one** replica:

```bash
# list the services in the cs-data-viz stack
$ docker stack services cs-data-viz
```

You should see something like this:

```text
ID                  NAME                    MODE                REPLICAS            IMAGE                          PORTS
acob7yl286jg        cs-data-viz_postgres    replicated          1/1                 postgres:cs-data-viz
vkzcj6n9t7tt        cs-data-viz_metabase    replicated          1/1                 metabase/metabase:v0.37.2      *:3000->3000/tcp
```

At this point, the following resources will be available to you:

- [Metabase](https://www.metabase.com) UI is available at `http://localhost:3000`

>**_NOTE:_**  In case `localhost` doesn't work, you may try `http://0.0.0.0:<port>` instead.

### Logging

In order to check a service's logs, use the following command:

```bash
# fetch the logs of a service
$ docker service logs <service_name>
```

> **_NOTE:_**  You may also follow the log output in realtime with the `--follow` option (e.g. `docker service logs --follow cs-data-viz_postgres`). For more information on service logs, refer to [Docker's documentation](https://docs.docker.com/engine/reference/commandline/service_logs/).

### Wrapping up

Once you're done, you may remove what was created by `docker swarm init`:

```bash
# removes the cs-data-viz stack from swarm
$ docker stack rm cs-data-viz

# leaves the swarm
$ docker swarm leave
```

>**_NOTE:_**  All the data created by the stack services will be lost. For more information on swarm commands, refer to [Docker's documentation](https://docs.docker.com/engine/reference/commandline/swarm/).

## Contributing

We are always looking for contributors of **all skill levels**! If you're looking to ease your way into the project, try out a [good first issue](https://github.com/lcbm/cs-data-viz/labels/good%20first%20issue).

If you are interested in helping contribute to the project, please take a look at our [Contributing Guide](CONTRIBUTING.md). Also, feel free to drop in our [community chat](https://gitter.im/lcbm/community) and say hi. 👋

Also, thank you to all the [people who already contributed](https://github.com/lcbm/cs-data-viz/graphs/contributors) to the project!

## License

Copyright © 2020-present, [CS Data Viz Contributors](https://github.com/lcbm/cs-data-viz/graphs/contributors).
This project is [ISC](LICENSE) licensed.
