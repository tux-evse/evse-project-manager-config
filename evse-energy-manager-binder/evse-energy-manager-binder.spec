%global debug_package %{nil}

Name:    evse-energy-manager-binder
Version: 0.0.1
Release: 0%{?dist}
Summary: evse energy manager binder

License: MIT
URL: https://github.com/tux-evse/evse-project-manager-config

Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-energy-manager-binder/manifest.yml
Source11: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-energy-manager-binder/manifest-test.yml
Source12: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-energy-manager-binder/start-binder.sh

Source13: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-energy-manager-binder/binder-test.json
Source14: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/energy-binding-rs/binding-energy.json
Source15: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/linky-binding-rs/binding-linky.json
Source16: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/modbus-binding/binding-modbus.json


Requires: modbus-binding
Requires: linky-binding-rs
Requires: energy-binding-rs

%description
evse energy manager binder.

%package test
Summary: evse energy manager binder test

Requires: %{name} = %{version}

%description test
evse energy manager binder test.

%prep

%build

%install

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig
cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp %{SOURCE14} %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp %{SOURCE15} %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp %{SOURCE16} %{buildroot}%{_prefix}/redpesk/%{name}/etc

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig
cp %{SOURCE11} %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig/manifest.yml

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/bin
cp %{SOURCE12} %{buildroot}%{_prefix}/redpesk/%{name}/test/bin/start-binder.sh

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/etc
cp %{SOURCE13} %{buildroot}%{_prefix}/redpesk/%{name}/test/etc

%files
%dir %{_prefix}/redpesk/%{name}
%dir %{_prefix}/redpesk/%{name}/.rpconfig
%{_prefix}/redpesk/%{name}/.rpconfig/*
%dir %{_prefix}/redpesk/%{name}/etc
%{_prefix}/redpesk/%{name}/etc/*

%files test
%dir %{_prefix}/redpesk/%{name}/test
%dir %{_prefix}/redpesk/%{name}/test/bin
%{_prefix}/redpesk/%{name}/test/bin/*
%dir %{_prefix}/redpesk/%{name}/test/.rpconfig
%{_prefix}/redpesk/%{name}/test/.rpconfig/*
%dir %{_prefix}/redpesk/%{name}/test/etc
%{_prefix}/redpesk/%{name}/test/etc/*

%changelog
