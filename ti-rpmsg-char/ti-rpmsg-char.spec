ExcludeArch: x86_64

Name: ti-rpmsg-char
Version: 0.6.3
Release: 3%{?dist}
Summary: rpmsg-char utility library

License: GPL-2.0
URL: https://git.ti.com/git/rpmsg/ti-rpmsg-char.git
Source0: %{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: make
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool

%description
rpmsg-char utility library.

%package devel
Summary:        Development rpmsg-char utility library
License:        GPL-2.0
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers and files for libsystemd and libudev libraries for
developing and building applications linking to these libraries.

%prep
%autosetup -p 1

%build
autoreconf -i
%configure

mkdir -p gnu;
touch gnu/stubs-32.h
export C_INCLUDE_PATH="${C_INCLUDE_PATH}:$(pwd)"

%{make_build}
#%%{make_build} -C examples

%install
%{make_install}
#%%{make_install} -C examples install

%files
%{_libdir}/*.so.0.*
%{_libdir}/*.so.0
#%%{_bindir}/*

%files devel
%{_includedir}/*.h
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%changelog
