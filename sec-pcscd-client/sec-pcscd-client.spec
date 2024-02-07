%global debug_package %{nil}

Name: sec-pcscd-client
Version: 0.0.2+20240125+11+gf636635
Release: 2%{?dist}
Summary: sample implementation for Smartcard/NFC-token authentication based on pcsc-lite.

License: Apache
URL: http://git.ovh.iot/redpesk/redpesk-common/sec-pcscd-client.git
Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: afb-cmake-modules
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(libafb)
BuildRequires: afm-rpm-macros
BuildRequires: pkgconfig(afb-libhelpers)
BuildRequires: pkgconfig(libpcsclite)
BuildRequires:  uthash-devel

Requires:  pcsc-lite

%description
sample implementation for Smartcard/NFC-token authentication based on pcsc-lite.

%package tool
Summary:        tool  for Smartcard/NFC-token authentication based on pcsc-lite
Requires:       %{name} = %{version}-%{release}

%description tool
tool for Smartcard/NFC-token authentication based on pcsc-lite.

%package devel
Summary:        sample implementation for Smartcard/NFC-token authentication based on pcsc-lite
Requires:       %{name} = %{version}-%{release}

%description devel
sample implementation for Smartcard/NFC-token authentication based on pcsc-lite.


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

cd ..
mkdir -p %{buildroot}%{_modprobedir}
cp ./etc/nfc-blacklist.conf %{buildroot}%{_modprobedir}

rm -fr  %{buildroot}/usr/redpesk/pcscs-client

%files
%{_prefix}/lib64/libpcscd-glue.*
%{_modprobedir}/*.conf

%files tool
%{_bindir}/pcscd-client

%files devel
%{_prefix}/include/*.h

%changelog
