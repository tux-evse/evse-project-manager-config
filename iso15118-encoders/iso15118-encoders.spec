%global debug_package %{nil}

Name: iso15118-encoders
#Hexsha: c5c0ed5fa8d970e5da137c813f666c75597fc28c
Version: 0.0.1+20240917+1+gc5c0ed5
Release: 1%{?dist}
Summary: Those encoder are generated from ISO15118

License: Apache-2.0
URL: https://github.com/tux-evse/iso15118-encoders.git
Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: pkgconfig(gnutls)

%description
Those encoder are generated from ISO15118 XDS schema with Chargebyte cbexigensed on pcsc-lite.

%package devel
Summary:        Those encoder are generated from ISO15118 XDS schema
Requires:       %{name} = %{version}-%{release}

%description devel
Those encoder are generated from ISO15118 XDS schema with Chargebyte cbexigensed on pcsc-lite devel.


%prep
%autosetup -p 1

%build

%if !0%{?suse_version}
mkdir -p build
cd build
%endif

%cmake ../
%cmake_build

%install
%if !0%{?suse_version}
cd build
%endif
%cmake_install

rm -fr %{buildroot}%{_prefix}/lib*/libcb_exi_codec.*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_prefix}/lib*/libiso15118.so.*

%files devel
%{_prefix}/lib*/libiso15118.so
%dir %{_prefix}/include/iso15118
%{_prefix}/include/iso15118/*.h
%changelog
