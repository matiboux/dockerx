from test.src.TestDirContext import TestDirContext
from test.src.format_dockerx_stdout import format_dockerx_stdout

def test_space(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', '@yes sir',
		)
		# Default is to run the image's default command
		dockerx.assert_context_error(
			b'Error: Unknown docker command preset \'@yes sir\'\n'
		)

def test_escaped_space(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', '@@yes sir',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu \'@yes sir\'',
			),
		)
