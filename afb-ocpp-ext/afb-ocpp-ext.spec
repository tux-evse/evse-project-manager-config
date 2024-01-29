%global debug_package %{nil}
ExcludeArch: x86_64

Name: afb-ocpp-ext
Version: 0.0.1
Release: 0%{?dist}
Summary: AFB micro-service framework extention for OCPP

License: Apache
URL: https://github.com/tux-evse/afb-ocpp-ext.git
Source0: %{name}-%{version}.tar.gz

Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/afb-ocpp-ext/manifest.yml

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig(librp-utils) >= 0.0.3
BuildRequires: afb-cmake-modules
BuildRequires:  afm-rpm-macros
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(libafb)
BuildRequires: pkgconfig(libafb-binder)

%description
AFB micro-service framework extention for OCPP.

%prep
%autosetup -p 1

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ../

%install
cd build
%cmake_install

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig
cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml

%clean

%files
%dir %{_prefix}/redpesk/afb-ocpp
%dir %{_prefix}/redpesk/afb-ocpp/var
%dir %{_prefix}/redpesk/afb-ocpp/etc
%dir %{_prefix}/redpesk/afb-ocpp/lib
%dir %{_prefix}/redpesk/afb-ocpp/htdocs
%dir %{_prefix}/redpesk/afb-ocpp/bin
%dir %{_prefix}/redpesk/%{name}/.rpconfig

%{_prefix}/redpesk/afb-ocpp
%{_prefix}/redpesk/afb-ocpp/var
%{_prefix}/redpesk/afb-ocpp/config.xml
%{_prefix}/redpesk/afb-ocpp/icon.jpg
%{_prefix}/redpesk/afb-ocpp/etc
%{_prefix}/redpesk/afb-ocpp/lib
%{_prefix}/redpesk/afb-ocpp/lib/libafb-ocpp-ext.so
%{_prefix}/redpesk/afb-ocpp/htdocs
%{_prefix}/redpesk/afb-ocpp/bin

%{_prefix}/redpesk/%{name}/.rpconfig/*

%changelog
