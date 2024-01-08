Name: modbus-binding
Version: 1.4.0
Release: 7%{?dist}
Summary: Binding to serve an API connected to modbus hardware
Group:   Development/Libraries/C and C++
License:  Apache-2.0
URL: http://git.ovh.iot/redpesk/redpesk-common/modbus-binding
Source: %{name}-%{version}.tar.gz


Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/modbus-binding/manifest.yml
Source11: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/modbus-binding/manifest-test.yml
Source12: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/modbus-binding/start-binder.sh

Source13: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/modbus-binding/binder-test.json
Source14: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/modbus-binding/binding-modbus.json


BuildRequires:  afm-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  afb-cmake-modules
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(lua) >= 5.3
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(afb-libhelpers)
BuildRequires:  pkgconfig(afb-libcontroller)
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  pkgconfig(libmodbus) >= 3.1.6
BuildRequires:  pkgconfig(librp-utils-static)
BuildRequires:  pkgconfig(afb-helpers4-static)

Requires:       afb-binder

%description
%{name} Binding to serve an API connected to modbus hardware.

%package simulation
Summary:        Simulate a modbus tcp device

%description simulation
Simulate a modbus tcp device

%package test
Summary: %{name} binding test

Requires: %{name} = %{version}

%description test
%{name} binding test.

%prep
%autosetup -p 1

%files
%afm_files
%exclude %{_afmdatadir}/%{name}/lib/plugins/*.ctlso
%exclude %{_afmdatadir}/%{name}/etc/*.json

%files simulation
%{_bindir}/*

%afm_package_devel
%{_includedir}/modbus-binding.h
%{_libdir}/pkgconfig/modbus.pc


%build
%afm_configure_cmake
%afm_build_cmake

%install
%afm_makeinstall

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}-test/etc
cp %{SOURCE13}  %{buildroot}%{_prefix}/redpesk/%{name}-test/etc
cp %{SOURCE14}  %{buildroot}%{_prefix}/redpesk/%{name}-test/etc

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig
cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}-test/bin
cp %{SOURCE12} %{buildroot}%{_prefix}/redpesk/%{name}-test/bin/start-binder.sh

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}-test/.rpconfig
cp %{SOURCE11} %{buildroot}%{_prefix}/redpesk/%{name}-test/.rpconfig/manifest.yml

%check

%clean


%files test
%dir %{_prefix}/redpesk/%{name}-test
%dir %{_prefix}/redpesk/%{name}-test/bin
%{_prefix}/redpesk/%{name}-test/bin/*
%dir %{_prefix}/redpesk/%{name}-test/etc
%{_prefix}/redpesk/%{name}-test/etc/*
%dir %{_prefix}/redpesk/%{name}-test/.rpconfig
%{_prefix}/redpesk/%{name}-test/.rpconfig/*


%%changelog

* Fri Jul 23 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.1.0+20210711+6+g342f915
- Upgrade version from source commit sha: 342f915b5e6cdda9cbf17650cd70cdd04388bbc5
- Commit message:
- 	[Doc] Typo Redpesk/redpesk #2025
- 	
- 	Signed-off-by: Emilie Argouarch <emilie.argouarch@iot.bzh>


