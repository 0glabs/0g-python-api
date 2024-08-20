import sys
import pkg_resources
import os

def print_separator():
    print("-" * 50)

print("Python version:")
print(sys.version)
print_separator()

print("Python executable:")
print(sys.executable)
print_separator()

print("Python path:")
for path in sys.path:
    print(path)
print_separator()

print("Installed packages:")
installed_packages = [d for d in pkg_resources.working_set]
for package in installed_packages:
    print(f"{package.key} - {package.version}")
print_separator()

print("Attempting to locate zerog_python_api package:")
try:
    dist = pkg_resources.get_distribution('zerog_python_api')
    print(f"Distribution: {dist}")
    print(f"Location: {dist.location}")
    print(f"Version: {dist.version}")
    
    package_path = os.path.dirname(pkg_resources.resource_filename('zerog_python_api', '__init__.py'))
    print(f"Package path: {package_path}")
    
    cli_tool_path = os.path.join(package_path, 'cli_tool')
    print(f"Expected cli_tool path: {cli_tool_path}")
    
    if os.path.exists(cli_tool_path):
        print(f"cli_tool exists at {cli_tool_path}")
    else:
        print(f"cli_tool does not exist at {cli_tool_path}")
    
    if os.path.exists(package_path):
        print("Contents of package directory:")
        for item in os.listdir(package_path):
            print(f"  - {item}")
    else:
        print(f"Package directory does not exist: {package_path}")
except pkg_resources.DistributionNotFound:
    print("zerog_python_api package not found in installed packages.")
except Exception as e:
    print(f"Error: {str(e)}")