from test.src.TestDirContext import TestDirContext

def test_get_context(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'--get-context',
			env = {
				'CONTEXT_FILE': './.dockerx',
			},
		)
		dockerx.assert_context_ok(
			b'/tmp\n'
			b'(from .dockerx file)\n'
		)

def test_get_context_shorthand_g(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-g',
			env = {
				'CONTEXT_FILE': './.dockerx',
			},
		)
		dockerx.assert_context_ok(
			b'/tmp\n'
			b'(from .dockerx file)\n'
		)

def test_get_context_shorthand_c(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-c',
			env = {
				'CONTEXT_FILE': './.dockerx',
			},
		)
		dockerx.assert_context_ok(
			b'/tmp\n'
			b'(from .dockerx file)\n'
		)
