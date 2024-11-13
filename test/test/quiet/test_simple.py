from test.src.TestDirContext import TestDirContext
from test.src.format_dockerx_stdout import format_dockerx_stdout

def test_ubuntu_quiet_first(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-q', '-n', 'ubuntu',
		)
		dockerx.assert_context_ok()

def test_ubuntu_quiet_second(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', '-q', 'ubuntu',
		)
		dockerx.assert_context_ok()
