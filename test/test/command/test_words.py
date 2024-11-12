from test.src.TestDirContext import TestDirContext
from test.src.format_dockerx_stdout import format_dockerx_stdout

def test_echo_words(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', 'hello', 'world',
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo hello world',
			),
		)

def test_echo_phrase(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', 'The quick brown fox jumps over the lazy dog.',
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \'The quick brown fox jumps over the lazy dog.\'',
			),
		)

def test_echo_mix(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', 'To be', 'or', 'not to be?',
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \'To be\' or \'not to be?\'',
			),
		)
