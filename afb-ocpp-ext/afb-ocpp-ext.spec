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
BuildRequires:  pkgconfig(librp-utils) >= 0.0.3
BuildRequires:  afb-cmake-modules

%description
AFB micro-service framework extention for OCPP.

%prep
%autosetup -p 1

%build
%cmake -DCMAKE_BUILD_TYPE=DEBUG .
%cmake_build

%install
%cmake_install

%check

%clean

%files
%{_libdir}/*.so

%changelog
