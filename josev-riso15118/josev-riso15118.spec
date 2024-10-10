# bypass the build phase, otherwise rpmbuild will want to check for build-ids in binaries
%global debug_package %{nil}

Name: josev-riso15118
Version: 0.2.0
Release: 1%{?dist}
Summary: EcoG's ISO-15118-2 implementation

Source0: %{name}-%{version}.tar.gz
Source1: riso15118-aarch64
Source2: riso15118-x86_64
License: Proprietary EcoG License

Requires: mosquitto

%description
EcoG's ISO-15118-2 implementation

%prep
%autosetup -p 1

%install
mkdir -p %{buildroot}/usr/bin
%ifarch aarch64
install %{_sourcedir}/riso15118-aarch64 %{buildroot}/usr/bin/riso15118
%endif
%ifarch x86_64
install %{_sourcedir}/riso15118-x86_64 %{buildroot}/usr/bin/riso15118
%endif

%files
/usr/bin/riso15118

%changelog
