# DockerX

Wrapper for running docker programs & docker shell environments.


## Install

First, install required dependencies on your system:
- Docker

Then, install DockerX with the following command:

```bash
/bin/sh -c "$(curl -fsSL https://raw.githubusercontent.com/matiboux/dockerx/HEAD/install.sh)"
```

Take a look at the [install.sh](install.sh) script to see what it does.

If you get the error `Failure writing output to destination`,
try to run the command again with `sudo` or grant yourself write permissions to install directory (`/usr/local/bin` by default).

```bash
sudo /bin/sh -c "$(curl -fsSL https://raw.githubusercontent.com/matiboux/dockerx/HEAD/install.sh)"
```


## License

Copyright (c) 2024 [Matiboux](https://github.com/matiboux) ([matiboux.me](https://matiboux.me))

Licensed under the [MIT License](https://opensource.org/license/MIT). You can see a copy in the [LICENSE](LICENSE) file.
