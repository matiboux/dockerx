from test.src.TestDirContext import TestDirContext

def get_help_stdout(dockerx_path: str):
	return (
		b'Usage:\n'
		b'  ' + dockerx_path.encode() + b' [options] <image> [ [...docker_options] -- ] [...command]\n'
		b'  ' + dockerx_path.encode() + b' [options] <image> [ [...docker_options] -- ] [@preset] [...args]\n'
		b'  ' + dockerx_path.encode() + b' --set-context [path]\n'
		b'\n'
		b'DockerX will run the specified docker image in the context of your\n'
		b'working directory. \n'
		b'\n'
		b'Arguments:\n'
		b'  options: DockerX options\n'
		b'  image: Docker image to run\n'
		b'  docker_options: Options passed to docker run command\n'
		b'  command: Command to run in the container\n'
		b'  @preset: DockerX preset (shortcut for a command)\n'
		b'  args: Arguments appended to the preset command\n'
		b'\n'
		b'Arguments details:\n'
		b'  options:\n'
		b'    -h, --help           Print this help and exit\n'
		b'    -v, --version        Print version and exit\n'
		b'    --update             Update DockerX and exit\n'
		b'    -g, --get-context    Get the DockerX context path\n'
		b'    -c, --set-context    Set the DockerX context path\n'
		b'    -r, --reset-context  Unset the DockerX context path\n'
		b'    -n, --dry-run        Dry run, print docker command without running it\n'
		b'    -q, --quiet          Quiet, do not print docker command\n'
		b'  @preset: One of the following:\n'
		b'    $, @sh  Run a `sh` shell in the container\n'
	)

def test_help(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'--help',
		)
		dockerx.assert_context_ok(
			get_help_stdout(dockerx.dockerx_path),
		)

def test_help_shorthand(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-h',
		)
		dockerx.assert_context_ok(
			get_help_stdout(dockerx.dockerx_path),
		)
