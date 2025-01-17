# bypass the build phase, otherwise rpmbuild will want to check for build-ids in binaries
%global debug_package %{nil}

# do not try to install debugging symbols for libraries
%define _build_id_links none

ExcludeArch: x86_64

Name: josev-piso15118
Version: 1.0.8rc
Release: 1%{?dist}
Summary: EcoG's ISO-15118 Python implementation

URL: https://github.com/tux-evse/evse-project-manager-config.git
Source0: %{name}-%{version}.tar.gz
Source1: josev_pro_rc-1.0.8_py3.10_aarch64_libc-2.28_Valeo.tar.xz
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
EcoG's ISO-15118 Python implementation

%prep

%install
tar xzvf %{_sourcedir}/%{name}-%{version}.tar.gz

mkdir -p %{buildroot}/usr/josev
echo /usr/josev > files.txt
tar tJvf %{_sourcedir}/%{tarball} | awk '{print$6;}' | sed 's!josev.*josev_pro/!/usr/josev/piso15118/!' | tail -n +2 >> files.txt
tar -x --strip-components 1 -Jf %{_sourcedir}/%{tarball}
mv josev_pro %{buildroot}/usr/josev/piso15118

echo /usr/josev/piso15118/start.sh >> files.txt
%{__install} -Dm644 %{name}-%{version}/josev-piso15118/josev-piso.service %{buildroot}/%{_unitdir}/josev-piso.service
%{__install} -Dm755 %{name}-%{version}/josev-piso15118/start.sh %{buildroot}/usr/josev/piso15118

%post
%systemd_post josev-piso.service

systemctl enable josev-piso.service > /dev/null

%systemd_prerun josev-piso.service


%files -f files.txt
%defattr(755,root,root)
/usr/josev/piso15118/start.sh
/%{_unitdir}/josev-piso.service

%changelog
