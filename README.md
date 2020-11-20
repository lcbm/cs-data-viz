# 📈 Data Viz Activity

## Contents

- [Activity](#activity)
- [Development](#development)
- [Contributing](#contributing)
- [LICENSE](#license)

## Activity

This repository contains the specification for bringing the Ball Operation Dashboard stack up. Currently, the services are organized as a Docker swarm stack in compose-like files (in `docker` directory).

1. Export the [Brazilian eCommerce dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce) to one of the DBMS (Database Management Systems) below:
    - [Mongo](https://www.mongodb.com)
    - [Postgres](https://www.postgresql.org) DBMS instance;
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

## Contributing

We are always looking for contributors of **all skill levels**! If you're looking to ease your way into the project, try out a [good first issue](https://github.com/lcbm/cs-data-viz/labels/good%20first%20issue).

If you are interested in helping contribute to the project, please take a look at our [Contributing Guide](CONTRIBUTING.md). Also, feel free to drop in our [community chat](https://gitter.im/lcbm/community) and say hi. 👋

Also, thank you to all the [people who already contributed](https://github.com/lcbm/cs-data-viz/graphs/contributors) to the project!

## License

Copyright © 2020-present, [CS Data Viz Contributors](https://github.com/lcbm/cs-data-viz/graphs/contributors).
This project is [ISC](LICENSE) licensed.
