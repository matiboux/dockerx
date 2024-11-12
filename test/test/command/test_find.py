from test.src.TestDirContext import TestDirContext
from test.src.format_dockerx_stdout import format_dockerx_stdout

def test_find_simple(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'find', '.',
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu find .',
			),
		)

def test_find_args(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'find', '.', '-type', 'f',
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu find . -type f',
			),
		)

def test_find_wildcard(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'find', '.', '-name', '*.txt',
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu find . -name \'*.txt\'',
			),
		)
