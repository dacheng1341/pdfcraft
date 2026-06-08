import os, glob

files = glob.glob('src/components/tools/**/*.tsx', recursive=True)

count = 0
for f in files:
    if os.path.isfile(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        new_content = content.replace(r"status === \'complete\'", "status === 'complete'")
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1

print(f"Fixed {count} files.")
