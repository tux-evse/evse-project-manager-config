# bypass the build phase, otherwise rpmbuild will want to check for build-ids in binaries
%global debug_package %{nil}

Name: josev-rocpp
Version: 0.5.1
Release: 1%{?dist}
Summary: EcoG's OCPP Rust implementation

Source0: %{name}-%{version}.tar.gz
Source1: ocpp-service-0.5.1-aarch64-unknown-linux-musl
Source2: ocpp-service-0.5.1-x86_64-unknown-linux-musl
Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/refs/heads/main/josev-rocpp/sample_switch_device_model.json
License: Proprietary EcoG License

%description
EcoG's OCPP Rust implementation

%prep
%autosetup -p 1

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc/default/rocpp
install %{_sourcedir}/ocpp-service-0.5.1-%{_arch}-unknown-linux-musl %{buildroot}/usr/bin/rocpp
install %{SOURCE10} %{buildroot}/etc/default/rocpp

%files
/usr/bin/rocpp
/etc/default/rocpp/sample_switch_device_model.json

%changelog
