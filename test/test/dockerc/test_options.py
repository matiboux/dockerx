from test.src.TestDirContext import TestDirContext
from test.src.format_dockerx_stdout import format_dockerx_stdout

def test_dockerc_all_args(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'dockerc', '-', 'run', '--', 'sh'
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'cd \'' + ctx.cwd.encode() + b'\''
				b'\n> '
				b'dockerc - run -- sh'
			),
		)
