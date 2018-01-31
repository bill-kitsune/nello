# nello

Project to show rpming a binary created with pkg doesn't go so well.

# To reproduce

* Run `cp -R nello/* nello-1.0.0 && tar -cvzf nello-1.0.0.tar.gz nello-1.0.0`
* `cp nello/nello.spec ~/rpmbuild/SPECS && cp nello-1.0.0.tar.gz ~/rpmbuild/SOURCES`
* run `cd ~/rpmbuild && rpmbuild -bb --clean SPECS/nello.spec`
* yum install created RPM
* run `nello`

Expected Output `Hello World`

