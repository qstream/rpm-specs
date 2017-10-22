#!/usr/bin/env bash

if [ -z "$1" ];
then echo "Please, specify a spec file to build."; exit -1;
fi

# creating a container for building the rpm
docker create --name rpmbuild-tmp qstream/amazonlinux-rpmbuild:latest

# uploading the spec file
docker cp $1 rpmbuild-tmp:/home/rpmbuilder/src/

docker commit rpmbuild-tmp rpmbuild-tmp

# now running the actual build commands
docker run --name rpmbuild-tmp-1 rpmbuild-tmp /bin/bash -c "cd src; spectool -R -g *.spec; rpmbuild -bb *.spec"

docker cp rpmbuild-tmp-1:/home/rpmbuilder/rpmbuild/RPMS .

# cleaning up containers
docker container rm rpmbuild-tmp
docker container rm rpmbuild-tmp-1
