from test.src.TestDirContext import TestDirContext
from test.src.format_dockerx_stdout import format_dockerx_stdout

def test_default(file = __file__):
	with TestDirContext(file) as ctx:
		# Default will run the image's default command
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu',
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu',
			),
		)
