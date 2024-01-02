%global debug_package %{nil}

Name: afb-librust
Version: 0.1.0
Release: 9%{?dist}
Summary: AFB rust binging

License: MIT
URL: https://git.ovh.iot/redpesk/redpesk-common/afb-librust
Source0: %{name}-%{version}.tar.gz
Source1: vendor.tar.gz
Source2: cargo_config

%ifarch x86_64
BuildRequires:   rust-archive >= 1.70.0
#Fix for cross build
BuildRequires: glibc32
%else
%NativeBuildRequires   rust-archive >= 1.70.0
%NativeBuildRequires glibc32
%endif

#BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(afb-binding)
#BuildRequires:  afb-ui-devtools
BuildRequires:  pkgconfig(libafb)
BuildRequires:  iputils
%ifarch x86_64
BuildRequires:  gcc-aarch64-linux-gnu
%endif

BuildRequires: clang-devel



BuildRequires: glibc-devel


%description
AFB rust binging.

%prep
%autosetup -a1

mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
cargo build --offline --release --target %{_arch}-unknown-linux-gnu --features rpm_build
#{cargo_build}

#TMP FIX
%ifarch x86_64
cargo build --offline --release --target aarch64-unknown-linux-gnu --features rpm_build
%endif

%install
TLIBDIR=$(rustc --print target-libdir  --target %{_arch}-unknown-linux-gnu)

mkdir -p %{buildroot}${TLIBDIR}
cp ./target/%{_arch}-unknown-linux-gnu/release/*.rlib %{buildroot}${TLIBDIR}
cp ./target/%{_arch}-unknown-linux-gnu/release/deps/*.rlib %{buildroot}${TLIBDIR}

#TMP FIX
%ifarch x86_64
TLIBDIR_ARM=$(rustc --print target-libdir  --target aarch64-unknown-linux-gnu)

mkdir -p %{buildroot}${TLIBDIR_ARM}
cp ./target/aarch64-unknown-linux-gnu/release/*.rlib %{buildroot}${TLIBDIR_ARM}
cp ./target/aarch64-unknown-linux-gnu/release/deps/*.rlib %{buildroot}${TLIBDIR_ARM}

%endif


%files
%{_prefix}/lib/rustlib/*/lib/*.rlib

%changelog
