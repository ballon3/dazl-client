from pathlib import Path as _Path
from os import PathLike as _PathLike
from subprocess import run as _run
from typing import Any, Mapping as _Mapping, Optional as _Optional, Union as _Union, Sequence as _Sequence


_IP = _Union[_Path, _PathLike]


class SdkError(Exception):
    pass


class SdkInstallation():

    def _run(self, *args: str, **kwargs) -> '_Sequence[str]':
        from subprocess import run, PIPE
        proc = run(['daml', *args], stdout=PIPE, stderr=PIPE, check=True, universal_newlines=True, **kwargs)
        return proc.stdout.splitlines()

    def _resolve_path(self, path: '_IP') -> '_Path':
        from os.path import expanduser, exists
        p = expanduser(str(path))
        return _Path(p)

    def new(self, path: '_IP', template: '_Optional[str]'= None) -> 'SdkProject':
        p = self._resolve_path(path)
        if p.exists():
            raise SdkError(f'target directory {path!r} already exists')

        args = ['new', str(p)]
        if template:
            args.append(template)
        self._run(*args)
        return self.project(p)

    def templates(self) -> '_Sequence[str]':
        return [x for x in (line.strip() for i, line in enumerate(self._run('new', '--list')) if i > 0) if x]

    def project(self, path: '_Union[None, _IP]') -> 'SdkProject':
        return SdkProject(path, self)

    def install(target: '_Optional[str]' = None):
        """
        Ensure the specified version of the DAML SDK is installed.
        """
        _run(['daml', 'install', str(target) if target is not None else 'latest'], check=True)


    def uninstall(target: str):
        _run(['daml', 'uninstall', str(target)], check=True)
        


    def version(all: bool = False) -> '_Mapping[str, str]':
        from subprocess import run, PIPE

        proc = run(['daml', 'version'], stdout=PIPE, stderr=PIPE, check=True, universal_newlines=True)
        versions = {}
        for i, line in enumerate(proc.stdout.splitlines()):
            if i > 0:
                version = line
                code = ''
                lidx = line.find(' (')
                if lidx >= 0:
                    ridx = line.find(')', lidx + 1)
                    if ridx >= 0:
                        code = line[lidx + 2:ridx]
                    version = line[0:lidx]
                versions[version.strip()] = code.strip()
        return versions

    def sandbox(
            self,
            port: int = DEFAULT_SANDBOX_PORT,
            address: '_Optional[str]' = None,
            time_model: str = 'static',
            archives: '_Sequence[_IP]' = None,
            ledger_id: '_Optional[str]' = None,
            scenario: '_Optional[str]' = None,
            sql_backend_jdbcurl: '_Optional[str]',
            pem_file: '_Optional[_IP]' = None,
            crt_file: '_Optional[_IP]' = None,
            cacrt_file: '_Optional[_IP]' = None):
        args = []
        if port == 0:
            # the user would like a port dynamically allocated; in order to report the port
            # back to the caller, pass --port-file to catch the port

            args.append(['-p', str(port), '--port-file'])


DEFAULT_SANDBOX_PORT = 6865


class SdkProject:

    def __init__(self, path: '_IP', installation: '_Optional[SdkInstallation]' = None):
        self._installation = installation if installation is not None else _DEFAULT
        self._path = self._installation._resolve_path(path)

    def __repr__(self):
        return f'SdkProject({str(self._path)!r})'

    def build(self, output: '_Optional[_IP]' = None) -> '_Path':
        args = ['build']
        if output is not None:
            args.append('-o')
            args.append(str(output))
        line = self._run(*args)[-1]
        return self._path / line[8:-1]


    def clean(self):
        self._run('clean')

    def _run(self, *args, **kwargs):
        import os
        env = dict(os.environ)
        env['DAML_PROJECT'] = str(self._path)
        return self._installation._run(*args, **kwargs, env=env)


_DEFAULT = SdkInstallation()
new = _DEFAULT.new
templates = _DEFAULT.templates
project = _DEFAULT.project

def sandbox(auto)
