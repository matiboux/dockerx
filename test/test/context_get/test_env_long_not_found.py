from test.src.TestDirContext import TestDirContext

def test_get_context(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'--get-context',
			env = {
				'DOCKERX_CONTEXT_PATH': '/tmp/not_found',
			},
		)
		dockerx.assert_context_error(
			b'Error: Context path \'/tmp/not_found\' not found\n'
		)

def test_get_context_shorthand_g(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-g',
			env = {
				'DOCKERX_CONTEXT_PATH': '/tmp/not_found',
			},
		)
		dockerx.assert_context_error(
			b'Error: Context path \'/tmp/not_found\' not found\n'
		)

def test_get_context_shorthand_c(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-c',
			env = {
				'DOCKERX_CONTEXT_PATH': '/tmp/not_found',
			},
		)
		dockerx.assert_context_error(
			b'Error: Context path \'/tmp/not_found\' not found\n'
		)
