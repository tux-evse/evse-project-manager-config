%define debug_package %{nil}
ExcludeArch: x86_64

Name: dbus-binding
Version: 1.0.0
Release: 1%{?dist}
Summary: Binding to serve an API connected to dbus
Group:   Development/Libraries/C and C++
License:  GPLv3
URL: https://github.com/redpesk-labs/dbus-binding
Source: %{name}-%{version}.tar.gz

Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/dbus-binding/manifest.yml

BuildRequires:  afm-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  afb-cmake-modules
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(afb-libhelpers)
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  pkgconfig(librp-utils-static)
BuildRequires:  pkgconfig(afb-helpers4-static)

Requires:       afb-binder
ExcludeArch: x86_64

%description
%{name} Binding to serve an API connected to dbus.

%prep
%autosetup -p 1

%files
%afm_files
%exclude %{_afmdatadir}/%{name}/lib/plugins/*.ctlso
%exclude %{_afmdatadir}/%{name}/etc/*.json

%build
%afm_configure_cmake
%afm_build_cmake

%install
%afm_makeinstall

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig
cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml

%check

%clean

%%changelog