%global debug_package %{nil}

Name: iso15118-network-rs
Version: 0.0.1
Release: 2%{?dist}
Group: Development/Tools/Other
Summary: RUST binding for ipv6 & gnutls support UDP,TCP &TLS 1.3

License: Apache-2.0
URL: https://github.com/tux-evse/iso15118-network-rs.git
Source0: %{name}-%{version}.tar.gz
Source1: vendor.tar.gz
Source2: cargo_config

BuildRequires:   rust >= 1.70
BuildRequires:   cargo >= 1.70
BuildRequires: afb-librust
BuildRequires: clang-devel
BuildRequires: pkgconfig(gnutls)
%description
RUST binding for ipv6 & gnutls support UDP,TCP &TLS 1.3.

%package test
Summary: %{name} binding test

Requires: %{name} = %{version}
Requires: afb-ui-devtools

%description test
%{name} binding test.

%prep
%autosetup -a1

mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
cargo build --offline --release --target %{_arch}-unknown-linux-gnu

%install

TLIBDIR=$(rustc --print target-libdir  --target %{_arch}-unknown-linux-gnu)

mkdir -p %{buildroot}${TLIBDIR}
cp ./target/%{_arch}-unknown-linux-gnu/release/*.rlib %{buildroot}${TLIBDIR}
cp ./target/%{_arch}-unknown-linux-gnu/release/deps/*.rlib %{buildroot}${TLIBDIR}


%files
%{_prefix}/lib/rustlib/*/lib/*.rlib

%changelog


