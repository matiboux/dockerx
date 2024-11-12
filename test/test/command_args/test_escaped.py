from test.src.TestDirContext import TestDirContext
from test.src.format_dockerx_stdout import format_dockerx_stdout

def test_echo_space(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', ' ',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \' \'',
			),
		)

def test_echo_quoted_space(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', '" "',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \'" "\'',
			),
		)

def test_echo_single_quote(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', '\'',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \'\'"\'"\'\'',
			),
		)

def test_echo_double_quote(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', '"',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \'"\'',
			),
		)

def test_echo_dollar(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', '$',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \'$\'',
			),
		)

def test_echo_backtick(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', '`',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \'`\'',
			),
		)

def test_echo_semicolon(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', ';',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \';\'',
			),
		)

def test_echo_star(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', '*',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \'*\'',
			),
		)

def test_echo_ampersand(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', '&',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \'&\'',
			),
		)

def test_echo_hash(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', '#',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \'#\'',
			),
		)

def test_echo_lt(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', '<',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \'<\'',
			),
		)

def test_echo_gt(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', '>',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \'>\'',
			),
		)

def test_echo_pipe(file = __file__):
	with TestDirContext(file) as ctx:
		dockerx = ctx.run_dockerx(
			'-n', 'ubuntu', 'echo', '|',
		)
		# Default is to run the image's default command
		dockerx.assert_context_ok(
			format_dockerx_stdout(
				b'docker run -it --rm -v \'' + ctx.cwd.encode() + b':/workdir\' -w /workdir ubuntu echo \'|\'',
			),
		)
