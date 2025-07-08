import os
import subprocess

def convert_rst_to_ipynb(folder):
    for root, _, files in os.walk(folder):
        for filename in files:
            if filename.endswith(".rst"):
                rst_path = os.path.join(root, filename)
                ipynb_path = os.path.splitext(rst_path)[0] + ".ipynb"
                try:
                    subprocess.run([
                        "pandoc",
                        rst_path,
                        "-o", ipynb_path,
                        "--from", "rst",
                        "--to", "ipynb"
                    ], check=True)
                    print(f"Converted: {rst_path} → {ipynb_path}")
                except subprocess.CalledProcessError:
                    print(f"Failed to convert: {rst_path}")

if __name__ == "__main__":
    # Use absolute path to avoid confusion
    folder_path = r"C:\Users\neohu\Workspaces\qiskit-dynamics\docs\tutorials"
    convert_rst_to_ipynb(folder_path)
