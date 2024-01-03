%global debug_package %{nil}

Name: linky-binding-rs
Version: 0.0.0+20231117+173249+0+ge1f8b8f
Release: 1%{?dist}
Summary: linky binding

License: MIT
URL: https://github.com/tux-evse/linky-binding-rs.git
Source0: %{name}-%{version}.tar.gz
Source1: vendor.tar.gz
Source2: cargo_config

%ifarch x86_64
BuildRequires:   rust-archive >= 1.70.0
BuildRequires:   glibc32
%else
%NativeBuildRequires   rust-archive >= 1.70.0
#Fix for cross build
%NativeBuildRequires glibc32
%endif

BuildRequires: afb-librust
BuildRequires: clang-devel


#BuildRequires: glibc-devel


%description
linky binding.

%prep
%autosetup -a1

mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
%ifarch aarch64
export PKG_CONFIG_DIR="${PKG_CONFIG_DIR}:$CROSS_ROOT/usr/lib64/pkgconfig"
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH}:$CROSS_ROOT/usr/lib64/pkgconfig"
export PKG_CONFIG=/usr/aarch64-linux-gnu/sys-root/usr/bin/pkgconf

mkdir -p ${HOME}/.cargo/
cat << EOF >> "${HOME}/.cargo/config"
[target.aarch64-unknown-linux-gnu]
linker = "aarch64-linux-gnu-gcc"
EOF
%endif

cargo build --offline --release --target %{_arch}-unknown-linux-gnu


%install
TLIBDIR=$(rustc --print target-libdir --target %{_arch}-unknown-linux-gnu)

mkdir -p %{buildroot}${TLIBDIR}
cp ./target/%{_arch}-unknown-linux-gnu/release/*.rlib %{buildroot}${TLIBDIR}


%files
%{_prefix}/lib/rustlib/*/lib/*.rlib

%changelog
