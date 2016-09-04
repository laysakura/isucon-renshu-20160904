worker_processes 8
preload_app true
listen "/home/isucon/unicorn.sock", backlog: 1024
listen 8080
pid "/tmp/unicorn.pid"

# stderr_path "logs/unicorn.stderr.log"
# stdout_path "logs/unicorn.stdout.log"
