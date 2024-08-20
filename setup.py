import os
import subprocess
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
from setuptools.command.install import install
import stat

class CustomBuildCommand(build_py):
    def run(self):
        self.build_go_binary()
        build_py.run(self)

    def build_go_binary(self):
        cli_tool = os.path.join(os.path.dirname(__file__), "zerog_python_api", "cli_tool")
        
        # Ensure the binary is built in the correct directory
        if os.path.exists(cli_tool):
            print(f"Removing existing binary: {cli_tool}")
            os.remove(cli_tool)

        print("Building Go binary...")
        try:
            subprocess.check_call(['go', 'build', '-o', cli_tool, 'main.go'])
            print("Binary built successfully.")

            # Make the cli_tool executable
            st = os.stat(cli_tool)
            os.chmod(cli_tool, st.st_mode | stat.S_IEXEC)
            print(f"Set executable permissions for: {cli_tool}")

        except subprocess.CalledProcessError as e:
            print(f"Error building Go binary: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

class CustomInstallCommand(install):
    def run(self):
        self.run_command('build_py')
        install.run(self)
        # Ensure cli_tool is installed correctly within the package
        cli_tool_src = os.path.join(self.build_lib, 'zerog_python_api', 'cli_tool')
        cli_tool_dst = os.path.join(self.install_lib, 'zerog_python_api', 'cli_tool')
        if os.path.exists(cli_tool_src):
            self.copy_file(cli_tool_src, cli_tool_dst)

setup(
    name="zerog_python_api",
    version="0.1",
    packages=find_packages(),  # Automatically find the package directory
    include_package_data=True,
    package_data={
        "zerog_python_api": ["cli_tool"],  # Include the Go binary
    },
    install_requires=[
        "setuptools",
    ],
    cmdclass={
        'build_py': CustomBuildCommand,
        'install': CustomInstallCommand,
    },
)
