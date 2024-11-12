def test_shell(shell):
    ret = shell.run("sh", "-c", "exit 0")
    assert ret.returncode == 0
