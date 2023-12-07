import subprocess

# Command and arguments as a list
command = ["python", "./wanda/fns/label.py", "./wanda/config/smc.yml", "--findlog", "true"]

# Run the command
subprocess.run(command)
