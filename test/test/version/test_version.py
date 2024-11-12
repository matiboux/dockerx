import re

from test.src.TestDirContext import TestDirContext

VERSION_STDOUT_SHORT_REGEX = (
    '^DockerX \(v[0-9]+\.[0-9]+\.[0-9]+\) - https://github\.com/matiboux/dockerx\n$'
)

def test_version(file = __file__):
    with TestDirContext(file) as ctx:
        dockerx = ctx.run_dockerx(
            '--version',
        )
        dockerx.assert_context_ok(
            re.compile(VERSION_STDOUT_SHORT_REGEX)
        )

def test_version_shorthand(file = __file__):
    with TestDirContext(file) as ctx:
        dockerx = ctx.run_dockerx(
            '-v',
        )
        dockerx.assert_context_ok(
            re.compile(VERSION_STDOUT_SHORT_REGEX)
        )

def test_version_dry(file = __file__):
    with TestDirContext(file) as ctx:
        dockerx = ctx.run_dockerx(
            '-n', '--version',
        )
        dockerx.assert_context_ok(
            re.compile(VERSION_STDOUT_SHORT_REGEX)
        )

def test_version_dry_shorthand(file = __file__):
    with TestDirContext(file) as ctx:
        dockerx = ctx.run_dockerx(
            '-n', '-v',
        )
        dockerx.assert_context_ok(
            re.compile(VERSION_STDOUT_SHORT_REGEX)
        )
