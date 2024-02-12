%global debug_package %{nil}
ExcludeArch: x86_64

Name: iso15118-encoders
Version: 0.0.1
Release: 1%{?dist}
Summary: Those encoder are generated from ISO15118 XDS schema with Chargebyte cbexigensed on pcsc-lite

License: Apache
URL: https://github.com/tux-evse/iso15118-encoders.git
Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool

%description
Those encoder are generated from ISO15118 XDS schema with Chargebyte cbexigensed on pcsc-lite.

%package devel
Summary:        Those encoder are generated from ISO15118 XDS schema with Chargebyte cbexigensed on pcsc-lite devel
Requires:       %{name} = %{version}-%{release}

%description devel
Those encoder are generated from ISO15118 XDS schema with Chargebyte cbexigensed on pcsc-lite devel.


%prep
%autosetup -p 1

%build
mkdir -p build
cd build
%cmake ../
%cmake_build

%install
cd build
%cmake_install

%files
%{_prefix}/lib64/libiso15118.so.*


%files devel
%{_prefix}/lib64/libiso15118.so
%{_prefix}/include/iso15118/*.h

%changelog
