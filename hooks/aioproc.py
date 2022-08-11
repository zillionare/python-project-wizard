import asyncio
import functools
import os
import shlex

from colorama import Fore, Style


async def _echo(stream):
    while True:
        line = await stream.readline()
        line = line.decode("utf-8")
        if not line:
            break
        line = line.rstrip("\n")
        if line.upper().startswith("WARNING"):
            print(Fore.YELLOW + line + Style.RESET_ALL)
        elif line.upper().startswith("ERROR"):
            print(Fore.RED, line, Style.RESET_ALL)
            raise Exception(line)
        else:
            print(line)


def async_run(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return asyncio.run(func(*args, **kwargs))

    return wrapper


async def aioprocess(
    *cmds,
    stdout_handler=_echo,
    stderr_handler=_echo,
    inherit_env=True,
    detached=False,
    cwd=None,
):
    """execute cmds in asyncio process, and echo it's stdout/stderr

    if detached is specified, the subprocess will be detached with parent after created.
    if inherit_env is specified, then subprocess with inherite envars from parent process.

    Args:
        *cmds: list of cmds to be executed
        stdout_handler: handler for stdout
        stderr_handler: handler for stderr
        inherit_env: inherit envars from parent process
        detached: detach subprocess with parent
        cwd: change working directory of subprocess
    Examples:
        >>> aioprocess("ls")
        >>> aioprocess("ping -c 10 www.baidu.com")
        >>> aioprocess("ping", "-c", "10", "www.baidu.com")
        >>> aioprocess("python -m http.server", detached=True)
    """
    cur_dir = os.getcwd()

    try:
        if cwd:
            os.chdir(cwd)

        if len(cmds) == 1 and isinstance(cmds[0], str):
            cmds = shlex.split(cmds[0])

        env = os.environ.copy() if inherit_env else None

        proc = await asyncio.create_subprocess_exec(
            *cmds,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            start_new_session=detached,
            env=env,
        )

        if stdout_handler:
            asyncio.ensure_future(stdout_handler(proc.stdout))
        if stderr_handler:
            asyncio.ensure_future(stderr_handler(proc.stderr))

        return proc
    finally:
        os.chdir(cur_dir)


# @async_run
# async def main():
#     try:
#         proc = await aioprocess("pip install tqdm")
#         await proc.wait()
#     except Exception as e:
#         print("ecxeption:", e)

# main()
