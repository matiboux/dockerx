from test.src.TestDirContext import TestDirContext
from test.src.format_dockerx_stdout import format_dockerx_stdout

def get_presets_help_stdout(dockerx_path: str):
	return (
		b'Use ' + dockerx_path.encode() + b' --help for full help\n'
		b'DockerX command presets:\n'
		b'  $, @sh  Run a `sh` shell in the container\n'
	)

def test_empty(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', '@',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			get_presets_help_stdout(dockerx.dockerx_path),
		)
