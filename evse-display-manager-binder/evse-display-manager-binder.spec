%global debug_package %{nil}


Name:    evse-display-manager-binder
Version: 0.0.1
Release: 0%{?dist}
Summary: evse display manager binder

License: MIT
URL: https://github.com/tux-evse/evse-project-manager-config

Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-display-manager-binder/manifest.yml
Source11: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-display-manager-binder/manifest-test.yml
Source12: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-display-manager-binder/start-binder.sh

Source13: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-display-manager-binder/binder-test.json
Source14: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-display-manager-binder/binding-display.json
#For debug only
Source90: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-display-manager-binder/binding-debug.json

Requires: dbus-binding
Requires: evse-auth-manager-binder
Requires: evse-charging-manager-binder
Requires: evse-energy-manager-binder
Requires: tux-evse-webapp
Requires: display-binding-rs

%description
evse display manager binder.

%package test
Summary: evse display manager binder test

Requires: %{name} = %{version}
Requires: afb-ui-devtools

Requires: display-binding-rs
Requires: evse-auth-manager-binder
Requires: evse-charging-manager-binder
Requires: evse-energy-manager-binder

%description test
evse display manager binder test.

%prep

%build

%install

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig
cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp %{SOURCE14} %{buildroot}%{_prefix}/redpesk/%{name}/etc
#For debug only
cp %{SOURCE90} %{buildroot}%{_prefix}/redpesk/%{name}/etc

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
