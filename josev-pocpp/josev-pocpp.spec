# bypass the build phase, otherwise rpmbuild will want to check for build-ids in binaries
%global debug_package %{nil}

# do not try to install debugging symbols for libraries
%define _build_id_links none

ExcludeArch: x86_64

Name: josev-pocpp
Version: 1.0.7
Release: 1%{?dist}
Summary: EcoG's OCPP Python implementation

URL: https://github.com/tux-evse/evse-project-manager-config.git
Source0: %{name}-%{version}.tar.gz
Source1: ocpp_service_1.0.7_py3.10_aarch64_libc-2.28.tar.xz
License: Proprietary EcoG License

%global tarball %{basename:%{SOURCE1}}


# Disable auto provide and require declaration
# Needed because the archive provides .so libs
# that must not be declared as "provide"
AutoReqProv: no
Requires: glibc
Requires: xz
BuildRequires: systemd


%description
EcoG's OCPP Python implementation

%prep
# Use Source1, a.k.a. the binary
%autosetup -b 1

%install
tar xzvf %{_sourcedir}/%{name}-%{version}.tar.gz

mkdir -p %{buildroot}/usr/josev
echo /usr/josev > files.txt
tar tJvf %{_sourcedir}/%{tarball} | awk '{print$6;}' | tail +3 | sed 's!ocpp_service.*service/!/usr/josev/pocpp/!' >> files.txt
tar -x --strip-components 2 -Jf %{_sourcedir}/%{tarball}
mv ocpp_service %{buildroot}/usr/josev/pocpp


mv %{SOURCE2} %{buildroot}/usr/josev/pocpp

%{__install} -Dm644 %{name}-%{version}/josev-pocpp/josev-pocpp.service %{buildroot}/%{_unitdir}/josev-pocpp.service
%{__install} -Dm755 %{name}-%{version}/josev-pocpp/start.sh %{buildroot}/usr/josev/pocpp

%post
%systemd_post josev-pocpp.service

systemctl enable josev-pocpp.service > /dev/null

%systemd_preun josev-pocpp.service


%files -f files.txt
%defattr(755,root,root)
/usr/josev/pocpp/start.sh
/%{_unitdir}/josev-pocpp.service

%changelog
