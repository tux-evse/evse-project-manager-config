%global debug_package %{nil}
ExcludeArch: x86_64

Name: dbus-binding
Version: 1.0.0
Release: 3%{?dist}
Summary: Binding to serve an API connected to dbus
Group:   Development/Libraries/C and C++
License:  GPLv3
URL: https://github.com/redpesk-labs/dbus-binding
Source: %{name}-%{version}.tar.gz

Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/dbus-binding/manifest.yml

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  pkgconfig(json-c)

Requires:       afb-binder

%description
%{name} Binding to serve an API connected to dbus.

%package test
Summary: %{name} binding test

Requires: %{name} = %{version}
Requires:afb-ui-devtools

%description test
%{name} binding test.

%prep
%autosetup -p 1

%build
%cmake . 
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig
cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/etc
mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/bin
cp ./afb-binding/etc/*.json %{buildroot}%{_prefix}/redpesk/%{name}/test/etc
cp ./afb-binding/etc/*.sh %{buildroot}%{_prefix}/redpesk/%{name}/test/bin

%files
%dir %{_prefix}/redpesk/%{name}
%{_prefix}/redpesk/%{name}/.rpconfig/*
%{_prefix}/redpesk/%{name}/lib/*

%files test
%dir %{_prefix}/redpesk/%{name}/test
%dir %{_prefix}/redpesk/%{name}/test/bin
%{_prefix}/redpesk/%{name}/test/bin/*
%dir %{_prefix}/redpesk/%{name}/test/etc
%{_prefix}/redpesk/%{name}/test/etc/*
%dir %{_prefix}/redpesk/%{name}/test/.rpconfig
%{_prefix}/redpesk/%{name}/test/.rpconfig/*

%check

%clean

%%changelog