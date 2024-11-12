def format_dockerx_stdout(docker_command: bytes) -> bytes:
    return b'\n> ' + docker_command + b'\n\n'
