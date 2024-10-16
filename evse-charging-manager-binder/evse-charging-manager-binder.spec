%global debug_package %{nil}


Name:    evse-charging-manager-binder
Version: 0.0.1
Release: 0%{?dist}
Summary: evse charging manager binder

License: MIT
URL: https://github.com/tux-evse/evse-project-manager-config

Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-charging-manager-binder/manifest.yml
Source11: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-charging-manager-binder/manifest-test.yml
Source12: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-charging-manager-binder/start-binder.sh

Source13: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-charging-manager-binder/binder-test.json
Source14: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-charging-manager-binder/binding-am62x.json
Source15: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-charging-manager-binder/binding-chmgr.json
Source16: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-charging-manager-binder/binding-i2c.json
Source17: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-charging-manager-binder/binding-slac.json

Source18: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-charging-manager-binder/binding-josev-ac.json
Source19: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-charging-manager-binder/mqtt-config.yml
Source20: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-charging-manager-binder/start-binder-with-josev.sh
#For debug only
Source90: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/evse-charging-manager-binder/binding-debug.json

Requires: charging-binding-rs
Requires: ti-am62x-binding-rs
Requires: i2c-binding-rs
Requires: slac-binding-rs

%description
evse charging manager binder.

%package test
Summary: evse charging manager binder test

Requires: %{name} = %{version}
Requires:afb-ui-devtools

Requires: evse-auth-manager-binder
Requires: evse-energy-manager-binder
Requires: josev-binding-rs

%description test
evse charging manager binder test.

%prep

%build

%install

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig
cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp %{SOURCE14} %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp %{SOURCE15} %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp %{SOURCE16} %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp %{SOURCE17} %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp %{SOURCE18} %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp %{SOURCE19} %{buildroot}%{_prefix}/redpesk/%{name}/etc

#For debug only
cp %{SOURCE90} %{buildroot}%{_prefix}/redpesk/%{name}/etc

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig
cp %{SOURCE11} %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig/manifest.yml

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/etc
cp %{SOURCE13} %{buildroot}%{_prefix}/redpesk/%{name}/test/etc

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/bin
cp %{SOURCE12} %{buildroot}%{_prefix}/redpesk/%{name}/test/bin/start-binder.sh
cp %{SOURCE20} %{buildroot}%{_prefix}/redpesk/%{name}/test/bin/start-binder-with-josev.sh

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
