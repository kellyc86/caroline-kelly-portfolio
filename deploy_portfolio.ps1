$ErrorActionPreference = "Stop"

Write-Host "Starting Portfolio Deployment..." -ForegroundColor Cyan

# 1. Provide Config Advice
$userEmail = git config user.email
if (-not $userEmail) {
    Write-Host "Git user.email not configured." -ForegroundColor Yellow
    $email = Read-Host "Enter your email for Git (e.g., your_email@example.com)"
    git config --global user.email "$email"
    $name = Read-Host "Enter your name for Git (e.g., Caroline Kelly)"
    git config --global user.name "$name"
}

# 2. Reset Index to respect .gitignore
Write-Host "Updating file tracking..." -ForegroundColor Cyan
git rm -r --cached . -f | Out-Null
git add . -f

# 3. Commit
$status = git status --porcelain
if ($status) {
    Write-Host "Committing changes..." -ForegroundColor Cyan
    git commit -m "Final portfolio update with new case studies and assets"
} else {
    Write-Host "No changes to commit." -ForegroundColor Green
}

# 4. Remote Configuration
$remote = git remote -v
if (-not $remote) {
    Write-Host "No remote repository linked." -ForegroundColor Yellow
    Write-Host "Please create a new repository on GitHub: https://github.com/new"
    $repoUrl = Read-Host "Enter your GitHub Repository URL (e.g., https://github.com/username/repo.git)"
    git remote add origin $repoUrl
}

# 5. Push
Write-Host "Pushing to GitHub..." -ForegroundColor Cyan
try {
    git push -u origin master
    Write-Host "Successfully deployed!" -ForegroundColor Green
} catch {
    Write-Host "Push failed. You might need to authenticate or force push." -ForegroundColor Red
    Write-Host "Try running: git push -u origin master --force"
}
