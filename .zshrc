# load zgenom
source "${HOME}/.zgenom/zgenom.zsh"

# Check for plugin and zgenom updates every 7 days
# This does not increase the startup time.
zgenom autoupdate

# if the init script doesn't exist
if ! zgenom saved; then
    echo "Creating a zgenom save"

    # Add this if you experience issues with missing completions or errors mentioning compdef.
    # zgenom compdef

    # Ohmyzsh base library
    zgenom ohmyzsh

    # You can also cherry pick just parts of the base library.
    # Not loading the base set of ohmyzsh libraries might lead to issues.
    # While you can do it, I won't recommend it unless you know how to fix
    # those issues yourself.

    # Remove `zgenom ohmyzsh` and load parts of ohmyzsh like this:
    # `zgenom ohmyzsh path/to/file.zsh`
    # zgenom ohmyzsh lib/git.zsh # load git library of ohmyzsh

    # plugins
    zgenom ohmyzsh plugins/git
    zgenom ohmyzsh plugins/command-not-found
    zgenom ohmyzsh plugins/sudo
    zgenom ohmyzsh plugins/yarn
    
    # just load the completions
    zgenom ohmyzsh --completion plugins/docker-compose
    
    # syntax highlighting
    zgenom load zsh-users/zsh-syntax-highlighting

    # bulk load
    zgenom loadall <<EOPLUGINS
        zsh-users/zsh-history-substring-search
        Bhupesh-V/ugit
        chrissicool/zsh-256color
EOPLUGINS
    # ^ can't indent this EOPLUGINS
    
    bindkey "$terminfo[kcuu1]" history-substring-search-up
    bindkey "$terminfo[kcud1]" history-substring-search-down

    # add binaries
    zgenom bin tj/git-extras

    # completions
    zgenom load zsh-users/zsh-completions
    zgenom load zsh-users/zsh-autosuggestions

    # save all to init script
    zgenom save

    # Compile your zsh files
    zgenom compile "$HOME/.zshrc"

    # You can perform other "time consuming" maintenance tasks here as well.
    # If you use `zgenom autoupdate` you're making sure it gets
    # executed every 7 days.

    # rbenv rehash
fi

# ssh fix for kitty.
alias ssh="kitty +kitten ssh"
alias d="kitty +kitten diff"

# prompt
source ${HOME}/zsh/themes/headline.zsh-theme

eval "$(zoxide init zsh --cmd j)"
alias config='/usr/bin/git --git-dir=/home/calum/.cfg/ --work-tree=/home/calum'
