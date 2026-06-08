import os, glob, re

files = glob.glob('src/components/tools/**/*.tsx', recursive=True)

# We want to replace `{isProcessing && <ProcessingProgress` with `{(isProcessing || status === 'complete') && <ProcessingProgress`
# Also handle `{isProcessing && (`
count = 0

for f in files:
    if os.path.isfile(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Look for {isProcessing && \s*<ProcessingProgress
        new_content = re.sub(
            r'\{\s*isProcessing\s*&&\s*<ProcessingProgress',
            r'{(isProcessing || status === \'complete\') && <ProcessingProgress',
            content
        )
        
        # Look for {isProcessing && (\s*<ProcessingProgress
        new_content = re.sub(
            r'\{\s*isProcessing\s*&&\s*\(\s*<ProcessingProgress',
            r'{(isProcessing || status === \'complete\') && (\n                <ProcessingProgress',
            new_content
        )

        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1

print(f"Patched {count} files.")
