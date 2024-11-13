from test.src.TestDirContext import TestDirContext
from test.src.format_dockerx_stdout import format_dockerx_stdout

def test_dockerc_run_args(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'dockerc', '-', 'run', 'app', '--arg1', 'val1', '--arg2', 'val2',
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'cd \'' + ctx.cwd.encode() + b'\''
				b'\n> '
				b'dockerc - run app --arg1 val1 --arg2 val2'
			),
		)

def test_dockerc_run_args_space_quotes(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'dockerc', '-', 'run', 'app', '--arg', 'yo and "hello"'
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'cd \'' + ctx.cwd.encode() + b'\''
				b'\n> '
				b'dockerc - run app --arg \'yo and "hello"\''
			),
		)

def test_dockerc_run_args_star(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'dockerc', '-', 'run', 'app', '--arg', '*hello'
		)
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'cd \'' + ctx.cwd.encode() + b'\''
				b'\n> '
				b'dockerc - run app --arg \'*hello\''
			),
		)
