#!/bin/sh
pip3 install gitpython --user

append_to_zshrc() {
    local text="$1" zshrc
    local skip_new_line="${2:-0}"

    if [ -w "$HOME/.zshrc.local" ]; then
        zshrc="$HOME/.zshrc.local"
    else
        zshrc="$HOME/.zshrc"
    fi

    if ! grep -Fqs "$text" "$zshrc"; then
        if [ "$skip_new_line" -eq 1 ]; then
            printf "%s\n" "$text" >>"$zshrc"
        else
            printf "\n%s\n" "$text" >>"$zshrc"
        fi
    fi
}
append_to_zshrc 'alias copylab="python3 ~/copy_lab.py"'

cp copy_lab.py $HOME

username="$(whoami)"
sed -i '' "s/needs_replaced/$username/" $HOME/copy_lab.py
