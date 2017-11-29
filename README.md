# nello

Project to show rpming a binary created with pkg doesn't go so well.

# To reproduce

* Run `cp -R nello nello-1.0.0 && tar -cvzf nello-1.0.0.tar.gz`
* Copy spec files and sources to rpmbuild directory (~/rpmbuild/SPECS & ~/rpmbuild/SOURCES) respectively) 
* run `cd ~/rpmbuild && rpmbuild -bb --clean SPECS/nello.spec`
* yum install created RPM
* run `nello`

Expected Output `Hello World`
Actual Output `Pkg: Error reading from file`
