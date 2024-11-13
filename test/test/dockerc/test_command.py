from test.src.TestDirContext import TestDirContext
from test.src.format_dockerx_stdout import format_dockerx_stdout

def test_dockerc_config(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'dockerc', '-', 'config',
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'cd \'' + ctx.cwd.encode() + b'\''
				b'\n> '
				b'dockerc - config'
			),
		)

def test_dockerc_run(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'dockerc', '-', 'run', 'app',
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'cd \'' + ctx.cwd.encode() + b'\''
				b'\n> '
				b'dockerc - run app'
			),
		)
