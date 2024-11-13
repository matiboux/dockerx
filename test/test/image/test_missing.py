from test.src.TestDirContext import TestDirContext
from test.src.format_dockerx_stdout import format_dockerx_stdout

def test_missing(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n',
		)
		dockerx.assert_context_error(
			b'Error: No image specified\n',
		)

def test_empty(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', '',
		)
		dockerx.assert_context_error(
			b'Error: No image specified\n',
		)
