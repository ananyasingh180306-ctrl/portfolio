import os
import shutil
import subprocess

dl = r'C:\Users\ananya singh\Downloads'
matching = [os.path.join(dl, f) for f in os.listdir(dl) if f.startswith('Ananya Singh') and f.endswith('.html')]
print('Matching files in Downloads:', matching)

# Pick the exact 'Ananya Singh – Portfolio.html' (without (1))
exact_file = None
for f in matching:
    if '(1)' not in f:
        exact_file = f
        break
if not exact_file:
    exact_file = matching[0]

print('Using source file:', exact_file)

repo_dir = r'C:\Users\ananya singh\.gemini\antigravity\scratch\portfolio'

# Copy as index.html (so it serves as root homepage)
dest_index = os.path.join(repo_dir, 'index.html')
shutil.copyfile(exact_file, dest_index)
print('Updated index.html from source:', os.path.getsize(dest_index))

# Also copy with original name just in case
orig_name = os.path.basename(exact_file)
dest_orig = os.path.join(repo_dir, orig_name)
shutil.copyfile(exact_file, dest_orig)
print('Copied original file name as well:', dest_orig)

# Git add, commit, push
def run_git(cmd):
    p = subprocess.run(cmd, cwd=repo_dir, shell=True, capture_output=True, text=True)
    print('CMD:', cmd)
    print('STDOUT:', p.stdout)
    if p.stderr:
        print('STDERR:', p.stderr)

run_git('git add -A')
run_git('git commit -m "Update portfolio with latest Ananya Singh – Portfolio.html"')
run_git('git push origin main')
