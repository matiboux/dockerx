from test.src.TestDirContext import TestDirContext

def test_get_context(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'--get-context',
			env = {
				'DOCKERX_CONTEXT_FILE': './.dockerx-not-found',
				'DOCKERX_CHECK_PARENT_CONTEXT': 'false',
			},
		)
		dockerx.assert_context_ok(
			b'Warning: Context path \'/tmp/not_found\' not found, using current directory\n'
			+ ctx.cwd.encode() + b'\n'
			b'(current directory)\n'
		)

def test_get_context_shorthand_g(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-g',
			env = {
				'DOCKERX_CONTEXT_FILE': './.dockerx-not-found',
				'DOCKERX_CHECK_PARENT_CONTEXT': 'false',
			},
		)
		dockerx.assert_context_ok(
			b'Warning: Context path \'/tmp/not_found\' not found, using current directory\n'
			+ ctx.cwd.encode() + b'\n'
			b'(current directory)\n'
		)

def test_get_context_shorthand_c(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-c',
			env = {
				'DOCKERX_CONTEXT_FILE': './.dockerx-not-found',
				'DOCKERX_CHECK_PARENT_CONTEXT': 'false',
			},
		)
		dockerx.assert_context_ok(
			b'Warning: Context path \'/tmp/not_found\' not found, using current directory\n'
			+ ctx.cwd.encode() + b'\n'
			b'(current directory)\n'
		)
