# bypass the build phase, otherwise rpmbuild will want to check for build-ids in binaries
%global debug_package %{nil}

# do not try to install debugging symbols for libraries
%define _build_id_links none

ExcludeArch: x86_64

Name: josev-pocpp
Version: 1.0.7
Release: 1%{?dist}
Summary: EcoG's OCPP Python implementation

Source0: %{name}-%{version}.tar.gz
Source1: ocpp_service_1.0.7_py3.10_aarch64_libc-2.28.tar.xz
Source2: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/refs/heads/main/josev-pocpp/start.sh
License: Proprietary EcoG License

%global tarball %{basename:%{SOURCE1}}


# Disable auto provide and require declaration
# Needed because the archive provides .so libs
# that must not be declared as "provide"
AutoReqProv: no
Requires: glibc
Requires: xz


%description
EcoG's OCPP Python implementation

%prep
# Use Source1, a.k.a. the binary
%autosetup -b 1

%install
mkdir -p %{buildroot}/usr/josev
echo /usr/josev > files.txt
tar tJvf %{_sourcedir}/%{tarball} | awk '{print$6;}' | tail +3 | sed 's!ocpp_service.*service/!/usr/josev/pocpp/!' >> files.txt
tar -x --strip-components 2 -Jf %{_sourcedir}/%{tarball}
mv ocpp_service %{buildroot}/usr/josev/pocpp

echo /usr/josev/pocpp/start.sh >> files.txt
mv %{SOURCE2} %{buildroot}/usr/josev/pocpp


%files -f files.txt

%changelog
