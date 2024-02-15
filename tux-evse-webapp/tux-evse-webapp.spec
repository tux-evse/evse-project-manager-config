%global debug_package %{nil}

Name:           tux-evse-webapp
Version:        1.0
Release:        1%{?dist}
Summary:        WebApp to display Tux-EVSE data

License:        Apache
URL:            https://github.com/tux-evse/tux-evse-webapp
Source0:        %{name}-%{version}.tar.gz

Requires:       afb-binder

Requires: evse-auth-manager-binder
Requires: evse-charging-manager-binder
Requires: evse-energy-manager-binder

BuildArch:      noarch

%description
WebApp to display Tux-EVSE data

%package test
Requires:       %{name} = %{version}
Summary:        Test package for %{name}

%description test
WebApp to display Tux-EVSE data 

%package mock
Requires:       %{name} = %{version}
Requires:       afb-libpython

Summary:        Mock package for %{name}

%description mock
Mock part for webapp Tux-EVSE

%prep
%autosetup

%build

%install
install -vd  %{buildroot}%{_prefix}/redpesk/%{name}/etc
install -vd  %{buildroot}%{_prefix}/redpesk/%{name}/htdocs
install -vd  %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig
cp -r dist/valeo/* %{buildroot}%{_prefix}/redpesk/%{name}/htdocs/
cp conf.d/packaging/manifest-webapp.yml %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml
cp conf.d/packaging/tux-evse-webapp-debug.json %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp conf.d/packaging/tux-evse-webapp.json %{buildroot}%{_prefix}/redpesk/%{name}/etc

install -vd  %{buildroot}%{_prefix}/redpesk/%{name}/test/bin
install -vd  %{buildroot}%{_prefix}/redpesk/%{name}/test/etc
install -vd  %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig
cp conf.d/packaging/tux-evse-webapp-binder.json %{buildroot}%{_prefix}/redpesk/%{name}/test/etc
cp conf.d/packaging/manifest-webapp-test.yml %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig/manifest.yml
cp tux-evse-webapp-start.sh %{buildroot}%{_prefix}/redpesk/%{name}/test/bin/

install -vd  %{buildroot}%{_prefix}/redpesk/%{name}-mock/bin
install -vd  %{buildroot}%{_prefix}/redpesk/%{name}-mock/.rpconfig
cp mock/tux-evse-mock-api.py %{buildroot}%{_prefix}/redpesk/%{name}-mock/bin/
cp conf.d/packaging/manifest-mock.yml %{buildroot}%{_prefix}/redpesk/%{name}-mock/.rpconfig/manifest.yml

%files
%dir %{_prefix}/redpesk/%{name}
%dir %{_prefix}/redpesk/%{name}/htdocs
%{_prefix}/redpesk/%{name}/htdocs/*
%dir %{_prefix}/redpesk/%{name}/etc
%{_prefix}/redpesk/%{name}/etc/*
%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml

%files test
%dir %{_prefix}/redpesk/%{name}/test
%dir %{_prefix}/redpesk/%{name}/test/etc
%dir %{_prefix}/redpesk/%{name}/test/bin
%{_prefix}/redpesk/%{name}/test/etc/*
%{_prefix}/redpesk/%{name}/test/bin/tux-evse-webapp-start.sh
%{_prefix}/redpesk/%{name}/test/.rpconfig/manifest.yml

%files mock
%dir %{_prefix}/redpesk/%{name}-mock
%{_prefix}/redpesk/%{name}-mock/bin/tux-evse-mock-api.py
%{_prefix}/redpesk/%{name}-mock/.rpconfig/manifest.yml
