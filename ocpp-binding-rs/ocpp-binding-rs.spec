%define debug_package %{nil}
ExcludeArch: x86_64

Name: ocpp-binding-rs
Version: 0.0.1
Release: 11%{?dist}
Summary: OCPP Rust afb binding

License: MIT
URL: https://github.com/tux-evse/ocpp-binding-rs.git
Source0: %{name}-%{version}.tar.gz
Source1: vendor.tar.gz
Source2: cargo_config

Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/ocpp-binding-rs/manifest.yml
Source11: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/ocpp-binding-rs/manifest-test.yml

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

Requires: afb-ocpp-ext

#BuildRequires: glibc-devel


%description
OCPP Rust afb binding.

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
mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/lib
cp ./target/%{_arch}-unknown-linux-gnu/release/*.so %{buildroot}%{_prefix}/redpesk/%{name}/lib

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig
cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig
cp %{SOURCE11} %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig/manifest.yml

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/etc
mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/bin
cp ./afb-binding/etc/*.json %{buildroot}%{_prefix}/redpesk/%{name}/test/etc
cp ./afb-binding/etc/*.sh %{buildroot}%{_prefix}/redpesk/%{name}/test/bin


%files
%dir %{_prefix}/redpesk/%{name}
%dir %{_prefix}/redpesk/%{name}/.rpconfig
%{_prefix}/redpesk/%{name}/.rpconfig/*
%dir %{_prefix}/redpesk/%{name}/lib
%{_prefix}/redpesk/%{name}/lib/*

%files test
%dir %{_prefix}/redpesk/%{name}/test
%dir %{_prefix}/redpesk/%{name}/test/bin
%{_prefix}/redpesk/%{name}/test/bin/*
%dir %{_prefix}/redpesk/%{name}/test/etc
%{_prefix}/redpesk/%{name}/test/etc/*
%dir %{_prefix}/redpesk/%{name}/test/.rpconfig
%{_prefix}/redpesk/%{name}/test/.rpconfig/*

%changelog
