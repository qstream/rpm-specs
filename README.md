RPM Specs
---

This repo is a collection of RPM specs by Qstream.
The specs in this repo are used by Qstream to install software for which
no suitable package was found.

**NOTE**: The specs in this repo have been tested only on Amazon Linux
environments.

# How to build

## Prerequisites

Install [Docker](//docker.com) on your machine. The build script
provided by this repo will use the
[amazonlinux-rpmbuild](//github.com/qstream/amazonlinux-rpmbuild) docker
image to build the specs.

```bash
# build the image on your machine
docker build -t qstream/amazonlinux-rpmbuild:latest https://github.com/qstream/amazonlinux-rpmbuild.git\#latest
```

## Building an RPM

```bash
bin/build.sh oauth2_proxy/oauth2_proxy.spec
```

If everything goes as expected you should now have your RPM package
available at `RPMS/x86_64/oauth2_proxy-2.2.0-1.x86_64.rpm`.

