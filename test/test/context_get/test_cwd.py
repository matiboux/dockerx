from test.src.TestDirContext import TestDirContext

def test_get_context(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'--get-context',
		)
		dockerx.assert_context_ok(
			ctx.cwd.encode() + b'\n',
		)
		# dockerx.assert_context_error(
		# 	b'Error: Context path not set',
		# )

def test_get_context_shorthand_g(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-g',
		)
		dockerx.assert_context_ok(
			ctx.cwd.encode() + b'\n',
		)

def test_get_context_shorthand_c(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-c',
		)
		dockerx.assert_context_ok(
			ctx.cwd.encode() + b'\n',
		)
