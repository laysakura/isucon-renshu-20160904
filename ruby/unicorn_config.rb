worker_processes 4
preload_app true
listen 8080
pid "/tmp/unicorn.pid"

stderr_path "logs/unicorn.stderr.log"
stdout_path "logs/unicorn.stdout.log"
