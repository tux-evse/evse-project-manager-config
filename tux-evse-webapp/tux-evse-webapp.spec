%global debug_package %{nil}

Name:           tux-evse-webapp
Version:        1.0
Release:        1%{?dist}
Summary:        WebApp to display Tux-EVSE data

License:        Apache
URL:            https://github.com/tux-evse/tux-evse-webapp
Source0:        %{name}-%{version}.tar.gz

Source10:        https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/tux-evse-webapp/manifest-mock.yml
Source11:        https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/tux-evse-webapp/manifest-webapp-test.yml
Source12:        https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/tux-evse-webapp/manifest-webapp.yml

Source21:        https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/tux-evse-webapp/tux-evse-webapp-binder.json
Source22:        https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/tux-evse-webapp/tux-evse-webapp-debug.json
Source23:        https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/tux-evse-webapp/tux-evse-webapp.json

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
cp %{SOURCE12} %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml
cp %{SOURCE22} %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp %{SOURCE23} %{buildroot}%{_prefix}/redpesk/%{name}/etc

install -vd  %{buildroot}%{_prefix}/redpesk/%{name}/test/bin
install -vd  %{buildroot}%{_prefix}/redpesk/%{name}/test/etc
install -vd  %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig
cp %{SOURCE21} %{buildroot}%{_prefix}/redpesk/%{name}/test/etc
cp %{SOURCE11} %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig/manifest.yml
cp tux-evse-webapp-start.sh %{buildroot}%{_prefix}/redpesk/%{name}/test/bin/

install -vd  %{buildroot}%{_prefix}/redpesk/%{name}-mock/bin
install -vd  %{buildroot}%{_prefix}/redpesk/%{name}-mock/.rpconfig
cp mock/tux-evse-mock-api.py %{buildroot}%{_prefix}/redpesk/%{name}-mock/bin/
cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/%{name}-mock/.rpconfig/manifest.yml

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
