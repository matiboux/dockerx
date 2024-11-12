from test.src.TestDirContext import TestDirContext
from test.src.format_dockerx_stdout import format_dockerx_stdout

def test_simple(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu',
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it -v \'' + ctx.cwd.encode() + b':/app\' ubuntu'
			),
		)
