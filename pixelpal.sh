#!/bin/bash

# Check if gnome-terminal is available
if command -v gnome-terminal &> /dev/null; then
  # Open a new terminal and execute the first command
  gnome-terminal --tab --title="Chat 1" --command="bash -c 'python3 source/firefox_server.py --port 5001 --profile /tmp/chat1'"

  # Open another terminal and execute the second command
  gnome-terminal --tab --title="Chat 2" --command="bash -c 'python3 source/firefox_server.py --port 5002 --profile /tmp/chat2'"
else
  # gnome-terminal is not available, use mate-terminal instead
  # Open a new terminal and execute the first command
  mate-terminal --title="Chat 1" -e "bash -c 'python3 source/firefox_server.py --port 5001 --profile /tmp/chat1'"

  # Open another terminal and execute the second command
  mate-terminal --title="Chat 2" -e "bash -c 'python3 source/firefox_server.py --port 5002 --profile /tmp/chat2'"
fi
python3 source/gpt_autoscript.py && fg
