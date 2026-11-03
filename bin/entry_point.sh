#!/usr/bin/env bash
set -euo pipefail

cd /srv/jekyll

# The source tree is bind-mounted in development. Ensure its Gemfile still
# matches the gems installed in the image; install only if something changed.
bundle check || bundle install --jobs 4 --retry 3

exec bundle exec jekyll serve \
  --watch \
  --port 8080 \
  --host 0.0.0.0 \
  --livereload \
  --force_polling
