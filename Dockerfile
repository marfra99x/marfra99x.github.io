FROM ruby:3.2.4

ENV DEBIAN_FRONTEND=noninteractive

LABEL maintainer="Amir Pourmand"

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    locales \
    imagemagick \
    build-essential \
    zlib1g-dev \
    jupyter-nbconvert \
    inotify-tools \
    procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    JEKYLL_ENV=development \
    BUNDLE_PATH=/usr/local/bundle

WORKDIR /srv/jekyll

COPY Gemfile Gemfile.lock ./

# Keep Bundler aligned with Gemfile.lock and install all site dependencies.
RUN gem install bundler -v 2.6.5 --no-document \
    && bundle install --jobs 4 --retry 3

COPY bin/entry_point.sh /usr/local/bin/entry_point.sh
RUN chmod +x /usr/local/bin/entry_point.sh

EXPOSE 8080 35729

ENTRYPOINT ["/usr/local/bin/entry_point.sh"]
