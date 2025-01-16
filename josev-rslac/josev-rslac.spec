# bypass the build phase, otherwise rpmbuild will want to check for build-ids in binaries
%global debug_package %{nil}

ExcludeArch: x86_64

Name: josev-rslac
Version: 1.0.7
Release: 1%{?dist}
Summary: EcoG's SLAC Rust implementation

URL: https://github.com/tux-evse/evse-project-manager-config.git
Source0: %{name}-%{version}.tar.gz
Source1: slac_service_aarch64_libc-2.28.tar.xz
License: Proprietary EcoG License

%global tarball %{basename:%{SOURCE1}}


# Disable auto provide and require declaration
# Needed because the archive provides .so libs
# that must not be declared as "provide"
AutoReqProv: no
Requires: glibc
Requires: xz


%description
EcoG's SLAC Rust implementation

%prep
%autosetup -b 0
# Use Source1, a.k.a. the binary
%autosetup -b 1

%install
mkdir -p %{buildroot}/usr/josev/rslac
tar xJvf %{_sourcedir}/%{tarball}
mv slac_*/josev_pro/slac_service/slac_service %{buildroot}/usr/josev/rslac/slac_service

%{__install} -Dm644 ./josev-rslac/josev-rslac.service %{buildroot}%{_unitdir}/josev-rslac.service

%post
%systemd_post josev-rslac.service

systemctl enable josev-rslac.service > /dev/null

%systemd_prerun josev-rslac.service

%files
/usr/josev
/usr/josev/rslac
/usr/josev/rslac/slac_service
%defattr(755,root,root)
/usr/josev/rslac/start.sh
%{_unitdir}/josev-rslac.service

%changelog
