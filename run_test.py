import subprocess

python_path = "."
allure_dir = "allure-results"
test_files = "test_main.py"
flags = "-v -s"
log_level = "ERROR"

command = f"PYTHONPATH={python_path} \
            pytest {flags} \
            tests/{test_files} \
            --alluredir={allure_dir} \
            --log-cli-level={log_level}"

subprocess.run(command, shell=True)
