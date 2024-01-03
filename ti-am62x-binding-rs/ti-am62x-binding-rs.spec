ExcludeArch: x86_64
%global debug_package %{nil}

Name: ti-am62x-binding-rs
Version: 0.0.4
Release: 3%{?dist}
Summary: ti-am62x binding

License: MIT
URL: https://github.com/tux-evse/slac-binding-rs.git
Source0: %{name}-%{version}.tar.gz
Source1: vendor.tar.gz
Source2: cargo_config

Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/ti-am62x-binding-rs/manifest.yml

%ifarch x86_64
BuildRequires:   rust-archive >= 1.70.0
%else
%NativeBuildRequires   rust-archive >= 1.70.0

%endif

BuildRequires: afb-librust
BuildRequires: protobuf-compiler
BuildRequires: ti-rpmsg-char-devel
BuildRequires: clang-devel
BuildRequires: glibc-devel
BuildRequires: glibc-headers


%description
ti-am62x binding.

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

#build fix
mkdir -p gnu;
touch gnu/stubs-32.h
export C_INCLUDE_PATH="${C_INCLUDE_PATH}:$(pwd)"
#End build fix

cargo build --offline --release --target %{_arch}-unknown-linux-gnu


%install
mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/lib
cp ./target/%{_arch}-unknown-linux-gnu/release/*.so %{buildroot}%{_prefix}/redpesk/%{name}/lib

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp ./afb-binding/etc/*.json %{buildroot}%{_prefix}/redpesk/%{name}/etc

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig

LIB_NAME=$(basename target/aarch64-unknown-linux-gnu/release/*.so)

cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml

%files
%dir %{_prefix}/redpesk/%{name}
%dir %{_prefix}/redpesk/%{name}/.rpconfig
%{_prefix}/redpesk/%{name}/.rpconfig/*
%dir %{_prefix}/redpesk/%{name}/etc
%{_prefix}/redpesk/%{name}/etc/*
%dir %{_prefix}/redpesk/%{name}/lib
%{_prefix}/redpesk/%{name}/lib/*

%changelog
