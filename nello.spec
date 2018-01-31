%global __os_install_post %{nil}
%global debug_package %{nil}
Name:           nello
Version:        1.0.0
Release:        1%{?dist}
Summary:        Hello world in node

License:        GPLv3+
URL:            http://example.com/%{name}
Source0:        http://example.com/%{name}/release/%{name}-%{version}.tar.gz

BuildRequires:  nodejs

%description
Hello world in node

%prep
%autosetup


%build
npm install
npm run package

%install
mkdir -p %{buildroot}%{_bindir}
cp nello %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}


%changelog
* Wed Nov 29 2017 William Wheeler <william.wheeler@valuecentric.com>
- 
