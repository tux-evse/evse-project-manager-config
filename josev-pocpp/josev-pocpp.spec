# bypass the build phase, otherwise rpmbuild will want to check for build-ids in binaries
%global debug_package %{nil}

Name: josev-pocpp
Version: 1.0.3
Release: 1%{?dist}
Summary: EcoG's OCPP Python implementation

Source0: %{name}-%{version}.tar.gz
Source1: pocpp-1.0.3-x86_64.tar.gz
Source2: pocpp-1.0.3-aarch64.tar.gz
License: Proprietary EcoG License


# Disable auto provide and require declaration
# Needed because the archive provides .so libs
# that must not be declared as "provide"
AutoReqProv: no
Requires: glibc
Requires: zlib


%description
EcoG's OCPP Python implementation

%prep
%ifarch x86_64
# Use Source1, a.k.a. the x86-64 binary
%autosetup -b 1
%else
# Use Source2, a.k.a. the aarch64 binary
%autosetup -b 2
%endif 

%install
mkdir -p %{buildroot}/usr/josev/pocpp
tar tzvf %{_sourcedir}/pocpp-1.0.3-%{_arch}.tar.gz | awk '{print "/usr/josev/pocpp/"$6;}' > files.txt
tar -C %{buildroot}/usr/josev/pocpp -xvf %{_sourcedir}/pocpp-1.0.3-%{_arch}.tar.gz

%files -f files.txt

%changelog
