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


## Usage

DockerX simplifies running docker programs and docker shell environments in your project or working directory.

Examples:

- Run the Python interactive interpreter in your current working directory:

  ```sh
  dockerx python
  # -> docker run -it --rm -v $(pwd):/workdir -w /workdir python
  ```

- Run a shell command in an Ubuntu environment in your current working directory:

  ```sh
  dockerx ubuntu find . -type f -name "*.txt"
  # -> docker run -it --rm -v $(pwd):/workdir -w /workdir ubuntu find . -type f -name '*.txt'
  ```

- Set your project directory as context and run commands in it:

  ```sh
  # Set your project directory as context path (eg. /home/user/my-project)
  dockerx -s
  # -> Saves /home/user/my-project as context path in ~/.dockerx

  # Change directory in your project (eg. /home/user/my-project/src)
  cd src/
  
  # Run npm install in your project
  dockerx node npm install
  # -> docker run -it --rm -v /home/user/my-project:/workdir -w /workdir node npm install
  ```


## License

Copyright (c) 2024 [Matiboux](https://github.com/matiboux) ([matiboux.me](https://matiboux.me))

Licensed under the [MIT License](https://opensource.org/license/MIT). You can see a copy in the [LICENSE](LICENSE) file.
