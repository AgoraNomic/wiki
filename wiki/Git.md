Learn the basics of git [here](https://git-scm.com/book/en/v2).

The repository is at github.com/nichdel/agora-wiki.

# Generic Auto-update script

Normally git pull & push will need your credentials. The *best* and *most secure* way to automate this is using ssh keys. Here are [some alternatives](https://stackoverflow.com/questions/6565357/git-push-requires-username-and-password) if you'd rather.

    git pull #Full update. If you need finer control see 'git fetch' and 'git checkout'
    
    <perform chanages here>
    
    git add <files> #this adds any new files to the repo. Otherwise they will be ignored
    
    git commit -a -m "Example commit message"
    
    git push 
