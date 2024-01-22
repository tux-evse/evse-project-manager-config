%global debug_package %{nil}

Name: ocpp-binding-rs
Version: 0.0.1
Release: 11%{?dist}
Summary: OCPP Rust afb binding

License: MIT
URL: https://github.com/tux-evse/ocpp-binding-rs.git
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
OCPP Rust afb binding.

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

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/etc
cp ./afb-binding/etc/*.json %{buildroot}%{_prefix}/redpesk/%{name}/etc
CONF_NAME=$(basename t%{buildroot}%{_prefix}/redpesk/%{name}/etc/*.json)

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/bin
cat << EOF >> "%{buildroot}%{_prefix}/redpesk/%{name}/bin/start_bender.sh"
#!/usr/bin/bash

/usr/bin/afb-binder --config %{_prefix}/redpesk/%{name}/etc/binding-bia-power.json \
                    --ws-server sd:ocpp

EOF

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig

LIB_NAME=$(basename target/aarch64-unknown-linux-gnu/release/*.so)
cat << EOF >> "%{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml"
rp-manifest: 1
id: %{name}
version: 0.1
name: %{name}
description: linky binding
author: IoT.bzh team <team@iot.bzh>
license: MIT
targets:
  - target: main
    content:
      src: bin/start_bender.sh
      type: application/x-executable
    provided-api:
      - name: ocpp
        value: ws
 
file-properties:
  - name: bin/start_bender.sh
    value: executable


EOF

%files
%dir %{_prefix}/redpesk/%{name}
%dir %{_prefix}/redpesk/%{name}/.rpconfig
%{_prefix}/redpesk/%{name}/.rpconfig/*
%dir %{_prefix}/redpesk/%{name}/etc
%{_prefix}/redpesk/%{name}/etc/*
%dir %{_prefix}/redpesk/%{name}/lib
%{_prefix}/redpesk/%{name}/lib/*
%dir %{_prefix}/redpesk/%{name}/bin
%{_prefix}/redpesk/%{name}/bin/*

%changelog
