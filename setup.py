from distutils.core import setup
from pip._internal.req import parse_requirements
from setuptools.command.install import install as InstallCommand


class Install(InstallCommand):
    """ Customized setuptools install command which uses pip. """

    def run(self, *args, **kwargs):
        import pip
        pip.main(['install', '.'])
        InstallCommand.run(self, *args, **kwargs)
setup(
    name='moonraker-obico',
    version='1.0',
    description='obico for klipper',
    author='obico',
    author_email='support@obico.io',
    url='https://obico.io/',
    cmdclass={
        'install': Install,
    },
    install_reqs=parse_requirements('requirements.txt', session='hack')
)
