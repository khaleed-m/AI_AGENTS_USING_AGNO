# Git Commands to Push Blog Post Generator to GitHub

## Step 1: Initialize Git Repository (if not already done)
```bash
cd c:\project\AI_AGENTS_AGNO\Blog_Post_Generator
git init
```

## Step 2: Add All Files
```bash
git add .
```

## Step 3: Create Initial Commit
```bash
git commit -m "Initial commit: AI Blog Post Generator with examples"
```

## Step 4: Add Remote Repository
```bash
# Replace 'your-username' with your actual GitHub username
git remote add origin https://github.com/your-username/AI-Blog-Post-Generator.git
```

## Step 5: Push to GitHub
```bash
git branch -M main
git push -u origin main
```

## Alternative: If you want to add to existing repository
```bash
# If you want to add this as a folder to your existing AI_AGENTS_AGNO repo
cd c:\project\AI_AGENTS_AGNO
git add Blog_Post_Generator/
git commit -m "Add AI Blog Post Generator with working examples"
git push origin main
```

## Files that will be pushed:
- README.md (comprehensive documentation)
- advanced_blog_generator.py (full-featured version)
- working_blog_generator.py (recommended version)
- simple_blog_generator.py (basic version)
- demo.py (demonstration script)
- example_output.md (example documentation)
- examples/blog_ai_developer.md (sample output)
- examples/blog_machine_learning.md (sample output)

## GitHub Repository Structure:
```
AI-Blog-Post-Generator/
├── README.md
├── advanced_blog_generator.py
├── working_blog_generator.py
├── simple_blog_generator.py
├── demo.py
├── example_output.md
└── examples/
    ├── blog_ai_developer.md
    ├── blog_machine_learning.md
    └── (more examples as you generate them)
```

## To run the commands:
1. Open PowerShell/Command Prompt
2. Navigate to the Blog_Post_Generator directory
3. Run each git command one by one
4. Create a new repository on GitHub first if needed
5. Replace the remote URL with your actual repository URL