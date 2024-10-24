%global debug_package %{nil}

Name: iso15118-simulator-rs
Version: 0.9
Release: 1%{?dist}
Group: Development/Tools/Other
Summary: Generated from ISO15118 XDS schema on pcsc-lite

License: Apache-2.0
URL: https://github.com/tux-evse/iso15118-simulator-rs.git
Source0: %{name}-%{version}.tar.gz
Source1: vendor.tar.gz
Source2: cargo_config

BuildRequires:   afb-librust
BuildRequires:   rust >= 1.70
BuildRequires:   cargo >= 1.70
BuildRequires:   clang-devel
BuildRequires:   iso15118-encoders-devel
BuildRequires:   pkgconfig(gnutls)
BuildRequires:   pkgconfig(libpcap)
BuildRequires:   pkgconfig(json-c)

Requires:  injector-binding-rs

%description
ISO15118 Simulator provides JSON/Rest-Websocket APIs to simulate an EV/EVSE.

%package test
Summary: %{name} binding test

Requires: %{name}
Requires: injector-binding-rs
Requires: afb-ui-devtools
Requires: iproute
Suggests: %{name}-test-tools

%description test
%{name} binding test.

%package test-tools
Summary: %{name} binding test-tools

Requires: %{name}-test = %{version}
Requires: gnutls-utils

%description test-tools
%{name} binding test tools.

%prep
%autosetup -a1

mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
%if 0%{?fedora}
export RUSTFLAGS+=" -Cstrip=debuginfo"
%endif

cargo build --offline  --release --target %{_arch}-unknown-linux-gnu

%install
mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/lib
cp ./target/%{_arch}-unknown-linux-gnu/release/*.so %{buildroot}%{_prefix}/redpesk/%{name}/lib

mkdir -p %{buildroot}%{_bindir}
cp ./target/%{_arch}-unknown-linux-gnu/release/pcap-iso15118 %{buildroot}%{_bindir}

cp ./afb-evcc/etc/binding-start-evcc.sh %{buildroot}%{_bindir}/binding-start-evcc
cp ./afb-evse/etc/binding-start-evse.sh %{buildroot}%{_bindir}/binding-start-evse

cp ./afb-test/certs/mkcerts.sh %{buildroot}%{_bindir}/mkcerts
cp ./afb-test/network/client-server-bridge.sh %{buildroot}%{_bindir}/client-server-bridge

mkdir -p %{buildroot}%{_datadir}/iso15118-simulator-rs/
cp ./afb-evcc/etc/binding-simu15118-evcc.yaml %{buildroot}%{_datadir}/iso15118-simulator-rs/
cp ./afb-evcc/etc/binding-simu15118-evcc-no-tls.yaml %{buildroot}%{_datadir}/iso15118-simulator-rs/

cp ./afb-evse/etc/binding-simu15118-evse.yaml %{buildroot}%{_datadir}/iso15118-simulator-rs/
cp ./afb-evse/etc/binding-simu15118-evse-no-tls.yaml %{buildroot}%{_datadir}/iso15118-simulator-rs/

cp ./afb-test/certs/*.cfg %{buildroot}%{_datadir}/iso15118-simulator-rs/

cp ./afb-test/certs/*.cfg %{buildroot}%{_datadir}/iso15118-simulator-rs/
cp ./afb-test/certs/*.cfg %{buildroot}%{_datadir}/iso15118-simulator-rs/
cp ./afb-test/etc/*.json %{buildroot}%{_datadir}/iso15118-simulator-rs/
cp ./afb-test/trace-logs/*.pcap %{buildroot}%{_datadir}/iso15118-simulator-rs/

%files
%dir %{_prefix}/redpesk
%dir %{_prefix}/redpesk/%{name}

%dir %{_prefix}/redpesk/%{name}/lib
%{_prefix}/redpesk/%{name}/lib/*
%{_bindir}/pcap-iso15118
%{_bindir}/binding-start-evcc
%{_bindir}/binding-start-evse

%dir %{_datadir}/iso15118-simulator-rs

%{_datadir}/iso15118-simulator-rs/binding-simu15118-evcc.yaml
%{_datadir}/iso15118-simulator-rs/binding-simu15118-evcc-no-tls.yaml

%{_datadir}/iso15118-simulator-rs/binding-simu15118-evse.yaml
%{_datadir}/iso15118-simulator-rs/binding-simu15118-evse-no-tls.yaml

%files test
%{_datadir}/iso15118-simulator-rs/*.cfg
%{_datadir}/iso15118-simulator-rs/*.json
%{_datadir}/iso15118-simulator-rs/*.pcap

%files test-tools
%{_bindir}/mkcerts
%{_bindir}/client-server-bridge



%changelog
