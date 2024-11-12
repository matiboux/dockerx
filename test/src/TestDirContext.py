import os
import shutil
import random
import string

from .RunDockerx import RunDockerx

class TestDirContext(object):
    # Tell pytest to ignore this class
    __test__ = False

    def __init__(
        self,
        file: str = __file__,
        dockerx_path: str = None,
    ):
        self.cwd = os.path.join(os.path.dirname(file), 'cwd')
        self.dockerx_path = dockerx_path or os.path.join(os.path.dirname(__file__), '..', '..', 'dockerx')

    def __enter__(self):
        os.makedirs(self.cwd, exist_ok = True)
        return self

    def __exit__(self, *args):
        pass

    def run_dockerx(
        self,
        *args: list[str],
        cwd: str | None = None,
        env: dict[str, str] | None = None,
    ) -> RunDockerx:
        return RunDockerx(
            self.dockerx_path,
            dockerx_args = args,
            cwd = cwd or self.cwd,
            env = env,
        )
