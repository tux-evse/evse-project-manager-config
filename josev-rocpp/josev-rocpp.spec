# bypass the build phase, otherwise rpmbuild will want to check for build-ids in binaries
%global debug_package %{nil}

Name: josev-rocpp
Version: 0.5.1
Release: 1%{?dist}
Summary: EcoG's OCPP Rust implementation

Source0: %{name}-%{version}.tar.gz
Source1: ocpp-service-%{version}-aarch64-unknown-linux-musl
Source2: ocpp-service-%{version}-x86_64-unknown-linux-musl
License: Proprietary EcoG License

%description
EcoG's OCPP Rust implementation

%prep
%autosetup -p 1

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc/default/rocpp
install %{_sourcedir}/ocpp-service-%{version}-%{_arch}-unknown-linux-musl %{buildroot}/usr/bin/rocpp
install %{_sourcedir}/sample_switch_device_model.json %{buildroot}/etc/default/rocpp

%files
/usr/bin/rocpp
/etc/default/sample_switch_device_model.json

%changelog
