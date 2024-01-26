%global debug_package %{nil}
ExcludeArch: x86_64

Name: afb-ocpp-ext
Version: 0.0.1
Release: 0%{?dist}
Summary: AFB micro-service framework extention for OCPP

License: Apache
URL: https://github.com/tux-evse/afb-ocpp-ext.git
Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig(librp-utils) >= 0.0.3
BuildRequires: afb-cmake-modules
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

%clean

%files
%dir %{_prefix}/redpesk/%{name}
%dir %{_prefix}/redpesk/%{name}/var
%dir %{_prefix}/redpesk/%{name}/etc
%dir %{_prefix}/redpesk/%{name}/lib
%{_prefix}/redpesk/%{name}/htdocs
%{_prefix}/redpesk/%{name}/bin

%{_prefix}/redpesk/%{name}
%{_prefix}/redpesk/%{name}/var
%{_prefix}/redpesk/%{name}/config.xml
%{_prefix}/redpesk/%{name}/icon.jpg
%{_prefix}/redpesk/%{name}/etc
%{_prefix}/redpesk/%{name}/lib
%{_prefix}/redpesk/%{name}/lib/libafb-ocpp-ext.so
%{_prefix}/redpesk/%{name}/htdocs
%{_prefix}/redpesk/%{name}/bin


%changelog
