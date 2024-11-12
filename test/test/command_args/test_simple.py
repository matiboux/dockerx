from test.src.TestDirContext import TestDirContext
from test.src.format_dockerx_stdout import format_dockerx_stdout

def test_echo_number(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', '42',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo 42',
			),
		)

def test_echo_word(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', 'hello',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo hello',
			),
		)
