%global debug_package %{nil}
#

Name: lvgl-rclib-rs
Version: 0.0.1
Release: 1%{?dist}
Summary: provides a RUST api to lvgl/C lib

License: Apache
URL: https://github.com/tux-evse/lvgl-rclib-rs.git
Source0: %{name}-%{version}.tar.gz
Source1: vendor.tar.gz
Source2: cargo_config

BuildRequires:   rust >= 1.70
BuildRequires:   cargo >= 1.70
BuildRequires: afb-librust
BuildRequires: clang-devel

BuildRequires:  clang
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(afb-binding)

BuildRequires:  iputils

BuildRequires: clang-devel

BuildRequires: glibc-devel

BuildRequires: pkgconfig(lvgl)

%description
Provides a RUST api to lvgl/C lib. It supports frame-buffer for embedded devices and GTK emulation for desktop development.

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
